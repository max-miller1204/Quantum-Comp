# Lectures__linear-algebra(III)+quantum-gates.pdf

## Page 1

# ① Quantum States

[Left diagram: vertical line segment with two dots labeled 0 (top) and 1 (bottom)]

**Bit**
0 or 1;
or probabilistic mixture

[Right diagram: Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ in front, $\ket{-}$ in back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$$
$$\alpha, \beta \in \mathbb{C},$$
$$|\alpha|^2 + |\beta|^2 = 1$$

$$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$$
$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

---

✱ States of live on the surface of the **Bloch sphere**. — they are described by 2-dimensional **state vectors**.

$\{\ket{k}\}_{k=0}^{d-1}$    $\{\ket{e_k}\}_{k=1}^{d}$

$$\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad \alpha,\beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1. \qquad \ket{\psi} = \alpha\ket{0} + \beta\ket{1}, \;\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

(States **inside** the sphere are also possible — they are described by **density matrices**. We will see this today!)

---

② **Matrices** (aka "linear operators")

$$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \ket{0}\bra{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$$

→ column indices

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad a,b,c,d \in \mathbb{C}. \quad \rightarrow \quad M = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}$$

[row/column labels: rows indexed 0,1; columns indexed 0,1]

↗ row indices

$$a = \bra{0}M\ket{0}, \quad b = \bra{0}M\ket{1}, \quad c = \bra{1}M\ket{0},$$
$$d = \bra{1}M\ket{1}.$$

– General $d\times d$ matrix: $\displaystyle M = \sum_{i,j=0}^{d-1} m_{ij}\ket{i}\bra{j}, \quad m_{ij} = \bra{i}M\ket{j}$

→ matrix elements.

## Page 2

⊛ <u>Notation</u>: $L(\mathbb{C}^d) \equiv$ set of all matrices/linear operators acting on $\mathbb{C}^d$ (i.e., $d \times d$ matrices) (dimension is $d^2$.)

- For any vector $\ket{v} \in \mathbb{C}^d$, $\ket{v}\bra{v} \in L(\mathbb{C}^d)$ is a $d \times d$ matrix.

$$\ket{v} = \sum_{k=0}^{d-1} v_k \ket{k} \implies \ket{v}\bra{v} = \left(\sum_{k=0}^{d-1} v_k \ket{k}\right)\left(\sum_{k'=0}^{d-1} \overline{v_{k'}} \bra{k'}\right) = \sum_{k,k'=0}^{d-1} v_k \overline{v_{k'}} \ket{k}\bra{k'}.$$

- <u>Identity matrix</u>: $\mathbb{1} \to \mathbb{1}\ket{v} = \ket{v}$ for all $\ket{v} \in \mathbb{C}^d$.

$$\mathbb{1} = \begin{pmatrix} 1 & & 0 \\ & 1 & \\ & & \ddots \\ 0 & & & 1 \end{pmatrix} = \sum_{k=0}^{d-1} \ket{k}\bra{k} \quad \overset{M_{ij} = \delta_{ij}}{\to} \quad \text{For any orthonormal basis } \{\ket{e_k}\}_{k=1}^d : \mathbb{1} = \sum_{k=1}^d \ket{e_k}\bra{e_k}.$$

- <u>Trace of a Matrix</u>: Sum of the diagonal elements.

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \to \text{Tr}[M] = a + d = \bra{0}M\ket{0} + \bra{1}M\ket{1}.$$

In general: $M = \sum_{i,j=0}^{d-1} M_{ij} \ket{i}\bra{j} \implies \text{Tr}[M] = \sum_{i=0}^{d-1} M_{i,i} = \sum_{i=0}^{d-1} \bra{i}M\ket{i}.$

⊛ Consider a state vector $\ket{\psi} = \alpha\ket{0} + \beta\ket{1} \implies \bra{\psi} = \overline{\alpha}\bra{0} + \overline{\beta}\bra{1}$, $|\alpha|^2 + |\beta|^2 = 1$.

$$\implies \ket{\psi}\bra{\psi} = (\alpha\ket{0} + \beta\ket{1})(\overline{\alpha}\bra{0} + \overline{\beta}\bra{1}) = \alpha\overline{\alpha}\ket{0}\bra{0} + \alpha\overline{\beta}\ket{0}\bra{1} + \beta\overline{\alpha}\ket{1}\bra{0} + \beta\overline{\beta}\ket{1}\bra{1}$$

$$= |\alpha|^2 \ket{0}\bra{0} + \alpha\overline{\beta}\ket{0}\bra{1} + \beta\overline{\alpha}\ket{1}\bra{0} + |\beta|^2 \ket{1}\bra{1} = \begin{pmatrix} |\alpha|^2 & \alpha\overline{\beta} \\ \beta\overline{\alpha} & |\beta|^2 \end{pmatrix}$$

$\hookrightarrow |\alpha|^2 = \Pr[0]$
$\quad\;\; |\beta|^2 = \Pr[1]$

Now take the trace: $\text{Tr}[\ket{\psi}\bra{\psi}] = |\alpha|^2 + |\beta|^2 = 1.$

In general: $\text{Tr}[\ket{v}\bra{v}] = \braket{v|v}$ for all $\ket{v} \in \mathbb{C}^d$.

## Page 3

**Proof:** Just use the definition!

$$\mathrm{Tr}(\ket{v}\bra{v}) = \sum_{k=0}^{d-1} \bra{k}\ket{v}\bra{v}\ket{k} = \sum_{k=0}^{d-1} \braket{v|k}\braket{k|v} = \bra{v}\left(\sum_{k=0}^{d-1} \ket{k}\bra{k}\right)\ket{v} = \braket{v|v}. \blacksquare$$

[annotation: $\bra{v}\mathbb{1}\ket{v}$, with $\sum_{k=0}^{d-1}\ket{k}\bra{k} = \mathbb{1}$]

**Similarly:** $\mathrm{Tr}\big[M\ket{v_1}\bra{v_2}\big] = \braket{v_2|M|v_1}$ for all $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$, $M \in L(\mathbb{C}^d)$.

**Proof:** 
$$\mathrm{Tr}\big[M\ket{v_1}\bra{v_2}\big] = \sum_{k=0}^{d-1}\bra{k}M\ket{v_1}\braket{v_2|k} = \sum_{k=0}^{d-1}\braket{v_2|k}\bra{k}M\ket{v_1} = \bra{v_2}\left(\sum_{k=0}^{d-1}\ket{k}\bra{k}\right)M\ket{v_1}$$

$$= \braket{v_2|M|v_1}. \blacksquare \qquad\qquad = \bra{v_2}\underbrace{\mathbb{1}\cdot M}_{=M}\ket{v_1}$$

[annotation: $\mathbb{1}\ket{v} = \ket{v}$, $\mathbb{1}\cdot M = M$]

---

- **Transpose of a matrix:** flip the rows and columns.

- $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \;\rightarrow\; M^T = \begin{pmatrix} a & c \\ b & d \end{pmatrix}$

- ⊛ **Note:** $\big(\ket{i}\bra{j}\big)^T = \ket{j}\bra{i}.$ $\qquad \underline{(M_1 + M_2)^T = M_1^T + M_2^T}$

- **In general:** $M = \sum_{i,j=0}^{d-1} m_{i,j}\ket{i}\bra{j} \;\Rightarrow\; M^T = \sum_{i,j=0}^{d-1} m_{i,j}\ket{j}\bra{i}$

$$M^T = \left(\sum_{i,j=0}^{d-1} m_{i,j}\ket{i}\bra{j}\right)^T = \sum_{i,j=0}^{d-1} m_{i,j}\big(\ket{i}\bra{j}\big)^T$$

- ⊛ A matrix $M$ is called **symmetric** if $M^T = M$.

$$M^T = M \;\rightarrow\; m_{i,j} = m_{j,i}$$

## Page 4

- <u>Conjugate Transpose of a Matrix:</u>

  - Recall for vectors: $\ket{v} = \begin{pmatrix} v_0 \\ v_1 \\ \vdots \\ v_{d-1} \end{pmatrix} \;\Rightarrow\; \bra{v} = \begin{pmatrix} \bar{v}_0 & \bar{v}_1 & \cdots & \bar{v}_{d-1} \end{pmatrix}$

    OR: $\ket{v} = \sum_{k=0}^{d-1} v_k \ket{k} \;\Rightarrow\; \bra{v} = \sum_{k=0}^{d-1} \bar{v}_k \bra{k}$.

  - Similar for matrices! $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \;\Rightarrow\; M^{\dagger} = \begin{pmatrix} \bar{a} & \bar{c} \\ \bar{b} & \bar{d} \end{pmatrix}$.   ($\dagger$ = "dagger")

  - In general: $M = \sum_{i,j=0}^{d-1} M_{i,j} \ket{i}\bra{j} \;\Rightarrow\; M^{\dagger} = \sum_{i,j=0}^{d-1} \overline{M_{i,j}} \ket{j}\bra{i}$

  $\circledast$ <u>Note:</u> $\big( \ket{i}\bra{j} \big)^{\dagger} = \ket{j}\bra{i}$.

  $\circledast$ A matrix $M$ is called <mark>Hermitian</mark> if $M^{\dagger} = M$.   $\;\to\; M_{i,j} = \overline{M_{j,i}}$

  $\quad M = \begin{pmatrix} a & b \\ \bar{b} & d \end{pmatrix}$, $\;\bar{a} = a,\; \bar{d} = d \;\;(a, d \in \mathbb{R})$

- <u>Inner Product and Orthonormal Bases of Matrices.</u>

  - Recall vector inner product: $\ket{u} = \sum_{k=0}^{d-1} u_k \ket{k}, \;\; \ket{v} = \sum_{k=0}^{d-1} v_k \ket{k}$

    $\Rightarrow \;\braket{u|v} = \Big( \sum_{k=0}^{d-1} \bar{u}_k \bra{k} \Big) \Big( \sum_{k=0}^{d-1} v_k \ket{k} \Big) = \sum_{k=0}^{d-1} \bar{u}_k v_k$

  - Matrix inner product: $\langle M_1, M_2 \rangle = \mathrm{Tr}\big[ M_1^{\dagger} M_2 \big]$, $\;\; \langle M_2, M_1 \rangle = \overline{\langle M_1, M_2 \rangle}$

    From this, we define a <u>norm for matrices</u>: $\| M \|_2 = \sqrt{\langle M, M \rangle} = \sqrt{\mathrm{Tr}[ M^{\dagger} M ]}$

  - Matrices $M_1, M_2$ are <u>orthogonal</u> if $\langle M_1, M_2 \rangle = 0$.

## Page 5

- We have bases for matrices as well! $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

Example: $d=2$, recall $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}.$

$\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$

The set $\{\ket{0}\bra{0}, \ket{0}\bra{1}, \ket{1}\bra{0}, \ket{1}\bra{1}\}$ is an orthonormal basis for $L(\mathbb{C}^2)$.

↳ Observe: there are $4 = 2^2$ elements! $\quad \langle B_i, B_j \rangle = \delta_{i,j}$

Check: take inner products!

$\langle \ket{0}\bra{0}, \ket{0}\bra{1} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{0})^\dagger (\ket{0}\bra{1}) \right] = \mathrm{Tr}\left[ \ket{0}\underbrace{\braket{0|0}}_{=1}\bra{1} \right] = \mathrm{Tr}\left[ \ket{0}\bra{1} \right] = \braket{1|0} = 0.$

