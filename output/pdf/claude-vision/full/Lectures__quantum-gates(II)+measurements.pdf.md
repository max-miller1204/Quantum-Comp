# Lectures__quantum-gates(II)+measurements.pdf

## Page 1

① <u>Recap: Quantum Gates</u>

- Quantum gates describe how the states of qubits evolve — Similar to classical logic gates like AND, OR, NOT.

- Composing gates leads to <u>circuits</u>, which are used to describe quantum computations.

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left, passing through 3 layers of gates (1st layer, 2nd layer, 3rd layer) separated by dashed vertical lines, ending in measurement read-outs $D \rightsquigarrow x_1', x_2', x_3', x_4', x_5', x_6'$ on the right. Below: $(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$. Arrow labeled "time" pointing right. The measurements are labeled "Measurement/read-out".]

- Mathematically, quantum gates are described by <u>unitary matrices/operators</u> $U^\dagger U = U U^\dagger = \mathbb{1}$. They are <u>norm and trace preserving</u>. They describe <u>basis changes</u>.

  $\ket{\psi} \to U\ket{\psi} \to \|U\ket{\psi}\| = \|\ket{\psi}\|$  $\quad \{U\ket{k}\}_{k=0}^{d-1}$

  $\rho \to U\rho U^\dagger \to \mathrm{Tr}(U\rho U^\dagger) = \mathrm{Tr}(\rho)$.

- <u>Examples</u>:

  - <u>Pauli gates</u>:
  
    $-\boxed{X}- \quad \to \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \left( X\ket{0} = \ket{1},\ X\ket{1} = \ket{0} \right)$

    $-\boxed{Y}- \quad \to \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \left( Y\ket{0} = i\ket{1},\ Y\ket{1} = -i\ket{0} \right)$

    $-\boxed{Z}- \quad \to \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \quad \left( Z\ket{0} = \ket{0},\ Z\ket{1} = -\ket{1} \right)$

## Page 2

- **Hadamard gate:** $-\boxed{H}-$  $\rightarrow H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

$$H\ket{0} = \ket{+} = \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})$$
$$H\ket{1} = \ket{-} = \frac{1}{\sqrt{2}}(\ket{0}-\ket{1})$$

- **Phase gate:** $-\boxed{S}-$ $\rightarrow S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$

- **T-gate:** $-\boxed{T}-$ $\rightarrow T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$

- **CNOT / CX gate:**  *"controlled-X"*

[Circuit diagram: control wire with dot connected vertically to target wire with X box; alternatively shown with $\oplus$ symbol on target]
  - top wire = control
  - bottom wire (with X) = target

$$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}X\ket{0} = \ket{1}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}X\ket{1} = \ket{1}\ket{0}$$

- **Rotation Gates:**

$$R_X(\theta) = e^{-i\frac{\theta}{2}X} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)X \quad \rightarrow \text{rotation around X-axis by angle } \theta.$$

$$R_Y(\theta) = e^{-i\frac{\theta}{2}Y} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Y \quad \rightarrow \text{rotation around Y-axis by angle } \theta.$$

$$R_Z(\theta) = e^{-i\frac{\theta}{2}Z} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Z \quad \rightarrow \text{rotation around Z-axis by angle } \theta.$$

## Page 3

② <u>Translating b/w circuit diagrams and math.</u>

[Circuit: $\ket{\psi}$ — [U] —]   $\leftrightarrow$   $U\ket{\psi}$

[Circuit: $\ket{\psi}$ — [$U_1$] — [$U_2$] —]   $\leftrightarrow$   $U_2 U_1 \ket{\psi}$

[Arrows indicating $U_1$ then $U_2$ applied in order]

<span style="color:red">↑ state vector (representing pure state).</span>

[Circuit: $\rho$ — [U] —]   $\leftrightarrow$   $U \rho U^\dagger$    $\quad$  $\rho = \ket{\psi}\bra{\psi} \;\to\; U\ket{\psi}\bra{\psi}U^\dagger$

<span style="color:red">↑ density operator (representing mixed state).</span>

