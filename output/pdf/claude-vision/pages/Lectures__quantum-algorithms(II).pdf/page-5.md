- **Example**: Superdense coding: using entanglement + 1 qubit to transmit 2 classical bits.

[Diagram: Alice and Bob share entangled state $\ket{\Phi^+}_{AB}$. Alice applies $X^x$ then $Z^z$ on her qubit (boxed: "Encoding bits z, x into one qubit."), then sends to Bob who performs a Bell measurement to recover $(x,z)$.]

② **The Swap test**

✻ How do we estimate the inner product of two (unknown) states on a quantum computer?

- **The swap gate**:

[Circuit: $\ket{\psi}$ and $\ket{\phi}$ enter a SWAP box; outputs are $\ket{\phi}$ and $\ket{\psi}$.]

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{1}\ket{0}$$
$$\ket{1}\ket{0} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}\ket{1}$$

As a matrix:

$$\begin{array}{c|cccc} & 00 & 01 & 10 & 11 \\ \hline 00 & 1 & 0 & 0 & 0 \\ 01 & 0 & 0 & 1 & 0 \\ 10 & 0 & 1 & 0 & 0 \\ 11 & 0 & 0 & 0 & 1 \end{array}$$

- **Circuit for the SWAP test**

[Circuit: top wire $\ket{0} - H - \bullet - H - X -$ (measurement); middle wire $\ket{\psi}$ and bottom wire $\ket{\phi}$ enter a SWAP gate controlled by the top qubit.]
