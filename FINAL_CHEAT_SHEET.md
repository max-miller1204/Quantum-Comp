# CS 4134 Final Cheat Sheet

Based on the repo material for **Quantum Computation and Information Processing**:
lectures, assignments 1-9, problem bank, and exam cover/study guide files.

## 0. Exam Strategy

- Always show the intermediate state, matrix, probability, or trace step. The exams deduct for missing or unclear steps.
- For circuits, compute on computational-basis states first, then extend by linearity.
- For measurement problems, write the POVM/projectors first, then apply Born's rule.
- For entanglement, use the quickest valid criterion: factorization, coefficient-matrix rank, Schmidt rank, or PPT if mixed.
- Global phase does not matter for state vectors: $|\psi\rangle$ and $e^{i\theta}|\psi\rangle$ represent the same physical pure state.
- Keep normalization visible: probabilities must sum to 1, state-vector norms must be 1, density matrices must have trace 1.

## 1. Core Notation And Linear Algebra

### Complex Numbers

- $z=a+bi$, $\bar z=a-bi$, $\mathrm{Re}(z)=a$, $\mathrm{Im}(z)=b$.
- $|z|^2=z\bar z=a^2+b^2$.
- Polar form: $z=re^{i\theta}=r(\cos\theta+i\sin\theta)$.
- $\overline{z_1+z_2}=\bar z_1+\bar z_2$, $\overline{z_1z_2}=\bar z_1\bar z_2$.

### Dirac Notation

- Ket $|v\rangle$: column vector.
- Bra $\langle v|$: conjugate transpose of $|v\rangle$.
- Inner product: $\langle v|w\rangle=\sum_i \bar v_i w_i$.
- $\langle v|w\rangle=\overline{\langle w|v\rangle}$.
- Norm: $\|v\|=\sqrt{\langle v|v\rangle}$.
- Normalized state vector: $\langle v|v\rangle=1$.
- Normalize: $|v\rangle/\sqrt{\langle v|v\rangle}$.
- Standard basis: $|0\rangle=(1,0)^T$, $|1\rangle=(0,1)^T$.

### Important Bases

- Computational/Z basis: $|0\rangle, |1\rangle$.
- X basis:
  - $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$
  - $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$
- Y basis:
  - $|+i\rangle=(|0\rangle+i|1\rangle)/\sqrt2$
  - $|-i\rangle=(|0\rangle-i|1\rangle)/\sqrt2$

### Outer Products And Projectors

- $|v\rangle\langle w|$ is a rank-one operator.
- $|v\rangle\langle v|$ is the projector onto $|v\rangle$ if $|v\rangle$ is normalized.
- Trace identities:
  - $\mathrm{Tr}[|v_1\rangle\langle v_2|]=\langle v_2|v_1\rangle$
  - $\mathrm{Tr}[M|v_1\rangle\langle v_2|]=\langle v_2|M|v_1\rangle$
  - $\mathrm{Tr}[AB]=\mathrm{Tr}[BA]$

### Orthonormal Bases

- Orthonormal: $\langle e_i|e_j\rangle=\delta_{ij}$.
- Completeness: if $\{|e_k\rangle\}_{k=1}^d$ is an ONB, then
  $$I_d=\sum_{k=1}^d |e_k\rangle\langle e_k|.$$
- Change of basis:
  $$|u\rangle=\sum_k \langle e_k|u\rangle |e_k\rangle.$$

### Matrix Classes

- Adjoint/conjugate transpose: $M^\dagger=\bar M^T$.
- Unitary: $U^\dagger U=UU^\dagger=I$.
  - Preserves inner products: $\langle Uv|Uw\rangle=\langle v|w\rangle$.
  - Columns form an ONB.
- Hermitian/self-adjoint: $M^\dagger=M$.
  - Eigenvalues are real.
  - Observable matrices are Hermitian.
  - General 2 by 2 Hermitian matrix:
    $$\begin{pmatrix}a&b+ci\\ b-ci&d\end{pmatrix},\quad a,b,c,d\in\mathbb R.$$
- Positive semidefinite: $M\succeq0$ iff $\langle v|M|v\rangle\ge0$ for all $|v\rangle$.
  - Equivalent for Hermitian $M$: all eigenvalues are nonnegative.
  - $M^\dagger M\succeq0$ always.

### Useful Conjugate-Transpose Identity

$$\langle v_2|M|v_1\rangle=\langle M^\dagger v_2|v_1\rangle.$$

### Building A Unitary From Two ONBs

If $\{|e_k\rangle\}$ and $\{|f_k\rangle\}$ are ONBs, then
$$U=\sum_k |e_k\rangle\langle f_k|$$
is unitary and maps $|f_k\rangle\mapsto |e_k\rangle$.

## 2. Tensor Products

- Tensor states: $|v\rangle\otimes|w\rangle$, also written $|v,w\rangle$.
- Operator action:
  $$(A\otimes B)(|v\rangle\otimes|w\rangle)=(A|v\rangle)\otimes(B|w\rangle).$$
- Two-qubit computational-basis order used in the repo:
  $$|00\rangle,\ |01\rangle,\ |10\rangle,\ |11\rangle.$$
