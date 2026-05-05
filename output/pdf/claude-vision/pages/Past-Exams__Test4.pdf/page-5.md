5. Let us use the following notation for the swap gate:

[Swap gate symbol: two X's connected by a vertical line]

Show that the swap gate can be written in terms of three CNOT gates as follows:

[Circuit equation: SWAP = CNOT (control top, target bottom) · CNOT (control bottom, target top) · CNOT (control top, target bottom)]

CNOT:

$\ket{00} \to \ket{00}$

$\ket{01} \to \ket{01}$

$\ket{10} \to \ket{11}$

$\ket{11} \to \ket{10}$

Swap:

$\ket{00} \to \ket{00}$

$\ket{01} \to \ket{10}$

$\ket{10} \to \ket{01}$

$\ket{11} \to \ket{11}$

for $\ket{00}$:

$\ket{00} \xrightarrow{\text{CNOT 1}} \ket{00} \xrightarrow{\text{CNOT 2}} \ket{00} \xrightarrow{\text{CNOT 3}} \ket{00}$

for $\ket{01}$:

$\ket{01} \xrightarrow{\text{CNOT 1}} \ket{01} \xrightarrow{\text{CNOT 2}} \ket{11} \xrightarrow{\text{CNOT 3}} \ket{10}$

for $\ket{10}$:

$\ket{10} \xrightarrow{\text{CNOT 1}} \ket{11} \xrightarrow{\text{CNOT 2}} \ket{01} \xrightarrow{\text{CNOT 3}} \ket{01}$ ✓

for $\ket{11}$:

$\ket{11} \xrightarrow{\text{CNOT 1}} \ket{10} \xrightarrow{\text{CNOT 2}} \ket{10} \xrightarrow{\text{CNOT 3}} \ket{11}$

6