[Circuit: $\rho$ — [$U_1$] — [$U_2$] —]   $\leftrightarrow$   $U_2 U_1 \rho U_1^\dagger U_2^\dagger$

[Dashed arrow at intermediate point: $U_1 \rho U_1^\dagger$]

[Two-qubit circuit:
 line 1: — [$U_1$] —
 line 2: — [$U_2$] — ]
$\leftrightarrow$   $U_1 \otimes U_2$

<span style="color:red">↑ tensor product of matrices.</span>

<span style="color:red">$U_1$ acts on qubit 1<br>
$U_2$ acts on qubit 2.</span>

## Page 4

<u>Recall</u>: $\ket{V_1} = \begin{pmatrix} a_1 \\ b_1 \end{pmatrix}$, $\ket{V_2} = \begin{pmatrix} a_2 \\ b_2 \end{pmatrix}$ $\Rightarrow$ $\ket{V_1} \otimes \ket{V_2} = \begin{pmatrix} a_1 a_2 \\ a_1 b_2 \\ b_1 a_2 \\ b_1 b_2 \end{pmatrix} = \begin{pmatrix} a_1 \begin{pmatrix} a_2 \\ b_2 \end{pmatrix} \\ b_1 \begin{pmatrix} a_2 \\ b_2 \end{pmatrix} \end{pmatrix}$

$M_1 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix}$, $M_2 = \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix}$ $\Rightarrow$ $M_1 \otimes M_2 = \begin{pmatrix} a_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} & b_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} \\ c_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} & d_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} \end{pmatrix}$

$= \begin{pmatrix} a_1 a_2 & a_1 b_2 & b_1 a_2 & b_1 b_2 \\ a_1 c_2 & a_1 d_2 & b_1 c_2 & b_1 d_2 \\ c_1 a_2 & c_1 b_2 & d_1 a_2 & d_1 b_2 \\ c_1 c_2 & c_1 d_2 & d_1 c_2 & d_1 d_2 \end{pmatrix}$

$\text{Tr}[M \otimes N] = \text{Tr}[N]\,\text{Tr}[M].$

$\langle M_1 \otimes M_2,\, N_1 \otimes N_2 \rangle = \langle M_1, N_1 \rangle \langle M_2, N_2 \rangle$

$\langle M, N \rangle = \text{Tr}(M^\dagger N).$

[Circuit diagram: three parallel wires labeled 1, 2, 3, each passing through a single-qubit gate $U_1$, $U_2$, $U_3$ respectively]  $\longleftrightarrow$  $U_1 \otimes U_2 \otimes U_3.$

[Circuit diagram: three input states $\ket{\psi_1}$, $\ket{\psi_2}$, $\ket{\psi_3}$ each entering gates $U_1$, $U_2$, $U_3$ respectively]  $\longleftrightarrow$  $(U_1 \otimes U_2 \otimes U_3)(\ket{\psi_1} \otimes \ket{\psi_2} \otimes \ket{\psi_3})$

$\qquad\qquad = U_1\ket{\psi_1} \otimes U_2\ket{\psi_2} \otimes U_3\ket{\psi_3}.$

## Page 5

- **Tracking the State of qubits through a circuit**

$$\ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$$

$$\ket{+}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{0}$$

[Circuit: top qubit $\ket{0}$ through $H$, then control of CNOT; bottom qubit $\ket{0}$ is target. Red arrows mark stages ① and ②.]

$$\ket{0}\ket{0} \xmapsto{\;①\;} H\ket{0}\ket{0} = \ket{+}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{0})$$

$$\xmapsto{\;②\;} \tfrac{1}{\sqrt{2}}\big(\underbrace{\text{CNOT}\ket{0}\ket{0}}_{\ket{0}\ket{0}} + \underbrace{\text{CNOT}\ket{1}\ket{0}}_{\ket{1}\ket{1}}\big)$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{1})$$

$$\ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0}-\ket{1})$$

