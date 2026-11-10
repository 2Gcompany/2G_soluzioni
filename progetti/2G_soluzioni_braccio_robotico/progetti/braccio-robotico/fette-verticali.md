# Braccio robotico – fette verticali

Il progetto diviso in 10 fette. Ogni fetta si può provare da sola e diventa una issue su GitHub. Le fette della stessa ondata si possono fare in parallelo; si parte da un'ondata solo quando la precedente è finita.

**Definizione di fatto, comune a tutte le fette:** testi in italiano semplice, nessun comando seriale visibile fuori da «Per curiosi», usabile da tastiera, focus sul titolo a ogni cambio schermata, annunci per lettori di schermo, layout corretto a 360 px.

Le persone A–E sono i cinque componenti della squadra. La divisione è una proposta: si può cambiare.

## Ondata 1

### Fetta 1 – Muovi i giunti (Persona A)
Come studente voglio muovere spalla, gomito e polso con dei cursori, così vedo come si muove il braccio.
- Un cursore per giunto, da 0 a 180°, con il valore accanto.
- Il disegno si aggiorna subito.

## Ondata 2 (dopo la fetta 1, in parallelo)

### Fetta 2 – Apri e chiudi la pinza (Persona B)
Come studente voglio aprire e chiudere la pinza, così capisco come si afferra un oggetto.
- Cursore da 0 a 100 %.
- Le dita si allontanano e si avvicinano nel disegno.

### Fetta 3 – Dove è arrivata la pinza (Persona A)
Come studente voglio vedere le coordinate della pinza, così collego gli angoli a un punto.
- x e y in millimetri, aggiornati a ogni movimento.
- Spiegazione della cinematica diretta nel README.

### Fetta 4 – Posizioni pronte (Persona C)
Come studente voglio premere un pulsante per portare il braccio in una posizione nota.
- Riposo, In alto, Afferra, Saluta.
- Movimento dolce; con «riduci movimento» attivo del sistema, lo spostamento è immediato.

### Fetta 5 – Limiti dei giunti (Persona D)
Come studente voglio che il braccio non vada oltre ciò che può fare il braccio vero, così non lo danneggio.
- Limiti per ogni giunto, diversi da 0–180° se serve.
- Avviso chiaro quando si arriva al limite.

### Fetta 6 – Per curiosi: vedi il comando (Persona E)
Come studente voglio vedere la riga che arriverebbe all'Arduino, così imparo il collegamento.
- Sezione richiudibile con il comando, ad esempio `S90 G90 P90 C40`.
- Il comando riflette tutti i cursori.

## Ondata 3 (dopo l'ondata 2)

### Fetta 7 – Raggiungi un punto (Persona A)
Come studente voglio toccare un punto del disegno e vedere il braccio che ci arriva, così capisco la cinematica inversa.
- Clic o tocco sul disegno: il braccio calcola gli angoli.
- Se il punto non si raggiunge, messaggio che lo spiega.

### Fetta 8 – Registra e ripeti (Persona B)
Come studente voglio salvare una sequenza di posizioni e riprodurla.
- «Registra posizione», «Riproduci», «Cancella sequenza».
- La sequenza si può fermare in ogni momento.

### Fetta 9 – Collegamento al braccio vero (Persona D)
Come studente voglio comandare il braccio vero dalla pagina, con la stessa interfaccia.
- Connessione alla porta seriale dal browser, solo dopo conferma esplicita.
- Pulsante «Ferma» sempre visibile.
- Velocità limitata e controllo dei limiti prima di ogni invio.

### Fetta 10 – Comando via WiFi (Persona E)
Come studente voglio comandare il braccio senza cavo, tramite il LOLIN V3.
- Gli stessi comandi della fetta 6, inviati sulla rete locale.
- Stessi controlli di sicurezza della fetta 9.

## Ordine di inizio

1. Fetta 1.
2. Dopo la fetta 1, in parallelo: fette 2, 3, 4, 5, 6.
3. Dopo l'ondata 2, in parallelo: fette 7 e 8.
4. Fetta 9 solo dopo la fetta 5. La fetta 10 solo dopo la fetta 9.

## Stato del prototipo

`prototipo/index.html` contiene una prima versione delle fette 1, 2, 3, 4 e 6. Mancano i limiti (fetta 5) e la parte di accessibilità della definizione di fatto: focus sul titolo, annunci per lettori di schermo e controllo a 360 px.
