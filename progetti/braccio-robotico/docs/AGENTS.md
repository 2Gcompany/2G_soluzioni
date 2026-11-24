# Istruzioni per l'agente – braccio robotico

## Contesto

Simulazione web di un braccio robotico a tre giunti con pinza, pensata per una lezione. Il braccio vero è stampato in 3D e comandato da un Arduino che riceve comandi seriali. Il piano del lavoro è in `fette-verticali.md`.

## Stato

`prototipo/index.html` è un unico file HTML senza dipendenze. Contiene una prima versione delle fette 1, 2, 3, 4 e 6. Mancano la fetta 5 (limiti dei giunti) e la parte di accessibilità della definizione di fatto.

## Ordine di inizio

1. Fetta 1.
2. In parallelo: fette 2, 3, 4, 5, 6.
3. In parallelo: fette 7 e 8.
4. Fetta 9 dopo la fetta 5. Fetta 10 dopo la fetta 9.

## Definizione di fatto

Testi in italiano semplice, nessun comando seriale visibile fuori da «Per curiosi», usabile da tastiera, focus sul titolo a ogni cambio schermata, annunci per lettori di schermo, layout corretto a 360 px.

## Regole

- Il formato dei comandi (`S G P C`) è un esempio. Prima di collegare il braccio vero si confronta con lo sketch Arduino reale e si adatta la funzione che prepara il testo.
- Finché non si arriva alle fette 9 e 10, la simulazione non apre nessuna porta seriale e non invia nulla in rete.
- Dalle fette 9 e 10 in poi: connessione solo dopo conferma esplicita, pulsante «Ferma» sempre visibile, angoli sempre dentro i limiti, velocità limitata.
- Un solo file HTML, senza librerie esterne, finché non c'è un motivo per cambiare.
