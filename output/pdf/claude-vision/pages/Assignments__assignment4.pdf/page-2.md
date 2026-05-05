(b) $\frac{1}{2}\left(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X + Y \otimes Y + Z \otimes Z\right) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$

5. Consider the following two-qubit density operator $\rho_{AB}$ of Alice and Bob:

$$\rho_{AB} = p_1 \ket{\Phi^+}\bra{\Phi^+}_{AB} + p_2 \ket{\Phi^-}\bra{\Phi^-}_{AB} + p_3 \ket{\Psi^+}\bra{\Psi^+}_{AB} + p_4 \ket{\Psi^-}\bra{\Psi^-}_{AB}, \tag{1}$$

where $p_1, p_2, p_3, p_4$ are probabilities ($p_1, p_2, p_3, p_4 \in [0,1]$ and $p_1 + p_2 + p_3 + p_4 = 1$) and we recall the two-qubit Bell state vectors:

$$\ket{\Phi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}), \quad \ket{\Psi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0}). \tag{2}$$

Suppose that Alice and Bob both measure their qubits with respect to the Pauli-$z$ basis; i.e., the POVM is $\{\ket{0}\bra{0}, \ket{1}\bra{1}\}$. What is the probability that they obtain *different* measurement outcomes?

6. Consider the state vector $\ket{\Psi^-}_{AB}$ of Alice and Bob, defined in (2).

   (a) If Alice and Bob both measure in the computational basis, then how are their outcomes correlated?
   
   (b) For every measurement outcome of Alice, calculate the corresponding post-measurement state of Bob.
   
   (c) Let $U \in \mathrm{L}(\mathbb{C}^2)$ be an arbitrary $2 \times 2$ unitary matrix. Prove that $(U \otimes U)\ket{\Psi^-}\bra{\Psi^-}(U \otimes U)^\dagger = \ket{\Psi^-}\bra{\Psi^-}$.
   
   (d) Conclude that if Alice and Bob both do a measurement with respect to the same but arbitrary basis, then their outcomes are always correlated in the same way as in the computational-basis measurement.

2
