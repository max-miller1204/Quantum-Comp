(b) How to extract information from a qubit? <u>Measurements</u>!

- A <u>measurement</u> (aka "positive operator-valued measure") is defined by $\rightarrow$ (POVM) a set of operators $\{M_x\}_{x \in \mathcal{X}}$ (some finite set $\mathcal{X}$), such that:

  (1) $M_x \geq 0 \;\; \forall x \in \mathcal{X}$. ($M_x \in L(\mathbb{C}^d) \to d \times d$ matrix for arbitrary dimension $d$.)

  (2) $\sum_{x \in \mathcal{X}} M_x = \mathbb{1}$

- For any state $\rho$, the outcome probabilities are given by
  $$\Pr(x) = \mathrm{Tr}[M_x \rho] \;\; \forall x \in \mathcal{X}.$$

- Examples of measurements:

  (1) Pauli-$Z$ / computational basis: $\{\underbrace{\ket{0}\bra{0}}_{M_0}, \underbrace{\ket{1}\bra{1}}_{M_1}\}$ &nbsp;&nbsp; $\ket{0}\bra{0} + \ket{1}\bra{1} = \mathbb{1}$. &nbsp;&nbsp; $Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$

  (2) Pauli-$X$: $\{\ket{+}\bra{+}, \ket{-}\bra{-}\}$, $\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$, $X\ket{\pm} = \pm\ket{\pm}$

  (3) Any basis: for any unitary $U$, $\{U\ket{0}\bra{0}U^\dagger, U\ket{1}\bra{1}U^\dagger\}$.

  $$\left(\underline{\text{Check}}: U\ket{0}\bra{0}U^\dagger + U\ket{1}\bra{1}U^\dagger = U\underbrace{(\ket{0}\bra{0} + \ket{1}\bra{1})}_{=\mathbb{1}}U^\dagger = UU^\dagger = \mathbb{1} \;\checkmark\right)$$

(c) <u>Entanglement</u>: One of the key distinguishing characteristics of quantum vs. classical.

- A state vector $\ket{\psi}_{AB}$ is entangled if it <u>cannot</u> be written as $\ket{\psi}_{AB} = \ket{\psi}_A \otimes \ket{\psi}_B$.
  $$\downarrow \text{ product state}$$

- Every state vector $\ket{\psi}_{AB}$ has a <u>Schmidt decomposition</u>:

  (1) $\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{e_k}_A \otimes \ket{f_k}_B$

  $\ket{\Phi^+} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0} + \ket{1}\ket{1})$.

  (2) $S_k$: Schmidt coefficients $(S_k > 0)$

  $\{\ket{e_k}_A\}_{k=1}^{r}$ and $\{\ket{f_k}_B\}_{k=1}^{r}$ are orthonormal vectors.
  $$\braket{e_k | e_{k'}} = \delta_{k,k'} = \begin{cases} 0 & \text{if } k \neq k' \\ 1 & \text{if } k = k' \end{cases}$$