$\langle \ket{0}\bra{1}, \ket{1}\bra{0} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{1})^\dagger \ket{1}\bra{0} \right] = \mathrm{Tr}\left[ \ket{1}\underbrace{\braket{0|1}}_{=0}\bra{0} \right] = 0.$

$\langle \ket{0}\bra{0}, \ket{0}\bra{0} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{0})^\dagger \ket{0}\bra{0} \right] = \mathrm{Tr}\left[ \ket{0}\underbrace{\braket{0|0}}_{=1}\bra{0} \right] = \mathrm{Tr}\left[ \ket{0}\bra{0} \right] = \braket{0|0} = 1$

In general: $\langle \ket{i}\bra{j}, \ket{k}\bra{\ell} \rangle = \mathrm{Tr}\left[ (\ket{i}\bra{j})^\dagger \ket{k}\bra{\ell} \right] = \mathrm{Tr}\left[ \ket{j}\underbrace{\braket{i|k}}_{=\delta_{i,k}}\bra{\ell} \right]$

$= \delta_{i,k}\, \mathrm{Tr}\left[ \ket{j}\bra{\ell} \right] = \delta_{i,k} \braket{\ell|j} = \delta_{i,k}\, \delta_{j,\ell}$

(★) Holds for arbitrary dimension! $\{\ket{i}\bra{j} : i,j \in \{0,1,\ldots,d-1\}\}$ is an orthonormal basis for $L(\mathbb{C}^d)$.

