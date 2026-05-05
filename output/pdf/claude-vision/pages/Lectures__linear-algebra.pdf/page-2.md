## ② Complex Numbers

- A complex number is a number $z \in \mathbb{C}$ (← Set of complex numbers) with a <u>real part</u> and <u>imaginary part</u>

$$z = x + yi, \quad i^2 = -1 \qquad \text{Example: } z = 3 + 2i$$

where $x$ is the **Real part** and $y$ is the **Imaginary part**.

✱ Initially conceived in the 1500s for solving polynomial equations.

- Can be represented in a 2D plane. (the "complex plane").

[Diagram: Complex plane with horizontal axis labeled $\text{Re}(z)$ ← real axis, vertical axis labeled $\text{Im}(z)$ ← Imaginary axis. A vector from origin to point $z = x + iy$, with horizontal component $x$ and vertical component $y$.]

Example: $z = 3 + 2i$

$\text{Re}(z) = 3, \quad \text{Im}(z) = 2.$

✱ We can represent this as a vector: 
$$\vec{v} = \begin{pmatrix} x \\ y \end{pmatrix}.$$

- <u>Complex conjugate</u>: flip the sign of the imaginary part.

$$z = x + yi \;\Rightarrow\; \bar{z} = z^* = x - yi \qquad \text{Example: } z = 3 + 2i \;\Rightarrow\; \bar{z} = 3 - 2i.$$

- <u>Modulus (or magnitude)</u>: 
$$|z|^2 = z \cdot \bar{z} = (x + yi)(x - yi)$$

$$= x^2 - xyi + yxi + y^2 \underbrace{(i)(-i)}_{= +1} \qquad i^2 = -1$$

$$= x^2 + y^2$$

$$\Rightarrow |z| = \sqrt{x^2 + y^2}$$
