✻ For this channel, it is useful to see the transformation in the standard basis.

$$\rho = \begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} \mapsto (1-\alpha)\rho + \alpha Z\rho Z = (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

where $a \in [0,1]$, $c \in \mathbb{C}$.

[arrow indicating the last product equals:]
$$= \begin{pmatrix} a & c \\ -\bar{c} & -(1-a) \end{pmatrix}$$

$$= (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} a & c \\ -\bar{c} & -(1-a) \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$$= \begin{pmatrix} a & -c \\ -\bar{c} & 1-a \end{pmatrix}$$

$$= (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} a & -c \\ -\bar{c} & 1-a \end{pmatrix} = \begin{pmatrix} a & (1-2\alpha)c \\ (1-2\alpha)\bar{c} & 1-a \end{pmatrix}$$

$\alpha = 0 \Rightarrow$ no noise
$\alpha = \tfrac{1}{2} \Rightarrow$ max. noise

✻ Off-diagonal terms are suppressed!

✻ For $\alpha = \tfrac{1}{2}$, the off-diagonal terms vanish! → superposition is gone!

- **Example:** Depolarizing channel: $\rho \mapsto (1-\alpha)\rho + \tfrac{\alpha}{3}X\rho X + \tfrac{\alpha}{3}Y\rho Y + \tfrac{\alpha}{3}Z\rho Z$

$$\begin{pmatrix} \text{With prob. } 1-\alpha, \text{ do nothing;} \\ \text{with prob. } \alpha, \text{ apply a Pauli} \\ \text{operator uniformly at random.} \end{pmatrix}$$

✻ For $\alpha = 3/4$: $\tfrac{1}{4}\rho + \tfrac{1}{4}X\rho X + \tfrac{1}{4}Y\rho Y + \tfrac{1}{4}Z\rho Z = \mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2}$  (Assignment!)

[underbrace under $\mathrm{Tr}[\rho]$: $=1$]

✻ Using this, we can write the depolarizing channel in an alternative way:
