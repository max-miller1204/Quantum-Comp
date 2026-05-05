# Past-Exams__Test4.pdf

## Page 1

1. Does $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ represent a valid quantum gate? State why or why not. What is $U\ket{0}$ and $U\ket{1}$?

Valid: $U^\dagger U = I$

$$U^\dagger = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$$

$$U^\dagger U = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1+1 & i-i \\ -i+i & 1+1 \end{pmatrix}$$

$$= \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$$

Yes, it's a valid quantum gate.

$$U\ket{0} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix} \checkmark$$

[dimensions noted: $2\times 2$, $2\times 1$]

$$U\ket{1} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} i \\ 1 \end{pmatrix}$$

2

## Page 2

2. Draw the quantum circuit for the quantum teleportation protocol. State the definition of every gate and/or measurement you draw in the circuit.

[Hand-drawn quantum circuit with two horizontal wires:
- Top wire: passes through an H (Hadamard) gate, then through a measurement box (labeled with an "X"-like symbol indicating measurement)
- Bottom wire: connected to the top wire by a vertical line at a control point (controlled-Swap), then passes through an H (Hadamard) gate, then through a measurement box
- Arrows label the gates: "Hadamard" pointing to the first H gate, "a measurement" pointing to the first measurement box, "controlled-Swap" pointing to the vertical connection, "Hadamard" pointing to the second H gate]

−10

3

## Page 3

3. Consider the following two state vectors, $\ket{v_1} = \frac{\sqrt{3}}{2}\ket{0} + \frac{i}{2}\ket{1}$ and $\ket{v_2} = \frac{i}{2}\ket{0} + \frac{\sqrt{3}}{2}\ket{1}$.

   (a) Prove that $\ket{v_1}$ and $\ket{v_2}$ are orthonormal.
   (b) Show that $\ket{v_1}\bra{v_1} + \ket{v_2}\bra{v_2} = \mathbb{1}$.
   (c) Consider a qubit in the state given by $\ket{u} = \frac{1}{2}\ket{0} - \frac{\sqrt{3}}{2}\ket{1}$. If we measure this state with respect to the measurement $\{\ket{v_1}\bra{v_1}, \ket{v_2}\bra{v_2}\}$, then what are the possible outcomes and their associated probabilities?

---

orthonormal = orthogonal & normal

a) $\braket{v_1|v_2} = \left| \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{3}}{2} \braket{0|1} + \frac{i}{2} \cdot \frac{i}{2} \braket{1|0} \right| = \frac{3}{4} + \frac{i^2}{4} = 1\;?$

[marked $-5$ in red]

$\braket{v_1|v_1} = \left| \left(\frac{\sqrt{3}}{2}\right)^2 + \left(\frac{i}{2}\right)^2 \right| = \frac{3}{4} + \frac{1}{4} = \frac{4}{4} = 1$

$\braket{v_2|v_2} = \left| \left(\frac{i}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2 \right| = \frac{1}{4} + \frac{3}{4} = \frac{4}{4} = 1$

b) $\ket{v_1}\bra{v_1} = \begin{pmatrix} \frac{\sqrt{3}}{2} \\ \frac{i}{2} \end{pmatrix} \begin{pmatrix} \frac{\sqrt{3}}{2} & -\frac{i}{2} \end{pmatrix} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix}$

[marked $-3$ in blue circle, ✓]

$\ket{v_2}\bra{v_2} = \begin{pmatrix} \frac{i}{2} \\ \frac{\sqrt{3}}{2} \end{pmatrix} \begin{pmatrix} -\frac{i}{2} & \frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix}$

$\ket{v_1}\bra{v_1} + \ket{v_2}\bra{v_2} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix} + \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$

c) $\ket{v_1}\bra{v_1}\ket{u} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix} \begin{pmatrix} \frac{1}{2} \\ -\frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{3}{8} \\ -\frac{\sqrt{3}}{8} \end{pmatrix}$

[marked $-2$]

$\ket{v_2}\bra{v_2}\ket{u} = \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix} \begin{pmatrix} \frac{1}{2} \\ -\frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{1}{8} \\ -\frac{3\sqrt{3}}{8} \end{pmatrix}$

## Page 4

4. Consider a probability distribution with two outcomes defined as follows:

$$\Pr[0] = \frac{1}{2}(1-\alpha), \quad \Pr[1] = \frac{1}{2}(1+\alpha).$$