- Kronecker product: if $A=(a_{ij})$, then $A\otimes B$ replaces each $a_{ij}$ by $a_{ij}B$.

## 3. Probability And Statistics

- Joint PMF: $p_{X,Y}(x,y)=\Pr[X=x,Y=y]$.
- Marginal: $p_X(x)=\sum_y p_{X,Y}(x,y)$.
- Conditional: $\Pr[A|B]=\Pr[A\cap B]/\Pr[B]$.
- Independence: $p_{X,Y}(x,y)=p_X(x)p_Y(y)$.
- Expectation: $\mathbb E[X]=\sum_x x\Pr[X=x]$.
- Variance: $\mathrm{Var}(X)=\mathbb E[X^2]-\mathbb E[X]^2$.
- Covariance: $\mathrm{Cov}(X,Y)=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]$.
- Sample mean estimator:
  $$\hat X_N=\frac1N\sum_{i=1}^N X_i,\quad \mathbb E[\hat X_N]=\mathbb E[X].$$
- If $\Pr[0]=\frac12(1+\alpha)$ and $\Pr[1]=\frac12(1-\alpha)$, record outcome 0 as $+1$ and outcome 1 as $-1$. Then:
  $$\mathbb E[X]=\alpha,\quad \hat X_N\to\alpha.$$

## 4. Density Operators And Qubit States

### Density Operator Definition

$\rho$ is a valid quantum state iff:

1. $\rho^\dagger=\rho$.
2. $\rho\succeq0$.
3. $\mathrm{Tr}[\rho]=1$.

### Pure Vs Mixed

- Pure state: $\rho=|\psi\rangle\langle\psi|$.
- Mixed state: $\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|$, with $p_i\ge0$, $\sum_i p_i=1$.
- Purity: $\mathrm{Tr}[\rho^2]$.
  - Pure iff $\mathrm{Tr}[\rho^2]=1$.
  - Maximally mixed in dimension $d$: $\rho=I_d/d$, purity $1/d$.

### Bloch Sphere

Every single-qubit state can be written as
$$\rho=\frac12(I+r_xX+r_yY+r_zZ)=\frac12(I+\vec r\cdot\vec\sigma).$$

- $\vec r=(r_x,r_y,r_z)$ is the Bloch vector.
- Valid state iff $|\vec r|\le1$.
- Pure iff $|\vec r|=1$.
- Mixed iff $|\vec r|<1$.
- $\mathrm{Tr}[\rho^2]=\frac12(1+|\vec r|^2)$.

Key points:

- $|0\rangle$: $(0,0,1)$.
- $|1\rangle$: $(0,0,-1)$.
- $|+\rangle$: $(1,0,0)$.
- $|-\rangle$: $(-1,0,0)$.
- $|+i\rangle$: $(0,1,0)$.
- $|-i\rangle$: $(0,-1,0)$.

## 5. Pauli Operators

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

Actions:

- $X|0\rangle=|1\rangle$, $X|1\rangle=|0\rangle$.
- $Y|0\rangle=i|1\rangle$, $Y|1\rangle=-i|0\rangle$.
- $Z|0\rangle=|0\rangle$, $Z|1\rangle=-|1\rangle$.

Properties:

- $X,Y,Z$ are Hermitian and unitary.
- $X^2=Y^2=Z^2=I$.
- $XY=iZ$, $YZ=iX$, $ZX=iY$.
- Anti-commutation: $XY=-YX$, $XZ=-ZX$, $YZ=-ZY$.
- Trace orthogonality: $\mathrm{Tr}[XY]=\mathrm{Tr}[XZ]=\mathrm{Tr}[YZ]=0$.
- $XZXZ=ZXZX=-I$.

### Pauli Decomposition

Any $M\in L(\mathbb C^2)$ can be written as
$$M=\frac12(c_0I+c_1X+c_2Y+c_3Z).$$

Coefficients:

- $c_0=\mathrm{Tr}[M]$
- $c_1=\mathrm{Tr}[XM]$
- $c_2=\mathrm{Tr}[YM]$
- $c_3=\mathrm{Tr}[ZM]$

For
$$M=\begin{pmatrix}p&q\\r&s\end{pmatrix}:$$

- $\mathrm{Tr}[M]=p+s$
- $\mathrm{Tr}[XM]=q+r$
- $\mathrm{Tr}[YM]=i(q-r)$
- $\mathrm{Tr}[ZM]=p-s$

$M$ is Hermitian iff $c_0,c_1,c_2,c_3$ are real.

### Important Two-Qubit Pauli Identities

$$|\Phi^+\rangle\langle\Phi^+|
=\frac14(I\otimes I+X\otimes X-Y\otimes Y+Z\otimes Z).$$

Swap operator:
$$F=\frac12(I\otimes I+X\otimes X+Y\otimes Y+Z\otimes Z).$$

Pauli twirl / full random Pauli:
$$\frac14(\rho+X\rho X+Y\rho Y+Z\rho Z)=\frac12I.$$

## 6. Measurements

### Projective Measurements

