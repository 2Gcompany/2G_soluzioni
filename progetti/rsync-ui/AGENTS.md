# Backup Foto (rsync-ui) – istruzioni per l'agente

Interfaccia per copiare le foto da scheda SD o fotocamera a un disco di backup, per un
fotografo che non vuole vedere comandi. Sotto c'è `rsync`. Progetto della mini startup della
classe 5D dell'ITIS Galileo Galilei.

## Stato attuale

- `prototipo/index.html` è un prototipo **simulato**: dati finti (`SOURCES`, `DESTINATIONS`,
  `PREVIEW`…), nessun `rsync` eseguito, nessun file toccato. È il riferimento per testi,
  schermate e comportamento.
- `buildCommand()` nel prototipo mostra come le scelte diventano opzioni `rsync`.
- Docker serve solo il prototipo statico (nginx non-root, sola lettura, `127.0.0.1:8080`).
- Lo stack per l'`rsync` reale non è ancora deciso: non sceglierlo da solo, chiedi.

## Da dove partire

- `fette-verticali.md`: il lavoro diviso in 13 fette. Ognuna attraversa interfaccia → logica →
  `rsync` reale ed è rilasciabile da sola. Ogni fetta ha storia, criteri e dipendenze.
- Le fette sono anche issue GitHub `[rsync-ui] …` su `panicerid/2G_soluzioni`: il numero
  dell'issue è il numero della fetta.
- `README.md`: avvio e tabella scelte → opzioni `rsync`.

Lavora su **una fetta alla volta**. Prima di iniziare controlla che le sue dipendenze siano fatte.

## Ordine e parallelismo

1. **#1 Copia minima**, da sola: fissa interfaccia, chiamata a `rsync` e lettura dell'esito.
2. Dopo la #1, in parallelo: #2, #3, #4, #5, #6, #7.
3. Dopo la #3: #8, #9, #10. Dopo la #4: #11, #12, #13. Non serve aspettare tutta l'ondata 2.

Punti di contatto:
- #5, #8, #9 aggiungono opzioni allo stesso comando `rsync` e al passo 3: tieni una sola
  funzione che costruisce il comando, come `buildCommand()`.
- #10 mostra quel comando: va chiusa dopo #5, #8, #9.
- #11 e #12 toccano gli stessi controlli dell'avanzamento.
- #13 completa l'esito «Da riprendere» della #6.

## Definizione di fatto (tutte le fette)

- Testi in italiano semplice, rivolti al fotografo.
- Nessun comando visibile fuori dalla sezione «Per curiosi».
- Usabile da tastiera; focus sul titolo a ogni cambio schermata.
- Annunci per lettori di schermo.
- Layout corretto a 360 px.

## Regole

- `rsync -n` (anteprima) non deve mai copiare; `--delete` solo dopo conferma esplicita (#8).
- Non cancellare o sovrascrivere foto fuori dalla destinazione scelta.
- Testa con cartelle di prova, mai con dischi o foto reali.
- Codice e nomi coerenti con il prototipo; cambi minimi, solo quello che la fetta chiede.
