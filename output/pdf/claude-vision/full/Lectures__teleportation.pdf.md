# Lectures__teleportation.pdf

## Page 1

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

## Page 2

(b) How to extract information from a qubit? <u>Measurements</u>!

- A <u>measurement</u> (aka "positive operator-valued measure") is defined by $\rightarrow$ (POVM) a set of operators $\{M_x\}_{x \in \mathcal{X}}$ (some finite set $\mathcal{X}$), such that:

  (1) $M_x \geq 0 \;\; \forall x \in \mathcal{X}$. ($M_x \in L(\mathbb{C}^d) \to d \times d$ matrix for arbitrary dimension $d$.)

  (2) $\sum_{x \in \mathcal{X}} M_x = \mathbb{1}$

- For any state $\rho$, the outcome probabilities are given by
  $$\Pr(x) = \mathrm{Tr}[M_x \rho] \;\; \forall x \in \mathcal{X}.$$

- Examples of measurements:

  (1) Pauli-$Z$ / computational basis: $\{\underbrace{\ket{0}\bra{0}}_{M_0}, \underbrace{\ket{1}\bra{1}}_{M_1}\}$ &nbsp;&nbsp; $\ket{0}\bra{0} + \ket{1}\bra{1} = \mathbb{1}$. &nbsp;&nbsp; $Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$

  (2) Pauli-$X$: $\{\ket{+}\bra{+}, \ket{-}\bra{-}\}$, $\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$, $X\ket{\pm} = \pm\ket{\pm}$

  (3) Any basis: for any unitary $U$, $\{U\ket{0}\bra{0}U^\dagger, U\ket{1}\bra{1}U^\dagger\}$.

  $$\left(\underline{\text{Check}}: U\ket{0}\bra{0}U^\dagger + U\ket{1}\bra{1}U^\dagger = U\underbrace{(\ket{0}\bra{0} + \ket{1}\bra{1})}_{=\mathbb{1}}U^\dagger = UU^\dagger = \mathbb{1} \;\checkmark\right)$$

(c) <u>Entanglement</u>: One of the key distinguishing characteristics of quantum vs. classical.

- A state vector $\ket{\psi}_{AB}$ is entangled if it <u>cannot</u> be written as $\ket{\psi}_{AB} = \ket{\psi}_A \otimes \ket{\psi}_B$.
  $$\downarrow \text{ product state}$$

- Every state vector $\ket{\psi}_{AB}$ has a <u>Schmidt decomposition</u>:

  (1) $\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{e_k}_A \otimes \ket{f_k}_B$

  $\ket{\Phi^+} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0} + \ket{1}\ket{1})$.

  (2) $S_k$: Schmidt coefficients $(S_k > 0)$

  $\{\ket{e_k}_A\}_{k=1}^{r}$ and $\{\ket{f_k}_B\}_{k=1}^{r}$ are orthonormal vectors.
  $$\braket{e_k | e_{k'}} = \delta_{k,k'} = \begin{cases} 0 & \text{if } k \neq k' \\ 1 & \text{if } k = k' \end{cases}$$

## Page 3

$r$: Schmidt rank.

(3) $\ket{\psi}_{AB}$ is entangled if and only if $\underline{r > 1}$.

- Entanglement of mixed states is more complicated!

  A mixed state (density operator) $\rho_{AB}$ is entangled it $\underline{\text{cannot}}$ be written as

  $$\rho_{AB} = \sum_{x \in \mathcal{X}} \underbrace{p(x)}_{\text{probabilities}} \tau_A^{(x)} \otimes \omega_B^{(x)} \rightarrow \text{This is } \underline{\text{Separable}}.$$

- ✱ If A & B are qubits, then $\rho_{AB}$ is separable if and only if $\rho_{AB}^{T_B} \geq 0$. $\quad$ <span style="color:red">↙ partial transpose</span>

## ② Teleportation

- A method to transfer the state of a qubit from Alice to Bob using entanglement and classical communication only.

- <u>Given</u>: (1) State vector that Alice wants to send to Bob.
  (2) Shared entangled state b/w Alice and Bob.

- <u>Goal</u>: Transfer the state of qubit $A'$ to Bob's qubit.

[Teleportation circuit diagram: Alice has qubit $\ket{\psi}_{A'}$ which together with her half of $\ket{\Phi^+}_{AB}$ goes into a Bell Measurement, producing classical bits $x \in \{0,1\}$ and $z \in \{0,1\}$. Bob's qubit (the other half of $\ket{\Phi^+}_{AB}$) has $X^x$ then $Z^z$ applied conditioned on the classical bits, yielding $\ket{\psi}_B$.]

- If $x=0$, do nothing. If $x=1$, apply $X$.
- If $z=0$, do nothing. If $z=1$, apply $Z$.

## Page 4

(a) Key ingredient: the two-qubit __Bell measurement__

- POVM is $\{\Phi^+, \Phi^-, \Psi^+, \Psi^-\}$, $\quad \Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}$, $\Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}$.

