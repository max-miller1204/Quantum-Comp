# ① Determining Entanglement.

(a) Given a state vector $\ket{\psi}_{AB}$, how to determine if it is entangled or not?
Precisely: $\exists\, \ket{\phi_1}_A, \ket{\phi_2}_B$ s.t. $\ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B$ ?

✸ **Theorem (Schmidt Decomposition):** Every state vector $\ket{\psi}_{AB}$ can be written as

$$\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{e_k}_A \otimes \ket{f_k}_B. \qquad \left(\ket{\psi}_{AB} = \sum_{i,j=0}^{d-1} c_{i,j} \ket{i}_A \otimes \ket{j}_B\right)$$

- $r$: Schmidt rank
- $\{S_k\}_{k=1}^{r}$: Schmidt coefficients $S_k > 0\ \forall k$
- $\{\ket{e_k}_A\}_{k=1}^{r}$ and $\{\ket{f_k}_B\}_{k=1}^{r}$ are orthonormal vectors.

(**Proof** (recall): Write the vector $\ket{\psi}_{AB}$ as a matrix, then do the singular value decomposition of the matrix.)

- The Schmidt rank is **unique** — so we get the following criterion:

$$\boxed{\begin{array}{l} \bullet \text{ If } r = 1, \text{ then } \ket{\psi} = \ket{e_1} \otimes \ket{f_1} \Rightarrow \text{not entangled!} \\[4pt] \bullet \text{ If } r > 1, \text{ then entangled!} \qquad \ket{\mathcal{E}^+} = \tfrac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k}_A \ket{k}_B \end{array}}$$

(b) What about mixed states? More complicated!

- **Example:** convex mixtures of Bell states. $\left(\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}),\ \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0})\right)$

$$\rho_{AB} = p_1 \Phi^+_{AB} + p_2 \Phi^-_{AB} + p_3 \Psi^+_{AB} + p_4 \Psi^-_{AB}, \quad \text{probabilities } p_1, p_2, p_3, p_4 \in [0,1]$$

$$\Phi^\pm_{AB} = \ket{\Phi^\pm}\bra{\Phi^\pm}_{AB},\quad \Psi^\pm_{AB} = \ket{\Psi^\pm}\bra{\Psi^\pm}_{AB}. \qquad p_1 + p_2 + p_3 + p_4 = 1$$
