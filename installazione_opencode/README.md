# 2G Soluzioni

## Installare OpenCode sul terminale di GitHub Codespaces

Questa guida spiega come installare e avviare **OpenCode** nel terminale di un Codespace GitHub.

### Prerequisiti
- Accesso al repository su GitHub (organizzazione 2Gcompany).
- Un Codespace creato per questo repository.
- Connessione di rete dal Codespace verso Internet (eventuali proxy/policy aziendali permettendo).

### 1. Apri il Codespace e il terminale
1. Apri il repository su GitHub.
2. Clicca **Code** → scheda **Codespaces**.
3. Seleziona **Create codespace on main** (o apri un Codespace esistente).
4. Quando l’ambiente è pronto, apri il terminale integrato con **Terminal → New Terminal** oppure con la scorciatoia <kbd>Ctrl</kbd>+<kbd>`</kbd>.

> Puoi aprire più terminali nello stesso Codespace: usa il pulsante `+` nel pannello del terminale oppure **Terminal → Split Terminal** per lavorare in parallelo.

### 2. Installa OpenCode
Nel terminale del Codespace esegui il comando ufficiale di installazione:

Se nel Codespace è disponibile Node.js/npm, puoi installare OpenCode:

```bash
npm install -g opencode-ai
```


### 4. Verifica l’installazione
Controlla che OpenCode sia disponibile:

```bash
opencode --version
```

Se il comando restituisce il numero di versione, l’installazione è completata correttamente.

### 5. Avvia e configura OpenCode
Avvia OpenCode dal terminale:

```bash
opencode
```

Al primo avvio ti potrebbe essere richiesto di:
- selezionare un provider/modello;

Segui le istruzioni mostrate a schermo per completare la configurazione iniziale.

### 6. Verifica che OpenCode risponda davvero (script Python)

`opencode --version` verifica solo che il comando ci sia: non dice se
OpenCode **parla davvero con il modello**. Per questo il repository include
uno script di verifica in Python che:

1. controlla che il comando `opencode` sia installato;
2. controlla che il server HTTP di OpenCode sia attivo (lo avvia se serve);
3. apre una sessione via API, manda un prompt con una **parola segreta**
   e controlla che la risposta del modello contenga quella parola.

Eseguilo dalla root del repository:

```bash
python3 installazione_opencode/verifica_opencode.py
```

Se tutto funziona vedi `VERIFICA SUPERATA ✅` e lo script esce con codice `0`,
altrimenti `VERIFICA FALLITA ❌` e codice `1`.

Opzioni utili:

```bash
# prova un modello specifico (formato PROVIDER/MODELLO)
python3 installazione_opencode/verifica_opencode.py --model opencode/big-pickle

# attende più a lungo la risposta (secondi, default 120)
python3 installazione_opencode/verifica_opencode.py --timeout 180
```

Lo script usa solo la libreria standard di Python: non serve installare
alcun pacchetto con `pip`.

### Risoluzione problemi
- **`opencode: command not found`**: esegui di nuovo `source ~/.bashrc` (o riapri il terminale) e verifica che la directory di installazione sia nel `PATH`.
- **Errore durante il download/installazione**: verifica la connettività del Codespace ed eventuali proxy o restrizioni di rete aziendali; se necessario contatta il team DevOps/IT di 2Gcompany.
- **Codespace ricreato**: se il Codespace viene eliminato e ricreato da zero, potrebbe essere necessario reinstallare OpenCode.

### Riferimenti
- Documentazione ufficiale: [https://opencode.ai/docs/](https://opencode.ai/docs/)
