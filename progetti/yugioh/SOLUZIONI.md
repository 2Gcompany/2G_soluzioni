# 🛠️ Soluzioni e modifiche

Qui raccolgo i problemi che ho incontrato durante lo sviluppo della **Guida Base a Yu-Gi-Oh!**, come li ho risolti e come è cambiato il progetto nel tempo.

---

## 🐞 Problemi e soluzioni

### 1. Pagina quasi vuota: le sezioni non comparivano

- **Cosa succedeva:** aprendo `index.html` si vedeva solo l'intestazione e il resto della pagina restava invisibile.
- **Causa:** le sezioni sono animate e compaiono mentre si scorre, ma questo dipendeva da uno script JavaScript. Lo script cercava due elementi (il pannello per ingrandire le immagini e il pulsante "torna su") che nel file erano scritti **dopo** lo script stesso, quindi non li trovava e si bloccava a metà.
- **Soluzione:** ho spostato quei due elementi prima dello script. Inoltre ho fatto in modo che le sezioni vengano nascoste **solo se lo script arriva fino in fondo senza errori**, così un eventuale problema futuro non rende più illeggibile la pagina.

### 2. Sfondo bianco

- **Cosa succedeva:** la pagina aveva lo sfondo bianco e il testo, chiaro, risultava quasi illeggibile.
- **Causa:** avevo scritto la regola CSS dello sfondo in forma abbreviata e in modo non valido (colore e sfumature nello stesso punto sbagliato), quindi il browser la ignorava.
- **Soluzione:** ho riscritto la regola per esteso, separando il colore di base (`background-color`) dalle sfumature (`background-image`).

### 3. Immagini delle carte che non comparivano

- **Cosa succedeva:** molte carte restavano con il riquadro col nome, senza immagine.
- **Causa:** la pagina chiedeva all'API di YGOPRODeck tutte le carte (una quarantina) nello stesso istante. L'API ha un limite di richieste al secondo e blocca chi lo supera.
- **Soluzione:** ora le richieste partono **una alla volta**, a piccoli intervalli. Le carte già scaricate vengono **salvate nel browser**, così dalla seconda apertura non serve più chiedere nulla.

### 4. Immagine del campo e video che non si vedevano

- **Cosa succedeva:** al posto del campo e dei video comparivano dei riquadri tratteggiati con scritto "da aggiungere", anche se i file erano su GitHub con i nomi giusti.
- **Causa:** avevo aperto `index.html` **direttamente dentro lo ZIP** scaricato da GitHub. In questo modo Windows copia in una cartella temporanea solo quel file e lascia indietro la cartella `assets`.
- **Soluzione:** estrarre prima tutto lo ZIP e poi aprire `index.html` dalla cartella estratta, dove `assets` si trova accanto al file. Controllo utile: nell'indirizzo del browser non devono comparire `Temp` o `.zip`.

### 5. Prime difficoltà con GitHub

- **Problema:** non conoscevo GitHub e non sapevo come organizzare il lavoro.
- **Soluzione:** ho lavorato in un **branch dedicato** (`Yu-Gi-Oh!`), senza toccare `main`, e ho caricato i file direttamente dal sito con **Add file → Upload files**. Per aggiornare un file ho caricato di nuovo quello nuovo con lo stesso nome, che sostituisce il vecchio.

---

## 🔄 Come è cambiato il progetto

| Versione | Modifiche |
|----------|-----------|
| **1. Bozza** | Prima pagina con le sezioni base, tabelle e carte d'esempio prese dall'API |
| **2. Contenuti ampliati** | Fasi del turno spiegate una per una, zone del campo, tipi di evocazione, esempi di mostri Effetto, Tipo e Attributo, Extra Deck dentro la sezione mostri, esempio per ogni tipo di Magia e Trappola, esempi di deck GOAT, modi di vincere e formati ampliati |
| **3. Grafica e contenuti multimediali** | Nuovo stile (tema scuro, menu fisso, barra di avanzamento, animazioni), immagine del campo di Master Duel, un video per ogni modo di vincere, immagini cliccabili per ingrandirle |
| **4. Correzioni** | Risolti i problemi 1, 2 e 3 descritti sopra |

## 💡 Scelta utile: riquadri al posto dei file mancanti

Se l'immagine del campo o un video non vengono trovati, la pagina non si rompe: mostra un riquadro che dice quale file manca e dove va messo. Questo mi ha aiutato a capire subito il problema numero 4.

## 📚 Cosa ho imparato

- come usare un branch e caricare file su GitHub
- che un file HTML che usa altri file (immagini, video) va aperto **con la sua cartella intera**
- che le API hanno dei limiti e va rispettato il numero di richieste
- che un errore in uno script può nascondere tutta la pagina, quindi conviene scrivere il codice in modo che il contenuto resti visibile anche quando qualcosa va storto
