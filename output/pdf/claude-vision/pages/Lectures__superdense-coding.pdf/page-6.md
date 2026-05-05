(Alice applies $Z$ to her qubit.)

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$$= \tfrac{1}{\sqrt{2}}\left( Z\ket{0}_A \ket{0}_B + Z\ket{1}_A \ket{1}_B \right)$$

$$= \tfrac{1}{\sqrt{2}}\left( \ket{0}_A \ket{0}_B - \ket{1}_A \ket{1}_B \right)$$

$$= \ket{\Phi^-}_{AB}$$

- <u>To encode $(1,1)$</u>: $(Z^1 X^1 \otimes \mathbb{1})\ket{\Phi^+}_{AB} = (ZX \otimes \mathbb{1})\tfrac{1}{\sqrt{2}}\left( \ket{0}_A \ket{0}_B + \ket{1}_A \ket{1}_B \right)$

$$= ZX$$

$$= \tfrac{1}{\sqrt{2}}\left( ZX\ket{0}_A \ket{0}_B + ZX\ket{1}_A \ket{1}_B \right)$$

$$\quad\quad = Z\ket{1} = -\ket{1} \qquad = Z\ket{0} = \ket{0}$$

$$= \tfrac{1}{\sqrt{2}}\left( -\ket{1}_A \ket{0}_B + \ket{0}_A \ket{1}_B \right)$$

$$= \ket{\Psi^-}_{AB}.$$

⊛ <u style="color:red">Observation</u>: <span style="color:red">These encoded states are the same as the measurement operators of the Bell measurement!</span>

(2) After encoding, Alice sends her qubit to Bob.

(3) Then Bob does a Bell measurement on both qubits.

⊛ <u>Recall</u>: the outcome of the Bell measurement is two bits of information.
  Outcome $\Phi^+ \leftrightarrow (0,0)$
  Outcome $\Psi^+ \leftrightarrow (0,1)$
  Outcome $\Phi^- \leftrightarrow (1,0)$
  Outcome $\Psi^- \leftrightarrow (1,1)$

  Each one of these outcomes occurs with some probability, depending on the state: if the state being measured is $\rho$, then:

  $$\Pr[\Phi^+] = \mathrm{Tr}[\rho\, \Phi^+], \quad \Pr[\Phi^-] = \mathrm{Tr}[\rho\, \Phi^-], \quad \Pr[\Psi^+] = \mathrm{Tr}[\rho\, \Psi^+], \quad \Pr[\Psi^-] = \mathrm{Tr}[\rho\, \Psi^-]$$
