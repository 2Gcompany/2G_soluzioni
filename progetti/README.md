# Guida Pokémon: tipi, statistiche e mosse

Sito web didattico in un unico file HTML che insegna le basi del combattimento nei giochi Pokémon.

## Cosa contiene

- **Le basi** di un combattimento (velocità, tipi, categoria delle mosse)
- **I 18 tipi** con colori e immunità principali
- **Doppi tipi e debolezze x4 / resistenze x0,25**, con un calcolatore interattivo
- **Tabella completa** dell'efficacia dei tipi (superefficace, poco efficace, immunità)
- **Statistiche**: statistiche base, IV, EV, livello, con formule e calcolatore
- **Nature**: tabella delle 25 nature (+10% / −10%) e scelte consigliate
- **Mosse fisiche, speciali e di stato**, STAB, priorità, colpi critici, scottatura
- **Formula del danno** e consigli per iniziare

## Come usarlo

1. Scarica `index.html`.
2. Aprilo con un doppio clic nel browser (non servono server, librerie o connessione).

## Pubblicarlo online (GitHub Pages)

1. Crea un repository su GitHub e carica `index.html` e `README.md`.
2. Vai in **Settings → Pages**.
3. In *Source* scegli il branch `main` e la cartella `/ (root)`, poi salva.
4. Dopo qualche minuto il sito sarà online all'indirizzo indicato da GitHub.

## Struttura

```
.
├── index.html   # il sito (HTML + CSS + JavaScript in un solo file)
└── README.md    # questo file
```

## Note

- La tabella dei tipi segue le regole attuali (dalla sesta generazione, con il tipo Folletto).
- Le formule delle statistiche e del danno sono quelle dei giochi principali.
- Progetto non ufficiale e a scopo educativo. Pokémon è un marchio di Nintendo, Game Freak e The Pokémon Company.
