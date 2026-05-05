# Lectures__quantum-gates.pdf

## Page 1

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

## Page 2

- ✻ <u>Origin</u>, $\vec{r} = (0,0,0) \to \rho = \frac{1}{2}(\ket{0}\bra{0} + \ket{1}\bra{1}) \to$ the <u>maximally-mixed state</u>  $\quad |\alpha|^2 + |\beta|^2 = 1$
  
  (A completely random state). $\quad = \frac{\mathbb{1}}{2}$

- ✻ <u>Points on the X-axis</u>: $\vec{r} = (\pm 1, 0, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm X) = \ket{\pm}\bra{\pm}, \quad \ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$

  These are eigenvectors of $X$! $\quad X\ket{\pm} = \pm\ket{\pm}. \to X\ket{+} = \ket{+}$
  (Eigenvalues of $X$ are $\pm 1$.) $\hspace{6cm} X\ket{-} = -\ket{-}$

- ✻ <u>Points on the Y-axis</u>: $\vec{r} = (0, \pm 1, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm Y) = \ket{\pm i}\bra{\pm i}, \quad \ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

  These are eigenvectors of $Y$! $\quad Y\ket{\pm i} = \pm \ket{\pm i}. \quad Y\ket{+i} = \ket{+i}$
  (Eigenvalues of $Y$ are $\pm 1$.) $\hspace{6cm} Y\ket{-i} = -\ket{-i}$

- ✻ <u>Points on the Z-axis</u>: $\vec{r} = (0, 0, \pm 1) \to \rho = \frac{1}{2}(\mathbb{1} \pm Z) \begin{matrix} ^{(+)}\to \ket{0}\bra{0} \\ _{(-)}\to \ket{1}\bra{1} \end{matrix}$

  These are eigenvectors of $Z$! $\quad Z\ket{0} = \ket{0}, \; Z\ket{1} = -\ket{1}.$ (Eigenvalues of $Z$ are $\pm 1$.)

- For higher dimensions, we don't have such a nice representation.

- We can still check if a state is pure using the <u>purity</u>:

  For density matrix $\rho$ in dimension $d$, $\quad \underline{\text{Tr}[\rho^2] \equiv \text{purity}}$

  The state $\rho$ is pure if and only if $\text{Tr}[\rho^2] = 1$.

- ✻ Every pure state is represented by a density matrix of the form $\rho = \ket{\psi}\bra{\psi}$, where $\ket{\psi} \in \mathbb{C}^d$ is a state vector ($\|\ket{\psi}\| = 1$).

  If a state is not pure, then we call it a <mark>mixed state.</mark>

- ✻ <u>Important fact</u>: Every mixed state can be written as a <u>convex combination</u> of pure states:
  
  $$\rho = \sum_{k=1}^{M} p_k \ket{\psi_k}\bra{\psi_k}, \quad p_k \in [0,1], \quad \sum_{k=1}^{M} p_k = 1.$$
  
  $\hspace{3cm}\uparrow$ probabilities.

## Page 3

$$\underline{\text{Check}}: \text{Tr}[\rho] = \sum_{k=1}^{m} p_k \underbrace{\text{Tr}\left[\ket{\psi_k}\bra{\psi_k}\right]}_{=1} = \sum_{k=1}^{m} p_k = 1 \quad \checkmark$$

$$\begin{pmatrix} (M_1+M_2)^\dagger \\ = M_1^\dagger + M_2^\dagger \end{pmatrix} \qquad \underline{\text{Check}}: \rho^\dagger = \sum_{k=1}^{m} p_k \underbrace{\left(\ket{\psi_k}\bra{\psi_k}\right)^\dagger}_{= \ket{\psi_k}\bra{\psi_k}} = \sum_{k=1}^{m} p_k \ket{\psi_k}\bra{\psi_k} = \rho \quad \checkmark$$

$$\left(\ket{v_1}\bra{v_2}\right)^\dagger = \ket{v_2}\bra{v_1}$$