$$\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{0} \pm \ket{1}\ket{1}\right)$$
$$\ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{1} \pm \ket{1}\ket{0}\right)$$

- Circuit description of the measurement:

[Circuit diagram: Two wires labeled $A'$ (top, source) and $A$ (bottom, target). A CNOT gate with control on $A'$ and target on $A$, followed by a Hadamard gate $H$ on the $A'$ wire, then $z$-basis measurements ($\ket{x}$ boxes) on both wires.]

Hadamard gate: $H\ket{0} = \ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$
$H\ket{1} = \ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0}-\ket{1})$

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$z$-basis measurement.

CNOT gate (source $\to$ target):
$$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

$\text{CNOT}\ket{0,0} = \ket{0,0}$
$\text{CNOT}\ket{0,1} = \ket{0,1}$
$\text{CNOT}\ket{1,0} = \ket{1,1}$
$\text{CNOT}\ket{1,1} = \ket{1,0}$

---

(b) __Protocol analysis__

$\ket{\psi}_{A'} = \alpha \ket{0}_{A'} + \beta \ket{1}_{A'} \quad \to$ State Alice wants to send to Bob. $\quad (|\alpha|^2 + |\beta|^2 = 1)$

$\ket{\Phi^+}_{AB} = \tfrac{1}{\sqrt{2}}\left(\ket{0,0}_{AB} + \ket{1,1}_{AB}\right) \to$ Shared entanglement.

(1) Joint initial state: 
$$\ket{\psi}_{A'} \otimes \ket{\Phi^+}_{AB} = \left(\alpha\ket{0}_{A'} + \beta\ket{1}_{A'}\right) \otimes \tfrac{1}{\sqrt{2}}\left(\ket{0,0}_{AB} + \ket{1,1}_{AB}\right)$$
$$= \tfrac{1}{\sqrt{2}}\Big(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB} + \beta\ket{1,0,0}_{A'AB} + \beta\ket{1,1,1}_{A'AB}\Big)$$

## Page 5

(2) $\text{CNOT}_{A'A}$: $\frac{1}{\sqrt{2}}(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB}$
$\qquad\qquad\qquad +\beta\underset{\color{red}1,1}{\ket{1,0,0}}_{A'AB} + \beta\underset{\color{red}1,0}{\ket{1,1,1}}_{A'AB})$

$\downarrow$

$\frac{1}{\sqrt{2}}(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB}$
$\qquad +\beta\ket{1,1,0}_{A'AB} + \beta\ket{1,0,1}_{A'AB})$

(3) Hadamard on $A'$: $\frac{1}{\sqrt{2}}(\alpha\underset{\color{red}\ket{+}}{\ket{0,0,0}}_{A'AB} + \alpha\underset{\color{red}\ket{+}}{\ket{0,1,1}}_{A'AB}$
$\qquad\qquad\qquad\qquad +\beta\underset{\color{red}\ket{-}}{\ket{1,1,0}}_{A'AB} + \beta\underset{\color{red}\ket{-}}{\ket{1,0,1}}_{A'AB})$

