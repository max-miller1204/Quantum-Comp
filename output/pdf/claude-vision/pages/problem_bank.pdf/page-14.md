18. Consider the three-qubit state vectors

$$\ket{\psi_1}_{ABC} = \frac{1}{\sqrt{2}}(\ket{0,0,0}_{ABC} + \ket{1,1,1}_{ABC}), \tag{59}$$

$$\ket{\psi_2}_{ABC} = \frac{1}{\sqrt{3}}(\ket{0,0,1}_{ABC} + \ket{0,1,0}_{ABC} + \ket{1,0,0}_{ABC}). \tag{60}$$

Determine the following partial traces.

(a) $\mathrm{Tr}_B\big[\ket{\psi_1}\bra{\psi_1}_{ABC}\big]$.

(b) $\mathrm{Tr}_B\big[\ket{\psi_2}\bra{\psi_2}_{ABC}\big]$.

(c) $\mathrm{Tr}_A\big[p\ket{\psi_1}\bra{\psi_1}_{ABC} + (1-p)\ket{\psi_2}\bra{\psi_2}_{ABC}\big]$, where $p \in [0,1]$.

(d) $\mathrm{Tr}_C\big[p\ket{\psi_1}\bra{\psi_2}_{ABC} + (1-p)\ket{\psi_2}\bra{\psi_1}_{ABC}\big]$, where $p \in [0,1]$.

19. Prove the following identity:

$$\mathrm{Tr}_E[(\mathbb{1}_E \otimes M_S) H_{ES} (\mathbb{1}_E \otimes N_S)] = M_S \, \mathrm{Tr}_E[H_{ES}] N_S, \tag{61}$$

where $H_{ES}$, $M_S$, and $N_S$ are arbitrary linear operators.

20. Consider the following two-qubit density operator $\rho_{AB}$ of Alice and Bob:

$$\rho_{AB} = (1-p)\ket{\Phi^+}\bra{\Phi^+}_{AB} + \frac{p}{3}(\ket{\Phi^-}\bra{\Phi^-}_{AB} + \ket{\Psi^+}\bra{\Psi^+}_{AB} + \ket{\Psi^-}\bra{\Psi^-}_{AB}), \tag{62}$$

where we recall the two-qubit Bell state vectors:

$$\ket{\Phi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}), \tag{63}$$

$$\ket{\Psi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0}). \tag{64}$$

Suppose that Alice and Bob both measure their qubits with respect to the Pauli-$z$ basis; i.e., the POVM is $\{\ket{0}\bra{0}, \ket{1}\bra{1}\}$. What is the probability that they obtain *different* measurement outcomes?

21. Consider the qubit state vectors

$$\ket{\psi_k} = \cos\left(\frac{2\pi k}{5}\right)\ket{0} + \sin\left(\frac{2\pi k}{5}\right)\ket{1}, \quad k \in \{0,1,2,3,4\}. \tag{65}$$

Verify that the set $\left\{\frac{2}{5}\ket{\psi_k}\bra{\psi_k}\right\}_{k=0}^{4}$ is a POVM.

22. Consider the three-qubit state vector $\ket{\psi_1}$ in (59), known as the *GHZ state vector*, and define the following set of eight state vectors:

$$\ket{\psi_{z,x_1,x_2}}_{ABC} := (Z^z \otimes X^{x_1} \otimes X^{x_2})\ket{\psi_1}_{ABC}, \quad z, x_1, x_2 \in \{0,1\}. \tag{66}$$

Prove that the set $\{\ket{\psi_{z,x_1,x_2}}\}_{z,x_1,x_2 \in \{0,1\}}$ is an orthonormal basis for $\mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^2$. Conclude that the set $\{\ket{\psi_{z,x_1,x_2}}\bra{\psi_{z,x_1,x_2}}\}_{z,x_1,x_2 \in \{0,1\}}$ is a POVM.

14
