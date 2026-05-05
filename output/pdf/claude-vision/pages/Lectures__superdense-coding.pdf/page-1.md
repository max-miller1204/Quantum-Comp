# ① Recap: Quantum teleportation

- A method to send arbitrary quantum information using entanglement and two bits of classical information.

[Diagram: Alice holds $\ket{\psi}_{A'}$ and one half of the entangled pair $\ket{\Phi^+}_{AB}$. She performs a Bell measurement on her two qubits, obtaining outcomes $x \in \{0,1\}$ and $z \in \{0,1\}$. These two classical bits are sent to Bob, who applies $X^x$ then $Z^z$ to his half of $\ket{\Phi^+}_{AB}$ to recover $\ket{\psi}_B$.]

- If $x=0$, do nothing; if $x=1$, apply $X$.
- If $z=0$, do nothing; if $z=1$, apply $Z$.

✱ Teleportation is **not** instantaneous / faster than light — it only works if Bob gets Alice's measurement outcomes → this takes time!

- The **Bell measurement** is a critical component.
  It is given by the POVM $\{\Phi^+, \Phi^-, \Psi^+, \Psi^-\}$, $\Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}$, $\Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}$,
  
  $$\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0} \pm \ket{1}\ket{1}), \qquad \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{1} \pm \ket{1}\ket{0}).$$

Circuit implementation:

[Circuit: two qubit lines. The top line goes through $H$ then a Pauli-$Z$ measurement. The bottom line is the target of a CNOT (control = top qubit) before the $H$, and is then measured in the $Z$ basis. The boxed region containing the two $Z$-measurements is labeled "Pauli-$Z$ measurement".]

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}\ket{0}$$

**Proof:** Let $\rho_{AB}$ be the initial state.

Let $U = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$ be the CNOT gate, and $H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ the Hadamard gate.

$H\ket{0} = \ket{+}$
$H\ket{1} = \ket{-}$
$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
