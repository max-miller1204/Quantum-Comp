⊛ This is just the **length** of the vector in the complex plane!

also called **norm**: $\| \ket{v} \| = \sqrt{x^2 + y^2}$.

- <u>Polar form</u>:

[Diagram: complex plane with horizontal axis labeled Re(z) ← real axis, vertical axis labeled Im(z) ← Imaginary axis. A purple vector from origin to point $z = x+iy$, with length $r$ and angle $\theta$ from real axis. Dotted lines drop to $x$ on real axis and $y$ on imaginary axis.]

$$z = re^{i\theta}, \quad r = \sqrt{x^2+y^2} = |z|.$$
$$\theta = \tan^{-1}\left(\frac{y}{x}\right)$$

⊛ $e^{i\theta} = \sum_{k=0}^{\infty} \frac{1}{k!}(i\theta)^k = \cos(\theta) + i\sin(\theta).$

$$\Rightarrow x = \underset{=\text{Re}(z)}{r\cos(\theta)}, \quad y = \underset{=\text{Im}(z)}{r\sin(\theta)}.$$

<u>Example</u>: $z = 3 + 2i \Rightarrow r = \sqrt{3^2 + 2^2} = \sqrt{9+4} = \sqrt{13}, \quad \theta = \tan^{-1}\left(\frac{2}{3}\right) \approx 33.69°.$

- <u>Addition and multiplication</u>:

$z_1 = x_1 + y_1 i, \quad z_2 = x_2 + y_2 i \;\rightarrow\; z_1 + z_2 = (x_1 + x_2) + (y_1 + y_2)i$

$z_1 + z_2 = x_1 + y_1 i + x_2 + y_2 i$
$\quad\;\;\, = (x_1 + x_2) + (y_1 + y_2)i$

$\begin{pmatrix} \text{Re}(z_1 + z_2) = \text{Re}(z_1) + \text{Re}(z_2) \\ \text{Im}(z_1 + z_2) = \text{Im}(z_1) + \text{Im}(z_2). \end{pmatrix}$

$z_1 \cdot z_2 = (x_1 + y_1 i)\cdot(x_2 + y_2 i) = x_1 x_2 + x_1 y_2 i + y_1 x_2 i + y_1 y_2 \underbrace{(i \cdot i)}_{=-1}$

$\qquad\quad = (x_1 x_2 - y_1 y_2) + i(x_1 y_2 + y_1 x_2).$

$z_1 = r_1 e^{i\theta_1}, \quad z_2 = r_2 e^{i\theta_2} \;\Rightarrow\; z_1 z_2 = r_1 \cdot r_2\, e^{i\theta_1} e^{i\theta_2} = r_1 \cdot r_2\, e^{i(\theta_1 + \theta_2)}$
