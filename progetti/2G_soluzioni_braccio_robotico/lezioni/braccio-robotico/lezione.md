# Lezione – Il braccio robotico

Durata indicativa: 1–2 ore. Materiale: il progetto in `progetti/braccio-robotico`, la wiki in `wiki/braccio-robotico`.

## Obiettivi

- Capire cos'è un braccio robotico: giunti, gradi di libertà, attuatori.
- Collegare gli angoli dei servo alla posizione della pinza (cinematica diretta).
- Vedere come un'interfaccia diventa un comando seriale per l'Arduino.

## Svolgimento

1. **Introduzione (10 min).** Esempi di bracci robotici nell'industria e nella vita di tutti i giorni. Domanda alla classe: quanti movimenti indipendenti ha un braccio umano?
2. **I giunti e i servo (10 min).** Spalla, gomito, polso, pinza. Ogni giunto ha un angolo.
3. **Dimostrazione della simulazione (15 min).** Si apre `prototipo/index.html`: si muovono i cursori e si guardano le coordinate della pinza.
4. **Cinematica diretta (15 min).** Si ricava la formula di x e y con seno e coseno, partendo da un braccio a un solo segmento.
5. **Dal cursore al comando (10 min).** Si apre «Per curiosi» e si legge la riga `S90 G90 P90 C40`. Si spiega che l'Arduino la riceve sulla porta seriale.
6. **Attività (20 min).** A coppie: portare la pinza a un punto indicato, poi creare una posizione nuova e scriverne il comando.
7. **Chiusura (5 min).** Cosa manca per passare al braccio vero: limiti dei giunti, sicurezza, collegamento seriale o WiFi.

## Domande per la verifica

- Cosa succede alla posizione della pinza se il gomito resta fermo e si muove solo la spalla?
- Perché serve un limite sugli angoli dei giunti?
- Quale informazione contiene la lettera `C` nel comando?

## Esercizi

- Cambiare le lunghezze dei segmenti nel codice e osservare cosa cambia.
- Aggiungere una posizione pronta «Raccogli».
