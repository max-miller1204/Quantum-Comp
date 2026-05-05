# Lectures__quantum-algorithms(II).pdf

## Page 1

① <u>Recap</u>: Quantum Circuits

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left. 

1st layer: $U_1$ acts on qubits 1,2; $U_2$ acts on qubits 3,4; $U_3$ acts on qubits 5,6.
2nd layer: $U_4$ acts on qubits 2,3; $U_5$ acts on qubits 4,5.
3rd layer: $U_6$ on qubits 1,2; $U_7$ on qubits 3,4; $U_8$ on qubits 5,6.

Each output line ends with a measurement (D) producing $x_1', x_2', x_3', x_4', x_5', x_6'$.]

$(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

1st layer | 2nd layer | 3rd layer  →  time

(✱) The circuit elements/gates are <u>unitaries</u>.
$$\left( U : U^\dagger U = U U^\dagger = \mathbb{1} \right)$$

Measurement / read-out:
$$\{\ket{0}\bra{0}, \ket{1}\bra{1}\} \rightarrow \begin{array}{l} \text{Pauli-}Z \\ \text{Computational} \\ \text{Basis.} \end{array}$$

---

(a) <u>Pauli gates</u>:

$-\boxed{X}- \quad \rightarrow \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \left( X\ket{0} = \ket{1},\ X\ket{1} = \ket{0} \right)$

$-\boxed{Y}- \quad \rightarrow \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \left( Y\ket{0} = i\ket{1},\ Y\ket{1} = -i\ket{0} \right)$

$-\boxed{Z}- \quad \rightarrow \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \quad \left( Z\ket{0} = \ket{0},\ Z\ket{1} = -\ket{1} \right)$

(b) <u>Hadamard gate</u>:

$-\boxed{H}- \quad \rightarrow \quad H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

$$H\ket{0} = \ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0} + \ket{1})$$
$$H\ket{1} = \ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0} - \ket{1}).$$

## Page 2

(c) <u>Phase gate</u>: $\;-\boxed{S}-\;\longrightarrow\; S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}\quad\begin{array}{l} S\ket{0} = \ket{0} \\ S\ket{1} = i\ket{1}\end{array}$

$$\ket{0} = \begin{pmatrix}1\\0\end{pmatrix},\;\ket{1}=\begin{pmatrix}0\\1\end{pmatrix}$$

$$S\ket{0} = \begin{pmatrix}1 & 0 \\ 0 & i\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}1\\0\end{pmatrix} = \ket{0}$$

(d) <u>T-gate</u>: $\;-\boxed{T}-\;\longrightarrow\; T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4}\end{pmatrix}$

(e) <u>CNOT / CX gate</u>:    "controlled-X"

[Circuit diagram: top wire is control (•), bottom wire is target with X box; or equivalent diagram with ⊕ symbol on target]

$\circledast\;\;\ket{a,b}\mapsto \ket{a,\,a\oplus b}$

$$\text{CNOT} = \begin{array}{c c} & \begin{array}{cccc} 00 & 01 & 10 & 11 \end{array} \\ \begin{array}{c} 00 \\ 01 \\ 10 \\ 11 \end{array} & \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \end{array}$$

$$\begin{aligned} \ket{0}\ket{0} &\mapsto \ket{0}\ket{0} \\ \ket{0}\ket{1} &\mapsto \ket{0}\ket{1} \\ \ket{1}\ket{0} &\mapsto \ket{1}\,X\ket{0} = \ket{1}\ket{1} \\ \ket{1}\ket{1} &\mapsto \ket{1}\,X\ket{1} = \ket{1}\ket{0} \end{aligned}$$

B/c of linearity, this determines the action on <u>any</u> state!

$$\ket{\gamma} = a\ket{0,0} + b\ket{0,1} + c\ket{1,0} + d\ket{1,1} \;\mapsto\; a\ket{0,0} + b\ket{0,1} + c\ket{1,1} + d\ket{1,0}$$

(f) <u>Controlled Unitary</u>

[Circuit diagram: top wire control (•), bottom wire with U box]

