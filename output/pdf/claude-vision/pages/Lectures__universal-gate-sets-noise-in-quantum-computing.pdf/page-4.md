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