A projective measurement is a set of orthogonal projectors $\{\Pi_x\}$ such that
$$\Pi_x^\dagger=\Pi_x,\quad \Pi_x\Pi_y=\delta_{xy}\Pi_x,\quad \sum_x\Pi_x=I.$$

Born rule:
$$\Pr[x]=\langle\psi|\Pi_x|\psi\rangle=\mathrm{Tr}[\Pi_x\rho].$$

Post-measurement state for pure input:
$$|\psi_x\rangle=\frac{\Pi_x|\psi\rangle}{\sqrt{\Pr[x]}}.$$

For density operators:
$$\rho_x=\frac{\Pi_x\rho\Pi_x}{\mathrm{Tr}[\Pi_x\rho]}.$$

### POVMs

A POVM is a finite set $\{M_x\}$ such that:

- $M_x\succeq0$ for all $x$.
- $\sum_xM_x=I$.

Outcome probability:
$$\Pr[x]=\mathrm{Tr}[M_x\rho].$$

Examples:

- Z measurement: $\{|0\rangle\langle0|,\ |1\rangle\langle1|\}$.
- X measurement: $\{|+\rangle\langle+|,\ |-\rangle\langle-|\}$.
- Any ONB measurement: $\{|e_k\rangle\langle e_k|\}$.
- Five-state POVM from Assignment 9:
  $$\left\{\frac25|\psi_k\rangle\langle\psi_k|\right\}_{k=0}^4,\quad
  |\psi_k\rangle=\cos(2\pi k/5)|0\rangle+\sin(2\pi k/5)|1\rangle.$$

For $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, the five-state POVM probabilities are
$$p_k=\frac25|\langle\psi_k|\psi\rangle|^2
=\frac25|\alpha\cos(2\pi k/5)+\beta\sin(2\pi k/5)|^2.$$

With $c_k=\cos(2\pi k/5)$ and $s_k=\sin(2\pi k/5)$:
$$p_k=\frac25\left(|\alpha|^2c_k^2+|\beta|^2s_k^2
+2\mathrm{Re}(\bar\alpha\beta)c_ks_k\right).$$

To show it is a POVM, use
$$\sum_k c_k^2=\frac52,\quad \sum_k s_k^2=\frac52,\quad \sum_k c_ks_k=0.$$

### Observable Expectation Values

For Hermitian observable
$$M=\sum_i\lambda_i|v_i\rangle\langle v_i|,$$
the measurement outcomes are eigenvalues $\lambda_i$ with probabilities
$$\Pr[\lambda_i]=\mathrm{Tr}[|v_i\rangle\langle v_i|\rho].$$

Expected value:
$$\mathbb E[M]=\sum_i\lambda_i\Pr[\lambda_i]=\mathrm{Tr}[M\rho].$$

If $M=\sum_j c_jU_j$ is decomposed into unitaries, estimate each
$\langle\psi|U_j|\psi\rangle$ using the Hadamard test and combine linearly.

## 7. Partial Trace

For product operators:

$$\mathrm{Tr}_A[P_A\otimes M_B]=\mathrm{Tr}[P_A]M_B.$$

$$\mathrm{Tr}_B[P_A\otimes M_B]=\mathrm{Tr}[M_B]P_A.$$

General basis rule:
$$\mathrm{Tr}_B[|i\rangle\langle j|_A\otimes|k\rangle\langle l|_B]
=|i\rangle\langle j|_A\langle l|k\rangle.$$

Useful identity:
$$\mathrm{Tr}_A[(I_A\otimes M_B)H_{AB}(I_A\otimes N_B)]
=M_B\,\mathrm{Tr}_A[H_{AB}]\,N_B.$$

For a two-qubit 4 by 4 matrix in basis $00,01,10,11$:

- $\mathrm{Tr}_B$ gives a 2 by 2 matrix whose entries are traces over B-index blocks.
- $\mathrm{Tr}_A$ sums A-index blocks.

Explicitly, if $M_{ab,a'b'}=\langle a,b|M|a',b'\rangle$, then
$$[\mathrm{Tr}_B(M)]_{a,a'}=\sum_{b\in\{0,1\}}M_{ab,a'b},\quad
[\mathrm{Tr}_A(M)]_{b,b'}=\sum_{a\in\{0,1\}}M_{ab,ab'}.$$

Reduced state:
$$\rho_A=\mathrm{Tr}_B[\rho_{AB}],\quad \rho_B=\mathrm{Tr}_A[\rho_{AB}].$$

## 8. Bell States And Entanglement

### Bell Basis

$$|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},\quad
|\Phi^-\rangle=\frac{|00\rangle-|11\rangle}{\sqrt2}.$$

$$|\Psi^+\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2},\quad
|\Psi^-\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}.$$

Facts:

- They form an ONB for two qubits.
- Each Bell state is maximally entangled.
- Reduced state of either qubit is maximally mixed: $I/2$.
- Bell measurement POVM:
  $$\{|\Phi^+\rangle\langle\Phi^+|,\ |\Phi^-\rangle\langle\Phi^-|,\ |\Psi^+\rangle\langle\Psi^+|,\ |\Psi^-\rangle\langle\Psi^-|\}.$$

