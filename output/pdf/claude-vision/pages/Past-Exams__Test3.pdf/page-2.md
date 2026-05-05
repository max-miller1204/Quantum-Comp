2. (a) Calculate both $\text{Tr}_A[M_{AB}]$ and $\text{Tr}_B[M_{AB}]$ for the following two-qubit matrix:

$$M_{AB} = \begin{pmatrix} 0 & 5+3i & 1-2i & 2+i \\ -3+2i & 1 & -i & 1+i \\ 2 & -2i & 3+2i & 0 \\ 1 & 5i & -3+2i & 1 \end{pmatrix} \tag{2}$$

(b) Let $\Phi^-_{AB} = \ket{\Phi^-}\bra{\Phi^-}_{AB}$. Prove that $\text{Tr}_B[\Phi^-_{AB}] = \frac{1}{2}\mathbb{1}_A$ and $\text{Tr}_A[\Phi^-_{AB}] = \frac{1}{2}\mathbb{1}_B$.

(c) Consider the three-qubit state vector $\ket{\psi_1}_{ABC} = \frac{1}{\sqrt{2}}(\ket{0,0,0}_{ABC} + \ket{1,1,1}_{ABC})$. Calculate $\text{Tr}_A[\ket{\psi_1}\bra{\psi_1}_{ABC}]$.

---

a) $\text{Tr}_A[M_{AB}] = \begin{pmatrix} \boxed{0} & \boxed{5+3i} & 1-2i & 2+i \\ -3+2i & \boxed{1} & -i & 1+i \\ 2 & -2i & \boxed{3+2i} & \boxed{0} \\ 1 & 5i & -3+2i & \boxed{1} \end{pmatrix} = \begin{pmatrix} 0+3+2i & 5+3i+0 \\ -3+2i + (-3+2i) & 1+1 \end{pmatrix}$

$$\text{Tr}_A[M_{AB}] = \begin{pmatrix} 3+2i & 5+3i \\ -6+4i & 2 \end{pmatrix}$$

$\text{Tr}_B[M_{AB}] = \begin{pmatrix} 0+1 & (1-2i)+(1+i) \\ 2+5i & (3+2i)+1 \end{pmatrix} = \begin{pmatrix} 1 & 2-i \\ 2+5i & 4+2i \end{pmatrix}$

b) $\Phi^- = \frac{1}{\sqrt{2}}(\ket{00} - \ket{11})$

$\ket{\Phi^-}\bra{\Phi^-}_{AB} = \frac{1}{2}(\ket{00} - \ket{11})^2$  → ↗ $(\ket{00}-\ket{11})(\ket{00}-\ket{11})$

$\frac{1}{2}\big[\ket{00}\ket{00} - \ket{00}\ket{11} - \ket{11}\ket{00} + \ket{11}\ket{11}\big]$ ✗

$\text{Tr}_B[\Phi^-_{AB}] = (\quad)_A \,\text{Tr}[\quad]$

c)

3
