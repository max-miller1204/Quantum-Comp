<u>Proof of (\*)</u>: $\text{Tr}_A[\Phi^+_{AB}] = \frac{1}{d}\text{Tr}_A\left[\left(\sum_{k=0}^{d-1} \ket{k}_A\ket{k}_B\right)\left(\sum_{k'=0}^{d-1}\bra{k'}_A\bra{k'}_B\right)\right]$

$\ket{\Phi^+}_{AB} = \frac{1}{\sqrt{d}}\sum_{k=0}^{d-1}\ket{k}\ket{k}$

$$= \frac{1}{d}\sum_{k,k'=0}^{d-1}\underbrace{\text{Tr}_A\left[\ket{k}\bra{k'}_A \otimes \ket{k}\bra{k'}_B\right]}_{}$$

$$= \text{Tr}[\ket{k}\bra{k'}_A]\,\ket{k}\bra{k'}_B$$

$$= \delta_{k,k'}\,\ket{k}\bra{k'}_B$$

$$= \frac{1}{d}\sum_{k=0}^{d-1}\ket{k}\bra{k}_B$$

$$= \frac{1}{d}\mathbb{1}_B. \;\blacksquare$$

(g) Mixed-state entanglement is much harder to characterize! (More on this later...).

③ <u>Purification of mixed states</u>

(a) <u>Recall</u>: For qubits, pure states are on the surface of the Bloch sphere; mixed states are inside.

[Bloch sphere diagram with axes $x, y, z$; $\ket{0}$ at top (+z), $\ket{1}$ at bottom (−z), $\ket{+}$ on +x, $\ket{-}$ on −x (shown rotated), $\ket{+i}$ on +y, $\ket{-i}$ on −y]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$
$\alpha, \beta \in \mathbb{C},$
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

Qubit
$\ket{0}$ or $\ket{1}$;
or *superposition*

General mixed states have the form $\rho = \sum_{k=1}^{N} p_k \underbrace{\ket{\psi_k}\bra{\psi_k}}_{\text{pure states}}$.

$p_k \rightarrow$ probabilities.
