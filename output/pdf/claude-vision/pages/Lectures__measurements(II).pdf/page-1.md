# ① Recap: Measurements

- To extract classical information from a qubit, we must <u>measure</u> it
- <u>Recall</u>: $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$ → Probability of 0: $|\alpha|^2$
  Probability of 1: $|\beta|^2$

  ⊛ <u>Axiom of quantum mechanics!</u> (aka "Born Rule")

  ⊛ <u>Note</u>: $|\alpha|^2 = |\braket{0|\psi}|^2$, $|\beta|^2 = |\braket{1|\psi}|^2$

  <u>Also</u>: $|\braket{0|\psi}|^2 = \braket{0|\psi}\braket{\psi|0} = \mathrm{Tr}[\ket{0}\bra{0}\ket{\psi}\bra{\psi}]$
  $\quad\quad\quad \equiv P_r[0]$

  $\quad\quad\quad$ → "Measurement operators"

  $|\braket{1|\psi}|^2 = \braket{1|\psi}\braket{\psi|1} = \mathrm{Tr}[\ket{1}\bra{1}\ket{\psi}\bra{\psi}]$
  $\quad\quad\quad \equiv P_r[1]$

  $$P_r[0] + P_r[1] = \mathrm{Tr}\big[\underbrace{(\ket{0}\bra{0} + \ket{1}\bra{1})}_{\mathbb{1}}\rho\big] = \mathrm{Tr}[\rho] = 1$$

- For a density matrix $\rho$: $P_r[0] = \mathrm{Tr}[\ket{0}\bra{0}\rho]$, $P_r[1] = \mathrm{Tr}[\ket{1}\bra{1}\rho]$.

⊛ This is often called a "computational-basis measurement" or a "$\{\ket{0}, \ket{1}\}$-basis measurement".

⊛ Recall that $\{\ket{0}, \ket{1}\}$ is also the eigenvectors of Pauli-Z:

$Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$. → So we also sometimes say "<u>Pauli-Z measurement</u>"

⊛ <u>Circuit symbol</u>: $\ket{\psi} \!-\!\boxed{x}\!=$

- <u>Pauli-X measurement</u>: measure along x-axis; equivalent to measuring in basis $\{\ket{+}, \ket{-}\}$ → $\ket{+}\bra{+} + \ket{-}\bra{-} = \mathbb{1}$

  ⊛ Recall: $\ket{+} = H\ket{0}$, $\ket{-} = H\ket{1}$, $H \equiv$ Hadamard gate
  $\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

  ⊛ $H$ unitary $\Rightarrow \{\ket{+}, \ket{-}\}$ is a basis!

[Bloch sphere on right: z-axis up with $\ket{0}$ at top, $\ket{1}$ at bottom; y-axis with $\ket{-i}$ and $\ket{+i}$; x-axis with $\ket{+}$ and $\ket{-}$]
