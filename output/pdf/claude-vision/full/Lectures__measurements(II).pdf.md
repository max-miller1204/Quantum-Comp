# Lectures__measurements(II).pdf

## Page 1

# ① Recap: Measurements

- To extract classical information from a qubit, we must <u>measure</u> it
- <u>Recall</u>: $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$ → Probability of 0: $|\alpha|^2$
  Probability of 1: $|\beta|^2$

  ⊛ <u>Axiom of quantum mechanics!</u> (aka "Born Rule")

  ⊛ <u>Note</u>: $|\alpha|^2 = |\braket{0|\psi}|^2$, $|\beta|^2 = |\braket{1|\psi}|^2$

  <u>Also</u>: $|\braket{0|\psi}|^2 = \braket{0|\psi}\braket{\psi|0} = \mathrm{Tr}[\ket{0}\bra{0}\ket{\psi}\bra{\psi}]$
  $\quad\quad\quad \equiv P_r[0]$

  $\quad\quad\quad$ → "Measurement operators"

  $|\braket{1|\psi}|^2 = \braket{1|\psi}\braket{\psi|1} = \mathrm{Tr}[\ket{1}\bra{1}\ket{\psi}\bra{\psi}]$
  $\quad\quad\quad \equiv P_r[1]$

  $$P_r[0] + P_r[1] = \mathrm{Tr}\big[\underbrace{(\ket{0}\bra{0} + \ket{1}\bra{1})}_{\mathbb{1}}\rho\big] = \mathrm{Tr}[\rho] = 1$$

- For a density matrix $\rho$: $P_r[0] = \mathrm{Tr}[\ket{0}\bra{0}\rho]$, $P_r[1] = \mathrm{Tr}[\ket{1}\bra{1}\rho]$.

⊛ This is often called a "computational-basis measurement" or a "$\{\ket{0}, \ket{1}\}$-basis measurement".

⊛ Recall that $\{\ket{0}, \ket{1}\}$ is also the eigenvectors of Pauli-Z:

$Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$. → So we also sometimes say "<u>Pauli-Z measurement</u>"

⊛ <u>Circuit symbol</u>: $\ket{\psi} \!-\!\boxed{x}\!=$

- <u>Pauli-X measurement</u>: measure along x-axis; equivalent to measuring in basis $\{\ket{+}, \ket{-}\}$ → $\ket{+}\bra{+} + \ket{-}\bra{-} = \mathbb{1}$

  ⊛ Recall: $\ket{+} = H\ket{0}$, $\ket{-} = H\ket{1}$, $H \equiv$ Hadamard gate
  $\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

  ⊛ $H$ unitary $\Rightarrow \{\ket{+}, \ket{-}\}$ is a basis!

[Bloch sphere on right: z-axis up with $\ket{0}$ at top, $\ket{1}$ at bottom; y-axis with $\ket{-i}$ and $\ket{+i}$; x-axis with $\ket{+}$ and $\ket{-}$]

## Page 2

✸ For a state vector $\ket{\psi}$: $\Pr[+] = |\braket{+|\psi}|^2 = \braket{+|\psi}\braket{\psi|+} = \mathrm{Tr}[\ket{+}\bra{+}\ket{\psi}\bra{\psi}]$.

$\Pr[-] = |\braket{-|\psi}|^2 = \braket{-|\psi}\braket{\psi|-} = \mathrm{Tr}[\ket{-}\bra{-}\ket{\psi}\bra{\psi}]$

✸ <u>For a density operator $\rho$</u>: $\Pr[+] = \mathrm{Tr}[\ket{+}\bra{+}\rho]$, $\Pr[-] = \mathrm{Tr}[\ket{-}\bra{-}\rho]$.

  <span style="color:red">↑ Measurement operators. ↑</span>

✸ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{H} - \boxed{X} \!=\!\!=$

