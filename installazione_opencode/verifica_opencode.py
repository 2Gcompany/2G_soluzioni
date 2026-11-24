#!/usr/bin/env python3
"""Verifica che OpenCode funzioni davvero: si apre E risponde con il modello.

Controlla due cose (come richiesto nella review del PR #32):

1. che il comando `opencode` sia installato e si avvii;
2. che il modello risponda davvero: lo script apre una sessione tramite
   l'API HTTP di OpenCode, manda un prompt che contiene una parola segreta
   e controlla che la risposta del modello riprodi quella parola.

Uso, dalla root del repository (nel terminale del Codespace):

    python3 installazione_opencode/verifica_opencode.py

Opzioni:

    --model PROVIDER/MODEL   modello da usare (default: modello predefinito
                             di OpenCode, con fallback su un modello gratuito)
    --timeout SECONDI        tempo massimo di attesa della risposta (default 120)

Exit code: 0 se tutto OK, 1 se qualcosa non funziona.
Usa solo la libreria standard di Python: non serve installare nulla con pip.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

# ---------------------------------------------------------------------------
# Utilità di output
# ---------------------------------------------------------------------------


def ok(testo: str) -> None:
    print(f"  ✅ {testo}")


def errore(testo: str) -> None:
    print(f"  ❌ {testo}")


def info(testo: str) -> None:
    print(f"  ℹ️  {testo}")


# ---------------------------------------------------------------------------
# Passo 1: il comando opencode esiste e risponde
# ---------------------------------------------------------------------------


def verifica_comando() -> str | None:
    """Restituisce la versione di OpenCode oppure None se il comando manca."""
    print("\n[1/4] Comando opencode")
    if shutil.which("opencode") is None:
        errore("comando `opencode` non trovato nel PATH")
        info("installa OpenCode con: npm install -g opencode-ai")
        return None
    try:
        res = subprocess.run(
            ["opencode", "--version"],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (subprocess.TimeoutExpired, OSError) as exc:
        errore(f"`opencode --version` non riesce a terminare: {exc}")
        return None
    if res.returncode != 0:
        errore(f"`opencode --version` è uscito con codice {res.returncode}")
        if res.stderr.strip():
            info(res.stderr.strip()[:300])
        return None
    versione = (res.stdout or res.stderr).strip()
    ok(f"OpenCode installato: {versione}")
    return versione


# ---------------------------------------------------------------------------
# Passo 2: il server HTTP di OpenCode è attivo (lo avvia se serve)
# ---------------------------------------------------------------------------


def _leggi_url_service() -> str | None:
    """Chiede al CLI lo stato del server e ne estrae l'URL."""
    try:
        res = subprocess.run(
            ["opencode", "service", "status"],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    for riga in (res.stdout + "\n" + res.stderr).splitlines():
        riga = riga.strip()
        if riga.startswith(("http://", "https://")):
            return riga
    return None


def avvia_server() -> str | None:
    """Restituisce l'URL del server OpenCode, avviandolo se non è attivo."""
    print("\n[2/4] Server HTTP di OpenCode")
    url = _leggi_url_service()
    if url is None:
        info("server non attivo: lo avvio con `opencode service start`")
        try:
            subprocess.run(
                ["opencode", "service", "start"],
                capture_output=True,
                text=True,
                timeout=120,
            )
        except (subprocess.TimeoutExpired, OSError) as exc:
            errore(f"impossibile avviare il server: {exc}")
            return None
        url = _leggi_url_service()
    if url is None:
        errore("nessun server OpenCode raggiungibile")
        info("prova a eseguire `opencode` una volta e poi rilancia lo script")
        return None
    ok(f"server attivo su {url}")
    return url


def leggi_password() -> str | None:
    """Legge la password del server da opencode/service.json (se presente)."""
    config_home = os.environ.get("XDG_CONFIG_HOME") or str(Path.home() / ".config")
    percorso = Path(config_home) / "opencode" / "service.json"
    try:
        dati = json.loads(percorso.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    password = dati.get("password")
    return password if isinstance(password, str) and password else None


# ---------------------------------------------------------------------------
# Client HTTP minimale sull'API di OpenCode
# ---------------------------------------------------------------------------


class Client:
    def __init__(self, base_url: str, password: str | None) -> None:
        self.base = base_url.rstrip("/")
        self.password = password

    def richiesta(self, metodo: str, percorso: str, corpo=None, timeout: int = 60):
        """Effettua una richiesta HTTP. Restituisce (status, dati_json)."""
        data = json.dumps(corpo).encode("utf-8") if corpo is not None else None
        req = urllib.request.Request(
            self.base + percorso,
            data=data,
            method=metodo,
            headers={"Content-Type": "application/json"},
        )
        if self.password:
            token = base64.b64encode(
                f"opencode:{self.password}".encode("utf-8")
            ).decode("ascii")
            req.add_header("Authorization", f"Basic {token}")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as risposta:
                grezzo = risposta.read()
                return risposta.status, (
                    json.loads(grezzo) if grezzo else None
                )
        except urllib.error.HTTPError as exc:
            grezzo = exc.read()
            try:
                payload = json.loads(grezzo)
            except ValueError:
                payload = grezzo.decode("utf-8", errors="replace")[:300]
            return exc.code, payload
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            return 0, f"connessione fallita: {exc}"


# ---------------------------------------------------------------------------
# Passo 3: scelta dei modelli da provare
# ---------------------------------------------------------------------------


def scegli_modelli(client: Client, richiesto: str | None) -> list[dict | None]:
    """Restituisce la lista dei modelli da provare.

    Ogni voce è un dict compatibile con Model.Ref ({providerID, id}) oppure
    None per usare il modello predefinito di OpenCode senza cambiarlo.
    """
    candidati: list[dict | None] = []

    if richiesto:
        # formato atteso: PROVIDER/MODELLO[#VARIANTE]
        testo, _, variante = richiesto.partition("#")
        provider, _, modello = testo.partition("/")
        if not provider or not modello:
            return []
        voce: dict = {"providerID": provider, "id": modello}
        if variante:
            voce["variant"] = variante
        candidati.append(voce)
        return candidati

    # modello predefinito di OpenCode (quello che vede lo studente)
    stato, dati = client.richiesta("GET", "/api/model/default")
    if stato == 200 and isinstance(dati, dict):
        modello = dati.get("data") or {}
        provider = modello.get("providerID")
        id_modello = modello.get("modelID") or modello.get("id")
        if provider and id_modello:
            candidati.append({"providerID": provider, "id": id_modello})

    # fallback: un modello gratuito del provider "opencode" (non serve API key)
    stato, dati = client.richiesta("GET", "/api/model")
    if stato == 200 and isinstance(dati, dict):
        for modello in dati.get("data") or []:
            if (
                modello.get("providerID") == "opencode"
                and modello.get("status") == "active"
            ):
                candidati.append(
                    {"providerID": "opencode", "id": modello["id"]}
                )
                break

    # elimina i duplicati, mantenendo l'ordine
    visti: set[tuple] = set()
    unici: list[dict | None] = []
    for voce in candidati:
        chiave = (voce["providerID"], voce["id"]) if voce else ("default", "")
        if chiave not in visti:
            visti.add(chiave)
            unici.append(voce)
    return unici


# ---------------------------------------------------------------------------
# Passo 4: apre una sessione, manda il prompt, legge la risposta
# ---------------------------------------------------------------------------


def _completato(messaggio: dict) -> bool:
    """True se il messaggio assistant ha finito di essere generato.

    Il campo `completed` vive dentro `time` (time.completed), non in cima.
    """
    tempo = messaggio.get("time") or {}
    return bool(tempo.get("completed") or messaggio.get("completed"))


def attendi_risposta(
    client: Client, sessione: str, precedenti: set[str], timeout: int
):
    """Attende il completamento della risposta del modello.

    Restituisce il messaggio assistant completo oppure None se scade il tempo.
    """
    scadenza = time.time() + timeout
    while time.time() < scadenza:
        # blocca finché il ciclo del modello non è inattivo (204 = finito)
        client.richiesta(
            "POST",
            f"/api/experimental/session/{sessione}/wait",
            timeout=max(1, int(scadenza - time.time())),
        )
        stato, dati = client.richiesta(
            "GET", f"/api/session/{sessione}/message?order=asc"
        )
        if stato == 200 and isinstance(dati, dict):
            assistenti = [
                m
                for m in dati.get("data") or []
                if m.get("type") == "assistant" and m.get("id") not in precedenti
            ]
            if assistenti:
                ultimo = assistenti[-1]
                if _completato(ultimo):
                    return ultimo
        time.sleep(1)
    return None


def prova_modello(client: Client, modello: dict | None, timeout: int):
    """Prova un singolo modello. Restituisce (nonce, risposta) o (None, errore)."""

    # crea una sessione dedicata a questo tentativo
    stato, dati = client.richiesta("POST", "/api/session", {})
    if stato != 200 or not isinstance(dati, dict):
        return None, f"creazione sessione fallita (HTTP {stato}): {dati}"
    sessione = (dati.get("data") or {}).get("id")
    if not sessione:
        return None, f"risposta inattesa alla creazione sessione: {dati}"

    try:
        if modello is not None:
            stato, dati = client.richiesta(
                "POST",
                f"/api/session/{sessione}/model",
                {"model": modello},
            )
            if stato not in (200, 204):
                return None, (
                    f"modello {modello['providerID']}/{modello['id']} "
                    f"non accettato (HTTP {stato}): {dati}"
                )

        # parole segrete diverse ad ogni tentativo
        nonce = "OPX" + uuid.uuid4().hex[:8].upper()
        prompt = (
            "Rispondi esattamente e unicamente con questa parola, "
            f"nient'altro: {nonce}"
        )

        # raccoglie gli id degli assistant già presenti (prima del prompt)
        _, vecchi = client.richiesta(
            "GET", f"/api/session/{sessione}/message?order=asc"
        )
        precedenti = {
            m.get("id")
            for m in (vecchi or {}).get("data") or []
            if m.get("type") == "assistant"
        }

        stato, dati = client.richiesta(
            "POST", f"/api/session/{sessione}/prompt", {"text": prompt}
        )
        if stato != 200:
            return None, f"invio prompt fallito (HTTP {stato}): {dati}"

        messaggio = attendi_risposta(client, sessione, precedenti, timeout)
        if messaggio is None:
            return None, f"nessuna risposta entro {timeout} secondi"

        if messaggio.get("error") or messaggio.get("finish") == "error":
            dettaglio = messaggio.get("error") or {}
            if isinstance(dettaglio, dict):
                dettaglio = dettaglio.get("message") or json.dumps(dettaglio)
            return None, f"il modello ha risposto con errore: {dettaglio}"

        testo = " ".join(
            parte.get("text", "")
            for parte in messaggio.get("content") or []
            if parte.get("type") == "text"
        ).strip()
        if not testo:
            return None, "risposta vuota dal modello"
        return (nonce, testo), None
    finally:
        # pulizia: la sessione di prova non serve più
        client.richiesta("DELETE", f"/api/session/{sessione}")


# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verifica che OpenCode si aprisca E risponda dal modello."
    )
    parser.add_argument(
        "--model",
        default=None,
        help="modello da usare, formato PROVIDER/MODELLO (es. opencode/big-pickle)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="secondi massimi di attesa della risposta (default 120)",
    )
    args = parser.parse_args()

    print("== Verifica OpenCode: si apre e interagisce con il modello ==")

    if verifica_comando() is None:
        return 1

    url = avvia_server()
    if url is None:
        return 1

    client = Client(url, leggi_password())
    stato, dati = client.richiesta("GET", "/api/info")
    if stato == 401:
        errore("il server risponde 401: password non trovata in service.json")
        info("riapri `opencode` una volta e rilancia lo script")
        return 1
    if stato != 200 or not isinstance(dati, dict):
        errore(f"/api/info non raggiungibile (HTTP {stato}): {dati}")
        return 1
    ok(f"server OpenCode {dati.get('version', '?')} raggiungibile via API")

    print("\n[3/4] Interazione con il modello")
    modelli = scegli_modelli(client, args.model)
    if not modelli:
        errore("nessun modello disponibile: configura un provider con `opencode`")
        return 1

    ultimo_errore = ""
    for modello in modelli:
        etichetta = (
            f"{modello['providerID']}/{modello['id']}"
            if modello
            else "modello predefinito"
        )
        info(f"provo il modello {etichetta}")
        risultato, motivo = prova_modello(client, modello, args.timeout)
        if risultato is None:
            ultimo_errore = motivo or "errore sconosciuto"
            info(f"non funziona con questo modello: {ultimo_errore}")
            continue

        nonce, risposta = risultato
        ok(f"il modello ha risposto: «{risposta}»")
        if nonce.lower() not in risposta.lower():
            errore("la risposta NON contiene la parola segreta")
            info("il modello ha risposto, ma in modo inaffidabile: riprova")
            return 1
        ok("la risposta contiene la parola segreta → il modello funziona")

        print("\n[4/4] Esito")
        ok("tutto OK: OpenCode si apre E interagisce con il modello")
        print("\nVERIFICA SUPERATA ✅")
        return 0

    print("\n[4/4] Esito")
    errore(f"nessun modello ha superato la verifica. Ultimo errore: {ultimo_errore}")
    info("esegui `opencode` e completa la configurazione di un provider")
    print("\nVERIFICA FALLITA ❌")
    return 1


if __name__ == "__main__":
    sys.exit(main())