- Special basis for $d=2$: <u>Pauli Matrices</u> (aka Pauli gates).

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$\mathrm{Tr}[X] = \mathrm{Tr}[Y] = \mathrm{Tr}[Z] = 0$

↳ <u>Bit-flip matrix</u>: $X\ket{0} = \ket{1}, \; X\ket{1} = \ket{0}.$

$X^2 = \mathbb{1}, \; Y^2 = \mathbb{1}, \; Z^2 = \mathbb{1}.$

$\mathrm{Tr}(X^\dagger X) = 2 = \mathrm{Tr}[Y^\dagger Y] = \mathrm{Tr}[Z^\dagger Z]$

## Page 6

They are Hermitian: $X^\dagger = X$, $Y^\dagger = Y$, $Z^\dagger = Z$.

They are orthogonal: $\langle X, Y \rangle = 0$, $\langle X, Z \rangle = 0$, $\langle Z, Y \rangle = 0$.

$\{\mathbb{1}, X, Y, Z\}$ forms orthogonal basis for $L(\mathbb{C}^2)$!

$$\text{Tr}(X^\dagger Y) = \text{Tr}\left[\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\right] = \text{Tr}\left[\begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}\right] = 0$$

$\Rightarrow$ Any $M \in L(\mathbb{C}^2)$ can be written as $M = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$.

