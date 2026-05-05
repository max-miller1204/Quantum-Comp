# Lectures__linear-algebra.pdf

## Page 1

# 1. What is a qubit?

[Diagram: A vertical line segment labeled "Bit" with 0 at top and 1 at bottom, representing classical bit values or probabilistic mixture in between.]

**Bit**
0 or 1;
or probabilistic mixture

[Diagram: Bloch sphere labeled "Qubit" with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ at front, $\ket{-}$ at back, $\ket{+i}$ on right, $\ket{-i}$ on left.]

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$$
$$\alpha, \beta \in \mathbb{C},$$
$$|\alpha|^2 + |\beta|^2 = 1$$

$$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$$
$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

---

✱ A <u>bit</u> takes a value either 0 or 1 — or any point in between

→ Probabilistic bit:
- Value is 0 with probability $p_0$.
- Value is 1 with probability $p_1$.

✱ $p_0 + p_1 = 1.$

→ So the <u>state</u> of a (probabilistic) bit is just a number b/w 0 and 1!

✱ The <u>state</u> of a qubit is a <u>point on the sphere</u> ← **Bloch sphere** — or any point inside the sphere. (We will understand the reasons for this later...).

→ We have to describe this using <u>vectors</u> of <u>complex numbers</u>.

→ $\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$, $\alpha, \beta \in \mathbb{C}$ (complex numbers).

&nbsp;&nbsp;&nbsp;&nbsp;↑
&nbsp;"ket"

$|\alpha|^2 = \alpha \cdot \bar{\alpha}$ : probability of 0
$|\beta|^2 = \beta \cdot \bar{\beta}$ : probability of 1.
&nbsp;&nbsp;&nbsp;&nbsp;↳ complex conjugate.

✱ In quantum mechanics, probabilities are "generated" by complex numbers.

## Page 2

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

## Page 3

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

## Page 4

## ③ Complex Vector Spaces

- Recall 2D and 3D vectors from linear algebra

[Diagram: 2D coordinate system with x and y axes, showing a vector from origin to point $(a, b)$ with dotted lines indicating components $a$ on x-axis and $b$ on y-axis]

$$\vec{v} = \begin{pmatrix} a \\ b \end{pmatrix}, \quad a, b \in \mathbb{R} \quad \text{\textcolor{red}{$\rightarrow$ real numbers}}$$

- We write $\vec{v} \in \mathbb{R}^2$ $\rightarrow$ all 2D vectors of real numbers.

\textcolor{red}{(Note: this is basically the same as the complex plane!)}

[Diagram: 3D coordinate system with x, y, z axes, showing a vector from origin to point $(a, b, c)$ with dotted lines indicating components]

- In 3D, vectors have three components.

$$\vec{v} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}; \quad a, b, c \in \mathbb{R}.$$

- We write $\underline{\vec{v} \in \mathbb{R}^3}$.

- For any dimension $d \in \{2, 3, \ldots\}$, we have $\vec{v} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix}$, $a_k \in \mathbb{R}$.

and we write $\vec{v} \in \mathbb{R}^d$. The $\underline{\text{norm}}$ (magnitude) of $\vec{v}$ is $\|\vec{v}\| = \sqrt{a_1^2 + a_2^2 + \cdots + a_d^2}$.

- We add (and subtract) vectors component-wise

$$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \quad \vec{v}_2 = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} \implies \vec{v}_1 + \vec{v}_2 = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ \vdots \\ a_d + b_d \end{pmatrix}.$$

## Page 5

- We can take the <u>dot product</u> of two vectors.

$$\vec{V}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \qquad \vec{V}_2 = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} \implies \vec{V}_1 \cdot \vec{V}_2 = a_1 b_1 + a_2 b_2 + \cdots + a_d b_d = \sum_{k=1}^{d} a_k b_k$$

⊛ <u>Observe</u>: $\vec{V}_1 \cdot \vec{V}_1 = a_1^2 + a_2^2 + \cdots + a_d^2 = \|\vec{V}\|^2.$

Geometric interpretation in 2D:

[Diagram: 2D coordinate axes with $x$ and $y$ labeled. Two vectors $\vec{V}_1$ and $\vec{V}_2$ drawn from the origin, with angle $\theta$ between them.]

$$\vec{V}_1 \cdot \vec{V}_2 = \|\vec{V}_1\| \cdot \|\vec{V}_2\| \cdot \cos\theta$$

⊛ So the dot product tells us how much the two vectors overlap.

- <u>Complex vectors</u> are similar!

$$\vec{V} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \longrightarrow \text{but now each } \underline{\underline{a_k \in \mathbb{C}}}! \quad \text{[Each } a_k \text{ is a complex number.]}$$

with $a_k = x_k + y_k i$

⊛ <u>We write $\vec{V} \in \mathbb{C}^d$.</u>

- Addition as before: $\vec{V}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \quad \vec{V}_2 = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} \implies \vec{V}_1 + \vec{V}_2 = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ \vdots \\ a_d + b_d \end{pmatrix}.$

- But dot product changes! And we call it "<u>inner product</u>" instead:

