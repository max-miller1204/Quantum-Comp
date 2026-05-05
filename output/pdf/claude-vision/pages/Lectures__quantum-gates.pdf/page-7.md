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