$\underline{\text{Check}}: \rho \succeq 0 \longrightarrow$ Yes, b/c we sum over PSD elements.

$$M_1, M_2 \succeq 0$$

$$\bra{v}(M_1+M_2)\ket{v} = \underbrace{\bra{v}M_1\ket{v}}_{\geq 0} + \underbrace{\bra{v}M_2\ket{v}}_{\geq 0} \geq 0$$

② <u>Quantum Circuits and gates.</u>

- <u>Recap</u>: classical computation: manipulation of bits via <u>logic gates</u> (AND, OR, NOT, XOR)

  For input $x \in \{0,1\}^n$, calculate $f(x)$ for some $f$.
  (How to realize $f$ with a circuit? How many gates / depth is necessary and/or sufficient?)

  ✱ We rarely think about computation in these terms anymore!

  ✱ We program in some <u>high-level language</u> (C++, python, julia) and then the code gets <u>compiled</u> into the machine-level language.

  ✱ Quantum computing is still thought about at the gate level.

  (Although "quantum programming languages" are being developed — qiskit is a simple example.)

## Page 4

- **Classical logic circuits:**

  [Circuit diagram: input $x_1$ goes into a NOT gate; inputs $x_2, x_3$ go into an OR gate; the NOT output and OR output feed into an AND gate; the AND output and another signal feed into a final OR gate.]

  - For every logic gate, we have a truth table (how 0 + 1 are transformed by the gate.)

  [Gate symbols shown: OR, AND, XOR, NOR, NAND, NOT]

  | A | NOT A |
  |---|-------|
  | 0 | 1     |
  | 1 | 0     |

  | A | B | A AND B |
  |---|---|---------|
  | 0 | 0 | 0       |
  | 0 | 1 | 0       |
  | 1 | 0 | 0       |
  | 1 | 1 | 1       |

  | A | B | A OR B |
  |---|---|--------|
  | 0 | 0 | 0      |
  | 0 | 1 | 1      |
  | 1 | 0 | 1      |
  | 1 | 1 | 1      |

  | A | B | A XOR B |
  |---|---|---------|
  | 0 | 0 | 0       |
  | 0 | 1 | 1       |
  | 1 | 0 | 1       |
  | 1 | 1 | 0       |

  | A (control bit) | B (target bit) | A CNOT B |
  |-----------------|----------------|----------|
  | 0               | 0              | 0  0     |
  | 0               | 1              | 0  1     |
  | 1               | 0              | 1  1     |
  | 1               | 1              | 1  0     |

  ⊛ Reversible version of XOR gate.

  $$A, B \mapsto A,\; A \oplus B. \quad \oplus$$

  - For a given circuit, we use these truth tables, combining them to get the truth table of the whole circuit.

## Page 5

- **Quantum Circuits and Gates**: very similar! But the gates act on the complex vector space $(\mathbb{C}^2)^{\otimes n}$ of $n$ qubits ⟶ they are represented by <mark>unitary matrices</mark>. ⟶ matrix $U \in L(\mathbb{C}^d)$ satisfying $U^\dagger U = U U^\dagger = \mathbb{1}$.

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left, passing through 3 layers of gate boxes (1st layer, 2nd layer, 3rd layer separated by dashed vertical lines), with measurement/read-out on the right giving outputs $\sim x_1', x_2', x_3', x_4', x_5', x_6'$. Time flows left to right. Inputs satisfy $(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$.]

- ✸ Each box represents a gate / unitary matrix.
- ✸ Multiply the gates to get a unitary matrix for the full circuit.

✸ Why unitary matrix? Comes from quantum physics (Schrödinger equation).

✸ To understand what the circuit does, we just have to know how it acts on basis vectors!

<u>Recall</u>: any state vector of $n$ qubits can be represented as