Correlations in Z basis:

- $|\Phi^\pm\rangle$: same outcomes, 00 or 11.
- $|\Psi^\pm\rangle$: opposite outcomes, 01 or 10.

Pauli action:

- $X$ on either qubit maps $|\Phi^+\rangle\leftrightarrow|\Psi^+\rangle$.
- $X$ on either qubit maps $|\Phi^-\rangle\leftrightarrow|\Psi^-\rangle$ up to global phase.
- $Z$ changes plus/minus sign within the same same/opposite family.

### Product Vs Entangled

Pure bipartite state:

- Product iff $|\psi\rangle_{AB}=|a\rangle_A\otimes|b\rangle_B$.
- Entangled iff it cannot be written as a product.

Coefficient-matrix test:

1. Write $|\psi\rangle=\sum_{ij}c_{ij}|i\rangle|j\rangle$.
2. Form coefficient matrix $C=(c_{ij})$.
3. Product iff $\mathrm{rank}(C)=1$.
4. Entangled iff $\mathrm{rank}(C)>1$.

### Schmidt Decomposition

Every bipartite pure state has
$$|\psi\rangle_{AB}=\sum_{k=1}^r s_k|a_k\rangle|b_k\rangle,$$
where $s_k>0$, $\{|a_k\rangle\}$ and $\{|b_k\rangle\}$ are ON sets.

- $s_k$ are Schmidt coefficients.
- $r$ is Schmidt rank.
- Product iff $r=1$.
- Entangled iff $r>1$.
- Compute by SVD of coefficient matrix $C=UDV^\dagger$.

### Mixed-State Separability And PPT

Mixed state is separable if
$$\rho_{AB}=\sum_k p_k\rho_A^{(k)}\otimes\rho_B^{(k)}.$$

If no such decomposition exists, it is entangled.

Partial transpose:

- Transpose only subsystem A or only subsystem B.
- If $\rho_{AB}$ is separable, then $\rho_{AB}^{T_A}\succeq0$ and $\rho_{AB}^{T_B}\succeq0$.
- For 2 by 2 and 2 by 3 systems, PPT is also sufficient: separable iff partial transpose is PSD.
- If partial transpose has a negative eigenvalue, the state is entangled.

### Classical Correlation Vs Entanglement

Classically correlated but separable example:
$$\rho=\frac12(|00\rangle\langle00|+|11\rangle\langle11|).$$

- Correlated in Z basis.
- Uncorrelated in X basis.

Singlet:
$$|\Psi^-\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}.$$

- Perfectly anti-correlated in any common basis.
- For any single-qubit unitary $U$:
  $$(U\otimes U)|\Psi^-\rangle\langle\Psi^-|(U\otimes U)^\dagger
  =|\Psi^-\rangle\langle\Psi^-|.$$

## 9. Purification And Vectorization

Maximally entangled unnormalized vector:
$$|\Gamma_d\rangle=\sum_{k=0}^{d-1}|k\rangle\otimes|k\rangle.$$

Vectorization:
$$|M\rangle\rangle=\mathrm{vec}(M)=(I\otimes M)|\Gamma_d\rangle.$$

For a 2 by 2 matrix
$$M=\begin{pmatrix}p&q\\r&s\end{pmatrix},\quad
\mathrm{vec}(M)=(p,r,q,s)^T.$$

Key identities:

- $\mathrm{vec}(|v_1\rangle\langle v_2|)=\overline{|v_2\rangle}\otimes|v_1\rangle$.
- $(I\otimes M)|\Gamma_d\rangle=(M^T\otimes I)|\Gamma_d\rangle$.
- $\mathrm{Tr}[M]=\langle\Gamma_d|(I\otimes M)|\Gamma_d\rangle$.
- $\mathrm{vec}(KML^\dagger)=(L\otimes K)\mathrm{vec}(M)$.

Purification from spectral decomposition:

If
$$\rho=\sum_k\lambda_k|\psi_k\rangle\langle\psi_k|,$$
then
$$|\psi_\rho\rangle=\sum_k\sqrt{\lambda_k}\,|\psi_k\rangle\otimes|\psi_k\rangle$$
is a purification, meaning tracing out one subsystem gives $\rho$.

## 10. Gates And Circuits

### Single-Qubit Gates

Hadamard:
$$H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

Actions:

- $H|0\rangle=|+\rangle$.
- $H|1\rangle=|-\rangle$.
- $H|+\rangle=|0\rangle$.
- $H|-\rangle=|1\rangle$.

Phase gate:
$$S=\begin{pmatrix}1&0\\0&i\end{pmatrix},\quad S^\dagger=\begin{pmatrix}1&0\\0&-i\end{pmatrix}.$$

T gate:
$$T=\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}.$$

Phase gate family:
$$S(\theta)=\begin{pmatrix}1&0\\0&e^{i\theta}\end{pmatrix}.$$

Rotation:
$$R_z(\theta)=e^{-i\theta Z/2}
=\begin{pmatrix}e^{-i\theta/2}&0\\0&e^{i\theta/2}\end{pmatrix}.$$

