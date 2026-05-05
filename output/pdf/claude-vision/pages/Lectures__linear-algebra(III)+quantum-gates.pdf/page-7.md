(2) $\text{Tr}(\rho) = 1$ (unit trace).

$$\text{Tr}\big[\ket{\psi}\bra{\psi}\big] = \braket{\psi|\psi} = |\alpha|^2 + |\beta|^2 = 1 \quad \checkmark$$

(from above!)

(3) $\rho \geq 0$ (Positive Semi-definite).

❋ A Hermitian matrix $M \in L(\mathbb{C}^d)$ is called **positive semi-definite** (denoted $M \geq 0$) if $\braket{v|M|v} \geq 0 \;\; \forall \; \ket{v} \in \mathbb{C}^d$.

This is equivalent to: all **eigenvalues** are **non-negative**.

❋ Recall **eigenvalues and eigenvectors**: $M\ket{v} = \lambda\ket{v}$, $M = U D U^\dagger$, $U^\dagger U = \mathbb{1}$.

[Annotations: $\ket{v}$ → Eigenvector, $\lambda$ → Eigenvalue, $D$ → diagonal matrix, $U$ → unitary]

Eigenvalue (Spectral) decomposition: $M = \sum_{k=1}^{r} \lambda_k \ket{v_k}\bra{v_k}$

❋ For $\rho = \ket{\psi}\bra{\psi} \to \braket{v|\rho|v} = \braket{v|\psi}\braket{\psi|v} = |\braket{\psi|v}|^2 \geq 0 \;\; \forall \; \ket{v} \;\; \checkmark$

- Any matrix satisfying (1), (2), (3) is called a **density matrix/operator**.

❋ **Axiom of Quantum Mechanics**: The state of any quantum system is mathematically by a density matrix. (arbitrary dimension).

- The density matrix $\rho = \ket{\psi}\bra{\psi}$ describes a **pure state**. (on the surface of the Bloch sphere.)
