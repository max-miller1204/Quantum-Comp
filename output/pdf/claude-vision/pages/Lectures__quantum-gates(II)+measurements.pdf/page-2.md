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