$$\ket{\psi} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}}, \quad c_{\vec{x}} \in \mathbb{C}, \quad \sum_{\vec{x} \in \{0,1\}^n} |c_{\vec{x}}|^2 = 1.$$

$$\left( \begin{array}{l} \vec{x} \equiv (x_1, x_2, \ldots, x_n), \; x_i \in \{0,1\} \\ \ket{\vec{x}} \equiv \ket{x_1, x_2, \ldots, x_n} \\ \quad\quad = \ket{x_1} \otimes \ket{x_2} \otimes \cdots \otimes \ket{x_n} \end{array} \right)$$

↳ input state of the quantum circuit.

$$\Rightarrow U \ket{\psi} = U \left( \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}} \right) = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \, \underline{U \ket{\vec{x}}}.$$

$\left( \text{✸ Linearity of matrices: } M(\alpha \ket{v_1} + \beta \ket{v_2}) = \alpha M \ket{v_1} + \beta M \ket{v_2} \right).$

## Page 6

- From calculating $U\ket{\vec{x}}$ for all $\vec{x}$, we get something like the "truth table" of the quantum circuit.

✱ Elementary quantum gates (building blocks of larger circuits).

- **Pauli gates:** $-\boxed{X}-\ \rightarrow\ X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\ \left(X\ket{0}=\ket{1},\ X\ket{1}=\ket{0}\right)$

  $X^\dagger = X$,
  $X^\dagger X = X^2 = \mathbb{1}$

  $\quad\quad\quad\quad\quad\quad\ \  -\boxed{Y}-\ \rightarrow\ Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\ \left(Y\ket{0}=i\ket{1},\ Y\ket{1}=-i\ket{0}\right)$

  $\quad\quad\quad\quad\quad\quad\ \  -\boxed{Z}-\ \rightarrow\ Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\ \left(Z\ket{0}=\ket{0},\ Z\ket{1}=-\ket{1}\right)$

- **Hadamard gate:** $-\boxed{H}-\ \rightarrow\ H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

  $H^\dagger = H \rightarrow H^2 = \mathbb{1}$.

  $H\ket{0} = \ket{+} = \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})$
  $H\ket{1} = \ket{-} = \frac{1}{\sqrt{2}}(\ket{0}-\ket{1})$.

- **Phase gate:** $-\boxed{S}-\ \rightarrow\ S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \rightarrow S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$

- **T-gate:** $-\boxed{T}-\ \rightarrow\ T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$

  $\underbrace{\phantom{e^{i\pi/4}}}_{\downarrow}$

  $e^{i\pi/4} = \cos\left(\frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{4}\right)$
  $\quad\quad = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}i$

## Page 7

- **CNOT / CX gate:** "controlled-X"

[Circuit: two horizontal wires, top wire has a control dot (labeled "control"), bottom wire has an X box (labeled "target")]   or   [equivalent circuit with control dot on top wire and ⊕ symbol on bottom wire]

$$\text{CNOT} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{pmatrix} \overset{00}{1} & \overset{01}{0} & \overset{10}{0} & \overset{11}{0} \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}X\ket{0} = \ket{1}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}X\ket{1} = \ket{1}\ket{0}$$

B/c of linearity, this determines the action on **any** state!

$$\ket{\psi} = a\ket{0,0} + b\ket{0,1} + c\ket{1,0} + d\ket{1,1} \mapsto a\ket{0,0} + b\ket{0,1} + c\ket{1,1} + d\ket{1,0}$$

---

- **Controlled-Z / CZ gate:**

[Circuit: top wire control dot, bottom wire Z box]   OR   [Circuit: control dot on both wires connected by vertical line — symmetric notation]

$$CZ = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{pmatrix} \overset{00}{1} & \overset{01}{0} & \overset{10}{0} & \overset{11}{0} \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$$

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}Z\ket{0} = \ket{1}\ket{0}$$
$$\ket{1}\ket{1} \mapsto \ket{1}Z\ket{1} = -\ket{1}\ket{1}$$

