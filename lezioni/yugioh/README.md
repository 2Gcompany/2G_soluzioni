<div align="center">

# 🃏 Guida Base a Yu-Gi-Oh!

**Una guida rapida, chiara e tutta in un file, per capire il gioco in pochi minuti.**

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Stato](https://img.shields.io/badge/stato-in%20sviluppo-orange)

</div>

---

## 📖 Descrizione

Questo progetto è un **sito web in un unico file `index.html`** che funge da guida introduttiva a *Yu-Gi-Oh! Trading Card Game*. È pensato per chi non ha mai giocato o per chi vuole ripassare le basi in modo veloce, senza dover leggere il regolamento completo.

Il file è **eseguibile universalmente**: non richiede installazioni, server o connessione a internet. Basta aprirlo con un qualsiasi browser (Chrome, Firefox, Edge, Safari) su qualsiasi dispositivo.

## ▶️ Come usarlo

1. Scarica il file `index.html` dalla cartella `lezioni/yugioh/`
2. Fai doppio clic sul file
3. Si apre nel browser e puoi consultare la guida

## 🗂️ Contenuti della guida

| # | Sezione | Cosa troverai |
|---|---------|---------------|
| 1 | **Regole base** | Obiettivo del gioco, Life Points, campo di gioco, attacco e danni |
| 2 | **Le fasi del turno** | Draw, Standby, Main 1, Battle, Main 2, End |
| 3 | **Tipi di carte** | Differenze tra mostri, magie e trappole |
| 4 | **Costruire un deck** | Regole di composizione e consigli base |
| 5 | **Extra Deck** | Come funziona e tipi di evocazione: Fusione, Synchro, Xyz, Link, Pendulum |
| 6 | **Modi di vincere** | Life Points a 0, Exodia, Final Countdown, Destiny Board |
| 7 | **Formati competitivi** | Breve presentazione di GOAT ed Edison |

---

## 1️⃣ Regole base

- Ogni giocatore parte con **8000 Life Points (LP)**
- Si vince portando a 0 gli LP dell'avversario (o con una delle condizioni speciali)
- Si gioca con un **Deck** da cui si pescano le carte; all'inizio si hanno **5 carte** in mano
- Una volta per turno si può fare una **Evocazione Normale** (o una Posa di un mostro coperto)
- Il campo comprende zone per i mostri, zone per Magie e Trappole, la zona Campo, il Cimitero e l'Extra Deck
- Quando un mostro attacca, si confrontano i punti: **ATK contro ATK** (il più basso viene distrutto e il proprietario perde la differenza in LP) oppure **ATK contro DEF** (se l'ATK è maggiore il mostro in difesa viene distrutto, senza danni diretti)

## 2️⃣ Le fasi del turno

```
Draw → Standby → Main Phase 1 → Battle → Main Phase 2 → End
```

| Fase | Cosa succede |
|------|--------------|
| **Draw Phase** | Si pesca 1 carta |
| **Standby Phase** | Si attivano gli effetti che avvengono "nella Standby Phase" |
| **Main Phase 1** | Si evocano mostri, si attivano Magie, si posano carte |
| **Battle Phase** | I mostri possono attaccare |
| **Main Phase 2** | Si possono ancora giocare carte dopo la battaglia |
| **End Phase** | Il turno finisce; si scarta fino ad avere massimo **6 carte** in mano |

## 3️⃣ Tipi di carte

### 👹 Mostri

| Tipo | Descrizione |
|------|-------------|
| **Normale** | Ha solo ATK/DEF, nessun effetto |
| **Effetto** | Ha un'abilità speciale, di solito attivabile in momenti precisi |
| **Rituale** | Si evoca con una Magia Rituale sacrificando altri mostri |
| **Pendulum** | Può essere usato come mostro o come Magia nelle zone Pendulum |
| **Extra Deck** | Fusione, Synchro, Xyz e Link (vedi sezione 5) |

### ✨ Magie

| Tipo | Descrizione |
|------|-------------|
| **Normale** | Si usa, ha il suo effetto e va al Cimitero |
| **Veloce (Quick-Play)** | Si può usare anche nel turno dell'avversario, se posata prima |
| **Continua** | Rimane sul campo e il suo effetto dura finché resta lì |
| **Equipaggiamento** | Si collega a un mostro e ne modifica le caratteristiche |
| **Campo** | Cambia le condizioni di tutto il campo, una per giocatore |
| **Rituale** | Serve per evocare i mostri Rituale |

### 🪤 Trappole

| Tipo | Descrizione |
|------|-------------|
| **Normale** | Si posa coperta e si attiva in risposta a un'azione, di solito dal turno successivo |
| **Continua** | Rimane sul campo con un effetto che dura |
| **Contromisura (Counter)** | Molto veloce, serve a rispondere e annullare altre carte |

## 4️⃣ Costruire un deck

- **Main Deck**: da **40 a 60 carte**
- **Extra Deck**: fino a **15 carte**
- **Side Deck**: fino a **15 carte**, usato tra una partita e l'altra
- Massimo **3 copie** della stessa carta (alcune carte sono Limitate a 1 o 2 copie dalla lista ufficiale)
- Consiglio: restare vicino a **40 carte** per pescare più spesso le carte importanti e mantenere una buona **coerenza**, cioè carte che funzionano bene insieme

## 5️⃣ Extra Deck e tipi di evocazione

L'**Extra Deck** è un mazzo separato di mostri speciali, evocati con meccaniche particolari e non pescati normalmente.

| Tipo | Come si evoca |
|------|---------------|
| 🟣 **Fusione** | Si uniscono mostri indicati sulla carta, di solito con *Polymerization* o un effetto simile |
| ⚪ **Synchro** | Si usa 1 mostro **Tuner** + mostri non-Tuner; la somma dei Livelli deve uguagliare il Livello del Synchro |
| ⚫ **Xyz** | Si sovrappongono 2 o più mostri dello **stesso Livello**; i mostri sotto diventano "materiali" da staccare per usare gli effetti |
| 🔵 **Link** | Si usano mostri come materiali in numero pari al Link Rating; non ha Livello né DEF, ma frecce che indicano le zone collegate |
| 🟢 **Pendulum** | Si usano due carte nelle zone Pendulum per evocare più mostri insieme, entro l'intervallo delle loro Scale |

> I Pendulum fanno parte del Main Deck, ma se vengono distrutti scoperti finiscono nell'Extra Deck.

## 6️⃣ Modi di vincere

| Condizione | Come funziona |
|------------|---------------|
| 💔 **Life Points a 0** | La vittoria più comune: gli LP dell'avversario arrivano a 0 |
| 🧩 **Exodia** | Se hai in mano tutti e 5 i pezzi di *Exodia the Forbidden One*, vinci subito |
| ⏳ **Final Countdown** | Paghi 2000 LP: dopo 20 turni, alla End Phase, vinci la partita |
| 🪧 **Destiny Board** | Con *Destiny Board* sul campo, posi uno alla volta gli "Spirit Message" I, N, A, L: quando sono tutti sul campo, vinci |

> Esistono altre condizioni di vittoria, ma sono molto rare e non rientrano in questa guida.

## 7️⃣ Formati competitivi: GOAT ed Edison

Sono due formati **non ufficiali** creati dalla community, che usano le carte e le liste dei Vietati di un periodo passato. Si giocano soprattutto in tornei organizzati dai fan o su simulatori online.

| | **GOAT** | **Edison** |
|---|---|---|
| **Periodo** | Circa 2005 | Circa 2010 |
| **Stile** | Lento e tattico, con pochi mostri e molte carte di controllo | Più veloce, con più opzioni di evocazione |
| **Extra Deck** | Pochi mostri Fusione | Fusione e Synchro |
| **Esempi di mazzi** | Goat Control | Blackwing, Gladiator Beast, Lightsworn |

---

## 🛠️ Tecnologie usate

- **HTML5** per la struttura della pagina
- **CSS3** per lo stile
- **JavaScript** per le parti interattive

## 📁 Struttura del progetto

```
lezioni/
└── yugioh/
    ├── index.html      → la guida (file eseguibile nel browser)
    ├── README.md       → questo file
    └── SOLUZIONI.md    → problemi incontrati, soluzioni e modifiche effettuate
```

## 📝 Soluzioni e modifiche

Tutti i problemi incontrati durante lo sviluppo e le modifiche fatte sono documentati nel file [`SOLUZIONI.md`](./SOLUZIONI.md).

## 👤 Autore

Progetto realizzato come lavoro per la classe 5E dell'ITIS Galileo Galilei.

*Yu-Gi-Oh! è un marchio di Konami. Questo progetto è puramente didattico e non è affiliato a Konami.*