[Circuit: top qubit $\ket{1}$ through $H$, then control of CNOT; bottom qubit $\ket{0}$ target. Stages ① and ②.]

$$\ket{1}\ket{0} \xmapsto{\;①\;} H\ket{1}\ket{0} = \ket{-}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{0})$$

$$\xmapsto{\;②\;} \tfrac{1}{\sqrt{2}}\big(\text{CNOT}\ket{0}\ket{0} - \text{CNOT}\ket{1}\ket{0}\big)$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{1})$$

---

[Three-qubit circuit: qubit 1 $\ket{0}$ — $H$ — • — — — $H$; qubit 2 $\ket{0}$ — $H$ — — • — $H$; qubit 3 $\ket{0}$ — — ⊕ — ⊕ — . Red arrows mark stages ①, ②, ③, ④.]

$$\ket{0}\ket{0}\ket{0} \xmapsto{\;①\;} \ket{+}\ket{+}\ket{0}$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\,\tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{0}$$

$$= \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{0} + \ket{1}\ket{0}\ket{0} + \ket{1}\ket{1}\ket{0}\big)$$

$$\xmapsto{\;②\;} \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{0} + \ket{1}\ket{0}\ket{1} + \ket{1}\ket{1}\ket{1}\big)$$

$$\xmapsto{\;③\;} \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{1} + \ket{1}\ket{0}\ket{1} + \ket{1}\ket{1}\ket{0}\big)$$

$$\xmapsto{\;④\;} \tfrac{1}{2}\big(\ket{+}\ket{+}\ket{0} + \ket{+}\ket{-}\ket{1} + \ket{-}\ket{+}\ket{1} + \ket{-}\ket{-}\ket{0}\big)$$

$$= \tfrac{1}{2}\Big(\underbrace{(\ket{+}\ket{+}+\ket{-}\ket{-})}_{(a)}\ket{0} + \underbrace{(\ket{+}\ket{-}+\ket{-}\ket{+})}_{(b)}\ket{1}\Big)$$

$$= \tfrac{1}{\sqrt{2}}\Big(\tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{1})\ket{0} + \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{1})\ket{1}\Big)$$

(a) $\tfrac{1}{2}\big(\ket{0}\ket{0}+\ket{0}\ket{1}+\ket{1}\ket{0}+\ket{1}\ket{1}$
$\quad\quad +\ket{0}\ket{0}-\ket{0}\ket{1}-\ket{1}\ket{0}+\ket{1}\ket{1}\big)$
$= \ket{0}\ket{0} + \ket{1}\ket{1}$

(b) $\tfrac{1}{2}\big(\ket{0}\ket{0}-\ket{0}\ket{1}+\ket{1}\ket{0}-\ket{1}\ket{1}$
$\quad\quad +\ket{0}\ket{0}+\ket{0}\ket{1}-\ket{1}\ket{0}-\ket{1}\ket{1}\big)$
$= \ket{0}\ket{0} - \ket{1}\ket{1}$

## Page 6

## ③ Measurements

- To extract classical information from a qubit, we must <u>measure</u> it