---

- **Controlled Unitary**

[Circuit: top wire control dot, bottom wire U box]

$$cU = \begin{pmatrix} \mathbb{1} & 0 \\ 0 & U \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ \hline 0 & 0 & & \\ 0 & 0 & \multicolumn{2}{c}{U} \end{pmatrix}$$

$$\underbrace{\phantom{xxx}}_{\text{2×2 unitary}}$$

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}U\ket{0}$$
$$\ket{1}\ket{1} \mapsto \ket{1}U\ket{1}$$

## Page 8

- **Rotation Gates:**

$$R_X(\theta) = e^{-i\frac{\theta}{2}X} \quad \rightarrow \text{rotation around X-axis by angle } \theta.$$

$$R_Y(\theta) = e^{-i\frac{\theta}{2}Y} \quad \rightarrow \text{rotation around Y-axis by angle } \theta.$$

$$R_Z(\theta) = e^{-i\frac{\theta}{2}Z} \quad \rightarrow \text{rotation around Z-axis by angle } \theta.$$

[Bloch sphere diagram with axes labeled $x$, $y$, $z$; points marked $\ket{+}$ on +x axis and $\ket{+i}$ on +y axis]

$$e^M := \sum_{k=0}^{\infty} \frac{1}{k!} M^k \quad (\text{matrix exponential})$$

$$\Rightarrow \quad e^{-i\frac{\theta}{2}X} = \sum_{k=0}^{\infty} \frac{1}{k!}\left(-i\frac{\theta}{2}X\right)^k$$

$$\left(\begin{array}{l} X^2 = \mathbb{1} \\ \Rightarrow X^k = \mathbb{1},\ k \text{ even} \\ \quad\ X^k = X,\ k \text{ odd} \end{array}\right)$$

$X^3 = \underbrace{X^2}_{\mathbb{1}} \cdot X = X \qquad X^4 = \underbrace{X^2 \cdot X^2}_{} = \mathbb{1}$

$$= \sum_{k=0}^{\infty} \frac{1}{(2k)!}\left(-i\frac{\theta}{2}X\right)^{2k} + \sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\left(-i\frac{\theta}{2}X\right)^{2k+1}$$

$$\underbrace{\phantom{xxxxxxxxxxxx}}_{0,2,4,6,\ldots} \qquad \underbrace{\phantom{xxxxxxxxxxxx}}_{1,3,5,7,\ldots}$$

$$= \sum_{k=0}^{\infty} \frac{1}{(2k)!}\left(\frac{\theta}{2}\right)^{2k}(-i)^{2k}\,\mathbb{1} + \sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\left(\frac{\theta}{2}\right)^{2k+1}(-i)^{2k+1} X$$

$$i \cdot i = i^2 = -1$$

$(-i)^1 = -i \quad (k=0)$

$(-i)^3 = \underbrace{-i \cdot -i}_{-1} \cdot -i = i \quad (k=1)$

$(-i)^5 = -i \qquad\qquad (k=2)$

$\vdots$

$(-i)^{2k+1} = -i(-1)^k$

$(-i)^2 = -i \cdot -i = -1 \quad (k=1)$

$(-i)^4 = ((-i)^2)^2 = 1 \quad (k=2)$

$(-i)^6 = -1 \qquad\qquad (k=3)$

$\vdots$

$(-i)^{2k} = (-1)^k$

## Page 9

$$= \underbrace{\sum_{k=0}^{\infty} \frac{1}{(2k)!} \left(\frac{\theta}{2}\right)^{2k} (-1)^k}_{\cos(\frac{\theta}{2})} \mathbb{1} \;-\; i \underbrace{\sum_{k=0}^{\infty} \frac{1}{(2k+1)!} \left(\frac{\theta}{2}\right)^{2k+1} (-1)^k}_{\sin(\frac{\theta}{2})} X$$

