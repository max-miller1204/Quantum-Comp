## ② Superdense Coding

✱ **Teleportation**: using entanglement + classical information to transmit quantum information.

✱ We can also use entanglement to transmit classical information!

- **Superdense coding**: using entanglement + 1 qubit to transmit 2 classical bits.

[Diagram: Alice and Bob share entangled state $\ket{\Phi^+}_{AB}$. Alice's qubit (red line) goes through gates $X^x$ then $Z^z$ (boxed: "Encoding bits $z, x$ into one qubit."), with classical control inputs $x$ and $z$. The qubit is then sent to Bob, who performs a Bell Measurement on both qubits, obtaining outcome $(x, z)$.]

(1) • To encode $(0,0)$: $\underbrace{(Z^0 X^0 \otimes \mathbb{1})}_{=\mathbb{1}}\ket{\Phi^+}_{AB} = \ket{\Phi^+}_{AB}$  (Alice does nothing).
$\quad\;\;(z, x)$

- To encode $(0,1)$: $\underbrace{(Z^0 X^1 \otimes \mathbb{1})}_{=X}\ket{\Phi^+}_{AB} = (X \otimes \mathbb{1}) \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B)$

(Alice applies $X$ to her qubit.) 
$\qquad\qquad\qquad\qquad\quad = \tfrac{1}{\sqrt{2}}(X\ket{0}_A\ket{0}_B + X\ket{1}_A\ket{1}_B)$

$\qquad\qquad\qquad\qquad\quad = \tfrac{1}{\sqrt{2}}(\ket{1}_A\ket{0}_B + \ket{0}_A\ket{1}_B)$

$\qquad\qquad\qquad\qquad\quad = \ket{\Psi^+}_{AB}$

- To encode $(1,0)$: $\underbrace{(Z^1 X^0 \otimes \mathbb{1})}_{=Z}\ket{\Phi^+}_{AB} = (Z \otimes \mathbb{1}) \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B)$