$$\begin{aligned} \ket{0}\ket{0} &\mapsto \ket{0}\ket{0} \\ \ket{0}\ket{1} &\mapsto \ket{0}\ket{1} \\ \ket{1}\ket{0} &\mapsto \ket{1}\,U\ket{0} \\ \ket{1}\ket{1} &\mapsto \ket{1}\,U\ket{1} \end{aligned}$$

$$cU = \begin{pmatrix} \mathbb{1} & 0 \\ 0 & U \end{pmatrix} = \ket{0}\bra{0}\otimes \mathbb{1} + \ket{1}\bra{1}\otimes U.$$

## Page 3

- **Example: Teleportation**

[Diagram: Alice (top) holds $\ket{\psi}_{A'}$ and one half of $\ket{\Phi^+}_{AB}$. She performs a Bell measurement, obtaining classical bits $z, x$ which are sent to Bob. Bob applies $X^x$ then $Z^z$ to his half of the entangled pair, recovering $\ket{\psi}_B$.]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}.$

(✱) **If Alice and Bob are not spatially separated, then the algorithm can be modified as follows:**

[Circuit diagram: Three wires labeled $\ket{\psi}_{A'}$, $\ket{0}_A$, $\ket{0}_B$. The red box on left contains: $H$ on $\ket{0}_A$, then CNOT from $A$ (control) to $B$ (target) — this prepares $\ket{\Phi^+}_{AB}$. Then CNOT with $A'$ as control and $A$ as target, $H$ on $A'$. Blue box on right: CNOT from $A$ to $B$ ($X$ correction), then controlled-$Z$ from $A'$ to $B$, output $\ket{\psi}_B$.]

$\ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0} + \ket{1})$

$$\ket{0}_A\ket{0}_B \mapsto \ket{+}_A\ket{0}_B = \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{0}_B) \mapsto \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B) = \ket{\Phi^+}$$

$$\ket{\psi}_{A'}\ket{0}_A\ket{0}_B \mapsto \ket{\psi}_{A'} \otimes \ket{\Phi^+}_{AB} = \tfrac{1}{\sqrt{2}}\big(\ket{\psi}_{A'}\ket{0}_A\ket{0}_B + \ket{\psi}_{A'}\ket{1}_A\ket{1}_B\big)$$

