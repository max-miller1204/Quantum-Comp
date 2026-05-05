# CS 4134 Final Cheat Sheet

Based on the repo material for **Quantum Computation and Information Processing**:
lectures, assignments 1-9, problem bank, and exam cover/study guide files.

## 0. Exam Strategy

- Always show the intermediate state, matrix, probability, or trace step. The exams deduct for missing or unclear steps.
- For circuits, compute on computational-basis states first, then extend by linearity.
- For measurement problems, write the POVM/projectors first, then apply Born's rule.
- For entanglement, use the quickest valid criterion: factorization, coefficient-matrix rank, Schmidt rank, or PPT if mixed.
- Global phase does not matter for state vectors: $\lvert \psi\rangle$ and $e^{i\theta}\lvert \psi\rangle$ represent the same physical pure state.
- Keep normalization visible: probabilities must sum to 1, state-vector norms must be 1, density matrices must have trace 1.

## 1. Core Notation And Linear Algebra

### Complex Numbers

- $z=a+bi$, $\bar z=a-bi$, $\mathrm{Re}(z)=a$, $\mathrm{Im}(z)=b$.
- $|z|^2=z\bar z=a^2+b^2$.
- Polar form: $z=re^{i\theta}=r(\cos\theta+i\sin\theta)$.
- $\overline{z_1+z_2}=\bar z_1+\bar z_2$, $\overline{z_1z_2}=\bar z_1\bar z_2$.

### Dirac Notation

- Ket $\lvert v\rangle$: column vector.
- Bra $\langle v\rvert$: conjugate transpose of $\lvert v\rangle$.
- Inner product: $\langle v\rvert w\rangle=\sum_i \bar v_i w_i$.
- $\langle v\rvert w\rangle=\overline{\langle w\rvert v\rangle}$.
- Norm: $\|v\|=\sqrt{\langle v\rvert v\rangle}$.
- Normalized state vector: $\langle v\rvert v\rangle=1$.
- Normalize: $\lvert v\rangle/\sqrt{\langle v\rvert v\rangle}$.
- Standard basis: $\lvert 0\rangle=(1,0)^T$, $\lvert 1\rangle=(0,1)^T$.

### Important Bases

- Computational/Z basis: $\lvert 0\rangle, \lvert 1\rangle$.
- X basis:
  - $\lvert +\rangle=(\lvert 0\rangle+\lvert 1\rangle)/\sqrt2$
  - $\lvert -\rangle=(\lvert 0\rangle-\lvert 1\rangle)/\sqrt2$
- Y basis:
  - $\lvert +i\rangle=(\lvert 0\rangle+i\lvert 1\rangle)/\sqrt2$
  - $\lvert -i\rangle=(\lvert 0\rangle-i\lvert 1\rangle)/\sqrt2$

### Outer Products And Projectors

- $\lvert v\rangle\langle w\rvert$ is a rank-one operator.
- $\lvert v\rangle\langle v\rvert$ is the projector onto $\lvert v\rangle$ if $\lvert v\rangle$ is normalized.
- Trace identities:
  - $\mathrm{Tr}[\lvert v_1\rangle\langle v_2\rvert]=\langle v_2\rvert v_1\rangle$
  - $\mathrm{Tr}[M\lvert v_1\rangle\langle v_2\rvert]=\langle v_2\rvert M\lvert v_1\rangle$
  - $\mathrm{Tr}[AB]=\mathrm{Tr}[BA]$

### Orthonormal Bases

- Orthonormal: $\langle e_i\rvert e_j\rangle=\delta_{ij}$.
- Completeness: if $\{\lvert e_k\rangle\}_{k=1}^d$ is an ONB, then
  $$I_d=\sum_{k=1}^d \lvert e_k\rangle\langle e_k\rvert.$$
- Change of basis:
  $$\lvert u\rangle=\sum_k \langle e_k\rvert u\rangle \lvert e_k\rangle.$$

### Matrix Classes

- Adjoint/conjugate transpose: $M^\dagger=\bar M^T$.
- Unitary: $U^\dagger U=UU^\dagger=I$.
  - Preserves inner products: $\langle Uv\rvert Uw\rangle=\langle v\rvert w\rangle$.
  - Columns form an ONB.
- Hermitian/self-adjoint: $M^\dagger=M$.
  - Eigenvalues are real.
  - Observable matrices are Hermitian.
  - General 2 by 2 Hermitian matrix:
    $$\begin{pmatrix}a&b+ci\\ b-ci&d\end{pmatrix},\quad a,b,c,d\in\mathbb R.$$
