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