- <u>Recall</u>: $\ket{\psi} = \alpha\ket{0} + \beta\ket{1} \rightarrow$ Probability of 0: $|\alpha|^2$  ⊛ <span style="color:red">Axiom of quantum mechanics! (aka "Born Rule")</span>
  
  $\alpha = \braket{0|\psi}, \;\beta = \braket{1|\psi}$  Probability of 1: $|\beta|^2$

  ⊛ <u>Note</u>: $|\alpha|^2 = |\braket{0|\psi}|^2,\; |\beta|^2 = |\braket{1|\psi}|^2$

  <u>Also</u>: $\underbrace{|\braket{0|\psi}|^2}_{\equiv \,\Pr(0)} = \braket{0|\psi}\braket{\psi|0} = \mathrm{Tr}\big[\ket{0}\bra{0}\,\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad\qquad\qquad\qquad\quad \braket{v_1|M|v_2} = \mathrm{Tr}\big[M\ket{v_2}\bra{v_1}\big]$

  $\underbrace{|\braket{1|\psi}|^2}_{\equiv \,\Pr(1)} = \braket{1|\psi}\braket{\psi|1} = \mathrm{Tr}\big[\ket{1}\bra{1}\,\ket{\psi}\bra{\psi}\big]$

  <u>Check</u>: $\Pr(0) + \Pr(1) = \mathrm{Tr}\big[\ket{0}\bra{0}\ket{\psi}\bra{\psi}\big] + \mathrm{Tr}\big[\ket{1}\bra{1}\ket{\psi}\bra{\psi}\big]$

  $\mathrm{Tr}[M_1 + M_2] = \mathrm{Tr}[M_1] + \mathrm{Tr}[M_2]$
  
  $\mathrm{Tr}\big[\ket{0}\bra{0}\ket{\psi}\bra{\psi} + \ket{1}\bra{1}\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad = \mathrm{Tr}\Big[\big(\underbrace{\ket{0}\bra{0} + \ket{1}\bra{1}}_{=\,\mathbb{1}}\big)\ket{\psi}\bra{\psi}\Big]$
  
  $\qquad\qquad = \mathrm{Tr}\big[\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad = \braket{\psi|\psi}$
  
  $\qquad\qquad = 1\;\checkmark$

  ⊛ This is often called a "<u>computational-basis measurement</u>"
  or a "$\{\ket{0},\ket{1}\}$-<u>basis measurement</u>".

  ⊛ Recall that $\{\ket{0},\ket{1}\}$ is also the eigenvectors of Pauli-Z:
  
  $Z\ket{0} = \ket{0},\; Z\ket{1} = -\ket{1}. \rightarrow$ So we also sometimes say "<u>Pauli-Z measurement</u>"

  ⊛ <u>Circuit symbol</u>:  $\ket{\psi}\!-\!\boxed{Z}\!=$

## Page 7

⊛ <u>Observe</u>: If $\ket{\psi} = \ket{0}$, then $\Pr(0) = 1$, $\Pr(1) = 0$.
If $\ket{\psi} = \ket{1}$, then $\Pr(0) = 0$, $\Pr(1) = 1$.

— We can measure with respect to other Pauli operators too!

[Bloch sphere diagram with $\ket{0}$ at top (+z), $\ket{1}$ at bottom, $\ket{+}$ on +x axis, $\ket{-}$ on −x, $\ket{+i}$ on +y, $\ket{-i}$ on −y]

- <u>Pauli-X measurement</u>: measure along x-axis; equivalent to measuring in basis $\{\ket{+}, \ket{-}\}$

⊛ Recall: $\ket{+} = H\ket{0}$, $\ket{-} = H\ket{1}$, $H \equiv$ Hadamard gate
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

⊛ $H$ unitary $\Rightarrow \{\ket{+}, \ket{-}\}$ is a basis!

⊛ For a state vector $\ket{\psi}$:
$$\Pr(+) = |\braket{+|\psi}|^2 = \braket{+|\psi}\braket{\psi|+} = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big]$$
$$\Pr(-) = |\braket{-|\psi}|^2 = \braket{-|\psi}\braket{\psi|-} = \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big]$$

$\ket{+} = H\ket{0}$
$\ket{-} = H\ket{1}$

<u>Check</u>: $\Pr(+) + \Pr(-) = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big] + \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big]$

$$= \mathrm{Tr}\Big[\underbrace{\big(\ket{+}\bra{+} + \ket{-}\bra{-}\big)}_{\downarrow}\ket{\psi}\bra{\psi}\Big] = \mathrm{Tr}\big[\ket{\psi}\bra{\psi}\big] = 1 \;\checkmark$$

$$= H\ket{0}\bra{0}H^\dagger + H\ket{1}\bra{1}H^\dagger = H\ket{0}\bra{0}H + H\ket{1}\bra{1}H$$
$$= H\underbrace{\big(\ket{0}\bra{0} + \ket{1}\bra{1}\big)}_{=\,\mathbb{1}}H$$
$$= HH = \mathbb{1}$$

