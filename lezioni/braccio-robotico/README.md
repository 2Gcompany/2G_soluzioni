# Braccio robotico – simulazione

Pagina web per capire come si muove un braccio robotico a tre giunti con pinza. Si muovono i cursori e si vede subito dove arriva la pinza. In sottofondo, un giorno, lavorerà il braccio vero comandato da Arduino.

## Come si avvia

```
docker compose up -d --build
```

Poi apri [http://localhost:8080](http://localhost:8080). Per fermare tutto: `docker compose down`.

Senza Docker: fai doppio clic su `prototipo/index.html`.

## Dai cursori ai comandi (parte didattica)

| Cosa muove la persona | Comando seriale | Valori |
| --------------------- | --------------- | ------ |
| Spalla                | `S`             | 0–180° |
| Gomito                | `G`             | 0–180° |
| Polso                 | `P`             | 0–180° |
| Apertura della pinza  | `C`             | 0–100 % |

Esempio di riga inviata all'Arduino: `S90 G90 P90 C40`. La riga si vede nella sezione «Per curiosi» della simulazione.

> Le lettere e i valori sono un esempio. Se il tuo sketch Arduino usa un altro formato, basta cambiare la funzione che prepara il testo in `prototipo/index.html`.

## Come si calcola la posizione della pinza

Ogni segmento parte dalla fine del precedente. Con gli angoli assoluti `a1`, `a2`, `a3` e le lunghezze `L1`, `L2`, `L3`:

```
x = L1·cos(a1) + L2·cos(a2) + L3·cos(a3)
y = L1·sin(a1) + L2·sin(a2) + L3·sin(a3)
```

Questa si chiama cinematica diretta: dagli angoli si ricava il punto.

## Attenzione

La simulazione è **solo grafica**: nessun comando viene inviato a un braccio vero e nessuna porta seriale viene aperta.

## Cosa contiene

`prototipo/index.html` (la simulazione), `Dockerfile` e `compose.yaml` (nginx non-root, filesystem in sola lettura, solo `127.0.0.1:8080`).
