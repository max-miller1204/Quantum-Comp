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
