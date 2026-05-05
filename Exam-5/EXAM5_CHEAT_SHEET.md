# CS 4134 Test 5 Cheat Sheet

Based on the Test 5 cover sheet, Assignments 8 and 9, and the refreshed OCR from the problem bank and late-course lectures.

## 0. Exam Strategy

- Exam date: Tuesday, May 5, 2026.
- Format: 6 problems, 75 minutes.
- Cover sheet provides: Pauli matrices $X,Y,Z$, X-basis states $|+\rangle,|-\rangle$, $H$, $S$, and CNOT.
- Always show intermediate states, branch amplitudes, probabilities, and trace steps. The grading policy deducts for missing or unclear work.
- For circuits, compute on computational-basis states first, then extend by linearity.
- For measurement problems, keep the unnormalized post-measurement branch visible; probability is its squared norm.
- Global phase does not matter: $|\psi\rangle$ and $e^{i\theta}|\psi\rangle$ represent the same state.

Likely problem map:

| Source | High-value content |
| --- | --- |
| Assignment 8 | Two-ancilla controlled-$S$ circuit, CNOT/Pauli identities, state preparation from $\lvert0\rangle$ |
| Assignment 9 | Pure vs mixed states, five-state POVM, Pauli algebra, Pauli decomposition, Pauli twirling |
| Problem bank | Same two-ancilla circuit as an $R_z(\theta)$ gate, imaginary Hadamard test, controlled-$S$ probabilities, universal gate sets |
| Noise lecture | Bit flip, phase flip, depolarizing channel, Bloch-vector transformations |

## 1. Core Gates And States

### Pauli Operators

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

Actions:

| Gate | $\lvert0\rangle$ | $\lvert1\rangle$ |
| --- | --- | --- |
| $X$ | $\lvert1\rangle$ | $\lvert0\rangle$ |
| $Y$ | $i\lvert1\rangle$ | $-i\lvert0\rangle$ |
| $Z$ | $\lvert0\rangle$ | $-\lvert1\rangle$ |

### X Basis And Hadamard

$$
\lvert+\rangle=\frac{\lvert0\rangle+\lvert1\rangle}{\sqrt2},\quad
\lvert-\rangle=\frac{\lvert0\rangle-\lvert1\rangle}{\sqrt2}.
$$

They are Pauli-X eigenvectors:

$$
X\lvert+\rangle=+\lvert+\rangle,\quad
X\lvert-\rangle=-\lvert-\rangle.
$$

$$
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

Actions:

| Input | Output |
| --- | --- |
| $\lvert0\rangle$ | $H\lvert0\rangle=\lvert+\rangle$ |
| $\lvert1\rangle$ | $H\lvert1\rangle=\lvert-\rangle$ |
| $\lvert+\rangle$ | $H\lvert+\rangle=\lvert0\rangle$ |
| $\lvert-\rangle$ | $H\lvert-\rangle=\lvert1\rangle$ |

Measuring in the X basis is the same as applying $H$ and measuring in the Z basis.

### Phase Gates

$$
S=\begin{pmatrix}1&0\\0&i\end{pmatrix},\quad
S^\dagger=\begin{pmatrix}1&0\\0&-i\end{pmatrix},\quad
S(\theta)=\begin{pmatrix}1&0\\0&e^{i\theta}\end{pmatrix}.
$$

$$S|0\rangle=|0\rangle,\quad S|1\rangle=i|1\rangle.$$

Rotation convention:

$$
R_z(\theta)=e^{-i\theta Z/2}
=\begin{pmatrix}e^{-i\theta/2}&0\\0&e^{i\theta/2}\end{pmatrix}.
$$

Up to global phase, $\mathrm{diag}(1,e^{i\theta})$ is $R_z(\theta)$.

### CNOT

With first qubit as control and second as target:

$$\mathrm{CNOT}|a,b\rangle=|a,b\oplus a\rangle.$$

Matrix in basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$:

$$
\mathrm{CNOT}=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}.
$$

## 2. Hadamard Test And Sampling

For $z=\langle\psi|U|\psi\rangle$, the real-part Hadamard test gives:

$$
\Pr[0]=\frac12(1+\mathrm{Re}(z)),\quad
\Pr[1]=\frac12(1-\mathrm{Re}(z)).
$$

State before measuring the ancilla:

$$
\frac12|0\rangle(I+U)|\psi\rangle+
\frac12|1\rangle(I-U)|\psi\rangle.
$$

Imaginary-part variants:

| Ancilla phase gate before controlled-$U$ | $\Pr[0]$ | $\Pr[1]$ | Estimate |
| --- | --- | --- | --- |
| $S$ | $\frac12(1-\mathrm{Im}(z))$ | $\frac12(1+\mathrm{Im}(z))$ | $\mathrm{Im}(z)=\Pr[1]-\Pr[0]$ |
| $S^\dagger$ | $\frac12(1+\mathrm{Im}(z))$ | $\frac12(1-\mathrm{Im}(z))$ | $\mathrm{Im}(z)=\Pr[0]-\Pr[1]$ |

Derivation shortcut:

$$
|0\rangle|\psi\rangle+\lambda|1\rangle U|\psi\rangle
\xrightarrow{H\text{ on ancilla}}
|0\rangle(|\psi\rangle+\lambda U|\psi\rangle)
+|1\rangle(|\psi\rangle-\lambda U|\psi\rangle),
$$
up to the common normalization factor.

Sampling estimator:

If
$$\Pr[0]=\frac12(1+\alpha),\quad \Pr[1]=\frac12(1-\alpha),$$
record outcome $0$ as $+1$ and outcome $1$ as $-1$. The sample average estimates $\alpha$.

Observable expectation values: any Hermitian $M=\sum_j c_j U_j$ decomposed into unitaries can be estimated by running the Hadamard test on each $U_j$ to estimate $\langle\psi|U_j|\psi\rangle$, then combining linearly to estimate $\langle M\rangle = \mathrm{Tr}[M\rho]$.

## 3. Assignment 8 Controlled-S Gadget

Two ancillas start in $|00\rangle$, each gets $H$, the third qubit is an arbitrary $|\psi\rangle$, and the first two qubits are measured in the Z basis after final $H$ gates.

Gate structure on the third qubit: **Toffoli, then $S$, then Toffoli**, where both ancillas are joint controls on each Toffoli (each vertical line carries dots on top and middle wires plus a target $\oplus$ on bottom). So $X$ is applied iff both ancillas read $1$. The branch operator on basis state $(a,b)$ of the ancillas is therefore

$$U_{ab}=X^{ab}\,S\,X^{ab},$$

where $ab$ is logical AND. (If you only had two CNOTs, $V_{ab}=X^bSX^a$, the probability $\Pr[00]$ would depend on $\lvert\psi\rangle$ — Toffolis are required for the $\lvert\psi\rangle$-independent $\frac{5}{8}$.)

After the first two Hadamards:

$$
\frac12\sum_{a,b\in\{0,1\}}|a,b\rangle|\psi\rangle.
$$

Branch operators on the third qubit:

| Branch | Operator |
| --- | --- |
| $00$ | $U_{00}=S$ |
| $01$ | $U_{01}=S$ |
| $10$ | $U_{10}=S$ |
| $11$ | $U_{11}=XSX=\mathrm{diag}(i,1)$ |

For measured outcome $m=(m_1,m_2)$, the unnormalized third-qubit branch is:

$$
|\phi_m\rangle=\frac14\sum_{a,b\in\{0,1\}}(-1)^{am_1+bm_2}U_{ab}|\psi\rangle.
$$

Outcomes:

| Outcome | Unnormalized branch | Probability | Normalized state |
| --- | --- | --- | --- |
| $00$ | $\frac14(3S+XSX)\lvert\psi\rangle$ | $5/8$ | $\frac{3S+XSX}{\sqrt{10}}\lvert\psi\rangle$ |
| $01$ | $\frac14(S-XSX)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |
| $10$ | $\frac14(S-XSX)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |
| $11$ | $\frac14(XSX-S)\lvert\psi\rangle$ | $1/8$ | global phase times $Z\lvert\psi\rangle$ |

Check:

$$\frac58+\frac18+\frac18+\frac18=1.$$

For outcome $00$:

$$
\frac{3S+XSX}{\sqrt{10}}
=\frac1{\sqrt{10}}
\begin{pmatrix}3+i&0\\0&1+3i\end{pmatrix}.
$$

The relative phase is:

$$
\frac{1+3i}{3+i}=\frac35+\frac45i=e^{i\theta}.
$$

So, up to global phase, the $00$ branch applies $R_z(\theta)$, where:

$$\cos\theta=\frac35,\quad \sin\theta=\frac45.$$

Summary: the circuit applies $R_z(\theta)$ (with $\cos\theta=3/5$, $\sin\theta=4/5$) to the third qubit when both ancilla outcomes are $0$; otherwise it applies $Z$ to the third qubit (up to global phase). This matches Problem 14 of the problem bank.

Post-measurement rule:

$$
|\psi_m\rangle=\frac{|\phi_m\rangle}{\sqrt{\Pr[m]}}.
$$

## 4. CNOT And Pauli Propagation

Best proof method: apply both sides to arbitrary $|a,b\rangle$ with $a,b\in\{0,1\}$.

Pauli propagation identities:

| Identity | Meaning |
| --- | --- |
| $\mathrm{CNOT}(X\otimes I)=(X\otimes X)\mathrm{CNOT}$ | $X$ on control spreads to target |
| $\mathrm{CNOT}(I\otimes X)=(I\otimes X)\mathrm{CNOT}$ | $X$ on target commutes through |
| $\mathrm{CNOT}(Z\otimes I)=(Z\otimes I)\mathrm{CNOT}$ | $Z$ on control commutes through |
| $\mathrm{CNOT}(I\otimes Z)=(Z\otimes Z)\mathrm{CNOT}$ | $Z$ on target spreads back to control |

Proof skeleton for $\mathrm{CNOT}(X\otimes I)=(X\otimes X)\mathrm{CNOT}$:

$$
\mathrm{CNOT}(X\otimes I)|a,b\rangle
=\mathrm{CNOT}|a\oplus1,b\rangle
=|a\oplus1,b\oplus a\oplus1\rangle.
$$

$$
(X\otimes X)\mathrm{CNOT}|a,b\rangle
=(X\otimes X)|a,b\oplus a\rangle
=|a\oplus1,b\oplus a\oplus1\rangle.
$$

Proof skeleton for $\mathrm{CNOT}(I\otimes Z)=(Z\otimes Z)\mathrm{CNOT}$:

$$
\mathrm{CNOT}(I\otimes Z)|a,b\rangle
=(-1)^b|a,b\oplus a\rangle.
$$

$$
(Z\otimes Z)\mathrm{CNOT}|a,b\rangle
=(-1)^a(-1)^{b\oplus a}|a,b\oplus a\rangle
=(-1)^b|a,b\oplus a\rangle.
$$

### Other Common Circuit Identities