- Positive semidefinite: $M\succeq0$ iff $\langle v\rvert M\lvert v\rangle\ge0$ for all $\lvert v\rangle$.
  - Equivalent for Hermitian $M$: all eigenvalues are nonnegative.
  - $M^\dagger M\succeq0$ always.

### Useful Conjugate-Transpose Identity

$$\langle v_2\rvert M\lvert v_1\rangle=\langle M^\dagger v_2\rvert v_1\rangle.$$

### Operator Norms And Trace Distance

- Hilbert-Schmidt norm: $\|M\|_{\mathrm{HS}}=\sqrt{\mathrm{Tr}[M^\dagger M]}$.
- Trace norm: $\|M\|_1=\mathrm{Tr}\sqrt{M^\dagger M}$.
- If $P\succeq0$, then $\|P\|_1=\mathrm{Tr}[P]$.
- Operator norm:
  $$\|M\|_\infty=\sqrt{\lambda_{\max}(M^\dagger M)}.$$
- If $U$ is unitary, then $\|U\|_\infty=1$.
- Trace distance:
  $$D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.$$
- Every pure state is the same trace distance from the maximally mixed state:
  $$D(\lvert \psi\rangle\langle\psi\rvert,I_d/d)=1-\frac1d.$$
- If $\rho$ has rank $r$ with nonzero eigenvalues $\lambda_1,\dots,\lambda_r$, then
  $$D(\rho,I_d/d)=\frac12\left(\sum_{k=1}^r\left|\lambda_k-\frac1d\right|+\frac{d-r}{d}\right).$$

### Building A Unitary From Two ONBs

If $\{\lvert e_k\rangle\}$ and $\{\lvert f_k\rangle\}$ are ONBs, then
$$U=\sum_k \lvert e_k\rangle\langle f_k\rvert$$
is unitary and maps $\lvert f_k\rangle\mapsto \lvert e_k\rangle$.

## 2. Tensor Products

- Tensor states: $\lvert v\rangle\otimes\lvert w\rangle$, also written $\lvert v,w\rangle$.
- Operator action:
  $$(A\otimes B)(\lvert v\rangle\otimes\lvert w\rangle)=(A\lvert v\rangle)\otimes(B\lvert w\rangle).$$
- Two-qubit computational-basis order used in the repo:
  $$\lvert 00\rangle,\ \lvert 01\rangle,\ \lvert 10\rangle,\ \lvert 11\rangle.$$
- Kronecker product: if $A=(a_{ij})$, then $A\otimes B$ replaces each $a_{ij}$ by $a_{ij}B$.

## 3. Probability And Statistics

- Joint PMF: $p_{X,Y}(x,y)=\Pr[X=x,Y=y]$.
- Marginal: $p_X(x)=\sum_y p_{X,Y}(x,y)$.
- Conditional: $\Pr[A|B]=\Pr[A\cap B]/\Pr[B]$.
- Total probability: if $\{B_i\}$ partitions the sample space, then
  $$\Pr[A]=\sum_i\Pr[A|B_i]\Pr[B_i].$$
- Bayes:
  $$\Pr[B_j|A]=\frac{\Pr[A|B_j]\Pr[B_j]}{\sum_i\Pr[A|B_i]\Pr[B_i]}.$$
- Independence: $p_{X,Y}(x,y)=p_X(x)p_Y(y)$.
- Expectation: $\mathbb E[X]=\sum_x x\Pr[X=x]$.
- Variance: $\mathrm{Var}(X)=\mathbb E[X^2]-\mathbb E[X]^2$.
- Covariance: $\mathrm{Cov}(X,Y)=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]$.
- PMF normalization: solve unknown constants from $\sum_xp_X(x)=1$.
- Markov-chain path probability:
  $$\Pr[X_0=x_0,\dots,X_n=x_n]=\Pr[X_0=x_0]\prod_{t=1}^nP_{x_{t-1},x_t}.$$
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

- Pure state: $\rho=\lvert \psi\rangle\langle\psi\rvert$.
- Mixed state: $\rho=\sum_i p_i\lvert \psi_i\rangle\langle\psi_i\rvert$, with $p_i\ge0$, $\sum_i p_i=1$.
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

- $\lvert 0\rangle$: $(0,0,1)$.
- $\lvert 1\rangle$: $(0,0,-1)$.
- $\lvert +\rangle$: $(1,0,0)$.
- $\lvert -\rangle$: $(-1,0,0)$.
- $\lvert +i\rangle$: $(0,1,0)$.
- $\lvert -i\rangle$: $(0,-1,0)$.