[Bloch sphere: $\ket{0}$ at top (+z), $\ket{1}$ at bottom, $\ket{+}$ on +x (front), $\ket{-}$ on −x, $\ket{+i}$ on +y, $\ket{-i}$ on −y. Axes labeled $z, y, x$.]

- <u>Pauli-Y measurement</u>: measure along $y$-axis; equivalent to measuring in basis $\{\ket{+i}, \ket{-i}\}$

✸ <span style="color:red">Recall: $\ket{+i} = SH\ket{0}$, $\ket{-i} = SH\ket{1}$, $H \equiv$ Hadamard gate</span>

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$S \equiv$ phase gate
$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

✸ <span style="color:red">$SH$ is unitary $\Rightarrow \{\ket{+i}, \ket{-i}\}$ is a basis!</span>

✸ For a state vector $\ket{\psi}$: $\Pr[+i] = |\braket{+i|\psi}|^2 = \braket{+i|\psi}\braket{\psi|+i} = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}]$.

$\ket{+i}\bra{+i} + \ket{-i}\bra{-i} = \mathbb{1}$.

$\Pr[-i] = |\braket{-i|\psi}|^2 = \braket{-i|\psi}\braket{\psi|-i} = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$

✸ <u>For a density operator $\rho$</u>: $\Pr[+i] = \mathrm{Tr}[\ket{+i}\bra{+i}\rho]$, $\Pr[-i] = \mathrm{Tr}[\ket{-i}\bra{-i}\rho]$.

  <span style="color:red">↑ Measurement operators. ↑</span>

— <u>Measuring multiple qubits</u>.

- Consider state vector $\ket{\psi}$ of $n$ qubits $\big(\ket{\psi} \in (\mathbb{C}^2)^{\otimes n}\big)$. → or density matrix $\rho$.

- Computational-basis measurement is a $\{\ket{0}, \ket{1}\}$ measurement on each qubit

- Outcome probabilities: $\Pr[0,0,1] = |\braket{0,0,1|\psi}|^2$ (for three qubits).
  
  with $\braket{0,0,1} = \bra{0}\otimes\bra{0}\otimes\bra{1}$
  
  $\Pr[x_1, x_2, x_3] = |\braket{x_1, x_2, x_3|\psi}|^2$, $x_1, x_2, x_3 \in \{0,1\}$.
  
  $= \mathrm{Tr}[\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3}\ket{\psi}\bra{\psi}]$

$\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3} = \ket{x_1}\bra{x_1} \otimes \ket{x_2}\bra{x_2} \otimes \ket{x_3}\bra{x_3}$

✸ For a density operator $\rho$: $\mathrm{Tr}[\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3}\rho]$.

## Page 3

## Expectation Value of an Observable.

**❋ Axiom of Quantum Mechanics:** Observables are described mathematically by **Hermitian operators**. $H^\dagger = H$.

- **Recall:** Hermitian operators have a *spectral/eigenvalue decomposition*:

$$H\ket{\chi_k} = \lambda_k \ket{\chi_k}$$

$$H = \sum_{k=1}^{d} \lambda_k \ket{\chi_k}\bra{\chi_k}$$

  ↑ eigenvectors.
  eigenvalues (real numbers).

**❋ Examples:** the Pauli operators!

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \ket{+}\bra{+} - \ket{-}\bra{-}$$

$$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \ket{+i}\bra{+i} - \ket{-i}\bra{-i}$$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \ket{0}\bra{0} - \ket{1}\bra{1}.$$

- Eigenvectors are orthonormal basis ⇒ they define a measurement!

$$\sum_{k=1}^{d} \ket{\chi_k}\bra{\chi_k} = \mathbb{1}.$$

For a density operator $\rho$:
$$\Pr[k] = \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big) \to \text{The associated ``observed'' value is } \lambda_k.$$

(Example: $k \equiv$ energy level of a molecule, $\lambda_k \equiv$ the energy value).