$\ket{\psi}_{A'} = \alpha\ket{0} + \beta\ket{1}$

$$= \tfrac{1}{\sqrt{2}}\big(\alpha\ket{0}_{A'}\ket{0}_A\ket{0}_B + \beta\ket{1}_{A'}\ket{0}_A\ket{0}_B$$
$$+ \alpha\ket{0}_{A'}\ket{1}_A\ket{1}_B + \beta\ket{1}_{A'}\ket{1}_A\ket{1}_B\big).$$

$$\xmapsto{\text{CNOT}_{A'A}} \tfrac{1}{\sqrt{2}}\big(\alpha\ket{0}_{A'}\ket{0}_A\ket{0}_B + \beta\ket{1}_{A'}\ket{1}_A\ket{0}_B$$
$$+ \alpha\ket{0}_{A'}\ket{1}_A\ket{1}_B + \beta\ket{1}_{A'}\ket{0}_A\ket{1}_B\big).$$

## Page 4

$\downarrow$

$\xmapsto{H_{A'}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{0}_B - \beta \ket{1}_{A'} \ket{1}_A \ket{0}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{1}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big).$

$\xmapsto{\text{CNOT}_{AB}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{0}_B \qquad {\color{blue} Z\ket{1} = -\ket{1}}$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big). \qquad {\color{blue} Z\ket{0} = \ket{0}}$

$\xmapsto{CZ_{A'B}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{1}_B + \beta \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B + \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big).$

$= \frac{1}{2} \Big( \ket{0}_{A'} \ket{0}_A \underbrace{\big( \alpha \ket{0}_B + \beta \ket{1}_B \big)}_{\color{blue}\ket{\psi}}$
$\qquad + \ket{0}_{A'} \ket{1}_A \underbrace{\big( \alpha \ket{0}_B + \beta \ket{1}_B \big)}_{\to \ket{\psi}}$
$\qquad + \ket{1}_{A'} \ket{0}_A \big( \alpha \ket{0}_B + \beta \ket{1}_B \big)$
$\qquad + \ket{1}_{A'} \ket{1}_A \big( \alpha \ket{0}_B + \beta \ket{1}_B \big) \Big)$

$= \frac{1}{2} \big( \ket{0}_{A'} \ket{0}_A + \ket{0}_{A'} \ket{1}_A + \ket{1}_{A'} \ket{0}_A + \ket{1}_{A'} \ket{1}_A \big) \ket{\psi}_B$

$\underline{\underline{= \ket{+}_{A'} \ket{+}_A \ket{\psi}_B}}$

## Page 5

- **Example**: Superdense coding: using entanglement + 1 qubit to transmit 2 classical bits.

[Diagram: Alice and Bob share entangled state $\ket{\Phi^+}_{AB}$. Alice applies $X^x$ then $Z^z$ on her qubit (boxed: "Encoding bits z, x into one qubit."), then sends to Bob who performs a Bell measurement to recover $(x,z)$.]

② **The Swap test**

✻ How do we estimate the inner product of two (unknown) states on a quantum computer?

- **The swap gate**:

[Circuit: $\ket{\psi}$ and $\ket{\phi}$ enter a SWAP box; outputs are $\ket{\phi}$ and $\ket{\psi}$.]

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{1}\ket{0}$$
$$\ket{1}\ket{0} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}\ket{1}$$

As a matrix:

$$\begin{array}{c|cccc} & 00 & 01 & 10 & 11 \\ \hline 00 & 1 & 0 & 0 & 0 \\ 01 & 0 & 0 & 1 & 0 \\ 10 & 0 & 1 & 0 & 0 \\ 11 & 0 & 0 & 0 & 1 \end{array}$$

- **Circuit for the SWAP test**

[Circuit: top wire $\ket{0} - H - \bullet - H - X -$ (measurement); middle wire $\ket{\psi}$ and bottom wire $\ket{\phi}$ enter a SWAP gate controlled by the top qubit.]

## Page 6

$$\ket{\psi_{\text{init}}} = \ket{0}\ket{\psi}\ket{\phi} \xmapsto{H} \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{\psi}\ket{\phi} + \ket{1}\ket{\psi}\ket{\phi}\right)$$

$H\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$

$$\xmapsto{\text{CSWAP}} \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{\psi}\ket{\phi} + \ket{1}\ket{\phi}\ket{\psi}\right)$$

$$\xmapsto{H} \tfrac{1}{2}\left(\ket{+}\ket{\psi}\ket{\phi} + \ket{-}\ket{\phi}\ket{\psi}\right) \qquad \ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\pm\ket{1})$$

$\{\ket{0}\bra{0}, \ket{1}\bra{1}\}.$

$$\ket{\psi_{\text{final}}} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\tfrac{1}{\sqrt{2}}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}) + \ket{1}\tfrac{1}{\sqrt{2}}(\ket{\psi}\ket{\phi}-\ket{\phi}\ket{\psi})\right)$$

$$= \tfrac{1}{2}\ket{0}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}) + \tfrac{1}{2}\ket{1}(\ket{\psi}\ket{\phi}-\ket{\phi}\ket{\psi})$$

Now measure — what is the probability of getting zero? (Recall partial measurements).

$\Pr[0] = \mathrm{Tr}\left[(\ket{0}\bra{0}\otimes \mathbb{1}\otimes \mathbb{1})\ket{\psi_{\text{final}}}\bra{\psi_{\text{final}}}\right].$

$\underbrace{\phantom{xxxxxxxxxx}}_{= \tfrac{1}{2}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi})}$

$$= \tfrac{1}{4}\mathrm{Tr}\left[\underbrace{(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi})(\bra{\psi}\bra{\phi}+\bra{\phi}\bra{\psi})}_{\ket{v}}\right] \qquad \mathrm{Tr}[\ket{v}\bra{v}] = \braket{v|v}$$