$$= \cos\left(\tfrac{\theta}{2}\right) \mathbb{1} - i \sin\left(\tfrac{\theta}{2}\right) X$$

(✱) Similar argument to show $R_y(\theta) = e^{-i\frac{\theta}{2} Y} = \cos(\tfrac{\theta}{2}) \mathbb{1} - i \sin(\tfrac{\theta}{2}) Y$

$$R_z(\theta) = e^{-i\frac{\theta}{2} Z} = \cos(\tfrac{\theta}{2}) \mathbb{1} - i \sin(\tfrac{\theta}{2}) Z$$

- **Important properties of Unitaries.**

  - <u>Unitaries preserve norm</u>: For $U \in L(\mathbb{C}^d)$ unitary, $\ket{v} \in \mathbb{C}^d$ arbitrary,

  $$\ket{\tilde{v}} = U\ket{v} \;\rightarrow\; \| \ket{\tilde{v}} \|^2 = \braket{\tilde{v}|\tilde{v}} = \braket{v | \underbrace{U^\dagger U}_{=\mathbb{1}} | v} = \braket{v|v}$$

  $$\left( (M_1 M_2)^\dagger = M_2^\dagger M_1^\dagger \right)$$

  $$\bra{\tilde{v}} = (\ket{\tilde{v}})^\dagger = (U\ket{v})^\dagger = \bra{v} U^\dagger$$

  - <u>Unitaries preserve states</u>: let $\rho$ be a density operator representing a mixed quantum state. Then the transformed state is given by

  $$\tilde{\rho} = U \rho U^\dagger \;\rightarrow\; \text{This is still a density matrix!}$$

  Check: (1) $\tilde{\rho}^\dagger = (U \rho U^\dagger)^\dagger = (U^\dagger)^\dagger \rho^\dagger U^\dagger = U \rho U^\dagger$ ✓
  
  $\;\;\;\;\underbrace{\;\;\;}_{\tilde{\rho}} \quad \underbrace{\;\;\;}_{=U} \underbrace{\;\;\;}_{=\rho} \underbrace{\;\;\;}_{\tilde{\rho}}$

  $$\left( (M_1 M_2 M_3)^\dagger = M_3^\dagger M_2^\dagger M_1^\dagger \right)$$

  (2) $\text{Tr}[\tilde{\rho}] = \text{Tr}[U \rho U^\dagger] = \text{Tr}[U^\dagger U \rho] = \text{Tr}[\rho] = 1$ ✓

  $$\left( \text{(✱) Cyclicity of trace: } \text{Tr}[M_1 M_2 M_3] = \text{Tr}[M_2 M_3 M_1] = \text{Tr}[M_3 M_2 M_1] \right)$$

## Page 10

(3) For arbitrary $\ket{v} \in \mathbb{C}^d$, $\bra{v} \tilde{\rho} \ket{v} = \underbrace{\bra{v} U}_{\bra{\tilde{v}}} \rho \underbrace{U^\dagger \ket{v}}_{\ket{\tilde{v}}}$

$$= \bra{\tilde{v}} \rho \ket{\tilde{v}} \geq 0 \quad \text{b/c } \rho \geq 0 \text{ by assumption}$$

$\Rightarrow$ So $\tilde{\rho} \geq 0$ ✓

---

— **Product of unitaries is a unitary:** if $U_1, U_2$ are unitaries, then $U = U_1 U_2$ is also a unitary.

Check: $U^\dagger U = (U_1 U_2)^\dagger U_1 U_2 = U_2^\dagger \underbrace{U_1^\dagger U_1}_{= \mathbb{1}} U_2 = U_2^\dagger U_2 = \mathbb{1}$ ✓

$U U^\dagger = (U_1 U_2)(U_1 U_2)^\dagger = U_1 \underbrace{U_2 U_2^\dagger}_{= \mathbb{1}} U_1^\dagger = U_1 U_1^\dagger = \mathbb{1}$ ✓
