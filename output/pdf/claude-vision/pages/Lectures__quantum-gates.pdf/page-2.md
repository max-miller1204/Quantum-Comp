- ✻ <u>Origin</u>, $\vec{r} = (0,0,0) \to \rho = \frac{1}{2}(\ket{0}\bra{0} + \ket{1}\bra{1}) \to$ the <u>maximally-mixed state</u>  $\quad |\alpha|^2 + |\beta|^2 = 1$
  
  (A completely random state). $\quad = \frac{\mathbb{1}}{2}$

- ✻ <u>Points on the X-axis</u>: $\vec{r} = (\pm 1, 0, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm X) = \ket{\pm}\bra{\pm}, \quad \ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$

  These are eigenvectors of $X$! $\quad X\ket{\pm} = \pm\ket{\pm}. \to X\ket{+} = \ket{+}$
  (Eigenvalues of $X$ are $\pm 1$.) $\hspace{6cm} X\ket{-} = -\ket{-}$

- ✻ <u>Points on the Y-axis</u>: $\vec{r} = (0, \pm 1, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm Y) = \ket{\pm i}\bra{\pm i}, \quad \ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

  These are eigenvectors of $Y$! $\quad Y\ket{\pm i} = \pm \ket{\pm i}. \quad Y\ket{+i} = \ket{+i}$
  (Eigenvalues of $Y$ are $\pm 1$.) $\hspace{6cm} Y\ket{-i} = -\ket{-i}$

- ✻ <u>Points on the Z-axis</u>: $\vec{r} = (0, 0, \pm 1) \to \rho = \frac{1}{2}(\mathbb{1} \pm Z) \begin{matrix} ^{(+)}\to \ket{0}\bra{0} \\ _{(-)}\to \ket{1}\bra{1} \end{matrix}$

  These are eigenvectors of $Z$! $\quad Z\ket{0} = \ket{0}, \; Z\ket{1} = -\ket{1}.$ (Eigenvalues of $Z$ are $\pm 1$.)

- For higher dimensions, we don't have such a nice representation.

- We can still check if a state is pure using the <u>purity</u>:

  For density matrix $\rho$ in dimension $d$, $\quad \underline{\text{Tr}[\rho^2] \equiv \text{purity}}$

  The state $\rho$ is pure if and only if $\text{Tr}[\rho^2] = 1$.

- ✻ Every pure state is represented by a density matrix of the form $\rho = \ket{\psi}\bra{\psi}$, where $\ket{\psi} \in \mathbb{C}^d$ is a state vector ($\|\ket{\psi}\| = 1$).

  If a state is not pure, then we call it a <mark>mixed state.</mark>

- ✻ <u>Important fact</u>: Every mixed state can be written as a <u>convex combination</u> of pure states:
  
  $$\rho = \sum_{k=1}^{M} p_k \ket{\psi_k}\bra{\psi_k}, \quad p_k \in [0,1], \quad \sum_{k=1}^{M} p_k = 1.$$
  
  $\hspace{3cm}\uparrow$ probabilities.