$\quad c_0, c_1, c_2, c_3 \in \mathbb{C}$.

## ③ Quantum States as Density Matrices

– We have seen state vectors:

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}, \quad \alpha,\beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1.$$

[Bloch sphere diagram with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ at front, $\ket{-}$ at back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$,
$\alpha, \beta \in \mathbb{C}$,
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

Qubit
$\ket{0}$ or $\ket{1}$;
or *superposition*

– Consider the matrix $\rho = \ket{\psi}\bra{\psi}$.
It has the following properties:

**(1)** $\rho = \rho^\dagger$ (Hermitian).

$\ket{\psi}\bra{\psi} = (\alpha\ket{0} + \beta\ket{1})(\bar{\alpha}\bra{0} + \bar{\beta}\bra{1})$
$= |\alpha|^2 \ket{0}\bra{0} + \alpha\bar{\beta}\ket{0}\bra{1} + \beta\bar{\alpha}\ket{1}\bra{0} + |\beta|^2 \ket{1}\bra{1}$

$(M_1 + M_2)^\dagger = M_1^\dagger + M_2^\dagger$

$(\ket{\psi}\bra{\psi})^\dagger = |\alpha|^2 (\ket{0}\bra{0})^\dagger + \overline{\alpha\bar{\beta}}(\ket{0}\bra{1})^\dagger + \overline{\beta\bar{\alpha}}(\ket{1}\bra{0})^\dagger + |\beta|^2 (\ket{1}\bra{1})^\dagger$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\downarrow \quad\quad\quad\quad\quad\quad\downarrow$
$\quad\quad\quad\quad\quad = \bar{\alpha}\cdot\bar{\bar{\beta}} = \bar{\alpha}\beta \quad = \bar{\beta}\cdot\bar{\bar{\alpha}} = \bar{\beta}\alpha$

$\left(\overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2\right)$
$\bar{\bar{z}} = z$

$= |\alpha|^2 \ket{0}\bra{0} + \bar{\alpha}\beta \ket{1}\bra{0} + \bar{\beta}\alpha\ket{0}\bra{1} + |\beta|^2 \ket{1}\bra{1}$

$= \ket{\psi}\bra{\psi}\ \checkmark$

## Page 7

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

## Page 8

- What about more general density matrices? Consider $d=2$.

We can write $\rho = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$ (b/c $\{\mathbb{1}, X, Y, Z\}$ is a basis).

We want this to satisfy: (1) $\rho^\dagger = \rho$; (2) $\text{Tr}(\rho) = 1$; (3) $\rho \geq 0$.

(1) $\rho^\dagger = \frac{1}{2}(\bar{c_0}\mathbb{1}^\dagger + \bar{c_1} X^\dagger + \bar{c_2} Y^\dagger + \bar{c_3} Z^\dagger)$  $\quad (\mathbb{1}^\dagger = \mathbb{1},\ X^\dagger = X,\ Y^\dagger = Y,\ Z^\dagger = Z)$

$\quad \downarrow$

$\quad = \frac{1}{2}(\bar{c_0}\mathbb{1} + \bar{c_1} X + \bar{c_2} Y + \bar{c_3} Z)$

$\quad \overset{(!)}{=} \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z) \iff c_0 = \bar{c_0},\ c_1 = \bar{c_1},\ c_2 = \bar{c_2},\ c_3 = \bar{c_3}$ (b/c $\{\mathbb{1}, X, Y, Z\}$ is a basis).

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ (all are real numbers).

(2) $\rho = \frac{1}{2}(r_0 \mathbb{1} + r_1 X + r_2 Y + r_3 Z),\ r_0, r_1, r_2, r_3 \in \mathbb{R}$.

$\text{Tr}(\rho) = \frac{1}{2}\big(r_0 \underbrace{\text{Tr}(\mathbb{1})}_{=2} + r_1 \underbrace{\text{Tr}(X)}_{=0} + r_2 \underbrace{\text{Tr}(Y)}_{=0} + r_3 \underbrace{\text{Tr}(Z)}_{=0}\big) \overset{(!)}{=} 1 \iff \underline{\underline{r_0 = 1}}$