$$\sum_{k=1}^{d} \Pr(k) = \sum_{k=1}^{d} \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big) = \mathrm{Tr}\Big(\underbrace{\Big(\sum_{k=1}^{d}\ket{\chi_k}\bra{\chi_k}\Big)}_{=\,\mathbb{1}}\rho\Big) = \mathrm{Tr}(\rho) = 1.$$

- The expected (aka "mean" or "average") value of an observable, given a state $\rho$, is

$$\sum_{k=1}^{d} \Pr(k)\cdot \lambda_k = \sum_{k=1}^{d} \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big)\cdot \lambda_k$$

$$= \mathrm{Tr}\Big(\underbrace{\Big(\sum_{k=1}^{d}\lambda_k\ket{\chi_k}\bra{\chi_k}\Big)}_{H}\rho\Big) = \underline{\underline{\mathrm{Tr}(H\rho)}}$$

$$\left(\begin{array}{l}\text{❋ Recall: for a}\\ \text{random variable } X,\\ \mathbb{E}(X) = \sum_x \Pr(X=x)\cdot x\end{array}\right)$$

## Page 4

② <u>Partial Measurements: Measuring Only Some Qubits</u>

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ enter from the left. Three layers of two-qubit gates (boxes) are applied. After the 3rd layer, the 1st, 3rd, and 5th qubits are measured (shown as red measurement boxes outputting $x$). Dashed vertical lines separate 1st layer, 2nd layer, 3rd layer. Time axis points to the right.]

$(x_1, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

✺ Suppose we only measure the 1st, 3rd, and 5th qubits.

— To get the measurement outcome probabilities, we apply the measurement operators only on the relevant qubits.

✺ <u>Notation</u>: States and operators for multiple qubits and qudits.

- For two qubits, the standard basis is $\{\ket{0}\otimes\ket{0}, \ket{0}\otimes\ket{1}, \ket{1}\otimes\ket{0}, \ket{1}\otimes\ket{1}\}$
  
  $\equiv \ket{0,0}, \equiv \ket{0,1}, \equiv \ket{1,0}, \equiv \ket{1,1}$
  
  [arrows pointing to first factor: "1st qubit"; second factor: "2nd qubit"]

  We often <u>label</u> the qubits by $A, B, C, \dots$

  So we write $\ket{0,0}_{AB} \equiv \ket{0}_A \otimes \ket{0}_B$.
  
  ["qubit A", "qubit B"]
  
  $\rightarrow$ For state vector $\ket{\psi}_{AB} \in \mathbb{C}^2 \otimes \mathbb{C}^2$
  
  [arrows: "qubit A", "qubit B"]

  $\ket{\psi}_{AB} = a\ket{0,0}_{AB} + b\ket{0,1}_{AB} + c\ket{1,0}_{AB} + d\ket{1,1}_{AB}$.

- Similar for three or more qubits: $\ket{\psi}_{ABC} = \sum_{\vec{x} \in \{0,1\}^3} c_{\vec{x}} \ket{\vec{x}}_{ABC}$
  
  $\ket{\vec{x}}_{ABC} \equiv \ket{x_1, x_2, x_3}_{ABC}$

## Page 5

For $n$ qubits: $\ket{\psi}_{A_1 A_2 \cdots A_n} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}}_{A_1 A_2 \cdots A_n}$

$$\hookrightarrow \equiv \ket{x_1, x_2, \ldots, x_n}_{A_1 A_2 \cdots A_n}$$
$$\equiv \ket{x_1}_{A_1} \otimes \ket{x_2}_{A_2} \otimes \cdots \otimes \ket{x_n}_{A_n}$$

- We do the same for linear operators (including density operators)

$M \in L(\mathbb{C}^d) \quad M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}) \to (d_A \cdot d_B) \times (d_A \cdot d_B)$ matrix

System $A$ has dimension $d_A$; $B$ has dimension $d_B$.