$$= \tfrac{1}{4}\left(\bra{\psi}\bra{\phi}+\bra{\phi}\bra{\psi}\right)\left(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}\right)$$

$$= \tfrac{1}{4}\Big(\underbrace{\braket{\psi|\psi}\braket{\phi|\phi}}_{=1} + \underbrace{\braket{\psi|\phi}\braket{\phi|\psi}}_{=|\braket{\psi|\phi}|^2} + \braket{\phi|\psi}\braket{\psi|\phi} + \underbrace{\braket{\phi|\phi}\braket{\psi|\psi}}_{=1}\Big)$$

$$\boxed{\Pr[0] = \tfrac{1}{2}\left(1 + |\braket{\psi|\phi}|^2\right)}$$

$$\Pr[1] = \tfrac{1}{2}\left(1 - |\braket{\psi|\phi}|^2\right)$$

❋ The probabilities contain the inner product!
   So how do we extract the value of the inner product?
   <u>We run the algorithm many times!</u>

- Each time we get outcome "0" → record $x_i = 1$  ⎫  ❋ This defines a <u>random</u>
- Each time we get outcome "1" → record $x_i = -1$ ⎭     <u>variable</u> $X$:
- Do this $N$ times, then take the <u>sample</u>
  <u>mean / average</u>: $\hat{x}_N = \tfrac{1}{N}\sum_{i=1}^{N} x_i$

$\Pr[X = \pm 1] = \tfrac{1}{2}\left(1 \pm |\braket{\psi|\phi}|^2\right).$

## Page 7

This defines a random variable $\hat{X}_N = \frac{1}{N}\sum_{i=1}^{N} X_i$. $\hat{X}_N$ is an <u>unbiased estimator</u> of $X$:

$$\mathbb{E}[\hat{X}_N] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X_i] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X] = \mathbb{E}[X].$$

$\qquad\qquad\quad = \mathbb{E}[X] \;\forall i$, b/c all samples are independent and identical.

$$\mathbb{E}[X] = \sum_x x\, \Pr[X=x]$$

$$\mathbb{E}[X] = (+1)\cdot \Pr[X=+1] + (-1)\cdot \Pr[X=-1] = \tfrac{1}{2}\left(1 + |\braket{\gamma|\phi}|^2\right) - \tfrac{1}{2}\left(1 - |\braket{\gamma|\phi}|^2\right) = |\braket{\gamma|\phi}|^2$$

- As $N \to \infty$, $\hat{X}_N \to \mathbb{E}[X] = |\braket{\gamma|\phi}|^2$  (<u>law of large numbers</u>).

⊛ So the sample average approaches the true (unknown) inner product!

```python
[89]: import numpy as np
      import matplotlib.pyplot as plt

      inner_product=0.8
      # Parameters
      p = (1/2)*(1-inner_product)        # probability of original "1"
      n_samples = 20000

      # Step 1: sample Bernoulli (0 or 1)
      samples = np.random.binomial(1, p, size=n_samples)

      # Step 2: map to +1 / -1
      mapped = 1 - 2 * samples   # 0 -> 1, 1 -> -1

      # Step 3: running average
      running_avg = np.cumsum(mapped) / np.arange(1, n_samples + 1)

      # True mean of the new variable
      true_mean = 1 - 2*p

      # Plot
      plt.figure()
      plt.plot(running_avg)#, label="Running average")
      plt.axhline(true_mean, linestyle='--', label="True inner product")

      plt.xlabel("Number of samples")
      plt.ylabel("Sample average")
      plt.title("Inner product estimation (swap test)")
      plt.legend()
      plt.show()
```

[Plot titled "Inner product estimation (swap test)". X-axis: "Number of samples" from 0 to 20000. Y-axis: "Sample average" from 0.60 to 1.00. A blue curve representing the running sample average starts with high variance near the origin (oscillating between ~0.60 and ~1.00) and quickly converges to ~0.80. A dashed horizontal line at 0.80 labeled "True inner product".]