## 5. Pauli Operators

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

Actions:

- $X\lvert 0\rangle=\lvert 1\rangle$, $X\lvert 1\rangle=\lvert 0\rangle$.
- $Y\lvert 0\rangle=i\lvert 1\rangle$, $Y\lvert 1\rangle=-i\lvert 0\rangle$.
- $Z\lvert 0\rangle=\lvert 0\rangle$, $Z\lvert 1\rangle=-\lvert 1\rangle$.

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

Hilbert-Schmidt norm in Pauli coefficients:
$$\|M\|_{\mathrm{HS}}=\sqrt{\frac12\left(|c_0|^2+|c_1|^2+|c_2|^2+|c_3|^2\right)}.$$

### Important Two-Qubit Pauli Identities

$$\lvert \Phi^+\rangle\langle\Phi^+\rvert
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
$$\Pr[x]=\langle\psi\rvert \Pi_x\lvert \psi\rangle=\mathrm{Tr}[\Pi_x\rho].$$

Post-measurement state for pure input:
$$\lvert \psi_x\rangle=\frac{\Pi_x\lvert \psi\rangle}{\sqrt{\Pr[x]}}.$$

For density operators:
$$\rho_x=\frac{\Pi_x\rho\Pi_x}{\mathrm{Tr}[\Pi_x\rho]}.$$

### POVMs

A POVM is a finite set $\{M_x\}$ such that:

- $M_x\succeq0$ for all $x$.
- $\sum_xM_x=I$.

Outcome probability:
$$\Pr[x]=\mathrm{Tr}[M_x\rho].$$

Examples:

- Z measurement: $\{\lvert 0\rangle\langle0\rvert,\ \lvert 1\rangle\langle1\rvert\}$.
- X measurement: $\{\lvert +\rangle\langle+\rvert,\ \lvert -\rangle\langle-\rvert\}$.
- Any ONB measurement: $\{\lvert e_k\rangle\langle e_k\rvert\}$.
- Five-state POVM from Assignment 9:
  $$\left\{\frac25\lvert \psi_k\rangle\langle\psi_k\rvert\right\}_{k=0}^4,\quad
  \lvert \psi_k\rangle=\cos(2\pi k/5)\lvert 0\rangle+\sin(2\pi k/5)\lvert 1\rangle.$$

For $\lvert \psi\rangle=\alpha\lvert 0\rangle+\beta\lvert 1\rangle$, the five-state POVM probabilities are
$$p_k=\frac25\left\lvert\langle\psi_k\rvert \psi\rangle\right\rvert^2
=\frac25|\alpha\cos(2\pi k/5)+\beta\sin(2\pi k/5)|^2.$$

With $c_k=\cos(2\pi k/5)$ and $s_k=\sin(2\pi k/5)$:
$$p_k=\frac25\left(|\alpha|^2c_k^2+|\beta|^2s_k^2
+2\mathrm{Re}(\bar\alpha\beta)c_ks_k\right).$$

To show it is a POVM, use
$$\sum_k c_k^2=\frac52,\quad \sum_k s_k^2=\frac52,\quad \sum_k c_ks_k=0.$$

Naimark/projective-measurement principle:

- Every POVM can be implemented as a projective measurement on a larger system with an added probe/ancilla.
- To prove this direction, build a unitary on system plus probe whose measurement branches reproduce the POVM effects.

### Observable Expectation Values

For Hermitian observable
$$M=\sum_i\lambda_i\lvert v_i\rangle\langle v_i\rvert,$$
the measurement outcomes are eigenvalues $\lambda_i$ with probabilities
$$\Pr[\lambda_i]=\mathrm{Tr}[\lvert v_i\rangle\langle v_i\rvert \rho].$$

Expected value:
$$\mathbb E[M]=\sum_i\lambda_i\Pr[\lambda_i]=\mathrm{Tr}[M\rho].$$

If $M=\sum_j c_jU_j$ is decomposed into unitaries, estimate each
$\langle\psi\rvert U_j\lvert \psi\rangle$ using the Hadamard test and combine linearly.

## 7. Partial Trace

For product operators:

$$\mathrm{Tr}_A[P_A\otimes M_B]=\mathrm{Tr}[P_A]M_B.$$

$$\mathrm{Tr}_B[P_A\otimes M_B]=\mathrm{Tr}[M_B]P_A.$$