General Pauli rotation:
$$e^{i\phi(\vec n\cdot\vec\sigma)}
=\cos(\phi)I+i\sin(\phi)(\vec n\cdot\vec\sigma),\quad |\vec n|=1.$$

State preparation from $|0\rangle$:

- $|+\rangle$: apply $H$.
- $|-\rangle$: apply $X$ then $H$, or $H$ then $Z$.
- $(|0\rangle-i|1\rangle)/\sqrt2$: apply $H$ then $S^\dagger$.
- $\cos(\theta/2)|0\rangle+\sin(\theta/2)|1\rangle$: apply $R_y(\theta)$.
- $(|0\rangle+e^{i\theta}|1\rangle)/\sqrt2$: apply $H$ then $S(\theta)$.

Useful $R_y$ convention:
$$R_y(\theta)=
\begin{pmatrix}
\cos(\theta/2)&-\sin(\theta/2)\\
\sin(\theta/2)&\cos(\theta/2)
\end{pmatrix}.$$

### Two-Qubit Gates

CNOT:
$$\mathrm{CNOT}|c,t\rangle=|c,c\oplus t\rangle.$$

Matrix in order $00,01,10,11$:
$$\mathrm{CNOT}=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}.$$

Operator form:
$$\mathrm{CNOT}=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes X.$$

Controlled-U:
$$C(U)=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes U
=\begin{pmatrix}I&0\\0&U\end{pmatrix}.$$

Controlled-Z:
$$CZ=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes Z
=\mathrm{diag}(1,1,1,-1).$$

Swap:
$$F|a,b\rangle=|b,a\rangle.$$

### Circuit Identities

- $CZ=(I\otimes H)\,\mathrm{CNOT}\,(I\otimes H)$, where $H$ is on the target.
- Swap = three CNOTs:
  $$\mathrm{SWAP}=\mathrm{CNOT}_{12}\mathrm{CNOT}_{21}\mathrm{CNOT}_{12}.$$
- Flip CNOT direction:
  $$\mathrm{CNOT}_{21}=(H\otimes H)\mathrm{CNOT}_{12}(H\otimes H).$$
- Pauli propagation through CNOT:
  - $\mathrm{CNOT}(X\otimes I)=(X\otimes X)\mathrm{CNOT}$
  - $\mathrm{CNOT}(I\otimes X)=(I\otimes X)\mathrm{CNOT}$
  - $\mathrm{CNOT}(Z\otimes I)=(Z\otimes I)\mathrm{CNOT}$
  - $\mathrm{CNOT}(I\otimes Z)=(Z\otimes Z)\mathrm{CNOT}$

Proof template for circuit identities:

1. Apply left side to $|00\rangle,|01\rangle,|10\rangle,|11\rangle$.
2. Apply right side to same basis.
3. Same action on basis means same operator by linearity.

### Assignment 8 / Problem Bank Controlled-S Gadget

This template appears in the final-review material: two ancilla qubits start in $|00\rangle$, each gets $H$, a controlled branch operation acts on an arbitrary third-qubit state $|\psi\rangle$, then the first two qubits get final $H$ gates and are measured in Z.

After the first two Hadamards:
$$\frac12\sum_{a,b\in\{0,1\}}|a,b\rangle|\psi\rangle.$$

Branch operators on the third qubit:

- $U_{00}=S$
- $U_{01}=S$
- $U_{10}=S$
- $U_{11}=XSX=\mathrm{diag}(i,1)$

After the final Hadamards, the unnormalized third-qubit state conditioned on measured outcome $m=(m_1,m_2)$ is
$$|\phi_m\rangle=\frac14\sum_{a,b}(-1)^{am_1+bm_2}U_{ab}|\psi\rangle.$$

Outcomes:

| Outcome | Unnormalized branch | Probability | Normalized state |
| --- | --- | --- | --- |
| 00 | $\frac14(3S+XSX)\lvert\psi\rangle$ | $5/8$ | $\frac{3S+XSX}{\sqrt{10}}\lvert\psi\rangle$ |
| 01 | $\frac14(S-XSX)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |
| 10 | $\frac14(S-XSX)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |
| 11 | $\frac14(XSX-S)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |

Check: $5/8+1/8+1/8+1/8=1$.

### Assignment 6 Measurement Circuit

For the circuit with initial $|00\rangle$, $H$ on the first qubit, controlled-$S$ on the second, then $H$ on the second and SWAP, the state before measurement is $|++\rangle$.

Measurement probabilities:

- Z on both qubits: all four outcomes $00,01,10,11$ have probability $1/4$.
- X on both qubits: $++$ has probability 1.
- Bell measurement: $\Phi^+$ and $\Psi^+$ each have probability $1/2$; $\Phi^-$ and $\Psi^-$ have probability 0.

### Matrix From Basis Actions

If a gate is defined by its action on basis states, its matrix columns are those output vectors in the same basis order. In the $00,01,10,11$ basis:

1. Column 1 is $U|00\rangle$.
2. Column 2 is $U|01\rangle$.
3. Column 3 is $U|10\rangle$.
4. Column 4 is $U|11\rangle$.