$\color{blue}H\ket{0} = \ket{+}$
$\color{blue}H\ket{1} = \ket{-}$

$\downarrow$

$\frac{1}{\sqrt{2}}(\alpha\ket{+,0,0}_{A'AB} + \alpha\ket{+,1,1}_{A'AB}$
$\qquad +\beta\ket{-,1,0}_{A'AB} + \beta\ket{-,0,1}_{A'AB})$

(4) Measure $A'A$ in the $Z$-basis / computational basis / $\{\ket{0},\ket{1}\}$ basis:

- **Four outcomes**: $00, 01, 10, 11 = (z,x)$

$\frac{1}{\sqrt{2}}(\alpha\ket{+,0,0}_{A'AB} + \alpha\ket{+,1,1}_{A'AB} + \beta\ket{-,1,0}_{A'AB} + \beta\ket{-,0,1}_{A'AB})$

$= \frac{1}{\sqrt{2}}\Big(\alpha\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})_{A'}\ket{0,0}_{AB} + \alpha\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})_{A'}\ket{1,1}_{AB}$
$\qquad + \beta\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})_{A'}\ket{1,0}_{AB} + \beta\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})_{A'}\ket{0,1}_{AB}\Big)$

$\downarrow$

$\ket{\phi}_{A'AB} = \Big(\ket{0,0}_{A'A}\frac{1}{2}(\alpha\ket{0}+\beta\ket{1})_B + \ket{0,1}_{A'A}\frac{1}{2}(\alpha\ket{1}+\beta\ket{0})_B$
$\qquad\qquad + \ket{1,0}_{A'A}\frac{1}{2}(\alpha\ket{0}-\beta\ket{1})_B + \ket{1,1}_{A'A}\frac{1}{2}(\alpha\ket{1}-\beta\ket{0})_B\Big)$

## Page 6

$\{\ket{0,0}\bra{0,0}, \ket{0,1}\bra{0,1}, \ket{1,0}\bra{1,0}, \ket{1,1}\bra{1,1}\}$