Suppose that the value of $\alpha$ is unknown. Describe a real-life procedure, based on repeatedly sampling from this probability distribution, that can be used to estimate the value of $\alpha$.

let $n_0$ be $a$ is $0$

$n_1$ be $a$ is $1$

$\hat{\alpha} = \Pr(0) - \Pr(1) \qquad \hat{p} = \frac{1}{2}(1-\alpha)$

$$\boxed{\hat{\alpha} = 1 - 2\left(\frac{n_0}{N}\right)} \qquad 2\hat{p} = 1 - \alpha$$

$$\hat{\alpha} = 1 - 2\hat{p}$$

$\hat{p} = \dfrac{n_0}{N}$

$\angle 10$

5

## Page 5

5. Let us use the following notation for the swap gate:

[Swap gate symbol: two X's connected by a vertical line]

Show that the swap gate can be written in terms of three CNOT gates as follows:

[Circuit equation: SWAP = CNOT (control top, target bottom) · CNOT (control bottom, target top) · CNOT (control top, target bottom)]

CNOT:

$\ket{00} \to \ket{00}$

$\ket{01} \to \ket{01}$

$\ket{10} \to \ket{11}$

$\ket{11} \to \ket{10}$

Swap:

$\ket{00} \to \ket{00}$

$\ket{01} \to \ket{10}$

$\ket{10} \to \ket{01}$

$\ket{11} \to \ket{11}$

for $\ket{00}$:

$\ket{00} \xrightarrow{\text{CNOT 1}} \ket{00} \xrightarrow{\text{CNOT 2}} \ket{00} \xrightarrow{\text{CNOT 3}} \ket{00}$

for $\ket{01}$:

$\ket{01} \xrightarrow{\text{CNOT 1}} \ket{01} \xrightarrow{\text{CNOT 2}} \ket{11} \xrightarrow{\text{CNOT 3}} \ket{10}$

for $\ket{10}$:

$\ket{10} \xrightarrow{\text{CNOT 1}} \ket{11} \xrightarrow{\text{CNOT 2}} \ket{01} \xrightarrow{\text{CNOT 3}} \ket{01}$ ✓

for $\ket{11}$:

$\ket{11} \xrightarrow{\text{CNOT 1}} \ket{10} \xrightarrow{\text{CNOT 2}} \ket{10} \xrightarrow{\text{CNOT 3}} \ket{11}$

6

## Page 6

6. Consider the circuit below. Prove that this circuit can be used to calculate the imaginary part of the inner product $\braket{\psi|U|\psi}$, namely, $\operatorname{Im}(\braket{\psi|U|\psi})$, where $U$ is an arbitrary single-qubit gate and $\ket{\psi}$ is an arbitrary single-qubit state vector. Here, $H$ denotes the Hadamard gate and $S$ denotes the phase gate.

[Circuit diagram: top wire starts with $\ket{0}$, passes through $H$, then $S^\dagger$, then a control dot, then $H$, then a measurement. Bottom wire starts with $\ket{\psi}$, passes through $U$ (controlled by top wire).]

H on $\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})\otimes\ket{\psi}$

$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

$\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\otimes\ket{0} + \ket{1}\otimes\ket{1})\otimes\ket{\psi}$

$S^\dagger$ on $H\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\otimes\ket{0} + i\ket{1}\otimes\ket{1})\otimes\ket{\psi}$

$\ket{00} \rightarrow \ket{00}$

$\ket{01} \rightarrow \ket{01}$

$\ket{10} \rightarrow \ket{10}$ +

$\ket{11} \rightarrow i\ket{11}$

$\;$ [circled: $-6$]

ctrl-$U$ on $\ket{\psi}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\ket{0} + i\ket{1}\ket{1})\otimes U\ket{\psi}$

H on $\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}\cdot\frac{1}{\sqrt{2}}(\ket{0}\ket{0}\otimes\ket{0} + i\ket{1}\ket{1}\otimes\ket{1})\otimes U\ket{\psi}$

by basis $\{\ket{0},\ket{1}\}$

$= \frac{1}{2}\left(\ket{0}\otimes(\ket{00}U\ket{\psi}) + \ket{1}\otimes(U_i\ket{11}\ket{\psi})\right)$

$\Pr_1 = $ squared $= \frac{1}{4}\left( \quad \right)^2$

$\Pr_2 = \frac{1}{4}\left(\text{same as this but w/ minus sign}\right)$