CZ from CNOT (Assignment 7 #1 / Problem Bank #10): $H$ on target conjugates $X$ to $Z$, so

$$\mathrm{CZ}=(I\otimes H)\,\mathrm{CNOT}\,(I\otimes H).$$

Proof on $|a,b\rangle$: $(I\otimes H)\mathrm{CNOT}(I\otimes H)|a,b\rangle$ — first $H$ sends $|b\rangle\to(|0\rangle+(-1)^b|1\rangle)/\sqrt2$, CNOT controls flip bottom, second $H$ recovers; net effect is $(-1)^{ab}|a,b\rangle=\mathrm{CZ}|a,b\rangle$.

SWAP from three CNOTs (Assignment 6 #3 / Problem Bank #9):

$$\mathrm{SWAP}=\mathrm{CNOT}_{12}\,\mathrm{CNOT}_{21}\,\mathrm{CNOT}_{12}.$$

Proof on $|a,b\rangle$: $\mathrm{CNOT}_{12}|a,b\rangle=|a,a\oplus b\rangle$; then $\mathrm{CNOT}_{21}|a,a\oplus b\rangle=|a\oplus(a\oplus b),a\oplus b\rangle=|b,a\oplus b\rangle$; then $\mathrm{CNOT}_{12}|b,a\oplus b\rangle=|b,b\oplus a\oplus b\rangle=|b,a\rangle$. ✓

Flip CNOT direction with Hadamards (Problem Bank #11):

$$\mathrm{CNOT}_{2\to1}=(H\otimes H)\,\mathrm{CNOT}_{1\to2}\,(H\otimes H).$$

Proof: conjugating CNOT by $H\otimes H$ swaps which qubit is the $X$-eigenstate (control) — equivalently $HXH=Z$, $HZH=X$ swaps roles of control and target.

## 5. Problem-Bank Circuit Extras

### Simple Controlled-S Circuit (Problem Bank #13 / Assignment 6 #4)

For the circuit with top qubit $|0\rangle$ then $H$, bottom qubit $|0\rangle$, controlled-$S$ (control top, $S$ as target on bottom), then $H$ on the bottom and a final swap:

- $S|0\rangle=|0\rangle$, so the controlled-$S$ does nothing on input $|0\rangle_{\text{bottom}}$.
- Before measurement, the two measured qubits are $|+\rangle|+\rangle$ (and $\mathrm{SWAP}|++\rangle=|++\rangle$).
- Therefore the Pauli-$Z$ outcome distribution is uniform:

$$\Pr[00]=\Pr[01]=\Pr[10]=\Pr[11]=\frac14.$$

For Assignment 6 #4, the same state $|++\rangle$ also gives Pauli-$X$ outcome $++$ with probability 1, and Bell-measurement outcomes $\Phi^+,\Psi^+$ each with probability $1/2$ (and $\Phi^-,\Psi^-$ with probability 0).

### Parity Circuit In X Basis (Problem Bank #7)

Three-qubit circuit: top qubit $|a\rangle\to H\to\bullet\to H$, middle qubit $|b\rangle\to H\to\bullet\to H$, bottom qubit $|0\rangle$ is the target of two CNOTs (one controlled by top, one controlled by middle). The circuit computes the X-basis parity of the top two qubits onto the bottom qubit:

| $(|a\rangle,|b\rangle)$ | Output (top, middle, bottom) |
| --- | --- |
| $(|+\rangle,|+\rangle)$ | $|+,+,0\rangle$ |
| $(|+\rangle,|-\rangle)$ | $|+,-,1\rangle$ |
| $(|-\rangle,|+\rangle)$ | $|-,+,1\rangle$ |
| $(|-\rangle,|-\rangle)$ | $|-,-,0\rangle$ |

So with the encoding $|+\rangle\mapsto 0$, $|-\rangle\mapsto 1$, the bottom qubit reads the parity $a\oplus b$ in the X basis. Mechanism: each $H$ pair conjugates the CNOT control from the X-eigenbasis to the Z-eigenbasis, so each CNOT effectively flips the bottom only when the corresponding top qubit is $|-\rangle$.

### Molmer-Sorensen Gate

Using basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$:

$$
MS=\frac1{\sqrt2}
\begin{pmatrix}
1&0&0&i\\
0&1&-i&0\\
0&-i&1&0\\
i&0&0&1
\end{pmatrix}.
$$

Matrix-from-actions rule: if a gate is defined by its basis-state outputs, those output vectors are the matrix columns in basis order.

### Universal Gate Sets

- Clifford group $\mathcal C_n$: unitaries $U$ such that $U P U^\dagger\in\pm\mathcal P_n^*$ for every nonidentity Pauli $P$ (modded out by global phase). Equivalently, the group generated by $\{H,S,\mathrm{CNOT}\}$.
- Useful Clifford conjugations: $HXH=Z$, $HZH=X$, $SXS^\dagger=Y$, $SZS^\dagger=Z$.
- $\{ \mathrm{CNOT},H,S\}$ generates Clifford gates, so it is not universal.
- $T=S(\pi/4)=\mathrm{diag}(1,e^{i\pi/4})$ is non-Clifford.
- Adding $T$ gives $\{\mathrm{CNOT},H,S,T\}$, which is universal.
- Since $T^2=S$, $\{\mathrm{CNOT},H,T\}$ is also universal.
- Another valid modification: arbitrary single-qubit gates plus CNOT.
- General lecture rule: Clifford gates plus one single-qubit non-Clifford gate is universal.
- Single-qubit ZYZ decomposition (Lemma 4.1): every single-qubit unitary equals $e^{i\delta} R_z(\alpha) R_y(\theta) R_z(\beta)$ for real $\alpha,\beta,\theta,\delta$.

## 6. State Preparation From $|0\rangle$

Global phases do not matter.

| Target state | Gates to apply to $\lvert0\rangle$ |
| --- | --- |
| $(\lvert0\rangle+\lvert1\rangle)/\sqrt2$ | $H$ |
| $(\lvert0\rangle-\lvert1\rangle)/\sqrt2$ | $ZH$, equivalently $S(\pi)H$ |
| $(\lvert0\rangle-i\lvert1\rangle)/\sqrt2$ | $S^\dagger H$, equivalently $S(-\pi/2)H$ |
| $\cos(\theta/2)\lvert0\rangle+\sin(\theta/2)\lvert1\rangle$ | $R_y(\theta)$ |
| $(\lvert0\rangle+e^{i\theta}\lvert1\rangle)/\sqrt2$ | $S(\theta)H$ |

Useful convention:

$$
R_y(\theta)=
\begin{pmatrix}
\cos(\theta/2)&-\sin(\theta/2)\\
\sin(\theta/2)&\cos(\theta/2)
\end{pmatrix}.
$$

## 7. Pure States, Mixed States, And Density Operators

$\rho$ is a valid density operator iff:

1. $\rho^\dagger=\rho$.
2. $\rho\succeq0$.
3. $\mathrm{Tr}[\rho]=1$.

Pure vs mixed:

| Type | Form | Test | Example |
| --- | --- | --- | --- |
| Pure | $\rho=\lvert\psi\rangle\langle\psi\rvert$ | $\mathrm{rank}(\rho)=1$ or $\mathrm{Tr}[\rho^2]=1$ | $\lvert0\rangle\langle0\rvert=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ |
| Mixed | $\rho=\sum_jp_j\lvert\psi_j\rangle\langle\psi_j\rvert$ | non-pure qubit has $\mathrm{Tr}[\rho^2]<1$ | $I/2=\frac12\lvert0\rangle\langle0\rvert+\frac12\lvert1\rangle\langle1\rvert$ |

Bloch representation:

$$
\rho=\frac12(I+r_xX+r_yY+r_zZ).
$$

For a qubit:

| State type | Bloch-vector condition |
| --- | --- |
| Valid state | $r_x^2+r_y^2+r_z^2\le1$ |
| Pure | $r_x^2+r_y^2+r_z^2=1$ |
| Mixed | $r_x^2+r_y^2+r_z^2<1$ |

## 8. Assignment 9 POVM

The state is:

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,\quad
|\alpha|^2+|\beta|^2=1.
$$

The measurement is:

$$
E_k=\frac25|\psi_k\rangle\langle\psi_k|,\quad
|\psi_k\rangle=\cos\left(\frac{2\pi k}{5}\right)|0\rangle+
\sin\left(\frac{2\pi k}{5}\right)|1\rangle,
\quad k=0,1,2,3,4.
$$

Outcome probability:

$$
p_k=\langle\psi|E_k|\psi\rangle
=\frac25|\langle\psi_k|\psi\rangle|^2.
$$

Explicitly:

$$
p_k=\frac25\left|
\alpha\cos\left(\frac{2\pi k}{5}\right)+
\beta\sin\left(\frac{2\pi k}{5}\right)
\right|^2.
$$

With $c_k=\cos(2\pi k/5)$ and $s_k=\sin(2\pi k/5)$:

$$
p_k=\frac25\left(|\alpha|^2c_k^2+|\beta|^2s_k^2
+2\mathrm{Re}(\bar\alpha\beta)c_ks_k\right).
$$

To show it is a valid POVM:

$$
E_k\succeq0,\quad
\sum_{k=0}^4E_k=I.
$$

Use:

$$
\sum_{k=0}^4c_k^2=\frac52,\quad
\sum_{k=0}^4s_k^2=\frac52,\quad
\sum_{k=0}^4c_ks_k=0.
$$

## 9. Pauli Algebra And Decomposition

Multiplication table:

| Product | Value | Reversed product |
| --- | --- | --- |
| $XY$ | $iZ$ | $YX=-iZ$ |
| $YZ$ | $iX$ | $ZY=-iX$ |
| $ZX$ | $iY$ | $XZ=-iY$ |

Therefore:

$$XY=-YX,\quad XZ=-ZX,\quad YZ=-ZY.$$

Trace facts:

$$
X^2=Y^2=Z^2=I,\quad
\mathrm{Tr}[X]=\mathrm{Tr}[Y]=\mathrm{Tr}[Z]=0.
$$

$$
\mathrm{Tr}[XY]=\mathrm{Tr}[XZ]=\mathrm{Tr}[YZ]=0,\quad
\mathrm{Tr}[X^2]=\mathrm{Tr}[Y^2]=\mathrm{Tr}[Z^2]=2.
$$

Any $M\in L(\mathbb C^2)$ can be written as:

$$
M=\frac12(c_0I+c_1X+c_2Y+c_3Z).
$$

Coefficients:

| Coefficient | Trace formula |
| --- | --- |
| $c_0$ | $\mathrm{Tr}[M]$ |
| $c_1$ | $\mathrm{Tr}[XM]$ |
| $c_2$ | $\mathrm{Tr}[YM]$ |
| $c_3$ | $\mathrm{Tr}[ZM]$ |

For
$$M=\begin{pmatrix}p&q\\r&s\end{pmatrix},$$
the useful traces are:

| Trace | Value |
| --- | --- |
| $\mathrm{Tr}[M]$ | $p+s$ |
| $\mathrm{Tr}[XM]$ | $q+r$ |
| $\mathrm{Tr}[YM]$ | $i(q-r)$ |
| $\mathrm{Tr}[ZM]$ | $p-s$ |

Proof idea: multiply $M=\frac12(c_0I+c_1X+c_2Y+c_3Z)$ by $I,X,Y,Z$ and take the trace. Orthogonality kills every nonmatching Pauli term.

## 10. Pauli Twirling And Noise Channels

Assignment 9 twirling identity:

$$
\frac14\rho+\frac14X\rho X+\frac14Y\rho Y+\frac14Z\rho Z=\frac12I.
$$

Using
$$
\rho=\frac12(I+r_xX+r_yY+r_zZ),
$$
the conjugations are:

| State | Bloch form |
| --- | --- |
| $\rho$ | $\frac12(I+r_xX+r_yY+r_zZ)$ |
| $X\rho X$ | $\frac12(I+r_xX-r_yY-r_zZ)$ |
| $Y\rho Y$ | $\frac12(I-r_xX+r_yY-r_zZ)$ |
| $Z\rho Z$ | $\frac12(I-r_xX-r_yY+r_zZ)$ |

Adding gives:

$$
\rho+X\rho X+Y\rho Y+Z\rho Z=2I.
$$

Divide by $4$ to get $I/2$. Interpretation: applying $I,X,Y,Z$ uniformly at random erases the Bloch vector and makes every single-qubit state maximally mixed.

Noise-channel formulas:

| Channel | Map | Bloch-vector transformation |
| --- | --- | --- |
| Bit flip | $\mathcal E(\rho)=(1-\alpha)\rho+\alpha X\rho X$ | $(r_x,r_y,r_z)\mapsto(r_x,(1-2\alpha)r_y,(1-2\alpha)r_z)$ |
| Phase flip / dephasing | $\mathcal E(\rho)=(1-\alpha)\rho+\alpha Z\rho Z$ | $(r_x,r_y,r_z)\mapsto((1-2\alpha)r_x,(1-2\alpha)r_y,r_z)$ |
| Depolarizing | $\mathcal E(\rho)=(1-\alpha)\rho+\frac\alpha3(X\rho X+Y\rho Y+Z\rho Z)$ | $(r_x,r_y,r_z)\mapsto(1-\frac{4\alpha}{3})(r_x,r_y,r_z)$ |

Dephasing in the standard basis:

$$
\rho=\begin{pmatrix}a&c\\\bar c&1-a\end{pmatrix}
\;\mapsto\;
\begin{pmatrix}a&(1-2\alpha)c\\(1-2\alpha)\bar c&1-a\end{pmatrix}.
$$

Diagonal entries are preserved; off-diagonal coherences are suppressed by $1-2\alpha$. At $\alpha=1/2$ the off-diagonals vanish and superposition is destroyed.

Special case:

$$
\frac14(\rho+X\rho X+Y\rho Y+Z\rho Z)=\frac12I.
$$

Equivalent ("all or nothing") form of the depolarizing channel, derived in lecture using the twirl identity:

$$
\mathcal E_{\mathrm{dep}}(\rho)=\left(1-\frac{4\alpha}{3}\right)\rho+\frac{4\alpha}{3}\frac{I}{2}.
$$

- $\alpha=0$: identity (no noise).
- $\alpha=3/4$: output is the maximally mixed state $I/2$.
- For $\alpha>3/4$, the prefactor $1-\frac{4\alpha}{3}$ is negative and the channel form is no longer a probability mixture (the original Pauli-mixture form is still a valid channel for $\alpha\in[0,1]$).

## 11. Solution Templates And Common Mistakes

Circuit probabilities:

1. Write the state after each major layer.
2. Keep the unnormalized branch state.
3. Compute probability as squared norm.
4. Normalize conditional state by dividing by $\sqrt{\Pr[\text{outcome}]}$.
5. Check probabilities sum to $1$.

Circuit identities:

1. Apply the left side to arbitrary $|a,b\rangle$.
2. Apply the right side to the same $|a,b\rangle$.
3. Show final vectors and phases match.
4. Conclude equality by linearity.

POVM problems:

1. State positivity: $E_k\succeq0$.
2. Show completeness: $\sum_kE_k=I$.
3. Use Born rule: $p_k=\langle\psi|E_k|\psi\rangle=\mathrm{Tr}[E_k\rho]$.

Pauli proofs:

1. Use the multiplication table or direct matrix multiplication.
2. For decomposition, use trace orthogonality.
3. Keep the factor $1/2$ in $M=\frac12(c_0I+c_1X+c_2Y+c_3Z)$.

Common mistakes:

- Forgetting complex conjugates in inner products.
- Squaring amplitudes instead of using modulus squared.
- Dropping the factor $1/4$ in the two-ancilla branch sum.
- Treating global phase as physically meaningful.
- Mixing up CNOT control and target qubits.
- Not normalizing a conditional post-measurement state.
- Claiming a POVM is valid without proving $\sum_kE_k=I$.
- Skipping trace steps in Pauli decomposition proofs.