General basis rule:
$$\mathrm{Tr}_B[\lvert i\rangle\langle j\rvert_A\otimes\lvert k\rangle\langle l\rvert_B]
=\lvert i\rangle\langle j\rvert_A\langle l\rvert k\rangle.$$

Useful identity:
$$\mathrm{Tr}_A[(I_A\otimes M_B)H_{AB}(I_A\otimes N_B)]
=M_B\,\mathrm{Tr}_A[H_{AB}]\,N_B.$$

For a two-qubit 4 by 4 matrix in basis $00,01,10,11$:

- $\mathrm{Tr}_B$ gives a 2 by 2 matrix whose entries are traces over B-index blocks.
- $\mathrm{Tr}_A$ sums A-index blocks.

Explicitly, if $M_{ab,a'b'}=\langle a,b\rvert M\lvert a',b'\rangle$, then
$$[\mathrm{Tr}_B(M)]_{a,a'}=\sum_{b\in\{0,1\}}M_{ab,a'b},\quad
[\mathrm{Tr}_A(M)]_{b,b'}=\sum_{a\in\{0,1\}}M_{ab,ab'}.$$

Reduced state:
$$\rho_A=\mathrm{Tr}_B[\rho_{AB}],\quad \rho_B=\mathrm{Tr}_A[\rho_{AB}].$$

## 8. Bell States And Entanglement

### Bell Basis

$$\lvert \Phi^+\rangle=\frac{\lvert 00\rangle+\lvert 11\rangle}{\sqrt2},\quad
\lvert \Phi^-\rangle=\frac{\lvert 00\rangle-\lvert 11\rangle}{\sqrt2}.$$

$$\lvert \Psi^+\rangle=\frac{\lvert 01\rangle+\lvert 10\rangle}{\sqrt2},\quad
\lvert \Psi^-\rangle=\frac{\lvert 01\rangle-\lvert 10\rangle}{\sqrt2}.$$

Facts:

- They form an ONB for two qubits.
- Each Bell state is maximally entangled.
- Reduced state of either qubit is maximally mixed: $I/2$.
- Bell measurement POVM:
  $$\{\lvert \Phi^+\rangle\langle\Phi^+\rvert,\ \lvert \Phi^-\rangle\langle\Phi^-\rvert,\ \lvert \Psi^+\rangle\langle\Psi^+\rvert,\ \lvert \Psi^-\rangle\langle\Psi^-\rvert\}.$$

Correlations in Z basis:

- $\lvert \Phi^\pm\rangle$: same outcomes, 00 or 11.
- $\lvert \Psi^\pm\rangle$: opposite outcomes, 01 or 10.

Pauli action:

- $X$ on either qubit maps $\lvert \Phi^+\rangle\leftrightarrow\lvert \Psi^+\rangle$.
- $X$ on either qubit maps $\lvert \Phi^-\rangle\leftrightarrow\lvert \Psi^-\rangle$ up to global phase.
- $Z$ changes plus/minus sign within the same same/opposite family.

### GHZ States

Three-qubit GHZ:
$$\lvert \mathrm{GHZ}_3\rangle=\frac{\lvert 000\rangle+\lvert 111\rangle}{\sqrt2}.$$

$n$-qubit GHZ:
$$\lvert \mathrm{GHZ}_n\rangle=\frac{\lvert 0\rangle^{\otimes n}+\lvert 1\rangle^{\otimes n}}{\sqrt2}.$$

Problem-bank GHZ basis:
$$\lvert \mathrm{GHZ}_{z,\vec x}\rangle=(Z^z\otimes X^{\vec x})\lvert \mathrm{GHZ}_n\rangle,\quad
z\in\{0,1\},\ \vec x\in\{0,1\}^{n-1}.$$

- These $2^n$ vectors form an ONB.
- Their projectors form a POVM.
- Tracing out any one qubit of $\lvert \mathrm{GHZ}_3\rangle\langle\mathrm{GHZ}_3\rvert$ kills the off-diagonal coherence and leaves classical correlation on the remaining pair.

### Product Vs Entangled

Pure bipartite state:

- Product iff $\lvert \psi\rangle_{AB}=\lvert a\rangle_A\otimes\lvert b\rangle_B$.
- Entangled iff it cannot be written as a product.

Coefficient-matrix test:

1. Write $\lvert \psi\rangle=\sum_{ij}c_{ij}\lvert i\rangle\lvert j\rangle$.
2. Form coefficient matrix $C=(c_{ij})$.
3. Product iff $\mathrm{rank}(C)=1$.
4. Entangled iff $\mathrm{rank}(C)>1$.