$$M_{AB} = \sum_{i,j=0}^{d_A - 1} \sum_{k,\ell=0}^{d_B - 1} M_{i,k;j,\ell} \, \ket{i,k}\bra{j,\ell}_{AB}$$

$$\hookrightarrow \equiv \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B \to \text{These form a basis for } L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}).$$

$$M_{A_1 A_2 \cdots A_n} \in L(\mathbb{C}^{d_{A_1}} \otimes \mathbb{C}^{d_{A_2}} \otimes \cdots \otimes \mathbb{C}^{d_{A_n}}) \to (d_{A_1} \cdot d_{A_2} \cdots d_{A_n}) \times (d_{A_1} \cdot d_{A_2} \cdots d_{A_n}) \text{ matrix.}$$

— Suppose we have a two-qubit density operator $\rho_{AB}$, and we measure the qubit $A$ in the computational basis.

Measurement operators are $\ket{0}\bra{0}$ and $\ket{1}\bra{1}$.

Probabilities are: 
$$\Pr[0] = \mathrm{Tr}\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B)\, \rho_{AB}\right]$$

$$\Pr[1] = \mathrm{Tr}\left[\underbrace{(\ket{1}\bra{1}_A \otimes \mathbb{1}_B)}_{\uparrow}\, \rho_{AB}\right]$$

We measure qubit $A$ only, so we apply the measurement operator only on $A$; we apply identity ("do nothing") on $B$.

## Page 6

If we measure only $B$, then: $\Pr[x] = \text{Tr}\left[(\mathbb{1}_A \otimes \ket{x}\bra{x}_B)\rho_{AB}\right]$, $x \in \{0,1\}$.

If we measure both $A$ & $B$, then: $\Pr[x_1, x_2] = \text{Tr}\left[\underbrace{(\ket{x_1}\bra{x_1}_A \otimes \ket{x_2}\bra{x_2}_B)}_{\ket{x_1, x_2}\bra{x_1, x_2}_{AB}}\rho_{AB}\right]$.

- Suppose we only measure the 1$^{st}$, 3$^{rd}$, and 5$^{th}$ qubits.

[Circuit diagram: 6 qubit lines labeled $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ from top to bottom. Three layers of two-qubit gates separated by dashed vertical lines (1$^{st}$ layer, 2$^{nd}$ layer, 3$^{rd}$ layer). At the end, measurement boxes labeled $x$ on qubits 1, 3, and 5 (drawn in red). Time axis points to the right.]

$(x_1, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

- Let the state before measurement be given by the density operator $\rho_{A_1 A_2 \cdots A_6}$

- The probability distribution is given by:

$$\Pr[x_1, x_2, x_3] = \text{Tr}\left[\left(\ket{x_1}\bra{x_1}_{A_1} \otimes \mathbb{1}_{A_2} \otimes \ket{x_2}\bra{x_2}_{A_3} \otimes \mathbb{1}_{A_4} \otimes \ket{x_3}\bra{x_3}_{A_5} \otimes \mathbb{1}_{A_6}\right) \rho_{A_1 \cdots A_6}\right].$$

$x_1, x_2, x_3 \in \{0,1\}$.

## ③ The Partial Trace

- When we only measure parts of a quantum system, we only need to know the state of that <u>subsystem</u> — we can "ignore" the rest of the system.

- The partial trace describes how (mathematically) to describe ignoring/discarding parts of a system.

## Page 7

- For a linear operator $M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B})$, the (full) trace is:

$$\text{Tr}[M_{AB}] = \sum_{k=0}^{d_A-1} \sum_{\ell=0}^{d_B-1} \braket{k,\ell|_{AB} M_{AB} | k,\ell}_{AB}. \quad \text{\color{red}(sum of the diagonal elements).}$$

<span style="color:red">(Recall that $\{\ket{k,\ell} : k \in \{0,1,\ldots,d_A-1\}, \ell \in \{0,1,\ldots,d_B-1\}\}$ is a basis.)</span>

