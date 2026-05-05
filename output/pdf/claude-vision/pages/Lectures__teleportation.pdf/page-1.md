# ① Recap of the course so far.

## (a) What is a qubit?

[Diagram on left: A bit, shown as two points labeled 0 (top) and 1 (bottom) connected by a line.]

**Bit**
0 or 1;
or probabilistic mixture

[Diagram on right: Bloch sphere with $\ket{0}$ at top (z-axis), $\ket{1}$ at bottom, $\ket{+}$ and $\ket{-}$ on x-axis, $\ket{+i}$ and $\ket{-i}$ on y-axis.]

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$$
$$\alpha, \beta \in \mathbb{C},$$
$$|\alpha|^2 + |\beta|^2 = 1$$

$$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$$
$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

---

- The state of a qubit is given by a <u>density matrix/operator</u>:

  (1) $\rho^\dagger = \rho$ (Hermitian) → **Conjugate transpose**

  (2) $\rho \geq 0$ (positive semi-definite ⇔ non-negative eigenvalues)

  (3) $\text{Tr}[\rho] = 1$ → **Sum of the diagonal elements.**

- Points on the surface of the Bloch sphere are given by state vectors; they are called <u>pure states</u>: $\rho = \ket{\psi}\bra{\psi}$, $\ket{\psi} \in \mathbb{C}^2$, $\|\ket{\psi}\|_2 = 1$.
  
  [arrow pointing to $\ket{\psi}$:] **State vector.**

- Points inside the Bloch sphere are <u>mixed states</u>:

$$\rho = \sum_{k=1}^{r} g_k \underbrace{\ket{\psi_k}\bra{\psi_k}}_{\text{pure states}}, \quad g_k \in [0,1], \quad \sum_{k=1}^{r} g_k = 1.$$

- <u>Quantum gates</u> are used to describe operations/computations on qubits. They are defined by <u>unitary matrices</u>: $U \in L(\mathbb{C}^d)$, $U^\dagger U = U U^\dagger = \mathbb{1}$.
