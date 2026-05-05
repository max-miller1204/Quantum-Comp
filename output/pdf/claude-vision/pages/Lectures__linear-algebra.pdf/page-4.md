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