<span style="color:blue">$\text{Tr}[M] = \sum_{k=0}^{d-1} \braket{k|M|k}$</span>

$$\text{Tr}[M_{AB}] = \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \big(\bra{k}_A \otimes \bra{\ell}_B\big) M_{AB} \big(\ket{k}_A \otimes \ket{\ell}_B\big).$$

- <u>Partial trace over B</u>: $\text{Tr}_B[M_{AB}] = \cancel{\sum_{k=0}^{d_A-1}}\sum_{\ell=0}^{d_B-1} \big(\cancel{\bra{k}_A}^{\;\mathbb{1}_A} \otimes \bra{\ell}_B\big) M_{AB} \big(\cancel{\ket{k}_A}^{\;\mathbb{1}_A} \otimes \ket{\ell}_B\big).$

  $$\downarrow$$
  $$= \sum_{\ell=0}^{d_B-1} \big(\mathbb{1}_A \otimes \bra{\ell}_B\big) M_{AB} \big(\mathbb{1}_A \otimes \ket{\ell}_B\big).$$

  ⊛ <u>Note</u>: the outcome is an operator! Not a scalar, like the full trace.

- <u>Partial trace over A</u>: $\text{Tr}_A[M_{AB}] = \sum_{k=0}^{d_A-1}\cancel{\sum_{\ell=0}^{d_B-1}} \big(\bra{k}_A \otimes \cancel{\bra{\ell}_B}^{\;\mathbb{1}_B}\big) M_{AB} \big(\ket{k}_A \otimes \cancel{\ket{\ell}_B}^{\;\mathbb{1}_B}\big).$

  $$\downarrow$$
  $$= \sum_{k=0}^{d_A-1} \big(\bra{k}_A \otimes \mathbb{1}_B\big) M_{AB} \big(\ket{k}_A \otimes \mathbb{1}_B\big).$$

  ⊛ <u>Note</u>: the outcome is an operator! Not a scalar, like the full trace.

- Some Properties:

(1) $\text{Tr}_A[M_A \otimes N_B] = \sum_{k=0}^{d_A-1} \big(\bra{k}_A \otimes \mathbb{1}_B\big)\big(M_A \otimes N_B\big)\big(\ket{k}_A \otimes \mathbb{1}_B\big).$

<span style="color:blue">$= \big(\bra{k}_A M_A \otimes \mathbb{1}_B \cdot N_B\big) = \bra{k}_A M_A \otimes N_B.$</span>

$$\downarrow$$
$$= \sum_{k=0}^{d_A-1} \braket{k|_A M_A | k}_A \, N_B$$
$$= \text{Tr}[M_A]\, N_B.$$

$$\left(\begin{array}{l} \circledast \text{ Property of tensor product:} \\ (M_1 \otimes M_2)(N_1 \otimes N_2) = M_1 N_1 \otimes M_2 N_2 \end{array}\right)$$

(2) $\text{Tr}_B[M_A \otimes N_B] = \text{Tr}[N_B]\, M_A.$

<span style="color:blue">$\big(\bra{k}_A M_A \otimes N_B\big)\big(\ket{k}_A \otimes \mathbb{1}_B\big) = \braket{k|M_A|k} \cdot N_B.$</span>

## Page 8

$M_{AB} \in L(\mathbb{C}^2 \otimes \mathbb{C}^2) \quad \to \quad M_{AB} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array} \begin{array}{c} \begin{matrix} 00 & 01 & 10 & 11 \end{matrix} \\ \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix} \end{array}$

[The matrix entries are grouped by 2×2 blocks: green circles $a_{11}, a_{22}$; purple $a_{13}, a_{24}$; pink $a_{31}, a_{42}$; orange $a_{33}, a_{44}$.]

$$= \sum_{i,j=0}^{1} \sum_{k,\ell=0}^{1} M_{i,k;j,\ell} \, \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B.$$

