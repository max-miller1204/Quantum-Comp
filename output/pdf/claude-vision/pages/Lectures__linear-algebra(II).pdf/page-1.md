## ① Recap

[Left: Bit diagram — vertical line with two dots labeled 0 (top) and 1 (bottom)]

**Bit**
0 or 1;
or probabilistic mixture

[Right: Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ on front, $\ket{-}$ on back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$
$\alpha, \beta \in \mathbb{C},$
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

---

✱ States of live on the surface of the **Bloch sphere**. — they are described by 2-dimensional **state vectors**.

$$\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad \alpha, \beta \in \mathbb{C}, \quad \underbrace{|\alpha|^2}_{\Pr[0]} + \underbrace{|\beta|^2}_{\Pr[1]} = 1. \quad \longrightarrow \quad \ket{\psi} = \alpha\ket{0} + \beta\ket{1}$$

$$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

(States **inside** the sphere are also possible — they are described by **density matrices**. We will see this later...)

## ② Complex Vector Spaces

$$\ket{v} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \longrightarrow \ket{v} = \sum_{k=1}^{d} a_k \ket{e_k}, \quad \ket{e_1} = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \ket{e_2} = \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, \ldots, \ket{e_d} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}$$

[Note in red: "Complex numbers!" pointing to $a_k$]

$$\bra{v} = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix} \longrightarrow \bra{v} = \sum_{k=1}^{d} \bar{a}_k \bra{e_k}.$$

$$\ket{v} = \sum_{k=0}^{d-1} a_k \ket{k}, \quad \ket{u} = \sum_{k=0}^{d-1} b_k \ket{k}$$

$$\braket{v|u} = \left( \sum_{k=0}^{d-1} \bar{a}_k \bra{k} \right) \left( \sum_{k'=0}^{d-1} b_{k'} \ket{k'} \right)$$
