# Backup Foto – prototipo cliccabile

Interfaccia amichevole per copiare le foto da scheda SD o fotocamera a un disco di backup,
pensata per un fotografo che non vuole vedere comandi. In sottofondo, un giorno, lavorerà `rsync`.

## Come si avvia

```
docker compose up -d --build
```
Poi apri http://localhost:8080 . Per fermare tutto: `docker compose down`.

Senza Docker: fai doppio clic su `prototipo/index.html`.

## Dalle scelte della persona ai comandi (parte didattica)

| Cosa sceglie la persona                       | Opzione rsync                          |
|-----------------------------------------------|----------------------------------------|
| Copia solo le foto nuove (predefinito)        | `-a` (copia tutto e salta ciò che non è cambiato) |
| Rispecchia esattamente la sorgente            | `--delete` (cancella dal backup ciò che non c'è più) |
| Controlla che ogni copia sia perfetta         | `-c` (confronta il contenuto, più lento) |
| Ignora i file di sistema nascosti             | `--exclude='.DS_Store'` `--exclude='Thumbs.db'` |
| Controlla prima di copiare (anteprima)        | `-n` (prova senza copiare niente)      |
| Barra di avanzamento e percentuale            | `--info=progress2`                     |
| Da dove / Dove le salvo                       | i due percorsi in fondo al comando     |

Il comando si vede nella sezione «Per curiosi» dell'anteprima e della schermata finale.

## Attenzione

L'interfaccia è ancora **simulata**: dati finti, nessun `rsync` reale viene eseguito
e nessun file viene toccato. La copia dura pochi secondi solo per la dimostrazione.

## Cosa contiene

`prototipo/index.html` (l'interfaccia), `Dockerfile` e `compose.yaml` (nginx non-root,
filesystem in sola lettura, solo `127.0.0.1:8080`).
