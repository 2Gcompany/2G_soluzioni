# AGENTS.md: istruzioni per l'agente (progetto `yugioh`)

Questo file è scritto per un assistente IA. Serve a due cose:
1. farti **imparare le basi di Yu-Gi-Oh!**, l'argomento del progetto
2. farti **aiutare la persona che prende in mano il progetto**, che sia per iniziare o per migliorarlo

La persona potrebbe essere un principiante assoluto di GitHub e di programmazione: spiega ogni passaggio in modo semplice e **rispondi in italiano**.

---

## 1. Cos'è il progetto

Una **guida per principianti a Yu-Gi-Oh! Trading Card Game**, realizzata come sito statico in un **unico file `index.html`** (HTML + CSS + JavaScript, nessuna libreria, nessuna installazione). Si apre con un doppio clic nel browser.

Cartella: `progetti/yugioh/`

| File | Contenuto |
|------|-----------|
| `index.html` | Tutta la guida: contenuti, stile e script |
| `assets/campo-master-duel.jpg` | Immagine del campo da Yu-Gi-Oh! Master Duel (sezione "Regole base") |
| `assets/video/*.mp4` | Un video per ogni modo di vincere: `life-points`, `exodia`, `final-countdown`, `destiny-board` |
| `README.md` | Presentazione del progetto |
| `SCELTE.md` | Perché il sito è fatto in questo modo |
| `SOLUZIONI.md` | Problemi incontrati, soluzioni e cronologia delle versioni |
| `AGENTS.md` / `CLAUDE.md` | Queste istruzioni |

Sezioni della pagina (id): `regole`, `turno`, `carte`, `deck`, `vittoria`, `formati`.

---

## 2. Yu-Gi-Oh! in breve (per imparare l'argomento)

**Obiettivo:** portare gli **Life Points (LP)** dell'avversario da 8000 a 0, o vincere con una condizione speciale.

**Preparazione:** si pescano 5 carte. Chi gioca per primo non pesca nel primo turno e non attacca. Chi deve pescare con il mazzo vuoto perde.

**Composizione del mazzo:** Main Deck 40-60 carte, Extra Deck 0-15, Side Deck 0-15, massimo 3 copie per carta (alcune sono Limitate a 1 o Semi-Limitate a 2 dalla lista del formato).

**Zone del campo:** 5 Zone Mostri (+ 2 Zone Mostri Extra), 5 Zone Magie/Trappole, Zona Campo, Cimitero (carte distrutte o usate, pubblico), Zona Bandita (carte rimosse dal gioco, più definitiva del Cimitero), Deck ed Extra Deck.

**Fasi del turno, nell'ordine:** Draw → Standby → Main Phase 1 → Battle → Main Phase 2 → End. In End Phase si scartano le carte oltre le 6 in mano. Ogni mostro attacca una sola volta per turno, salvo effetti.

**Evocazioni:**
- *Normale*: una volta per turno dalla mano. Livello 5-6 richiede 1 Tributo, Livello 7+ ne richiede 2
- *Posa (Set)*: mostro coperto in Difesa, conta come Evocazione Normale
- *Flip*: si gira un mostro coperto
- *Speciale*: senza limiti per turno, solo tramite effetti

**Combattimento:** ATK contro ATK, il più basso viene distrutto e il suo proprietario perde la differenza. ATK contro DEF: se ATK > DEF il mostro in difesa è distrutto senza danni, se ATK < DEF chi attacca perde la differenza.

