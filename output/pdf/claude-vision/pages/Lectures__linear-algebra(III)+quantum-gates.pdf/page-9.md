$$\rho = \frac{1}{2}\begin{pmatrix} 1+r_z & r_x - i r_y \\ r_x + i r_y & 1 - r_z \end{pmatrix} \implies \lambda_\pm = \frac{1}{2}\left(1 \pm \sqrt{r_x^2 + r_y^2 + r_z^2}\right) \geq 0.$$

Need $\lambda_- \geq 0 \implies \frac{1}{2}\left(1 - \sqrt{r_x^2 + r_y^2 + r_z^2}\right) \geq 0 \implies \boxed{r_x^2 + r_y^2 + r_z^2 \leq 1}$

$$\vec{r} = (r_x, r_y, r_z) \in \mathbb{R}^3 \text{ inside the unit sphere!}$$

Observe: $\|\rho\|_2^2 = \text{Tr}[\rho^2] = \frac{1}{2}\left(1 + r_x^2 + r_y^2 + r_z^2\right) \leq 1$
$$\underbrace{\phantom{r_x^2+r_y^2+r_z^2}}_{\leq 1}$$

$\rho = \frac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)$

[Bloch sphere diagram: z-axis up with $\ket{0}$ at top, $\ket{1}$ at bottom; x-axis with $\ket{+}$ and $\ket{-}$ marked; y-axis with $\ket{+i}$ and $\ket{-i}$ marked]

For a pure state $\rho = \ket{\psi}\bra{\psi}$, $\rho^2 = \ket{\psi}\underbrace{\braket{\psi|\psi}}_{=1}\bra{\psi} = \ket{\psi}\bra{\psi} \implies \text{Tr}[\rho^2] = 1$
$\rho^2 = \rho$

$\implies r_x^2 + r_y^2 + r_z^2 = 1 \implies$ pure states are on the surface of the unit sphere!

✻ We call $\text{Tr}[\rho^2]$ the **purity** of $\rho \to \rho$ pure if and only if $\text{Tr}[\rho^2] = 1$.

✻ <u>Origin</u>, $\vec{r} = (0,0,0)$ contains the **maximally-mixed state**: $\frac{\mathbb{1}}{2}$.

$\frac{\mathbb{1}}{2} = \frac{1}{2}(\ket{0}\bra{0} + \ket{1}\bra{1})$

✻ <u>Points on the X-axis</u>: $\vec{r} = (\pm 1, 0, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm X) = \ket{\pm}\bra{\pm}$, $\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$$= \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ \pm 1 \end{pmatrix}$$

These are eigenstates of $X$! $X\ket{\pm} = \pm \ket{\pm}$.

✻ <u>Points on the Y-axis</u>: $\vec{r} = (0, \pm 1, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm Y) = \ket{\pm i}\bra{\pm i}$,
$$\ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1}) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ \pm i \end{pmatrix}$$

These are eigenstates of $Y$! $Y\ket{\pm i} = \pm \ket{\pm i}$.

✻ <u>Points on the Z-axis</u>: $\vec{r} = (0, 0, \pm 1) \to \rho = \frac{1}{2}(\mathbb{1} \pm Z) \begin{matrix} \xrightarrow{(+)} \ket{0}\bra{0} \\ \xrightarrow{(-)} \ket{1}\bra{1} \end{matrix}$  $\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$
$\ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

These are eigenstates of $Z$! $Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$.