$$\mathrm{Tr}_B[M_{AB}] = \sum_{i,j=0}^{1} \sum_{k,\ell=0}^{1} M_{i,k;j,\ell} \, \underbrace{\mathrm{Tr}_B\!\left[\ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B\right]}_{=\,\ket{i}\bra{j}\,\cdot\,\underbrace{\mathrm{Tr}[\ket{k}\bra{\ell}]}_{\delta_{k,\ell}}} = \sum_{i,j=0}^{1} \sum_{k=0}^{1} M_{i,k;j,k} \, \ket{i}\bra{j}_A$$

$$\mathrm{Tr}_B[M_{AB}] = \begin{array}{c} \\ 0 \\ 1 \end{array} \begin{array}{c} \begin{matrix} 0 & \quad 1 \end{matrix} \\ \begin{pmatrix} a_{11}+a_{22} & a_{13}+a_{24} \\ a_{31}+a_{42} & a_{33}+a_{44} \end{pmatrix} \end{array}$$

## Page 9

- Recall: for a computational-basis measurement on qubit $A$ of two-qudit system $AB$ in state $\rho_{AB}$: $\Pr[x] = \text{Tr}\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B) \rho_{AB} \big)$

  $\{\ket{k,\ell}: k \in \{0,1,\ldots,d_A-1\},\ \ell \in \{0,1,\ldots,d_B-1\}\}$ is a basis

  $\quad \xrightarrow{\ \ } \underline{= \text{Tr}\big[ \ket{x}\bra{x}_A \,\text{Tr}_B(\rho_{AB}) \big]}.$

$$\Rightarrow \text{Tr}\big[ (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big] = \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \bra{k,\ell}_{AB}\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big)\ket{k,\ell}_{AB}.$$

(This is a sum over the diagonal elements.)

$$= \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} (\bra{k}_A \otimes \bra{\ell}_B)\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big)(\ket{k}_A \otimes \ket{\ell}_B).$$

$\left( \circledast \text{ Property of tensor product:} \atop (M_1 \otimes M_2)(N_1 \otimes N_2) = M_1 N_1 \otimes M_2 N_2 \right)$

$$= \bra{k}_A (\mathbb{1}_A \otimes \bra{\ell}_B)(\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$\left( \circledast\ (\mathbb{1}_A \otimes M_B)(N_A \otimes \mathbb{1}_B) \atop = N_A \otimes M_B \atop = (N_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes M_B). \right)$

$$= \bra{k}_A \ket{x}\bra{x}_A (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$$= \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \bra{k}_A \ket{x}\bra{x}_A (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$$= \sum_{k=0}^{d_A-1} \bra{k}_A \ket{x}\bra{x}_A \left( \underbrace{\sum_{\ell=0}^{d_B-1} (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)}_{\equiv\, \text{Tr}_B(\rho_{AB})\ \to\ \text{the partial trace!}} \right) \ket{k}_A$$

## Page 10

Compare with the full trace:

$$\mathrm{Tr}(\rho_{AB}) = \sum_{k=0}^{d_A-1} \sum_{\ell=0}^{d_B-1} \left(\bra{k}_A \otimes \bra{\ell}_B\right) \rho_{AB} \left(\ket{k}_A \otimes \ket{\ell}_B\right).$$

$$= \mathrm{Tr}\left[\ket{x}\bra{x}_A \underbrace{\mathrm{Tr}_B(\rho_{AB})}_{=\rho_A}\right]$$

For measurement of $B$ instead: $\Pr(x) = \mathrm{Tr}\left[\left(\mathbb{1}_A \otimes \ket{x}\bra{x}_B\right)\rho_{AB}\right] = \mathrm{Tr}\left[\ket{x}\bra{x}_B \underbrace{\mathrm{Tr}_A(\rho_{AB})}_{=\rho_B}\right].$