(3) $\rho = \frac{1}{2}(\mathbb{1} + r_1 X + r_2 Y + r_3 Z) \to$ Find the eigenvalues!

$\left(\begin{array}{c}
\circledast\ \underline{\text{Observe}}: \cdot \langle X, \rho \rangle = \text{Tr}(X\rho) = \text{Tr}\big[X \cdot \tfrac{1}{2}(\mathbb{1} + r_1 X + r_2 Y + r_3 Z)\big] \\
\quad\quad\quad\quad = \tfrac{1}{2}\big(\underbrace{\text{Tr}(X)}_{=0} + r_1 \underbrace{\text{Tr}(X^2)}_{=2} + r_2 \underbrace{\text{Tr}(XY)}_{=0} + r_3 \underbrace{\text{Tr}(XZ)}_{=0}\big) \\
\quad\quad\quad\quad\quad \downarrow \\
\quad\quad\quad\quad\quad = r_1 \\
\quad\quad \cdot \langle Y, \rho \rangle = r_2 \\
\quad\quad \cdot \langle Z, \rho \rangle = r_3.
\end{array}\right.$

## Page 9

$$\rho = \frac{1}{2}\begin{pmatrix} 1+r_z & r_x - i r_y \\ r_x + i r_y & 1 - r_z \end{pmatrix} \implies \lambda_\pm = \frac{1}{2}\left(1 \pm \sqrt{r_x^2 + r_y^2 + r_z^2}\right) \geq 0.$$

Need $\lambda_- \geq 0 \implies \frac{1}{2}\left(1 - \sqrt{r_x^2 + r_y^2 + r_z^2}\right) \geq 0 \implies \boxed{r_x^2 + r_y^2 + r_z^2 \leq 1}$

$$\vec{r} = (r_x, r_y, r_z) \in \mathbb{R}^3 \text{ inside the unit sphere!}$$

Observe: $\|\rho\|_2^2 = \text{Tr}[\rho^2] = \frac{1}{2}\left(1 + r_x^2 + r_y^2 + r_z^2\right) \leq 1$
$$\underbrace{\phantom{r_x^2+r_y^2+r_z^2}}_{\leq 1}$$

$\rho = \frac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)$

[Bloch sphere diagram: z-axis up with $\ket{0}$ at top, $\ket{1}$ at bottom; x-axis with $\ket{+}$ and $\ket{-}$ marked; y-axis with $\ket{+i}$ and $\ket{-i}$ marked]

For a pure state $\rho = \ket{\psi}\bra{\psi}$, $\rho^2 = \ket{\psi}\underbrace{\braket{\psi|\psi}}_{=1}\bra{\psi} = \ket{\psi}\bra{\psi} \implies \text{Tr}[\rho^2] = 1$
$\rho^2 = \rho$

$\implies r_x^2 + r_y^2 + r_z^2 = 1 \implies$ pure states are on the surface of the unit sphere!

✻ We call $\text{Tr}[\rho^2]$ the **purity** of $\rho \to \rho$ pure if and only if $\text{Tr}[\rho^2] = 1$.

✻ <u>Origin</u>, $\vec{r} = (0,0,0)$ contains the **maximally-mixed state**: $\frac{\mathbb{1}}{2}$.

$\frac{\mathbb{1}}{2} = \frac{1}{2}(\ket{0}\bra{0} + \ket{1}\bra{1})$

✻ <u>Points on the X-axis</u>: $\vec{r} = (\pm 1, 0, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm X) = \ket{\pm}\bra{\pm}$, $\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$$= \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ \pm 1 \end{pmatrix}$$

These are eigenstates of $X$! $X\ket{\pm} = \pm \ket{\pm}$.

✻ <u>Points on the Y-axis</u>: $\vec{r} = (0, \pm 1, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm Y) = \ket{\pm i}\bra{\pm i}$,
$$\ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1}) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ \pm i \end{pmatrix}$$

These are eigenstates of $Y$! $Y\ket{\pm i} = \pm \ket{\pm i}$.

✻ <u>Points on the Z-axis</u>: $\vec{r} = (0, 0, \pm 1) \to \rho = \frac{1}{2}(\mathbb{1} \pm Z) \begin{matrix} \xrightarrow{(+)} \ket{0}\bra{0} \\ \xrightarrow{(-)} \ket{1}\bra{1} \end{matrix}$  $\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$
$\ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

These are eigenstates of $Z$! $Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$.