### Schmidt Decomposition

Every bipartite pure state has
$$\lvert \psi\rangle_{AB}=\sum_{k=1}^r s_k\lvert a_k\rangle\lvert b_k\rangle,$$
where $s_k>0$, $\{\lvert a_k\rangle\}$ and $\{\lvert b_k\rangle\}$ are ON sets.

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
$$\rho=\frac12(\lvert 00\rangle\langle00\rvert +\lvert 11\rangle\langle11\rvert).$$

- Correlated in Z basis.
- Uncorrelated in X basis.

Singlet:
$$\lvert \Psi^-\rangle=\frac{\lvert 01\rangle-\lvert 10\rangle}{\sqrt2}.$$

- Perfectly anti-correlated in any common basis.
- For any single-qubit unitary $U$:
  $$(U\otimes U)\lvert \Psi^-\rangle\langle\Psi^-\rvert (U\otimes U)^\dagger
  =\lvert \Psi^-\rangle\langle\Psi^-\rvert.$$

## 9. Purification And Vectorization

Maximally entangled unnormalized vector:
$$\lvert \Gamma_d\rangle=\sum_{k=0}^{d-1}\lvert k\rangle\otimes\lvert k\rangle.$$

Vectorization:
$$\lvert M\rangle\rangle=\mathrm{vec}(M)=(I\otimes M)\lvert \Gamma_d\rangle.$$

For a 2 by 2 matrix
$$M=\begin{pmatrix}p&q\\r&s\end{pmatrix},\quad
\mathrm{vec}(M)=(p,r,q,s)^T.$$

Key identities:

- $\mathrm{vec}(\lvert v_1\rangle\langle v_2\rvert)=\overline{\lvert v_2\rangle}\otimes\lvert v_1\rangle$.
- $(I\otimes M)\lvert \Gamma_d\rangle=(M^T\otimes I)\lvert \Gamma_d\rangle$.
- $\mathrm{Tr}[M]=\langle\Gamma_d\rvert (I\otimes M)\lvert \Gamma_d\rangle$.
- $\mathrm{vec}(KML^\dagger)=(\overline L\otimes K)\mathrm{vec}(M)$.

Purification from spectral decomposition:

If
$$\rho=\sum_k\lambda_k\lvert \psi_k\rangle\langle\psi_k\rvert,$$
then
$$\lvert \psi_\rho\rangle_{ES}=\sum_k\sqrt{\lambda_k}\,\overline{\lvert \psi_k\rangle}_E\otimes\lvert \psi_k\rangle_S
=(I_E\otimes\sqrt\rho)\lvert \Gamma_d\rangle$$
is a purification, meaning $\mathrm{Tr}_E[\lvert \psi_\rho\rangle\langle\psi_\rho\rvert]=\rho$.

## 10. Gates And Circuits

### Single-Qubit Gates

Hadamard:
$$H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

Actions:

- $H\lvert 0\rangle=\lvert +\rangle$.
- $H\lvert 1\rangle=\lvert -\rangle$.
- $H\lvert +\rangle=\lvert 0\rangle$.
- $H\lvert -\rangle=\lvert 1\rangle$.

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

State preparation from $\lvert 0\rangle$:

- $\lvert +\rangle$: apply $H$.
- $\lvert -\rangle$: apply $X$ then $H$, or $H$ then $Z$.
- $(\lvert 0\rangle-i\lvert 1\rangle)/\sqrt2$: apply $H$ then $S^\dagger$.
- $\cos(\theta/2)\lvert 0\rangle+\sin(\theta/2)\lvert 1\rangle$: apply $R_y(\theta)$.
- $(\lvert 0\rangle+e^{i\theta}\lvert 1\rangle)/\sqrt2$: apply $H$ then $S(\theta)$.

Useful $R_y$ convention:
$$R_y(\theta)=
\begin{pmatrix}
\cos(\theta/2)&-\sin(\theta/2)\\
\sin(\theta/2)&\cos(\theta/2)
\end{pmatrix}.$$

### Two-Qubit Gates

CNOT:
$$\mathrm{CNOT}\lvert c,t\rangle=\lvert c,c\oplus t\rangle.$$

Matrix in order $00,01,10,11$:
$$\mathrm{CNOT}=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}.$$

Operator form:
$$\mathrm{CNOT}=\lvert 0\rangle\langle0\rvert \otimes I+\lvert 1\rangle\langle1\rvert \otimes X.$$

