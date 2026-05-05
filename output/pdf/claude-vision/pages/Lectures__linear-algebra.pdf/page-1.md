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