- <u>Outcome $(0,0)$</u>: $\Pr(0,0) = \text{Tr}\left[(\ket{0,0}\bra{0,0}_{A'A} \otimes \mathbb{1}_B) \ket{\phi}\bra{\phi}_{A'AB}\right]$

$$\downarrow$$

$$= \text{Tr}\left[(\bra{0,0}_{A'A} \otimes \mathbb{1}_B) \ket{\phi}\bra{\phi}_{A'AB} (\ket{0,0}_{A'A} \otimes \mathbb{1}_B)\right]$$

$(\bra{0,0}_{A'A} \otimes \mathbb{1}_B)\ket{\phi}_{A'AB} = (\bra{0,0}_{A'A} \otimes \mathbb{1}_B) \tfrac{1}{2}\Big(\ket{0,0}_{A'A}(\alpha\ket{0}+\beta\ket{1})_B + \ket{0,1}_{A'A}(\alpha\ket{1}+\beta\ket{0})_B$

$$+ \ket{1,0}_{A'A}(\alpha\ket{0}-\beta\ket{1})_B + \ket{1,1}_{A'A}(\alpha\ket{1}-\beta\ket{0})_B\Big)$$

$$\downarrow$$

$$= \tfrac{1}{2}\Big(\underbrace{\braket{0,0|0,0}_{A'A}}_{1}(\alpha\ket{0}+\beta\ket{1})_B + \underbrace{\braket{0,0|0,1}_{A'A}}_{0}(\alpha\ket{1}+\beta\ket{0})_B$$

$$+ \underbrace{\braket{0,0|1,0}_{A'A}}_{0}(\alpha\ket{0}-\beta\ket{1})_B + \underbrace{\braket{0,0|1,1}_{A'A}}_{0}(\alpha\ket{1}-\beta\ket{0})_B\Big)$$

$$\downarrow$$

$$= \tfrac{1}{2}(\alpha\ket{0}_B + \beta\ket{1})$$

$$\downarrow$$

$$= \tfrac{1}{2}\ket{\psi}_B \;\;\Rightarrow\;\; \Pr(0,0) = \text{Tr}\left[\tfrac{1}{2}\ket{\psi}\bra{\psi}\tfrac{1}{2}\right] = \tfrac{1}{4}\underbrace{\text{Tr}[\ket{\psi}\bra{\psi}]}_{=1} = \tfrac{1}{4}.$$

<span style="color:red">State of Bob conditioned on outcome $(0,0)$ is $\ket{\psi}$!  
(Exactly the state Alice wanted to send.)</span>

- <u>Outcome $(0,1)$</u>: $\Pr(0,1) = \text{Tr}\left[(\ket{0,1}\bra{0,1}_{A'A} \otimes \mathbb{1}_B) \ket{\phi}\bra{\phi}_{A'AB}\right]$

$$\downarrow$$

$$= \text{Tr}\left[(\bra{0,1}_{A'A} \otimes \mathbb{1}_B)\ket{\phi}\bra{\phi}_{A'AB}(\ket{0,1}_{A'A}\otimes\mathbb{1}_B)\right].$$

$$\ket{\phi}_{A'AB} = \tfrac{1}{2}\Big(\ket{0,0}_{A'A}(\alpha\ket{0}+\beta\ket{1})_B + \underline{\ket{0,1}_{A'A}(\alpha\ket{1}+\beta\ket{0})_B}$$

$$+ \ket{1,0}_{A'A}(\alpha\ket{0}-\beta\ket{1})_B + \ket{1,1}_{A'A}(\alpha\ket{1}-\beta\ket{0})_B\Big)$$

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$

$X\ket{\psi} = \alpha X\ket{0} + \beta X\ket{1} = \alpha\ket{1} + \beta\ket{0}$

$(\bra{0,1}_{A'A} \otimes \mathbb{1}_B)\ket{\phi}_{A'AB} = \tfrac{1}{2}(\alpha\ket{1}+\beta\ket{0}) = \tfrac{1}{2}X\ket{\psi}_B.$ <span style="color:red">$\to$ Pauli $X$.</span>

$$\text{Tr}\left[\tfrac{1}{2}X\ket{\psi}\bra{\psi}X\tfrac{1}{2}\right] = \tfrac{1}{4}\text{Tr}[X\ket{\psi}\bra{\psi}X] = \tfrac{1}{4}\text{Tr}[\ket{\psi}\bra{\psi}] = \tfrac{1}{4}.$$

$\Rightarrow \Pr(0,1) = \tfrac{1}{4}$  $\qquad\qquad$ <span style="color:blue">$X^2 = \mathbb{1}$</span>

## Page 7

⇒ State of Bob conditioned on Alice's outcome is $X\ket{\psi}$.

- <u>Outcome (1,0)</u>: $\Pr(1,0) = \text{Tr}\Big[ \big(\bra{1,0}_{A'A} \otimes \mathbb{I}_B\big) \ket{\phi}\bra{\phi}_{A'AB} \big(\ket{1,0}_{A'A} \otimes \mathbb{I}_B\big) \Big]$

$$\ket{\phi}_{A'AB} = \tfrac{1}{2}\Big( \ket{0,0}_{A'A}\big(\alpha\ket{0}+\beta\ket{1}\big)_B + \ket{0,1}_{A'A}\big(\alpha\ket{1}+\beta\ket{0}\big)_B$$
$$+ \ket{1,0}_{A'A}\big(\alpha\ket{0}-\beta\ket{1}\big)_B + \ket{1,1}_{A'A}\big(\alpha\ket{1}-\beta\ket{0}\big)_B \Big)$$

$\ket{\psi} = \alpha\ket{0}+\beta\ket{1}$
$Z\ket{\psi} = \alpha Z\ket{0} + \beta Z\ket{1}$, $\quad Z\ket{1}=-\ket{1}$
$\quad\quad = \alpha\ket{0} - \beta\ket{1}$.

$\big(\bra{1,0}_{A'A} \otimes \mathbb{I}_B\big)\ket{\phi}_{A'AB} = \tfrac{1}{2}\big(\alpha\ket{0}-\beta\ket{1}\big) = \tfrac{1}{2} Z\ket{\psi}$ → Pauli $Z$

$$\text{Tr}\big[\tfrac{1}{2} Z\ket{\psi}\bra{\psi} Z \tfrac{1}{2}\big] = \tfrac{1}{4}\text{Tr}\big[Z\ket{\psi}\bra{\psi} Z\big] = \tfrac{1}{4}\text{Tr}\big[\ket{\psi}\bra{\psi}\big] = \tfrac{1}{4}.$$

$Z^2 = \mathbb{I}$

$\Rightarrow \Pr(1,0) = \tfrac{1}{4}$

⇒ State of Bob conditioned on Alice's outcome is $Z\ket{\psi}$.

- <u>Outcome (1,1)</u>: $\Pr(1,1) = \text{Tr}\Big[ \big(\bra{1,1}_{A'A} \otimes \mathbb{I}_B\big) \ket{\phi}\bra{\phi}_{A'AB} \big(\ket{1,1}_{A'A} \otimes \mathbb{I}_B\big) \Big]$

$$\ket{\phi}_{A'AB} = \tfrac{1}{2}\Big( \ket{0,0}_{A'A}\big(\alpha\ket{0}+\beta\ket{1}\big)_B + \ket{0,1}_{A'A}\big(\alpha\ket{1}+\beta\ket{0}\big)_B$$
$$+ \ket{1,0}_{A'A}\big(\alpha\ket{0}-\beta\ket{1}\big)_B + \ket{1,1}_{A'A}\big(\alpha\ket{1}-\beta\ket{0}\big)_B \Big)$$

$\big(\bra{1,1}_{A'A} \otimes \mathbb{I}_B\big)\ket{\phi}_{A'AB} = \tfrac{1}{2}\big(\alpha\ket{1}-\beta\ket{0}\big) = \tfrac{1}{2} XZ\ket{\psi}_B$

$$\text{Tr}\big[\tfrac{1}{2} XZ\ket{\psi}\bra{\psi} ZX \tfrac{1}{2}\big] = \tfrac{1}{4}\text{Tr}\big[ZX\ket{\psi}\bra{\psi} XZ\big] = \tfrac{1}{4}\text{Tr}\big[\ket{\psi}\bra{\psi}\big] = \tfrac{1}{4}.$$

$\Rightarrow \Pr(1,1) = \tfrac{1}{4}$

$Z^2 = \mathbb{I},\ X^2 = \mathbb{I}$

⇒ State of Bob conditioned on Alice's outcome is $XZ\ket{\psi}$.

## Page 8

**Summary:**
- $\Pr(0,0) = \tfrac{1}{4} \to$ State $\ket{\psi}$ for Bob.
- $\Pr(0,1) = \tfrac{1}{4} \to$ State $X\ket{\psi}$ for Bob.
- $\Pr(1,0) = \tfrac{1}{4} \to$ State $Z\ket{\psi}$ for Bob.
- $\Pr(1,1) = \tfrac{1}{4} \to$ State $XZ\ket{\psi}$ for Bob.

(5) After the measurement, Alice communicates the outcomes to Bob.

(6) Depending on the outcome, Bob applies a __correction__:

[column labels in red: $z\ \ x$]

$0,0 \to$ No correction

$0,1 \to$ Apply Pauli-$X$  $\quad X(X\ket{\psi}) = \underbrace{X^2}_{=\mathbb{1}}\ket{\psi} = \ket{\psi}$

$1,0 \to$ Apply Pauli-$Z$  $\quad Z(Z\ket{\psi}) = \underbrace{Z^2}_{=\mathbb{1}}\ket{\psi} = \ket{\psi}$

$1,1 \to$ Apply Pauli-$X$, then Pauli-$Z$

Then Bob recovers Alice's state!

⊛ Teleportation is __not__ instantaneous / faster than light — it only works if Bob gets Alice's measurement outcomes ⤳ this takes time!

⊛ The teleported state can also be a mixed state.