Controlled-U:
$$C(U)=\lvert 0\rangle\langle0\rvert \otimes I+\lvert 1\rangle\langle1\rvert \otimes U
=\begin{pmatrix}I&0\\0&U\end{pmatrix}.$$

Controlled-Z:
$$CZ=\lvert 0\rangle\langle0\rvert \otimes I+\lvert 1\rangle\langle1\rvert \otimes Z
=\mathrm{diag}(1,1,1,-1).$$

Swap:
$$F\lvert a,b\rangle=\lvert b,a\rangle.$$

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

1. Apply left side to $\lvert 00\rangle,\lvert 01\rangle,\lvert 10\rangle,\lvert 11\rangle$.
2. Apply right side to same basis.
3. Same action on basis means same operator by linearity.

### Assignment 8 / Problem Bank Controlled-S Gadget

Circuit: two ancilla qubits start in $\lvert 00\rangle$, each gets $H$. The third qubit holds $\lvert\psi\rangle$. The two ancillas jointly control two Toffoli gates (CCX) with target on the third qubit; an $S$ gate sits between them. The first two qubits get final $H$ gates and are measured in Z.

After the first two Hadamards:
$$\frac12\sum_{a,b\in\{0,1\}}\lvert a,b\rangle\lvert \psi\rangle.$$

Each Toffoli applies $X$ to qubit 3 only when $a=b=1$. So the operator on qubit 3 conditioned on $(a,b)$ is $U_{ab}=X^{ab}\,S\,X^{ab}$:

- $U_{00}=U_{01}=U_{10}=S$
- $U_{11}=XSX=\mathrm{diag}(i,1)$

After the final Hadamards, the unnormalized third-qubit state conditioned on measured outcome $m=(m_1,m_2)$ is
$$\lvert \phi_m\rangle=\frac14\sum_{a,b}(-1)^{am_1+bm_2}U_{ab}\lvert \psi\rangle.$$

Outcomes:

| Outcome | Unnormalized branch | Probability | Normalized state |
| --- | --- | --- | --- |
| 00 | $\frac14(3S+XSX)\lvert\psi\rangle$ | $5/8$ | $\frac{3S+XSX}{\sqrt{10}}\lvert\psi\rangle$ |
| 01 | $\frac14(S-XSX)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |
| 10 | $\frac14(S-XSX)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |
| 11 | $\frac14(XSX-S)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |

Check: $5/8+1/8+1/8+1/8=1$.

### Assignment 6 Measurement Circuit

For the circuit with initial $\lvert 00\rangle$, $H$ on the first qubit, controlled-$S$ on the second, then $H$ on the second and SWAP, the state before measurement is $\lvert ++\rangle$.

Measurement probabilities:

- Z on both qubits: all four outcomes $00,01,10,11$ have probability $1/4$.
- X on both qubits: $++$ has probability 1.
- Bell measurement: $\Phi^+$ and $\Psi^+$ each have probability $1/2$; $\Phi^-$ and $\Psi^-$ have probability 0.

### Matrix From Basis Actions

If a gate is defined by its action on basis states, its matrix columns are those output vectors in the same basis order. In the $00,01,10,11$ basis:

1. Column 1 is $U\lvert 00\rangle$.
2. Column 2 is $U\lvert 01\rangle$.
3. Column 3 is $U\lvert 10\rangle$.
4. Column 4 is $U\lvert 11\rangle$.

Use this for custom gates such as the Molmer-Sorensen gate: write each mapped output as a four-entry column, then assemble the columns.

## 11. Teleportation

Goal: transfer an unknown qubit state
$$\lvert \psi\rangle=\alpha\lvert 0\rangle+\beta\lvert 1\rangle$$
from Alice to Bob using one shared Bell pair and two classical bits.

Resource:
$$\lvert \Phi^+\rangle_{AB}=(\lvert 00\rangle+\lvert 11\rangle)/\sqrt2.$$

Protocol:

1. Alice has unknown qubit $A'$ and her half $A$ of $\lvert \Phi^+\rangle_{AB}$.
2. Alice applies CNOT from $A'$ to $A$.
3. Alice applies $H$ to $A'$.
4. Alice measures $A'A$ in the Z basis, getting two bits.
5. Alice sends the two classical bits to Bob.
6. Bob applies a Pauli correction.

Outcome table (Alice outcome $(z, x)$, where $z$ is the H'd qubit's bit):

