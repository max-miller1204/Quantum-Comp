- What about more general density matrices? Consider $d=2$.

We can write $\rho = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$ (b/c $\{\mathbb{1}, X, Y, Z\}$ is a basis).

We want this to satisfy: (1) $\rho^\dagger = \rho$; (2) $\text{Tr}(\rho) = 1$; (3) $\rho \geq 0$.

(1) $\rho^\dagger = \frac{1}{2}(\bar{c_0}\mathbb{1}^\dagger + \bar{c_1} X^\dagger + \bar{c_2} Y^\dagger + \bar{c_3} Z^\dagger)$  $\quad (\mathbb{1}^\dagger = \mathbb{1},\ X^\dagger = X,\ Y^\dagger = Y,\ Z^\dagger = Z)$

$\quad \downarrow$

$\quad = \frac{1}{2}(\bar{c_0}\mathbb{1} + \bar{c_1} X + \bar{c_2} Y + \bar{c_3} Z)$

$\quad \overset{(!)}{=} \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z) \iff c_0 = \bar{c_0},\ c_1 = \bar{c_1},\ c_2 = \bar{c_2},\ c_3 = \bar{c_3}$ (b/c $\{\mathbb{1}, X, Y, Z\}$ is a basis).

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ (all are real numbers).

(2) $\rho = \frac{1}{2}(r_0 \mathbb{1} + r_1 X + r_2 Y + r_3 Z),\ r_0, r_1, r_2, r_3 \in \mathbb{R}$.

$\text{Tr}(\rho) = \frac{1}{2}\big(r_0 \underbrace{\text{Tr}(\mathbb{1})}_{=2} + r_1 \underbrace{\text{Tr}(X)}_{=0} + r_2 \underbrace{\text{Tr}(Y)}_{=0} + r_3 \underbrace{\text{Tr}(Z)}_{=0}\big) \overset{(!)}{=} 1 \iff \underline{\underline{r_0 = 1}}$

(3) $\rho = \frac{1}{2}(\mathbb{1} + r_1 X + r_2 Y + r_3 Z) \to$ Find the eigenvalues!

$\left(\begin{array}{c}
\circledast\ \underline{\text{Observe}}: \cdot \langle X, \rho \rangle = \text{Tr}(X\rho) = \text{Tr}\big[X \cdot \tfrac{1}{2}(\mathbb{1} + r_1 X + r_2 Y + r_3 Z)\big] \\
\quad\quad\quad\quad = \tfrac{1}{2}\big(\underbrace{\text{Tr}(X)}_{=0} + r_1 \underbrace{\text{Tr}(X^2)}_{=2} + r_2 \underbrace{\text{Tr}(XY)}_{=0} + r_3 \underbrace{\text{Tr}(XZ)}_{=0}\big) \\
\quad\quad\quad\quad\quad \downarrow \\
\quad\quad\quad\quad\quad = r_1 \\
\quad\quad \cdot \langle Y, \rho \rangle = r_2 \\
\quad\quad \cdot \langle Z, \rho \rangle = r_3.
\end{array}\right.$
