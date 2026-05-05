(d) If $\ket{a} = \ket{-}$ and $\ket{b} = \ket{-}$, then find the resulting state at the end of the circuit.

(e) Using your answers to the previous parts, explain why this circuit calculates the parity of the first two qubits in the $X$ basis.

8. Prove that $U_1 := Z^{-1/4} X^{1/4}$ and $U_2 := H^{-1/2} Z^{-1/4} X^{1/4} H^{1/2}$ can be written solely as a product of $H$ and $T$. Recall that $H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ and $T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$.

9. Let us use the following notation for the swap gate:

$$\text{[swap gate symbol: two crosses connected vertically]} \tag{79}$$

Show that the swap gate can be written in terms of three CNOT gates as follows:

$$\text{[swap]} = \text{[CNOT with control on top, target bottom; then CNOT with control bottom, target top; then CNOT with control on top, target bottom]} \tag{80}$$

10. Show that the controlled-$Z$ gate can be written in terms of the Hadamard gate and the CNOT gate as follows:

$$\text{[controlled-Z gate]} = \text{[H on target, then CNOT, then H on target]} \tag{81}$$

11. Show that the control and target qubits of the CNOT gate can be changed by adding Hadamard gates before and after as follows:

$$\text{[CNOT with control on bottom, target on top]} = \text{[H on both wires, then CNOT (control top, target bottom), then H on both wires]} \tag{82}$$

12. Prove the following circuit identities.

(a) $\text{CNOT}(X \otimes \mathbb{1}) = (X \otimes X)\text{CNOT}$.

$$\text{[X on top wire, then CNOT (control top, target bottom)]} = \text{[CNOT, then X on both top and bottom wires]} \tag{83}$$

(b) $\text{CNOT}(\mathbb{1} \otimes X) = (\mathbb{1} \otimes X)\text{CNOT}$.

$$\text{[X on bottom wire, then CNOT]} = \text{[CNOT, then X on bottom wire]} \tag{84}$$

(c) $\text{CNOT}(Z \otimes \mathbb{1}) = (Z \otimes \mathbb{1})\text{CNOT}$.

$$\text{[Z on top wire, then CNOT]} = \text{[CNOT, then Z on top wire]} \tag{85}$$

19
