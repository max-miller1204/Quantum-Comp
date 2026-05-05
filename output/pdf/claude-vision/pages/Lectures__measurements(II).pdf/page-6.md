If we measure only $B$, then: $\Pr[x] = \text{Tr}\left[(\mathbb{1}_A \otimes \ket{x}\bra{x}_B)\rho_{AB}\right]$, $x \in \{0,1\}$.

If we measure both $A$ & $B$, then: $\Pr[x_1, x_2] = \text{Tr}\left[\underbrace{(\ket{x_1}\bra{x_1}_A \otimes \ket{x_2}\bra{x_2}_B)}_{\ket{x_1, x_2}\bra{x_1, x_2}_{AB}}\rho_{AB}\right]$.

- Suppose we only measure the 1$^{st}$, 3$^{rd}$, and 5$^{th}$ qubits.

[Circuit diagram: 6 qubit lines labeled $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ from top to bottom. Three layers of two-qubit gates separated by dashed vertical lines (1$^{st}$ layer, 2$^{nd}$ layer, 3$^{rd}$ layer). At the end, measurement boxes labeled $x$ on qubits 1, 3, and 5 (drawn in red). Time axis points to the right.]

$(x_1, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

- Let the state before measurement be given by the density operator $\rho_{A_1 A_2 \cdots A_6}$

- The probability distribution is given by:

$$\Pr[x_1, x_2, x_3] = \text{Tr}\left[\left(\ket{x_1}\bra{x_1}_{A_1} \otimes \mathbb{1}_{A_2} \otimes \ket{x_2}\bra{x_2}_{A_3} \otimes \mathbb{1}_{A_4} \otimes \ket{x_3}\bra{x_3}_{A_5} \otimes \mathbb{1}_{A_6}\right) \rho_{A_1 \cdots A_6}\right].$$

$x_1, x_2, x_3 \in \{0,1\}$.

## ③ The Partial Trace

- When we only measure parts of a quantum system, we only need to know the state of that <u>subsystem</u> — we can "ignore" the rest of the system.

- The partial trace describes how (mathematically) to describe ignoring/discarding parts of a system.
