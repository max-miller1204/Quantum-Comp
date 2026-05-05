If the qubit state is given by a density operator $\rho$, then after the noise it is

$$(1-\alpha)\rho + \alpha X\rho X \quad \rightarrow \text{"Bit-flip channel"}$$

- $(1-\alpha)\rho$: Do nothing with probability $1-\alpha$
- $\alpha X\rho X$: Apply the X gate with probability $\alpha$.

[Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom; vertical blue line connecting them with red dots indicating the mixed state along the z-axis]

$$\ket{0}\bra{0} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \mapsto (1-\alpha)\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \alpha \underbrace{X\ket{0}\bra{0}X}_{=\ket{1}\bra{1}} = \begin{pmatrix} 1-\alpha & 0 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & \alpha \end{pmatrix}$$

$$= \begin{pmatrix} 1-\alpha & 0 \\ 0 & \alpha \end{pmatrix}$$

$$= (1-\alpha)\ket{0}\bra{0} + \alpha\ket{1}\bra{1}.$$

✸ If we measured the initial (noiseless) state, then we would get the outcome "0" with probability 1 → after noise, the state becomes mixed: with probability $1-\alpha$ we get "0" and with probability $\alpha$ we get "1".

✸ So $\alpha$ quantifies the amount of noise! 
- $\alpha = 0 \Rightarrow$ no noise
- $\alpha = \frac{1}{2} \Rightarrow \boxed{\frac{1}{2}\ket{0}\bra{0} + \frac{1}{2}\ket{1}\bra{1}}$

✸ For a general density matrix: recall the form $\rho = \frac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)$

$r_x, r_y, r_z$ → Coordinates in the Bloch sphere.

[Bloch sphere with axes labeled: z-axis up with $\ket{0}$ at top and $\ket{1}$ at bottom; y-axis to the right with $\ket{+i}$, and $\ket{-i}$ on the opposite side; x-axis coming out toward viewer with $\ket{+}$ in front and $\ket{-}$ behind]

How do those coordinates transform after the noise?

$$(r_x, r_y, r_z) \mapsto (r_x', r_y', r_z') \;?$$
