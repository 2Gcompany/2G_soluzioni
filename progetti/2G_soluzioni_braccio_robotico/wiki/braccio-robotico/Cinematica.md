# Cinematica

Ogni segmento parte dalla fine del precedente. Con gli angoli assoluti `a1`, `a2`, `a3` e le lunghezze `L1`, `L2`, `L3`:

```
x = L1·cos(a1) + L2·cos(a2) + L3·cos(a3)
y = L1·sin(a1) + L2·sin(a2) + L3·sin(a3)
```

Nella simulazione l'angolo del cursore 90° significa «il segmento prosegue dritto»:

```
a1 = spalla
a2 = a1 + (gomito - 90)
a3 = a2 + (polso - 90)
```

Questa è la **cinematica diretta**: dagli angoli si ricava il punto. La **cinematica inversa** fa il contrario (dal punto agli angoli) ed è la fetta 7 del piano.