Use this for custom gates such as the Molmer-Sorensen gate: write each mapped output as a four-entry column, then assemble the columns.

## 11. Teleportation

Goal: transfer an unknown qubit state
$$|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$$
from Alice to Bob using one shared Bell pair and two classical bits.

Resource:
$$|\Phi^+\rangle_{AB}=(|00\rangle+|11\rangle)/\sqrt2.$$

Protocol:

1. Alice has unknown qubit $A'$ and her half $A$ of $|\Phi^+\rangle_{AB}$.
2. Alice applies CNOT from $A'$ to $A$.
3. Alice applies $H$ to $A'$.
4. Alice measures $A'A$ in the Z basis, getting two bits.
5. Alice sends the two classical bits to Bob.
6. Bob applies a Pauli correction.

Outcome table:

| Alice outcome | Bob before correction | Bob correction |
| --- | --- | --- |
| 00 | $\lvert\psi\rangle$ | $I$ |
| 01 | $X\lvert\psi\rangle$ | $X$ |
| 10 | $Z\lvert\psi\rangle$ | $Z$ |
| 11 | $XZ\lvert\psi\rangle$ up to phase | apply $X$ then $Z$ |

Every Alice outcome has probability $1/4$.

Important:

- Teleportation is not faster than light because Bob needs Alice's classical bits.
- It works for mixed states too, by linearity/density-operator version.

## 12. Superdense Coding

Goal: send two classical bits using one transmitted qubit, assuming Alice and Bob already share $|\Phi^+\rangle$.

Protocol:

1. Alice and Bob share $|\Phi^+\rangle$.
2. Alice encodes two bits using a Pauli on her qubit.
3. Alice sends her qubit to Bob.
4. Bob performs a Bell measurement.
5. Bell outcome reveals Alice's two bits.

Common encoding table:

| Bits | Alice operation | State sent to Bell measurement |
| --- | --- | --- |
| 00 | $I$ | $\lvert\Phi^+\rangle$ |
| 01 | $X$ | $\lvert\Psi^+\rangle$ |
| 10 | $Z$ | $\lvert\Phi^-\rangle$ |
| 11 | $XZ$ | $\lvert\Psi^-\rangle$ up to phase |

Reason it works: Bell states are orthonormal, so Bob can distinguish them perfectly.

## 13. Swap Test

Goal: estimate closeness/fidelity of two pure states:
$$|\langle\psi|\phi\rangle|^2.$$

Circuit:

1. Ancilla starts $|0\rangle$.
2. Apply $H$ to ancilla.
3. Apply controlled-SWAP to $|\psi\rangle$ and $|\phi\rangle$.
4. Apply $H$ to ancilla.
5. Measure ancilla in Z basis.

Probabilities:

$$\Pr[0]=\frac12(1+|\langle\psi|\phi\rangle|^2),$$
$$\Pr[1]=\frac12(1-|\langle\psi|\phi\rangle|^2).$$

Estimator:

- Record outcome 0 as $+1$ and outcome 1 as $-1$.
- Sample average estimates $|\langle\psi|\phi\rangle|^2$.

Related POVM for testing equality to known $|\phi\rangle$:
$$\{|\phi\rangle\langle\phi|,\ I-|\phi\rangle\langle\phi|\}.$$

Use Cauchy-Schwarz to show $I-|\phi\rangle\langle\phi|\succeq0$:
$$\langle v|(I-|\phi\rangle\langle\phi|)|v\rangle
=\langle v|v\rangle-|\langle v|\phi\rangle|^2\ge0.$$

## 14. Hadamard Test

Goal: estimate $\langle\psi|U|\psi\rangle$ for unitary $U$.

### Real Part

Circuit:

1. Ancilla $|0\rangle$.
2. Apply $H$ to ancilla.
3. Apply controlled-$U$.
4. Apply $H$ to ancilla.
5. Measure ancilla in Z basis.

Probabilities:

$$\Pr[0]=\frac12(1+\mathrm{Re}\langle\psi|U|\psi\rangle),$$
$$\Pr[1]=\frac12(1-\mathrm{Re}\langle\psi|U|\psi\rangle).$$

### Imaginary Part

Use $S^\dagger$ on the ancilla before controlled-$U$:

1. $H$
2. $S^\dagger$
3. controlled-$U$
4. $H$
5. Z measurement

Then:

$$\Pr[0]=\frac12(1+\mathrm{Im}\langle\psi|U|\psi\rangle),$$
$$\Pr[1]=\frac12(1-\mathrm{Im}\langle\psi|U|\psi\rangle).$$

Estimator:

- If $\Pr[0]=\frac12(1+\alpha)$ and $\Pr[1]=\frac12(1-\alpha)$, encode outcomes as $+1,-1$.
- Sample mean estimates $\alpha$.

## 15. Quantum Fourier Transform

### Classical DFT

For signal $x_0,\dots,x_{N-1}$:
$$y_k=\frac1{\sqrt N}\sum_{j=0}^{N-1}e^{2\pi ijk/N}x_j.$$

### QFT Definition

