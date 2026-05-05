✸ For a state vector $\ket{\psi}$: $\Pr[+] = |\braket{+|\psi}|^2 = \braket{+|\psi}\braket{\psi|+} = \mathrm{Tr}[\ket{+}\bra{+}\ket{\psi}\bra{\psi}]$.

$\Pr[-] = |\braket{-|\psi}|^2 = \braket{-|\psi}\braket{\psi|-} = \mathrm{Tr}[\ket{-}\bra{-}\ket{\psi}\bra{\psi}]$

✸ <u>For a density operator $\rho$</u>: $\Pr[+] = \mathrm{Tr}[\ket{+}\bra{+}\rho]$, $\Pr[-] = \mathrm{Tr}[\ket{-}\bra{-}\rho]$.

  <span style="color:red">↑ Measurement operators. ↑</span>

✸ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{H} - \boxed{X} \!=\!\!=$

[Bloch sphere: $\ket{0}$ at top (+z), $\ket{1}$ at bottom, $\ket{+}$ on +x (front), $\ket{-}$ on −x, $\ket{+i}$ on +y, $\ket{-i}$ on −y. Axes labeled $z, y, x$.]

- <u>Pauli-Y measurement</u>: measure along $y$-axis; equivalent to measuring in basis $\{\ket{+i}, \ket{-i}\}$

✸ <span style="color:red">Recall: $\ket{+i} = SH\ket{0}$, $\ket{-i} = SH\ket{1}$, $H \equiv$ Hadamard gate</span>

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$S \equiv$ phase gate
$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

✸ <span style="color:red">$SH$ is unitary $\Rightarrow \{\ket{+i}, \ket{-i}\}$ is a basis!</span>

✸ For a state vector $\ket{\psi}$: $\Pr[+i] = |\braket{+i|\psi}|^2 = \braket{+i|\psi}\braket{\psi|+i} = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}]$.

$\ket{+i}\bra{+i} + \ket{-i}\bra{-i} = \mathbb{1}$.

$\Pr[-i] = |\braket{-i|\psi}|^2 = \braket{-i|\psi}\braket{\psi|-i} = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$

✸ <u>For a density operator $\rho$</u>: $\Pr[+i] = \mathrm{Tr}[\ket{+i}\bra{+i}\rho]$, $\Pr[-i] = \mathrm{Tr}[\ket{-i}\bra{-i}\rho]$.

  <span style="color:red">↑ Measurement operators. ↑</span>

— <u>Measuring multiple qubits</u>.

- Consider state vector $\ket{\psi}$ of $n$ qubits $\big(\ket{\psi} \in (\mathbb{C}^2)^{\otimes n}\big)$. → or density matrix $\rho$.

- Computational-basis measurement is a $\{\ket{0}, \ket{1}\}$ measurement on each qubit

- Outcome probabilities: $\Pr[0,0,1] = |\braket{0,0,1|\psi}|^2$ (for three qubits).
  
  with $\braket{0,0,1} = \bra{0}\otimes\bra{0}\otimes\bra{1}$
  
  $\Pr[x_1, x_2, x_3] = |\braket{x_1, x_2, x_3|\psi}|^2$, $x_1, x_2, x_3 \in \{0,1\}$.
  
  $= \mathrm{Tr}[\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3}\ket{\psi}\bra{\psi}]$

$\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3} = \ket{x_1}\bra{x_1} \otimes \ket{x_2}\bra{x_2} \otimes \ket{x_3}\bra{x_3}$

✸ For a density operator $\rho$: $\mathrm{Tr}[\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3}\rho]$.