⊛ <u>Observe</u>: $\Pr(+) = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[H\ket{0}\bra{0}H\,\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[\ket{0}\bra{0}\,\underline{H\ket{\psi}\bra{\psi}H}\big]$

$\quad\;\; \Pr(-) = \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[H\ket{1}\bra{1}H\,\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[\ket{1}\bra{1}\,\underline{H\ket{\psi}\bra{\psi}H}\big]$

[with $\ket{\psi'}$ labeled above $H\ket{\psi}\bra{\psi}H$]

$\Rightarrow$ Apply $H$ gate to $\ket{\psi}$, then measure in $\{\ket{0}, \ket{1}\}$ basis!

$X\ket{+} = \ket{+},\; X\ket{-} = -\ket{-}$

## Page 8

⊛ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{H} - \boxed{X} \models$

$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

[Bloch sphere with $\ket{0}$ at top (z-axis), $\ket{1}$ at bottom, $\ket{+}$ and $\ket{-}$ on x-axis, $\ket{+i}$ and $\ket{-i}$ on y-axis]

- <u>Pauli-Y measurement</u>: measure along $y$-axis; equivalent to measuring in basis $\{\ket{+i}, \ket{-i}\}$

⊛ <span style="color:red">Recall: $\ket{+i} = SH\ket{0}$, $\ket{-i} = SH\ket{1}$, $H \equiv$ Hadamard gate</span>

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

⊛ <span style="color:red">$SH$ unitary $\Rightarrow \{\ket{+i}, \ket{-i}\}$ is a basis!</span>

$S \equiv$ phase gate
$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

⊛ For a state vector $\ket{\psi}$:

$$P_r(+i) = |\braket{+i|\psi}|^2 = \braket{+i|\psi}\braket{\psi|+i} = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}]$$

$$P_r(-i) = |\braket{-i|\psi}|^2 = \braket{-i|\psi}\braket{\psi|-i} = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$$

<u>Check</u>: $P_r(+i) + P_r(-i) = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}] + \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$

$$= \mathrm{Tr}\big[(\ket{+i}\bra{+i} + \ket{-i}\bra{-i})\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}[\ket{\psi}\bra{\psi}] = 1 \checkmark$$

<span style="color:blue">$\ket{+i} = SH\ket{0}$
$\ket{-i} = SH\ket{1}$</span>

$$= SH\ket{0}\bra{0}HS^\dagger + SH\ket{1}\bra{1}HS^\dagger = SH\ket{0}\bra{0}HS^\dagger + SH\ket{1}\bra{1}HS^\dagger$$

$$= SH\big(\ket{0}\bra{0} + \ket{1}\bra{1}\big)HS^\dagger$$
$$\quad\quad\quad\quad\quad\quad = \mathbb{1}$$
$$= SH \cdot HS^\dagger = SS^\dagger = \mathbb{1}$$
$$\quad\;\; = \mathbb{1}$$

⊛ <u>Observe</u>: $P_r(+i) = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}] = \mathrm{Tr}[SH\ket{0}\bra{0}HS^\dagger \underbrace{\ket{\psi}\bra{\psi}}_{}] = \mathrm{Tr}[\ket{0}\bra{0}HS^\dagger\ket{\psi}\bra{\psi}SH]$

$P_r(-i) = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}] = \mathrm{Tr}[SH\ket{1}\bra{1}HS^\dagger\ket{\psi}\bra{\psi}] = \mathrm{Tr}[\ket{1}\bra{1}\underline{HS^\dagger\ket{\psi}}\bra{\psi}SH]$

$\Rightarrow$ Apply $S^\dagger$, then $H$ gate to $\ket{\psi}$, then measure in $\{\ket{0}, \ket{1}\}$ basis!

⊛ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{S^\dagger} - \boxed{H} - \boxed{X} \models$

## Page 9

## — Measuring multiple qubits.

- Consider state vector $\ket{\psi}$ of $n$ qubits $\left(\ket{\psi} \in (\mathbb{C}^2)^{\otimes n}\right)$.

