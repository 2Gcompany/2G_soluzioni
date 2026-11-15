# 🧭 Scelte progettuali

Qui spiego perché ho sviluppato la **Guida Base a Yu-Gi-Oh!** in questo modo.

---

## 1. Argomento e obiettivo

Ho scelto Yu-Gi-Oh! perché è un gioco che conosco e che mi appassiona, ed ha molte regole e tipi di carte che si prestano bene a una guida. L'obiettivo è una guida **per principianti**, chiara e riassunta ma abbastanza completa: regole base, fasi del turno, tipi di carte, Extra Deck, costruzione del deck, modi di vincere e formati GOAT ed Edison. Ho lasciato fuori le regole più tecniche e le condizioni di vittoria molto rare, per non appesantire la lettura.

## 2. Perché HTML, CSS e JavaScript

Volevo un programma che funzionasse **ovunque**, senza installare nulla. Un sito in HTML si apre con qualsiasi browser, su qualsiasi dispositivo, con un semplice doppio clic su `index.html`, ed è adatto a una guida da consultare.

| Linguaggio | Ruolo nel progetto |
|------------|--------------------|
| **HTML** | Struttura e contenuti |
| **CSS** | Colori, tabelle, animazioni, adattamento ai telefoni |
| **JavaScript** | Immagini delle carte, ingrandimento delle immagini, barra di avanzamento |

Ho tenuto tutto in **un solo file** per renderlo facile da condividere e da correggere.

## 3. Immagini delle carte tramite API

Scaricare tutte le immagini avrebbe appesantito il progetto, quindi uso l'**API gratuita di YGOPRODeck**. I compromessi:

- serve internet per vedere le carte (senza, compare un riquadro col nome)
- l'API limita le richieste al secondo, quindi la pagina carica le carte **una alla volta** e **ricorda** quelle già viste

## 4. Immagine e video da Master Duel

Per far capire meglio il gioco ho inserito un'**immagine del campo** nella sezione delle zone e un **breve video per ogni modo di vincere**, con l'animazione di fine partita. Questi file stanno nella cartella `assets`, perché i video sono troppo pesanti per stare dentro `index.html`.

## 5. Grafica e usabilità

Ho scelto un tema scuro con dettagli dorati e viola, per richiamare l'atmosfera del gioco. Ho aggiunto un menu fisso, una barra di avanzamento e un layout adatto anche agli schermi piccoli. Tutte le immagini sono **cliccabili** per ingrandirle, perché le carte piccole sono difficili da leggere.

## 6. Limiti

- le carte richiedono la connessione a internet
- la cartella `assets` deve restare accanto a `index.html`
- le liste dei mazzi GOAT ed Edison sono semplificate, non sono decklist ufficiali

## 7. Strumenti utilizzati

Mi sono aiutato con l'intelligenza artificiale (Claude) per scrivere il codice e organizzare i contenuti. Argomento, struttura e contenuti sono scelte mie, e ho provato personalmente il risultato.

---

📝 I problemi incontrati e le modifiche fatte sono in [`SOLUZIONI.md`](./SOLUZIONI.md).
