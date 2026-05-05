They are Hermitian: $X^\dagger = X$, $Y^\dagger = Y$, $Z^\dagger = Z$.

They are orthogonal: $\langle X, Y \rangle = 0$, $\langle X, Z \rangle = 0$, $\langle Z, Y \rangle = 0$.

$\{\mathbb{1}, X, Y, Z\}$ forms orthogonal basis for $L(\mathbb{C}^2)$!

$$\text{Tr}(X^\dagger Y) = \text{Tr}\left[\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\right] = \text{Tr}\left[\begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}\right] = 0$$

$\Rightarrow$ Any $M \in L(\mathbb{C}^2)$ can be written as $M = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$.

$\quad c_0, c_1, c_2, c_3 \in \mathbb{C}$.

## ③ Quantum States as Density Matrices

– We have seen state vectors:

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}, \quad \alpha,\beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1.$$

[Bloch sphere diagram with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ at front, $\ket{-}$ at back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$,
$\alpha, \beta \in \mathbb{C}$,
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

Qubit
$\ket{0}$ or $\ket{1}$;
or *superposition*

– Consider the matrix $\rho = \ket{\psi}\bra{\psi}$.
It has the following properties:

**(1)** $\rho = \rho^\dagger$ (Hermitian).

$\ket{\psi}\bra{\psi} = (\alpha\ket{0} + \beta\ket{1})(\bar{\alpha}\bra{0} + \bar{\beta}\bra{1})$
$= |\alpha|^2 \ket{0}\bra{0} + \alpha\bar{\beta}\ket{0}\bra{1} + \beta\bar{\alpha}\ket{1}\bra{0} + |\beta|^2 \ket{1}\bra{1}$

$(M_1 + M_2)^\dagger = M_1^\dagger + M_2^\dagger$

$(\ket{\psi}\bra{\psi})^\dagger = |\alpha|^2 (\ket{0}\bra{0})^\dagger + \overline{\alpha\bar{\beta}}(\ket{0}\bra{1})^\dagger + \overline{\beta\bar{\alpha}}(\ket{1}\bra{0})^\dagger + |\beta|^2 (\ket{1}\bra{1})^\dagger$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\downarrow \quad\quad\quad\quad\quad\quad\downarrow$
$\quad\quad\quad\quad\quad = \bar{\alpha}\cdot\bar{\bar{\beta}} = \bar{\alpha}\beta \quad = \bar{\beta}\cdot\bar{\bar{\alpha}} = \bar{\beta}\alpha$

$\left(\overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2\right)$
$\bar{\bar{z}} = z$

$= |\alpha|^2 \ket{0}\bra{0} + \bar{\alpha}\beta \ket{1}\bra{0} + \bar{\beta}\alpha\ket{0}\bra{1} + |\beta|^2 \ket{1}\bra{1}$

$= \ket{\psi}\bra{\psi}\ \checkmark$