- Computational-basis measurement is a $\{\ket{0}, \ket{1}\}$ measurement on each qubit.

- Outcome probabilities: $\Pr[0,0,1] = |\underbrace{\bra{0,0,1}}_{\bra{0}\otimes\bra{0}\otimes\bra{1}}\ket{\psi}|^2$ (for three qubits).

$$\Pr[x_1, x_2, x_3] = |\braket{x_1, x_2, x_3 | \psi}|^2, \quad x_1, x_2, x_3 \in \{0,1\}.$$

- What is the probability that the first qubit is 0?

$$\Pr[1^{st}\text{ qubit } 0] = \Pr[0,0,0] + \Pr[0,0,1] + \Pr[0,1,0] + \Pr[0,1,1].$$

$$\left\{\begin{matrix} 000 \\ 001 \\ 010 \\ 011 \end{matrix}\right. \quad \begin{matrix} 100 \\ 101 \\ 110 \\ 111 \end{matrix}$$

$$\Pr[2^{nd}\text{ qubit } 1] = \Pr[0,1,0] + \Pr[0,1,1] + \Pr[1,1,0] + \Pr[1,1,1].$$

- We can simultaneously measure each qubit in a different basis.

**Example:** measure $1^{st}$ & $3^{rd}$ qubit in Z-basis, $2^{nd}$ in X-basis.

$$\Pr[0, +, 1] = |\underbrace{\bra{0, +, 1}}_{= \bra{0}\otimes\bra{+}\otimes\bra{1}}\ket{\psi}|^2$$

## Page 10

## ④ Observables

- In quantum mechanics, measurement outcomes are not deterministic — they occur with some probability.

- What is the *expected* outcome of a measurement?

- Recall: For a probability mass function $p_X(x)$, $\quad \left( \begin{array}{l} p_X(x) \in [0,1] \;\; \forall x \in \mathcal{X} \\ \sum_{x \in \mathcal{X}} p_X(x) = 1 \end{array} \right)$

  [Red annotation: $X$ is a Random variable $\to \Pr(X = x) = p_X(x)$.]

  the expected value is

$$\mathbb{E}(X) = \sum_x p_X(x) \cdot x$$

- We can measure w.r.t. any orthonormal basis — consider basis $\{\ket{e_k}\}_{k=1}^{d}$.

  Outcomes are labeled by $k$
  Outcome $k$ is associated with value $\lambda_k$. $\leftrightarrow$ random variable $X$

  For a state vector $\ket{\psi} \in \mathbb{C}^d$, the probability distribution is

$$\Pr(k) = |\braket{e_k|\psi}|^2 \equiv \Pr(X = \lambda_k)$$

  The expected value of $X$ is:

  [Blue annotation: $\braket{v_1 | M | v_2} = \mathrm{Tr}\left[ M \ket{v_2}\bra{v_1} \right]$.]

$$\mathbb{E}(X) = \sum_{k=1}^{d} \Pr(X = \lambda_k) \cdot \lambda_k = \sum_{k=1}^{d} |\braket{e_k|\psi}|^2 \cdot \lambda_k = \sum_{k=1}^{d} \braket{e_k | \psi}\braket{\psi | e_k} \cdot \lambda_k$$

$$= \sum_{k=1}^{d} \mathrm{Tr}\!\left( \ket{e_k}\bra{e_k} \psi \rangle\langle \psi \right) \cdot \lambda_k = \mathrm{Tr}\!\left[ \left( \sum_{k=1}^{d} \lambda_k \ket{e_k}\bra{e_k} \right) \ket{\psi}\bra{\psi} \right] = \mathrm{Tr}\!\left[ H \ket{\psi}\bra{\psi} \right].$$

$$H \ket{e_{k'}} = \sum_{k=1}^{d} \lambda_k \ket{e_k}\underbrace{\braket{e_k|e_{k'}}}_{\delta_{k,k'}} = \lambda_{k'} \ket{e_{k'}}$$

[Red annotation: $H \to$ Hermitian operator.]