For dimension $d$:
$$Q_d|j\rangle=\frac1{\sqrt d}\sum_{k=0}^{d-1}\omega^{jk}|k\rangle,\quad
\omega=e^{2\pi i/d}.$$

Matrix entries:
$$[Q_d]_{k,j}=\frac1{\sqrt d}\omega^{jk}.$$

Facts:

- $Q_d$ is unitary.
- For $d=2$, $Q_2=H$.
- For $n$ qubits, $d=2^n$.
- Circuit uses Hadamards and controlled phase rotations, followed by reversal/permutation of qubit order.

Rotation gates used in QFT circuits:
$$R_m=\begin{pmatrix}1&0\\0&e^{2\pi i/2^m}\end{pmatrix}.$$

## 16. Universal Gate Sets

Goal: implement arbitrary unitaries from elementary gates.

Two versions:

- Exact universality: usually requires infinitely many gates/continuous rotations.
- Approximate universality: finite gate set approximates arbitrary unitaries to desired error.

Single-qubit gates:

- Every single-qubit unitary can be decomposed using rotations, e.g. $R_z$, $R_y$, and phases.
- Rotation families $R_x(\theta), R_y(\theta), R_z(\theta)$ are continuous, so exact universality is not finite.

Clifford group:

- Generated by $H$, $S$, and CNOT.
- Clifford gates map Pauli operators to Pauli operators under conjugation.
- $\{H,S,\mathrm{CNOT}\}$ is not universal.

Make it universal by adding any one-qubit non-Clifford gate such as $T$:

- $\{H,S,\mathrm{CNOT},T\}$ is universal.
- Since $S=T^2$, $\{H,\mathrm{CNOT},T\}$ is also universal.

Problem-bank answer for "three ways to modify Clifford set":

- Add $T$.
- Replace/add a non-Clifford single-qubit rotation.
- Add any gate outside the Clifford group that, with Clifford gates, gives an approximate universal set.

## 17. Noise And Quantum Channels

Noise can be modeled as random unwanted gates applied to a state.

### Bit-Flip Channel

Let $p$ be the error probability. Apply $X$ with probability $p$, do nothing with probability $1-p$:
$$\mathcal E_X(\rho)=(1-p)\rho+pX\rho X.$$

Bloch-vector transformation:
$$r_x'=r_x,\quad r_y'=(1-2p)r_y,\quad r_z'=(1-2p)r_z.$$

### Phase-Flip / Dephasing Channel

Apply $Z$ with probability $p$, do nothing with probability $1-p$:
$$\mathcal E_Z(\rho)=(1-p)\rho+pZ\rho Z.$$

Bloch-vector transformation:
$$r_x'=(1-2p)r_x,\quad r_y'=(1-2p)r_y,\quad r_z'=r_z.$$

Matrix effect:

If
$$\rho=\begin{pmatrix}a&c\\\bar c&1-a\end{pmatrix},$$
then dephasing keeps diagonal entries and suppresses off-diagonal entries:
$$c\mapsto(1-2p)c.$$

At $p=1/2$, off-diagonal coherence vanishes.

### Depolarizing Channel

With probability $1-p$, do nothing; with probability $p$, apply one of $X,Y,Z$ uniformly:

$$\mathcal E_{\mathrm{dep}}(\rho)
=(1-p)\rho+\frac{p}{3}(X\rho X+Y\rho Y+Z\rho Z).$$

Bloch-vector transformation:
$$\vec r'=\left(1-\frac{4p}{3}\right)\vec r.$$

Equivalent form:
$$\mathcal E_{\mathrm{dep}}(\rho)
=\left(1-\frac{4p}{3}\right)\rho+\frac{4p}{3}\frac I2.$$

At $p=3/4$, the output is maximally mixed $I/2$.

## 18. Quantum Error Correction: 3-Qubit Bit-Flip Code

Logical encoding:

$$|0_L\rangle=|000\rangle,\quad |1_L\rangle=|111\rangle.$$

Arbitrary logical state:
$$|\psi_L\rangle=\alpha|0_L\rangle+\beta|1_L\rangle
=\alpha|000\rangle+\beta|111\rangle.$$

Corrects one bit flip.

Measure parity checks:

- $p_{01}=\mathrm{parity}(q_0,q_1)$.
- $p_{12}=\mathrm{parity}(q_1,q_2)$.

Syndrome table:

| $p_{01}$ | $p_{12}$ | Error | Correction |
| --- | --- | --- | --- |
| 0 | 0 | none | do nothing |
| 1 | 0 | flip on $q_0$ | apply $X$ to $q_0$ |
| 1 | 1 | flip on $q_1$ | apply $X$ to $q_1$ |
| 0 | 1 | flip on $q_2$ | apply $X$ to $q_2$ |

The problem bank asks in the order $(p_{12},p_{01})=(\mathrm{parity}(q_1,q_2),\mathrm{parity}(q_0,q_1))$:

| $p_{12}$ | $p_{01}$ | Correction |
| --- | --- | --- |
| 0 | 0 | do nothing |
| 0 | 1 | apply $X$ to $q_0$ |
| 1 | 0 | apply $X$ to $q_2$ |
| 1 | 1 | apply $X$ to $q_1$ |