**Tipi di carte:**
- *Mostri del Main Deck:* Normale, Effetto (Flip, all'evocazione, da Cimitero, Rapido...), Rituale, Pendulum
- *Mostri dell'Extra Deck:* Fusione (Polymerization o simili), Synchro (Tuner + non-Tuner, Livelli sommati), Xyz (stesso Livello, Rango, materiali da staccare), Link (Link Rating, frecce)
- *Magie:* Normale, Veloce, Continua, Equipaggiamento, Campo, Rituale
- *Trappole:* Normale, Continua, Contromisura (Counter). Non si attivano nel turno in cui sono poste
- Ogni mostro ha anche un **Tipo** (Drago, Incantatore, Macchina...) e un **Attributo** (LUCE, OSCURITÀ, TERRA, ACQUA, FUOCO, VENTO, DIVINO)

**Modi di vincere trattati:** LP a 0, Exodia the Forbidden One (5 pezzi in mano), Final Countdown (20 turni dopo aver pagato 2000 LP), Destiny Board (Spirit Message I, N, A, L).

**Formati:** *GOAT* (circa 2005, solo Fusione nell'Extra Deck, stile lento e di controllo) ed *Edison* (circa 2010, Fusione e Synchro, più veloce). Sono formati non ufficiali della community.

**Regola d'oro:** non inventare mai il testo o gli effetti di una carta. Verificalo sull'API (vedi sotto) prima di scriverlo. Se non sei sicuro, dillo.

---

## 3. Come è fatto il codice

### Carte d'esempio
Sono elementi `<div class="ex" data-cards="...">`. Formato: `Etichetta|Nome carta|Descrizione effetto;Etichetta|Nome carta|Descrizione`.
- il nome deve essere **identico a quello inglese ufficiale** (serve per cercarlo nell'API)
- nella descrizione **non usare i caratteri `;` e `|`** (sono i separatori)
- lo script `creaCarta` crea il riquadro con l'immagine

### Immagini delle carte: API YGOPRODeck
Endpoint: `https://db.ygoprodeck.com/api/v7/cardinfo.php?name=NOME`.
- **limite: 20 richieste al secondo**, oltre si viene bloccati (circa un'ora). Per questo le richieste passano da una coda (`accoda`) con 150 ms di pausa e i risultati sono salvati nel `localStorage` (chiave `ygo`). **Non rimuovere la coda e non fare richieste in parallelo**
- se l'immagine non carica, resta un riquadro col nome

### Immagine e video
Elementi `<figure class="media" data-img="..." data-video="..." data-caption="...">`. Lo script crea `<img>` o `<video>`. Se il file manca, mostra un riquadro tratteggiato con il percorso atteso.

### Ingrandimento
Ogni `<img>` dentro `.ex` o `.media` si apre nel pannello `#lb` al clic. Per le carte si usa l'immagine grande (`data-big`).

### Stile
Variabili CSS in `:root`. Tema scuro con dettagli dorati (`--gold`) e viola (`--accent`).

---

## 4. Errori già fatti: non ripeterli

- **Ordine nel file:** gli elementi `#lb` e `#top` devono stare **prima** dello `<script>`, altrimenti lo script si blocca e la pagina resta vuota
- **Animazione delle sezioni:** la classe `js` che le nasconde viene aggiunta solo a fine script. Non spostarla in testa alla pagina
- **Sfondo:** non scrivere `background` in forma abbreviata mescolando colore e gradienti. Usa `background-color` e `background-image` separati
- **Apertura del file:** `index.html` va aperto da una cartella **estratta**, mai dentro lo ZIP, altrimenti `assets` non si trova
- **Testo:** usare l'apostrofo tipografico `’` nel testo visibile

Dettagli in `SOLUZIONI.md`.

---

## 5. Come lavorare (workflow)

1. Lavora sempre su un **branch**, mai direttamente su `main`
2. Modifica `index.html`, poi **provalo** aprendolo da una cartella estratta, con `assets` accanto
3. Controlla che tutte le immagini delle carte compaiano e che le sezioni siano visibili
4. Fai un commit con un messaggio chiaro, in italiano (se il repo ha la skill `commit` in `.claude/skills/commit`, usala)
5. Aggiorna `SOLUZIONI.md` (problema, causa, soluzione, nuova versione) e `SCELTE.md` se cambi una decisione di progetto
6. Apri o aggiorna la **pull request** verso `main`

Se la persona non sa usare GitHub, guidala: ad esempio **Add file → Upload files** per caricare un file nello stesso branch, e **Code → Download ZIP** per scaricare il progetto.

---

## 6. Idee per migliorare

- un **quiz** finale per verificare cosa si è imparato
- un **contatore di Life Points** interattivo
- una pagina o sezione sul **Damage Step** e sulle **velocità delle carte (Spell Speed)**
- altre carte d'esempio, o la scelta di una carta casuale
- scaricare le immagini in `assets` per non dipendere da internet e dall'API
- una versione in inglese
- una ricerca nella pagina e un indice con link ai singoli argomenti
- verificare con liste ufficiali i mazzi GOAT ed Edison, che oggi sono **semplificati**

## 7. Limiti noti

- le carte richiedono internet
- le liste dei mazzi GOAT ed Edison e le date dei formati sono approssimative
- la guida è un'introduzione, non sostituisce il regolamento ufficiale
