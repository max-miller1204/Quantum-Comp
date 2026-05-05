# Lectures__universal-gate-sets-noise-in-quantum-computing.pdf

## Page 1

# ① Universal Gate Sets

- We want to use a set of elementary gates to execute <u>arbitrary</u> unitaries on $n$ qubits.

[Diagram: a quantum circuit on 4 wires showing several single-qubit boxes and two-qubit boxes spanning adjacent wires arranged in columns, illustrating decomposition of an arbitrary unitary into elementary gates.]

- <u>Two versions</u>: 
  - Exact  ↓ Requires (uncountably) infinite # of gates in the set.
  - Approximate. → we can allow for some error/deviation in the implementation. → Relevant when we want the set to be finite.

(a) <u>Exact case</u>: CNOT + all single-qubit gates are universal! ( ✱ This set <u>is not finite</u>.)

> **Lemma 4.1.** Every unitary $2\times 2$ matrix can be expressed as
> $$\begin{pmatrix} e^{i\delta} & 0 \\ 0 & e^{i\delta} \end{pmatrix} \begin{pmatrix} e^{i\alpha/2} & 0 \\ 0 & e^{-i\alpha/2} \end{pmatrix} \begin{pmatrix} \cos\theta/2 & \sin\theta/2 \\ -\sin\theta/2 & \cos\theta/2 \end{pmatrix}$$
> $$\times \begin{pmatrix} e^{i\beta/2} & 0 \\ 0 & e^{-i\beta/2} \end{pmatrix},$$
> where $\delta, \alpha, \theta,$ and $\beta$ are real valued. Moreover, any special unitary $2\times 2$ matrix (i.e., with unity determinant) can be expressed as
> $$\begin{pmatrix} e^{i\alpha/2} & 0 \\ 0 & e^{-i\alpha/2} \end{pmatrix} \begin{pmatrix} \cos\theta/2 & \sin\theta/2 \\ -\sin\theta/2 & \cos\theta/2 \end{pmatrix} \begin{pmatrix} e^{i\beta/2} & 0 \\ 0 & e^{-i\beta/2} \end{pmatrix}.$$

✱ Recall the rotation gates!

$$R_x(\theta) = e^{-i\frac{\theta}{2}X} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)X$$

$$R_y(\theta) = e^{-i\frac{\theta}{2}Y} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Y$$

$$R_z(\theta) = e^{-i\frac{\theta}{2}Z} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Z$$

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

<u>Observe</u>: 
$$R_y(\theta) = \begin{pmatrix} \cos(\tfrac{\theta}{2}) & 0 \\ 0 & \cos(\tfrac{\theta}{2}) \end{pmatrix} - i\begin{pmatrix} 0 & -i\sin(\tfrac{\theta}{2}) \\ i\sin(\tfrac{\theta}{2}) & 0 \end{pmatrix} = \begin{pmatrix} \cos(\tfrac{\theta}{2}) & -\sin(\tfrac{\theta}{2}) \\ \sin(\tfrac{\theta}{2}) & \cos(\tfrac{\theta}{2}) \end{pmatrix}$$

## Page 2

$$R_z(\theta) = \begin{pmatrix} \cos(\frac{\theta}{2}) & 0 \\ 0 & \cos(\frac{\theta}{2}) \end{pmatrix} - i \begin{pmatrix} \sin(\frac{\theta}{2}) & 0 \\ 0 & -\sin(\frac{\theta}{2}) \end{pmatrix} \qquad e^{i\varphi} = \cos(\varphi) + i\sin(\varphi)$$

$$= \begin{pmatrix} \cos(\frac{\theta}{2}) - i\sin(\frac{\theta}{2}) & 0 \\ 0 & \cos(\frac{\theta}{2}) + i\sin(\frac{\theta}{2}) \end{pmatrix}$$

$$= \begin{pmatrix} e^{-i\frac{\theta}{2}} & 0 \\ 0 & e^{i\frac{\theta}{2}} \end{pmatrix}$$

★ So every single-qubit gate can be decomposed into rotation gates:

$$U = R_z(\alpha)\, R_y(\theta)\, R_z(\beta), \quad \text{for appropriate angles } \alpha, \beta, \theta.$$

> *Lemma 5.1.* For a unitary $2\times 2$ matrix $W$, a $\wedge_1(W)$ gate can be simulated by a network of the form
>
> [Circuit diagram: controlled-$W$ gate equals a circuit with control line passing through CNOTs interleaved with single-qubit gates $A$, $B$, $C$ on the target line: $-A-\oplus-B-\oplus-C-$, with controls on the top wire.]
>
> where $A$, $B$, and $C \in SU(2)$ if and only if $W \in SU(2)$.

(b) <u>Approximate case</u>: Arises when the # of gates in the set is finite

(B/c the set of unitaries is uncountably infinite, while the set of sequences of gates from a finite set will be countably infinite.)

★ <mark>Theorem:</mark> <u>Clifford gates</u> + <u>one single-qubit non-Clifford gate</u> is universal!

$$\hookrightarrow T \text{ gate!} \quad T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$$

– Recall Pauli operators on $n$ qubits: $\mathcal{P}_n = \{I, X, Y, Z\}^{\otimes n} \to P = I \otimes X \otimes Y \otimes X \otimes Z$
$$\hookrightarrow 4^n$$

$\to$ Let $\mathcal{P}_n^* = \mathcal{P}_n \setminus \{I^{\otimes n}\}$
$\hookrightarrow$ exclude the identity gate.

## Page 3

- Define the $n$-qubit Clifford group as

$$\mathcal{C}_n := \left\{ U : P \in \pm \mathcal{P}_n^* \Rightarrow UPU^\dagger \in \pm \mathcal{P}_n^* \right\} / U(1) \quad \rightarrow \text{mod out global phase}$$

$\rightarrow$ Transforms Paulis to Paulis (up to sign)

$H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \rightarrow HXH = Z, \; HZH = X$

⊛ <u>Theorem</u>: $\mathcal{C}_n = \langle H_i, S_i, \text{CNOT}_{i,j} \;:\; i,j \in \{1,2,\ldots,n\} \rangle / U(1)$

  ⊛ $H, S, \text{CNOT}$ are <u>generators</u> of the Clifford group!

  ⊛ (Take all possible products of $H, S, \text{CNOT}$, and ignore global phase.)

⊛ <mark><u>Corollary</u>:</mark> $\{H, S, \text{CNOT}, T\}$ is universal $\rightarrow \{H, \text{CNOT}, T\}$ is universal. $(S = T^2)$.

---

② <u>Noise and Errors in Quantum Computing</u>

⊛ In quantum computing, we care about <u>precise control</u> of qubits — but they inevitably <u>interact with their environment</u>! This evolution is unitary.

(<u>ideal case</u>).

[Circuit: $\ket{0} \longrightarrow \boxed{G} \longrightarrow G\ket{0}$]

  $\underbrace{\phantom{\boxed{G}}}_{\text{Unitary gate.}}$

(<u>reality</u>) $\rightarrow$ gate noise.

[Circuit:
- System: $\ket{0} \longrightarrow$ [box $\mathcal{N}$] $\longrightarrow \mathcal{N}(\ket{0}\bra{0}) \rightarrow$ "quantum channel"
- Environment: $\ket{0} \longrightarrow$ [into box, traced out]
]

## Page 4

(reality) → decoherence
↓
Qubit state drifts over time.

[Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$, $\ket{-}$, $\ket{+i}$, $\ket{-i}$ on equator. A purple arrow shows the state drifting from near $\ket{0}$ toward the interior, with another arrow pointing to the center labeled:]

Origin: maximally-mixed state $\frac{\mathbb{1}}{2}$.

(a) Any <u>unwanted gate</u> applied to the qubit can be thought of as noise.

<u>Example</u>: Bit flip → Pauli-X gate, $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

$X\ket{0} = \ket{1}$, $X\ket{1} = \ket{0}$ → <span style="color:red">opposite ends of the Bloch sphere!</span>

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1} \to X\ket{\psi} = \alpha\ket{1} + \beta\ket{0}$

→ measurement probabilities get flipped!

