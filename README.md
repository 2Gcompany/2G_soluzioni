# 2G Soluzioni

## Installare OpenCode sul terminale di GitHub Codespaces

Questa guida spiega come installare e avviare **OpenCode** nel terminale di un Codespace GitHub.

### Prerequisiti
- Accesso al repository su GitHub (organizzazione 2Gcompany).
- Un Codespace creato per questo repository.
- Connessione di rete dal Codespace verso Internet (eventuali proxy/policy aziendali permettendo).

### 1. Apri il Codespace e il terminale
1. Apri il repository su GitHub.
2. Clicca **Code** → scheda **Codespaces**.
3. Seleziona **Create codespace on main** (o apri un Codespace esistente).
4. Quando l’ambiente è pronto, apri il terminale integrato con **Terminal → New Terminal** oppure con la scorciatoia <kbd>Ctrl</kbd>+<kbd>`</kbd>.

> Puoi aprire più terminali nello stesso Codespace: usa il pulsante `+` nel pannello del terminale oppure **Terminal → Split Terminal** per lavorare in parallelo.

### 2. Installa OpenCode
Nel terminale del Codespace esegui il comando ufficiale di installazione:

```bash
curl -fsSL https://opencode.ai/install | bash
```

Lo script installa OpenCode per l’utente corrente (di solito nella directory `~/.opencode/bin`).

#### Alternativa con npm
Se nel Codespace è disponibile Node.js/npm, puoi installare OpenCode anche così:

```bash
npm install -g opencode-ai
```

### 3. Aggiorna il PATH della sessione corrente
Per usare subito il comando `opencode` senza chiudere il terminale, ricarica la configurazione della shell:

```bash
source ~/.bashrc
```

Se utilizzi `zsh`, esegui invece:

```bash
source ~/.zshrc
```

### 4. Verifica l’installazione
Controlla che OpenCode sia disponibile:

```bash
opencode --version
```

Se il comando restituisce il numero di versione, l’installazione è completata correttamente.

### 5. Avvia e configura OpenCode
Avvia OpenCode dal terminale:

```bash
opencode
```

Al primo avvio ti potrebbe essere richiesto di:
- selezionare un provider/modello;
- configurare le credenziali (es. API key o accesso al provider), in base al servizio scelto.

Segui le istruzioni mostrate a schermo per completare la configurazione iniziale.

### Risoluzione problemi
- **`opencode: command not found`**: esegui di nuovo `source ~/.bashrc` (o riapri il terminale) e verifica che la directory di installazione sia nel `PATH`.
- **Errore durante il download/installazione**: verifica la connettività del Codespace ed eventuali proxy o restrizioni di rete aziendali; se necessario contatta il team DevOps/IT di 2Gcompany.
- **Codespace ricreato**: se il Codespace viene eliminato e ricreato da zero, potrebbe essere necessario reinstallare OpenCode.

### Riferimenti
- Documentazione ufficiale: [https://opencode.ai/docs/](https://opencode.ai/docs/)
