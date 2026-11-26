# For Honor – Parry Trainer

Un semplice allenatore di parry ispirato a *For Honor*, che gira direttamente nel browser: un solo file HTML, nessuna installazione, nessuna dipendenza.

Il reticolo di guardia ha tre direzioni (alto, sinistra, destra) e si controlla con il movimento del mouse. Gli attacchi arrivano da direzioni casuali e devi parare al momento giusto.

## Come si usa

1. Scarica `for-honor-parry-trainer.html` e aprilo con un doppio clic (funziona con Chrome, Edge, Firefox e Safari).
2. **Muovi il mouse** rispetto al centro dello scudo per scegliere la guardia: la sezione selezionata si illumina di blu.
3. Quando compare una sagoma rossa su una delle tre sezioni, si restringe verso lo scudo: l'impatto avviene quando coincide con esso.
4. **Clicca col tasto destro** nel momento dell'impatto, tenendo la guardia nella stessa direzione dell'attacco, per fare il parry.

## Risultati possibili

| Risultato | Significato |
|---|---|
| **PARRY!** | Guardia giusta e click dentro la finestra di parry |
| **Bloccato** | Guardia giusta, ma click mancato (troppo presto, troppo tardi o assente) |
| **COLPITO!** | Guardia nella direzione sbagliata al momento dell'impatto |

In basso trovi i contatori di parry, blocchi, colpi subiti, serie in corso e record.

## Impostazioni

| Opzione | Intervallo | Descrizione |
|---|---|---|
| Tempo di arrivo dell'attacco | 100 – 1200 ms | Quanto impiega l'attacco ad arrivare: più è basso, più è difficile |
| Finestra di parry ± | 20 – 300 ms | Tolleranza del click rispetto all'impatto |
| Pausa tra attacchi | 100 – 2000 ms | Tempo fisso tra la fine di un attacco e l'inizio del successivo |
| Pausa casuale | on/off | Se attiva, la pausa è casuale tra 100 ms e il valore impostato |

## Pubblicarlo con GitHub Pages

1. Rinomina il file in `index.html` (oppure lascia il nome originale e usa l'indirizzo completo del file).
2. Carica il file nel repository.
3. Vai su **Settings → Pages**, scegli il branch `main` e la cartella `/ (root)`, poi salva.
4. Dopo qualche minuto il trainer sarà online all'indirizzo `https://<tuo-utente>.github.io/<nome-repository>/`.

## Note

- Su schermi touch il tocco conta come parry, perché non esiste il tasto destro.
- Il menu contestuale del browser è disattivato all'interno della pagina, per non coprire il gioco.
- Progetto non ufficiale, realizzato da fan: non è affiliato a Ubisoft e *For Honor* è un marchio dei rispettivi proprietari.