[Bloch sphere with $\ket{0}$ and $\ket{1}$ marked in red, indicating the X gate maps between these antipodal points.]

<u>Example</u>: Rotations → $R_x(\theta), R_y(\theta), R_z(\theta)$

✱ Recall teleportation! The state before Bob's correction is precisely a noisy version of the true state Alice wants to send.

(b) <u>Different gates</u> can also be applied <u>randomly</u> to the state

- <u>Example</u>: Apply $X$ with probability $\alpha$, do nothing with probability $1-\alpha$.

## Page 5

If the qubit state is given by a density operator $\rho$, then after the noise it is

$$(1-\alpha)\rho + \alpha X\rho X \quad \rightarrow \text{"Bit-flip channel"}$$

- $(1-\alpha)\rho$: Do nothing with probability $1-\alpha$
- $\alpha X\rho X$: Apply the X gate with probability $\alpha$.

[Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom; vertical blue line connecting them with red dots indicating the mixed state along the z-axis]

$$\ket{0}\bra{0} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \mapsto (1-\alpha)\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \alpha \underbrace{X\ket{0}\bra{0}X}_{=\ket{1}\bra{1}} = \begin{pmatrix} 1-\alpha & 0 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & \alpha \end{pmatrix}$$

$$= \begin{pmatrix} 1-\alpha & 0 \\ 0 & \alpha \end{pmatrix}$$

$$= (1-\alpha)\ket{0}\bra{0} + \alpha\ket{1}\bra{1}.$$

✸ If we measured the initial (noiseless) state, then we would get the outcome "0" with probability 1 → after noise, the state becomes mixed: with probability $1-\alpha$ we get "0" and with probability $\alpha$ we get "1".

✸ So $\alpha$ quantifies the amount of noise! 
- $\alpha = 0 \Rightarrow$ no noise
- $\alpha = \frac{1}{2} \Rightarrow \boxed{\frac{1}{2}\ket{0}\bra{0} + \frac{1}{2}\ket{1}\bra{1}}$

✸ For a general density matrix: recall the form $\rho = \frac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)$

$r_x, r_y, r_z$ → Coordinates in the Bloch sphere.

[Bloch sphere with axes labeled: z-axis up with $\ket{0}$ at top and $\ket{1}$ at bottom; y-axis to the right with $\ket{+i}$, and $\ket{-i}$ on the opposite side; x-axis coming out toward viewer with $\ket{+}$ in front and $\ket{-}$ behind]

How do those coordinates transform after the noise?

$$(r_x, r_y, r_z) \mapsto (r_x', r_y', r_z') \;?$$

## Page 6

$$(1-\alpha)\rho + \alpha X\rho X = \underbrace{(1-\alpha)\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)}_{\rho} + \alpha \underbrace{X\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)X}_{\rho}$$

$$\underline{XY = -YX}$$
$$\underline{XZ = -ZX}$$

$$= \tfrac{1}{2}(X\mathbb{1}X + r_x \underbrace{XXX}_{=X^2 \cdot X = X} + r_y \underbrace{XYX}_{=-X^2 Y = -Y} + r_z \underbrace{XZX}_{=-X^2 Z = -Z})$$
$$\underbrace{= X^2}_{=\mathbb{1}}$$

$$= (1-\alpha)\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z) + \alpha\tfrac{1}{2}(\mathbb{1} + r_x X - r_y Y - r_z Z)$$

$$= \tfrac{1}{2}\Big((1-\alpha+\alpha)\mathbb{1} + ((1-\alpha)r_x + \alpha r_x)X$$
$$\qquad + ((1-\alpha)r_y - \alpha r_y)Y$$
$$\qquad + ((1-\alpha)r_z - \alpha r_z)Z\Big)$$