$$\vec{V}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \quad \vec{V}_2 = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} \implies \langle \vec{V}_1, \vec{V}_2 \rangle = \bar{a}_1 b_1 + \bar{a}_2 b_2 + \cdots + \bar{a}_d b_d.$$

## Page 6

- Conjugate transpose of a vector:

$$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \rightarrow \vec{v}_1^\dagger = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix}$$

$$\vec{v}^T = \begin{pmatrix} a_1 & a_2 & \cdots & a_d \end{pmatrix}$$

✱ Observe: $\vec{v}_1^\dagger \vec{v}_2 = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix} \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} = \bar{a}_1 b_1 + \bar{a}_2 b_2 + \cdots + \bar{a}_d b_d = \langle \vec{v}_1, \vec{v}_2 \rangle.$

We will use this fact all the time in quantum computing!

✱ Norm of a complex vector is $\|\vec{v}\| = \sqrt{|a_1|^2 + |a_2|^2 + \cdots + |a_d|^2} = \sqrt{\langle \vec{v}, \vec{v} \rangle}$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad \underbrace{\phantom{xxx}}_{a_i \cdot \bar{a}_i}$

— <u>Basis</u> of a vector space.

- We can write a vector as

$$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} = \begin{pmatrix} a_1 \\ 0 \\ \vdots \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ a_2 \\ \vdots \\ 0 \end{pmatrix} + \cdots + \begin{pmatrix} 0 \\ 0 \\ \vdots \\ a_d \end{pmatrix}$$

$$= a_1 \underbrace{\begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}}_{\vec{e}_1} + a_2 \underbrace{\begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}}_{\vec{e}_2} + \cdots + a_d \underbrace{\begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}}_{\vec{e}_d}$$

$$= \sum_{k=1}^{d} a_k \vec{e}_k \quad \longrightarrow \text{The "standard" basis}$$

✱ $\{\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_d\}$ are <u>basis vectors</u>. Every vector can be written as a <u>linear combination</u> of these basis vectors.

## Page 7

✺ These basis vectors are __orthonormal__

Two parts to this term:

1. __Orthogonal__: $\langle \vec{e}_i, \vec{e}_j \rangle = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$

   $\equiv \delta_{i,j} \rightarrow$ "Kronecker delta"

2. __Normalised__: $\|\vec{e}_k\| = \sqrt{\langle \vec{e}_k, \vec{e}_k \rangle} = 1$ for all $k$.

[Right side, in blue:]
$d = 3 \rightarrow \vec{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix},\ \vec{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$

$\vec{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

$\langle \vec{e}_1, \vec{e}_2 \rangle = (1\ 0\ 0) \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = 0$

$\langle \vec{e}_1, \vec{e}_1 \rangle = (1\ 0\ 0) \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = 1$

✺ We can extract the components of a vector in this basis using the inner product:

$$\langle \vec{e}_k, \vec{v} \rangle = \left\langle \vec{e}_k, \sum_{\ell=1}^{d} a_\ell \vec{e}_\ell \right\rangle = \sum_{\ell=1}^{d} \underbrace{\langle \vec{e}_k, \vec{e}_\ell \rangle}_{\delta_{k,\ell}} a_\ell = a_k.$$

[Right side, in blue:]
$\langle \vec{e}_1, a_1 \vec{e}_1 + a_2 \vec{e}_2 \rangle$
$= a_1 \underbrace{\langle \vec{e}_1, \vec{e}_1 \rangle}_{=1} + a_2 \underbrace{\langle \vec{e}_1, \vec{e}_2 \rangle}_{=0}$
$= a_1$

— __Bra-ket notation__: very important, used throughout quantum information and quantum computing.

$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \rightarrow \vec{v}_1^\dagger = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix}$

[Blue annotations:]
$|v_1\rangle$, $|v_1\rangle = \sum_{k=1}^{d} a_k |e_k\rangle$, $|e_1\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$

[Red annotations:]
relabel as $|v_1\rangle \rightarrow$ call it a "ket".

relabel as $\langle v_1 | \rightarrow$ call it "bra"

- Then the inner product is $\langle \vec{v}_1, \vec{v}_2 \rangle = \vec{v}_1^\dagger \vec{v}_2 = \langle v_1 | v_2 \rangle$

  [Red:] "bra-ket"

[Bottom right:] $\delta_{k,k'}$

## Page 8

- We write the basis vectors as $\ket{e_k}$

$$\rightarrow \ket{v} = \sum_{k=1}^{d} a_k \ket{e_k} \quad \rightarrow \quad \bra{v} = \sum_{k=1}^{d} \bar{a}_k \bra{e_k} \quad \rightarrow \quad \braket{v|v} = \sum_{k=1}^{d} \bar{a}_k \cdot a_k = \sum_{k=1}^{d} |a_k|^2 = \| \ket{v} \|^2$$

$$\left( \sum_{k=1}^{d} \bar{a}_k \bra{e_k} \right) \left( \sum_{k'=1}^{d} a_{k'} \ket{e_{k'}} \right) = \sum_{k,k'=1}^{d} \bar{a}_k a_{k'} \braket{e_k | e_{k'}}$$

⊛ With this abstract notation, we do not have to explicitly write column vectors! (Helpful for large vectors — for $n$ qubits the size of the vectors is $2^n$!)
