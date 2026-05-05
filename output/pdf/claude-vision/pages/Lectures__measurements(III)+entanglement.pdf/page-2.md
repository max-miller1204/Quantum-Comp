For a two-qubit operator: 
$$M_{AB} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{pmatrix} \overset{00}{a_{11}} & \overset{01}{a_{12}} & \overset{10}{a_{13}} & \overset{11}{a_{14}} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}$$

$$\mathrm{Tr}_B(M_{AB}) = \mathrm{Tr}_B\!\left[\begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}\right] = \begin{pmatrix} a_{11}+a_{22} & a_{13}+a_{24} \\ a_{31}+a_{42} & a_{33}+a_{44} \end{pmatrix}$$

[The 4×4 matrix is partitioned into 2×2 blocks; within each block, the diagonal entries are summed to produce the corresponding entry of the reduced 2×2 matrix. Color-coding: $a_{11},a_{22}$ (orange) → top-left; $a_{13},a_{24}$ (pink) → top-right; $a_{31},a_{42}$ (purple) → bottom-left; $a_{33},a_{44}$ (red) → bottom-right.]

$$\mathrm{Tr}_A(M_{AB}) = \mathrm{Tr}_A\!\left[\begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}\right] = \begin{pmatrix} a_{11}+a_{33} & a_{12}+a_{34} \\ a_{21}+a_{43} & a_{22}+a_{44} \end{pmatrix}$$

[Color-coding: $a_{11},a_{33}$ (orange) → top-left; $a_{12},a_{34}$ (pink) → top-right; $a_{21},a_{43}$ (purple) → bottom-left; $a_{22},a_{44}$ (red) → bottom-right.]

— The most general form of a measurement is given by a <u>positive operator-valued measure (POVM)</u>: a (finite) set $\{M_x\}_{x \in \mathcal{X}}$ ← outcome labels.

(1) $M_x \geq 0 \quad \forall\, x \in \mathcal{X}$

(2) $\sum_x M_x = \mathbb{1}$.

- Probabilities are given by $\Pr(x) = \mathrm{Tr}(M_x \rho)$

❋ <u>Check</u>: $\sum_{x \in \mathcal{X}} \Pr(x) = \sum_{x \in \mathcal{X}} \mathrm{Tr}(M_x \rho) = \mathrm{Tr}\!\left[\underbrace{\left(\sum_x M_x\right)}_{=\mathbb{1}}\rho\right] = \mathrm{Tr}(\rho) = 1.$ ✓