## 19. High-Yield Problem Templates

### Determine If A Matrix Is A Valid Gate

1. Compute $U^\dagger U$.
2. If $U^\dagger U=I$, it is a valid quantum gate.
3. To find $U|0\rangle$ and $U|1\rangle$, read the first and second columns of $U$.

### Measurement Probabilities For A State Vector

For $|\psi\rangle=\sum_x\alpha_x|x\rangle$ in the measurement basis:

$$\Pr[x]=|\alpha_x|^2.$$

If measuring in another ONB $\{|e_k\rangle\}$:

$$\Pr[k]=|\langle e_k|\psi\rangle|^2.$$

Post-measurement state is the normalized projected state.

### Measurement Probabilities For A Density Matrix

For POVM $\{M_x\}$:

$$\Pr[x]=\mathrm{Tr}[M_x\rho].$$

For joint Alice/Bob local measurement:

$$\Pr[a,b]=\mathrm{Tr}[(M_a\otimes N_b)\rho_{AB}].$$

### Show A Set Is A POVM

1. Show each $M_x$ is PSD.
2. Show $\sum_xM_x=I$.

For rank-one positive operators $c|\psi\rangle\langle\psi|$ with $c\ge0$, positivity is automatic.

### Show A Set Is An ONB

1. Check normalization of each vector.
2. Check pairwise inner products are zero.
3. Count that there are $d$ vectors in $d$-dimensional space.

### Find A Schmidt Decomposition

1. Write coefficient matrix $C=(c_{ij})$.
2. Compute or reason about rank/SVD.
3. Singular values are Schmidt coefficients.
4. Rank 1 means product; rank greater than 1 means entangled.

### Prove Bell-State Measurement Correlations

1. Expand Bell state in the chosen basis.
2. Apply Born rule to each pair outcome.
3. Compare joint distribution with marginals.
4. If joint equals product of marginals, outcomes are independent.

### Partial Trace Of A 2-Qubit Matrix

With basis order $00,01,10,11$:

- For $\mathrm{Tr}_B$, group matrix into four 2 by 2 blocks by A indices and trace each block.
- For $\mathrm{Tr}_A$, sum the A-diagonal blocks for each B index.

### Prove Circuit Identities

Use computational-basis states:

$$|00\rangle,\ |01\rangle,\ |10\rangle,\ |11\rangle.$$

If both sides map every basis vector to the same output, the circuits are identical.

### Estimate An Unknown $\alpha$ From Binary Outcomes

If
$$\Pr[0]=\frac12(1+\alpha),\quad \Pr[1]=\frac12(1-\alpha),$$
then repeat $N$ times:

- outcome 0 -> $+1$
- outcome 1 -> $-1$

Sample mean estimates $\alpha$.

## 20. What Was Given On Recent Exam Covers

Recent exam covers in the repo provided:

- Pauli matrices $X,Y,Z$.
- Pauli-X eigenvectors $|\pm\rangle$ on Exams 3 and 5.
- Bell state vectors on Exam 3.
- Hadamard $H$.
- Phase gate $S$.
- CNOT.
- Swap on Exam 4.

Even if a formula is given, know how to use it:

- Matrix columns give gate action on basis vectors.
- Tensor products build multi-qubit gates.
- Measurement probabilities still require Born's rule.
- Circuit identities still require a proof or basis-state verification.

## 21. Common Mistakes

- Forgetting complex conjugates in inner products.
- Using amplitudes instead of modulus-squared probabilities.
- Forgetting to normalize conditional post-measurement states.
- Mixing up CNOT control and target.
- Treating a global phase as physically meaningful.
- Claiming a POVM is valid without checking both positivity and $\sum_xM_x=I$.
- Forgetting that density matrices use $\mathrm{Tr}[M\rho]$, not just state-vector amplitudes.
- Dropping the factor from Hadamards in branch-sum circuit calculations.

## 22. Final Focus Checklist

You should be able to do the following without notes:

- Normalize complex vectors and compute inner products.
- Convert between computational, X, and Y bases.
- Check whether a matrix is Hermitian, PSD, unitary, or a density operator.
- Use Pauli decomposition and Bloch vectors.
- Compute Z/X/Bell measurement probabilities.
- Compute post-measurement states.
- Take partial traces.
- Identify pure vs mixed states using $\mathrm{Tr}[\rho^2]$.
- Determine product vs entangled pure states by factorization, matrix rank, or Schmidt rank.
- Use Bell-state correlations and Bell-basis measurements.
- Explain and calculate teleportation corrections.
- Explain and calculate superdense coding encodings.
- Prove CNOT, CZ, Swap, and Pauli propagation identities.
- Run the swap-test and Hadamard-test probability derivations.
- Use sample averages to estimate an unknown quantity from repeated measurements.
- Define QFT and recognize its unitary/circuit structure.
- Explain why Clifford gates alone are not universal and why adding $T$ helps.
- Apply bit-flip, phase-flip, and depolarizing channels to Bloch vectors.
- Use the 3-qubit bit-flip code syndrome table.
