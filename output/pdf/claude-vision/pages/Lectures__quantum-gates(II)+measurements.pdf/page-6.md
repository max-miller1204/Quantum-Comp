## ③ Measurements

- To extract classical information from a qubit, we must <u>measure</u> it

- <u>Recall</u>: $\ket{\psi} = \alpha\ket{0} + \beta\ket{1} \rightarrow$ Probability of 0: $|\alpha|^2$  ⊛ <span style="color:red">Axiom of quantum mechanics! (aka "Born Rule")</span>
  
  $\alpha = \braket{0|\psi}, \;\beta = \braket{1|\psi}$  Probability of 1: $|\beta|^2$

  ⊛ <u>Note</u>: $|\alpha|^2 = |\braket{0|\psi}|^2,\; |\beta|^2 = |\braket{1|\psi}|^2$

  <u>Also</u>: $\underbrace{|\braket{0|\psi}|^2}_{\equiv \,\Pr(0)} = \braket{0|\psi}\braket{\psi|0} = \mathrm{Tr}\big[\ket{0}\bra{0}\,\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad\qquad\qquad\qquad\quad \braket{v_1|M|v_2} = \mathrm{Tr}\big[M\ket{v_2}\bra{v_1}\big]$

  $\underbrace{|\braket{1|\psi}|^2}_{\equiv \,\Pr(1)} = \braket{1|\psi}\braket{\psi|1} = \mathrm{Tr}\big[\ket{1}\bra{1}\,\ket{\psi}\bra{\psi}\big]$

  <u>Check</u>: $\Pr(0) + \Pr(1) = \mathrm{Tr}\big[\ket{0}\bra{0}\ket{\psi}\bra{\psi}\big] + \mathrm{Tr}\big[\ket{1}\bra{1}\ket{\psi}\bra{\psi}\big]$

  $\mathrm{Tr}[M_1 + M_2] = \mathrm{Tr}[M_1] + \mathrm{Tr}[M_2]$
  
  $\mathrm{Tr}\big[\ket{0}\bra{0}\ket{\psi}\bra{\psi} + \ket{1}\bra{1}\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad = \mathrm{Tr}\Big[\big(\underbrace{\ket{0}\bra{0} + \ket{1}\bra{1}}_{=\,\mathbb{1}}\big)\ket{\psi}\bra{\psi}\Big]$
  
  $\qquad\qquad = \mathrm{Tr}\big[\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad = \braket{\psi|\psi}$
  
  $\qquad\qquad = 1\;\checkmark$

  ⊛ This is often called a "<u>computational-basis measurement</u>"
  or a "$\{\ket{0},\ket{1}\}$-<u>basis measurement</u>".

  ⊛ Recall that $\{\ket{0},\ket{1}\}$ is also the eigenvectors of Pauli-Z:
  
  $Z\ket{0} = \ket{0},\; Z\ket{1} = -\ket{1}. \rightarrow$ So we also sometimes say "<u>Pauli-Z measurement</u>"

  ⊛ <u>Circuit symbol</u>:  $\ket{\psi}\!-\!\boxed{Z}\!=$
