# Layer Lab – Stampa 3D

Sito interattivo che spiega la **stampa 3D** (manifattura additiva) agli studenti di quarta superiore.
È una pagina unica, senza librerie da installare: basta aprire `index.html` in un browser
(doppio clic sul file, nessun server necessario).

## Contenuto

Undici "strati" (sezioni):

1. Il quadro generale: additivo, sottrattivo, formativo e storia
2. Dal file all'oggetto: il flusso di lavoro, con gioco di ordinamento
3. Anatomia di una stampante FDM
4. G-code: editor con anteprima del percorso
5. Slicer Lab: tempo, peso e qualità
6. Tecnologie: FDM, SLA, SLS, metallo
7. Materiali e test del caldo
8. Applicazioni nel mondo reale
9. Pronto soccorso stampa: diagnosi dei difetti
10. Quiz finale con grado
11. Sicurezza, ambiente, responsabilità e glossario

## Cosa contiene

`index.html` (pagina completa: HTML, CSS e JavaScript in un unico file).

## Pubblicare su GitHub Pages

1. Su github.com clicca **New repository**, scegli un nome (per esempio `layer-lab`) e lascia **Public**.
2. Nel repository clicca **uploading an existing file**, trascina `index.html` e `README.md`, poi **Commit changes**.
3. Vai in **Settings → Pages**. In *Build and deployment* scegli **Deploy from a branch**, branch `main`, cartella `/ (root)`, poi **Save**.
4. Dopo uno o due minuti il sito è online su `https://IL-TUO-UTENTE.github.io/layer-lab/`.

## Note tecniche

- Tutto il codice (HTML, CSS, JavaScript) è dentro `index.html`.
- I font (Unbounded, Figtree, JetBrains Mono) arrivano da Google Fonts. Senza connessione la pagina usa i font di sistema e funziona lo stesso.
- Funziona su computer e telefono, con tema chiaro e scuro.
- I valori numerici dei simulatori sono semplificati a scopo didattico.
