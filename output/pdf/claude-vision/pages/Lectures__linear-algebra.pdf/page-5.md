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
