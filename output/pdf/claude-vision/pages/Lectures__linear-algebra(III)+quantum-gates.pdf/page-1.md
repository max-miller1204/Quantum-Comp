# ① Quantum States

[Left diagram: vertical line segment with two dots labeled 0 (top) and 1 (bottom)]

**Bit**
0 or 1;
or probabilistic mixture

[Right diagram: Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ in front, $\ket{-}$ in back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$$
$$\alpha, \beta \in \mathbb{C},$$
$$|\alpha|^2 + |\beta|^2 = 1$$

$$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$$
$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

---

✱ States of live on the surface of the **Bloch sphere**. — they are described by 2-dimensional **state vectors**.

$\{\ket{k}\}_{k=0}^{d-1}$    $\{\ket{e_k}\}_{k=1}^{d}$

$$\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad \alpha,\beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1. \qquad \ket{\psi} = \alpha\ket{0} + \beta\ket{1}, \;\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

(States **inside** the sphere are also possible — they are described by **density matrices**. We will see this today!)

---

② **Matrices** (aka "linear operators")

$$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \ket{0}\bra{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$$

→ column indices

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad a,b,c,d \in \mathbb{C}. \quad \rightarrow \quad M = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}$$

[row/column labels: rows indexed 0,1; columns indexed 0,1]

↗ row indices

$$a = \bra{0}M\ket{0}, \quad b = \bra{0}M\ket{1}, \quad c = \bra{1}M\ket{0},$$
$$d = \bra{1}M\ket{1}.$$

– General $d\times d$ matrix: $\displaystyle M = \sum_{i,j=0}^{d-1} m_{ij}\ket{i}\bra{j}, \quad m_{ij} = \bra{i}M\ket{j}$

→ matrix elements.
