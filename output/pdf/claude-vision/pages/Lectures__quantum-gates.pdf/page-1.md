① <u>Recap: Density Matrices</u>

- A <u>density matrix</u> in dimension $d \in \{2,3,\ldots\}$ is a $d \times d$ matrix $\rho \in L(\mathbb{C}^d)$ satisfying the following properties:

    (1) <u>Hermitian</u>: $\rho^\dagger = \rho$  $\quad \dagger \equiv$ conjugate transpose.

    (2) <u>Unit Trace</u>: $\text{Tr}[\rho] = 1$ $\quad$ (Recall: Tr ≡ trace ≡ sum of diagonal elements of a matrix)

    (3) <u>Positive Semi-definite</u>: $\rho \geq 0$

    ✱ This means that $\langle v | \rho | v \rangle \geq 0 \;\; \forall \; |v\rangle \in \mathbb{C}^d$.
    Equivalently: all the <u>eigenvalues</u> of $\rho$ are non-negative.
    $\hookrightarrow M|v\rangle = \lambda |v\rangle$

✱ <u>Axiom of Quantum Mechanics</u>: The state of any quantum system is mathematically described by a density matrix. (arbitrary dimension).
State vector: $|\psi\rangle \to \||\psi\rangle\| = 1 \to \rho = |\psi\rangle\langle\psi|$

- For $d=2$ (qubits), density matrices are synonymous with points on and inside the unit sphere.

[Bloch sphere diagram: sphere with $|0\rangle$ at top (+z), $|1\rangle$ at bottom (-z), $|+\rangle$ and $|-\rangle$ on x-axis, $|+i\rangle$ and $|-i\rangle$ on y-axis. Labeled "(Bloch sphere)".]

→ Point $\vec{r} \in \mathbb{R}^3$ (real 3D space)
$\vec{r} = (r_x, r_y, r_z)$, $\rho = \frac{1}{2}(\mathbb{1} + r_x \underline{X} + r_y \underline{Y} + r_z \underline{Z})$.

$r_x^2 + r_y^2 + r_z^2 \leq 1$, $r_x = \text{Tr}[\rho X]$, $r_y = \text{Tr}[\rho Y]$, $r_z = \text{Tr}[\rho Z]$.

$\text{Tr}[\rho X] = \text{Tr}\left[\frac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z) X\right]$
$\quad = \frac{1}{2}(\text{Tr}[X] + r_x \text{Tr}[\mathbb{1}] + r_y \text{Tr}[YX] + r_z \text{Tr}[ZX])$
$\quad = r_x.$

- $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$, $Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (<u>Pauli matrices</u>).

- If $r_x^2 + r_y^2 + r_z^2 = 1$, then $\rho$ is a <u>pure state</u>: it can be written as $\rho = |\psi\rangle\langle\psi|$, where $|\psi\rangle \in \mathbb{C}^2$ is a <u>state vector</u>; $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$.