| Alice outcome $(z,x)$ | Bob before correction | Bob correction |
| --- | --- | --- |
| 00 | $\lvert\psi\rangle$ | $I$ |
| 01 | $X\lvert\psi\rangle$ | $X$ |
| 10 | $Z\lvert\psi\rangle$ | $Z$ |
| 11 | $XZ\lvert\psi\rangle$ | apply $X$ then $Z$ |

Every Alice outcome has probability $1/4$. Bob's correction $Z^zX^x$ recovers $\lvert\psi\rangle$ since $Z^zX^x \cdot XZ = I$ when $(z,x)=(1,1)$.

Important:

- Teleportation is not faster than light because Bob needs Alice's classical bits.
- It works for mixed states too, by linearity/density-operator version.

## 12. Superdense Coding

Goal: send two classical bits using one transmitted qubit, assuming Alice and Bob already share $\lvert \Phi^+\rangle$.

Protocol:

1. Alice and Bob share $\lvert \Phi^+\rangle$.
2. Alice encodes two bits using a Pauli on her qubit.
3. Alice sends her qubit to Bob.
4. Bob performs a Bell measurement.
5. Bell outcome reveals Alice's two bits.

Common encoding table (bits $(z, x)$, Alice applies $Z^z X^x$, i.e., $X$ first, then $Z$):

| Bits $(z,x)$ | Alice operation | State sent to Bell measurement |
| --- | --- | --- |
| 00 | $I$ | $\lvert\Phi^+\rangle$ |
| 01 | $X$ | $\lvert\Psi^+\rangle$ |
| 10 | $Z$ | $\lvert\Phi^-\rangle$ |
| 11 | $ZX$ | $\lvert\Psi^-\rangle$ |

Reason it works: Bell states are orthonormal, so Bob can distinguish them perfectly. (If Alice applies $XZ$ instead of $ZX$, the encoded state for $(1,1)$ is $-\lvert\Psi^-\rangle$, indistinguishable from $\lvert\Psi^-\rangle$ under measurement.)

## 13. Swap Test

Goal: estimate closeness/fidelity of two pure states:
$$\left\lvert\langle\psi\rvert \phi\rangle\right\rvert^2.$$

Circuit:

1. Ancilla starts $\lvert 0\rangle$.
2. Apply $H$ to ancilla.
3. Apply controlled-SWAP to $\lvert \psi\rangle$ and $\lvert \phi\rangle$.
4. Apply $H$ to ancilla.
5. Measure ancilla in Z basis.

Probabilities:

$$\Pr[0]=\frac12(1+\left\lvert\langle\psi\rvert \phi\rangle\right\rvert^2),$$
$$\Pr[1]=\frac12(1-\left\lvert\langle\psi\rvert \phi\rangle\right\rvert^2).$$

Estimator:

- Record outcome 0 as $+1$ and outcome 1 as $-1$.
- Sample average estimates $\left\lvert\langle\psi\rvert \phi\rangle\right\rvert^2$.

Related POVM for testing equality to known $\lvert \phi\rangle$:
$$\{\lvert \phi\rangle\langle\phi\rvert,\ I-\lvert \phi\rangle\langle\phi\rvert\}.$$

Use Cauchy-Schwarz to show $I-\lvert \phi\rangle\langle\phi\rvert \succeq0$:
$$\langle v\rvert (I-\lvert \phi\rangle\langle\phi\rvert)\lvert v\rangle
=\langle v\rvert v\rangle-\left\lvert\langle v\rvert \phi\rangle\right\rvert^2\ge0.$$

## 14. Hadamard Test

Goal: estimate $\langle\psi\rvert U\lvert \psi\rangle$ for unitary $U$.

### Real Part

Circuit:

1. Ancilla $\lvert 0\rangle$.
2. Apply $H$ to ancilla.
3. Apply controlled-$U$.
4. Apply $H$ to ancilla.
5. Measure ancilla in Z basis.

Probabilities:

$$\Pr[0]=\frac12(1+\mathrm{Re}\langle\psi\rvert U\lvert \psi\rangle),$$
$$\Pr[1]=\frac12(1-\mathrm{Re}\langle\psi\rvert U\lvert \psi\rangle).$$

### Imaginary Part

Use $S^\dagger$ on the ancilla before controlled-$U$ if you want the same sign convention as the real-part estimator:

1. $H$
2. $S^\dagger$
3. controlled-$U$
4. $H$
5. Z measurement

Then:

$$\Pr[0]=\frac12(1+\mathrm{Im}\langle\psi\rvert U\lvert \psi\rangle),$$
$$\Pr[1]=\frac12(1-\mathrm{Im}\langle\psi\rvert U\lvert \psi\rangle).$$

If the circuit uses $S$ instead, the signs flip:
$$\Pr[0]=\frac12(1-\mathrm{Im}\langle\psi\rvert U\lvert \psi\rangle),\quad
\Pr[1]=\frac12(1+\mathrm{Im}\langle\psi\rvert U\lvert \psi\rangle).$$

Estimator:

- If $\Pr[0]=\frac12(1+\alpha)$ and $\Pr[1]=\frac12(1-\alpha)$, encode outcomes as $+1,-1$.
- Sample mean estimates $\alpha$.

## 15. Quantum Fourier Transform

### Classical DFT

For signal $x_0,\dots,x_{N-1}$:
$$y_k=\frac1{\sqrt N}\sum_{j=0}^{N-1}e^{2\pi ijk/N}x_j.$$

### QFT Definition

For dimension $d$:
$$Q_d\lvert j\rangle=\frac1{\sqrt d}\sum_{k=0}^{d-1}\omega^{jk}\lvert k\rangle,\quad
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

$$\lvert 0_L\rangle=\lvert 000\rangle,\quad \lvert 1_L\rangle=\lvert 111\rangle.$$

Arbitrary logical state:
$$\lvert \psi_L\rangle=\alpha\lvert 0_L\rangle+\beta\lvert 1_L\rangle
=\alpha\lvert 000\rangle+\beta\lvert 111\rangle.$$

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
3. To find $U\lvert 0\rangle$ and $U\lvert 1\rangle$, read the first and second columns of $U$.

### Measurement Probabilities For A State Vector

For $\lvert \psi\rangle=\sum_x\alpha_x\lvert x\rangle$ in the measurement basis:

$$\Pr[x]=|\alpha_x|^2.$$

If measuring in another ONB $\{\lvert e_k\rangle\}$:

$$\Pr[k]=\left\lvert\langle e_k\rvert \psi\rangle\right\rvert^2.$$

Post-measurement state is the normalized projected state.

### Measurement Probabilities For A Density Matrix

For POVM $\{M_x\}$:

$$\Pr[x]=\mathrm{Tr}[M_x\rho].$$

For joint Alice/Bob local measurement:

$$\Pr[a,b]=\mathrm{Tr}[(M_a\otimes N_b)\rho_{AB}].$$

### Show A Set Is A POVM

1. Show each $M_x$ is PSD.
2. Show $\sum_xM_x=I$.

For rank-one positive operators $c\lvert \psi\rangle\langle\psi\rvert$ with $c\ge0$, positivity is automatic.

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

$$\lvert 00\rangle,\ \lvert 01\rangle,\ \lvert 10\rangle,\ \lvert 11\rangle.$$

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

- Pauli matrices $X,Y,Z$ on Exams 2-5.
- Pauli-X eigenvectors $\lvert \pm\rangle$ on Exams 3 and 5.
- Bell state vectors on Exams 2 and 3.
- Hadamard $H$ on Exams 4 and 5.
- Phase gate $S$ on Exams 4 and 5.
- CNOT on Exams 4 and 5.
- Swap on Exams 2 and 4.

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
- Use Bayes/total probability, PMF normalization, and Markov-chain path products.
- Convert between computational, X, and Y bases.
- Check whether a matrix is Hermitian, PSD, unitary, or a density operator.
- Use Pauli decomposition and Bloch vectors.
- Compute Z/X/Bell measurement probabilities.
- Compute post-measurement states.
- Take partial traces.
- Identify pure vs mixed states using $\mathrm{Tr}[\rho^2]$.
- Determine product vs entangled pure states by factorization, matrix rank, or Schmidt rank.
- Use Bell-state, Bell-basis, and GHZ-basis measurement facts.
- Explain and calculate teleportation corrections.
- Explain and calculate superdense coding encodings.
- Prove CNOT, CZ, Swap, and Pauli propagation identities.
- Run the swap-test and Hadamard-test probability derivations.
- Use sample averages to estimate an unknown quantity from repeated measurements.
- Define QFT and recognize its unitary/circuit structure.
- Explain why Clifford gates alone are not universal and why adding $T$ helps.
- Apply bit-flip, phase-flip, and depolarizing channels to Bloch vectors.
- Use operator norms, trace distance, and the 3-qubit bit-flip code syndrome table.