$$= \tfrac{1}{2}(\mathbb{1} + \underbrace{r_x}_{r'_x = r_x} X + \underbrace{(1-2\alpha)r_y}_{r'_y} Y + \underbrace{(1-2\alpha)r_z}_{r'_z} Z).$$

<u>Check</u>: If $\rho = \ket{0}\bra{0}$, then $r_x = 0$, $r_y = 0$, $r_z = 1 \xrightarrow{\alpha=1} r'_x = 0,\; r'_y = 0,\; r'_z = -1$ ✓

- <u>Example</u>: Phase-flip / dephasing channel

$$\rho \mapsto \underbrace{(1-\alpha)\rho}_{\text{Do nothing with probability } 1-\alpha} + \underbrace{\alpha Z\rho Z}_{\text{Apply Pauli-}Z\text{ with probability }\alpha}.$$

(✱) Now how do the coordinates transform?

$$\rho = \tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z) \longmapsto \rho' = \tfrac{1}{2}(\mathbb{1} + r'_x X + r'_y Y + r'_z Z)$$

$$r'_x = (1-2\alpha) r_x,\quad r'_y = (1-2\alpha) r_y,\quad r'_z = r_z.$$

## Page 7

✻ For this channel, it is useful to see the transformation in the standard basis.

$$\rho = \begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} \mapsto (1-\alpha)\rho + \alpha Z\rho Z = (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

where $a \in [0,1]$, $c \in \mathbb{C}$.

[arrow indicating the last product equals:]
$$= \begin{pmatrix} a & c \\ -\bar{c} & -(1-a) \end{pmatrix}$$

$$= (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} a & c \\ -\bar{c} & -(1-a) \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$$= \begin{pmatrix} a & -c \\ -\bar{c} & 1-a \end{pmatrix}$$

$$= (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} a & -c \\ -\bar{c} & 1-a \end{pmatrix} = \begin{pmatrix} a & (1-2\alpha)c \\ (1-2\alpha)\bar{c} & 1-a \end{pmatrix}$$

$\alpha = 0 \Rightarrow$ no noise
$\alpha = \tfrac{1}{2} \Rightarrow$ max. noise

✻ Off-diagonal terms are suppressed!

✻ For $\alpha = \tfrac{1}{2}$, the off-diagonal terms vanish! → superposition is gone!

- **Example:** Depolarizing channel: $\rho \mapsto (1-\alpha)\rho + \tfrac{\alpha}{3}X\rho X + \tfrac{\alpha}{3}Y\rho Y + \tfrac{\alpha}{3}Z\rho Z$

$$\begin{pmatrix} \text{With prob. } 1-\alpha, \text{ do nothing;} \\ \text{with prob. } \alpha, \text{ apply a Pauli} \\ \text{operator uniformly at random.} \end{pmatrix}$$

✻ For $\alpha = 3/4$: $\tfrac{1}{4}\rho + \tfrac{1}{4}X\rho X + \tfrac{1}{4}Y\rho Y + \tfrac{1}{4}Z\rho Z = \mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2}$  (Assignment!)

[underbrace under $\mathrm{Tr}[\rho]$: $=1$]

✻ Using this, we can write the depolarizing channel in an alternative way:

## Page 8

$$\tfrac{1}{4}\rho + \tfrac{1}{4} X\rho X + \tfrac{1}{4} Y\rho Y + \tfrac{1}{4} Z\rho Z = \mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2} \implies X\rho X + Y\rho Y + Z\rho Z = 4\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2} - \rho$$

$$\implies \rho \mapsto (1-\alpha)\rho + \tfrac{\alpha}{3}\left(4\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2} - \rho\right)$$

$$= (1-\alpha)\rho + \tfrac{4\alpha}{3}\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2} - \tfrac{\alpha}{3}\rho$$

$$= \left(1 - \alpha - \tfrac{\alpha}{3}\right)\rho + \tfrac{4\alpha}{3}\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2}$$

$$= \underbrace{\left(1 - \tfrac{4\alpha}{3}\right)\rho}_{\text{"all"}} + \underbrace{\tfrac{4\alpha}{3}\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2}}_{\text{"nothing"}} \quad \left(\text{"all or nothing"}\right).$$

"all" (state perfectly intact)

"nothing" (all information about state is lost)

$$\beta = 1 - \tfrac{4\alpha}{3}, \quad \rho \mapsto \beta \cdot \rho + (1-\beta)\tfrac{\mathbb{1}}{2}$$
