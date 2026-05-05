# Lectures__superdense-coding.pdf

## Page 1

# ① Recap: Quantum teleportation

- A method to send arbitrary quantum information using entanglement and two bits of classical information.

[Diagram: Alice holds $\ket{\psi}_{A'}$ and one half of the entangled pair $\ket{\Phi^+}_{AB}$. She performs a Bell measurement on her two qubits, obtaining outcomes $x \in \{0,1\}$ and $z \in \{0,1\}$. These two classical bits are sent to Bob, who applies $X^x$ then $Z^z$ to his half of $\ket{\Phi^+}_{AB}$ to recover $\ket{\psi}_B$.]

- If $x=0$, do nothing; if $x=1$, apply $X$.
- If $z=0$, do nothing; if $z=1$, apply $Z$.

✱ Teleportation is **not** instantaneous / faster than light — it only works if Bob gets Alice's measurement outcomes → this takes time!

- The **Bell measurement** is a critical component.
  It is given by the POVM $\{\Phi^+, \Phi^-, \Psi^+, \Psi^-\}$, $\Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}$, $\Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}$,
  
  $$\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0} \pm \ket{1}\ket{1}), \qquad \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{1} \pm \ket{1}\ket{0}).$$

Circuit implementation:

[Circuit: two qubit lines. The top line goes through $H$ then a Pauli-$Z$ measurement. The bottom line is the target of a CNOT (control = top qubit) before the $H$, and is then measured in the $Z$ basis. The boxed region containing the two $Z$-measurements is labeled "Pauli-$Z$ measurement".]

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}\ket{0}$$

**Proof:** Let $\rho_{AB}$ be the initial state.

Let $U = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$ be the CNOT gate, and $H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ the Hadamard gate.

$H\ket{0} = \ket{+}$
$H\ket{1} = \ket{-}$
$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$

## Page 2

[Circuit diagram: Input $\rho_{AB}$ on two qubits A (top) and B (bottom). A CNOT gate with A as control and B as target, then a Hadamard H on qubit A, then Pauli-Z measurement boxes (labeled X) on both qubits.]

$\rho_{AB} \mapsto U\rho_{AB}U^\dagger \mapsto (H\otimes \mathbb{1})U\rho_{AB}U^\dagger(H^\dagger \otimes \mathbb{1})$

↑ Pauli-Z measurement.   ↓ State just before measurement.

Now do a Pauli-Z measurement on each qubit.

The POVM is $\{|0,0\rangle\langle 0,0|, |0,1\rangle\langle 0,1|, |1,0\rangle\langle 1,0|, |1,1\rangle\langle 1,1|\}$.

Outcome probabilities:

$\Pr(z,x) = \mathrm{Tr}\big[|z,x\rangle\langle z,x|_{AB}\,(H\otimes\mathbb{1})\,U\rho_{AB}U^\dagger\,(H^\dagger\otimes\mathbb{1})\big]$

$\qquad \mathrm{Tr}\big[|z,x\rangle\langle z,x|\,\sigma\big]$

$\mathrm{Tr}[ABC] = \mathrm{Tr}[CAB] = \mathrm{Tr}[BCA]$

$= \mathrm{Tr}\big[(H^\dagger\otimes\mathbb{1})|z,x\rangle\langle z,x|_{AB}(H\otimes\mathbb{1})\,U\rho_{AB}U^\dagger\big]$  (cyclicity of trace)

$= \mathrm{Tr}\big[\underbrace{U^\dagger(H^\dagger\otimes\mathbb{1})|z,x\rangle\langle z,x|_{AB}(H\otimes\mathbb{1})U}_{M_{z,x}}\,\rho_{AB}\big]$  (cyclicity of trace again).

$U^\dagger = U$ (b/c CNOT is Hermitian)

$H^\dagger = H$ (b/c Hadamard is also Hermitian). $\Rightarrow M_{z,x} = U(H\otimes\mathbb{1})|z,x\rangle\langle z,x|(H\otimes\mathbb{1})U$

(1) $U(H\otimes\mathbb{1})|0,0\rangle = \mathrm{CNOT}|+,0\rangle = \mathrm{CNOT}\tfrac{1}{\sqrt{2}}(|0\rangle|0\rangle + |1\rangle|0\rangle)$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(\mathrm{CNOT}|0\rangle|0\rangle + \underbrace{\mathrm{CNOT}|1\rangle|0\rangle}_{=|1\rangle|1\rangle})$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(|0\rangle|0\rangle + |1\rangle|1\rangle)$

$\qquad\qquad = |\Phi^+\rangle$

$\Rightarrow M_{0,0} = \Phi^+$

$|+\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$

(2) $U(H\otimes\mathbb{1})|0,1\rangle = \mathrm{CNOT}|+,1\rangle = \mathrm{CNOT}\tfrac{1}{\sqrt{2}}(|0\rangle|1\rangle + |1\rangle|1\rangle)$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(\mathrm{CNOT}|0\rangle|1\rangle + \mathrm{CNOT}|1\rangle|1\rangle)$

## Page 3

$$= \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{1} + \ket{1}\ket{0}\right)$$

$$= \ket{\Psi^+}$$

$$\Rightarrow \underline{M_{0,1} = \Psi^+}$$

(3) $U(H \otimes \mathbb{1})\ket{1,0} = \text{CNOT}\ket{-,0} = \text{CNOT}\,\tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{0} - \ket{1}\ket{0}\right)$

$$= \tfrac{1}{\sqrt{2}}\left(\text{CNOT}\ket{0}\ket{0} - \text{CNOT}\ket{1}\ket{0}\right)$$

$$= \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{0} - \ket{1}\ket{1}\right)$$

$$= \ket{\Phi^-}$$

$$\Rightarrow \underline{M_{1,0} = \Phi^-}$$

(4) $U(H \otimes \mathbb{1})\ket{1,1} = \text{CNOT}\ket{-,1} = \text{CNOT}\,\tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{1} - \ket{1}\ket{1}\right)$

$$= \tfrac{1}{\sqrt{2}}\left(\text{CNOT}\ket{0}\ket{1} - \text{CNOT}\ket{1}\ket{1}\right)$$

$$= \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{1} - \ket{1}\ket{0}\right)$$

$$= \ket{\Psi^-}$$

$$\Rightarrow \underline{M_{1,1} = \Psi^-} \quad \blacksquare$$

Also, $\Phi^+ + \Phi^- + \Psi^+ + \Psi^- = \mathbb{1}$.

<u>Proof</u>: Go to the matrix representation.

$$\ket{\Phi^+} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{0} + \ket{1}\ket{1}\right) = \begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \tfrac{1}{\sqrt{2}} \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

## Page 4

$$\Rightarrow \Phi^+ = \ket{\Phi^+}\bra{\Phi^+} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \frac{1}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{2}} & 0 & 0 & \frac{1}{\sqrt{2}} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & 0 & 0 & \frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \frac{1}{2} & 0 & 0 & \frac{1}{2} \end{pmatrix}$$

$$\ket{\Phi^-} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{0} - \ket{1}\ket{1}\big) = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ 0 \\ -\frac{1}{\sqrt{2}} \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

$$\Rightarrow \Phi^- = \ket{\Phi^-}\bra{\Phi^-} = \begin{pmatrix} \frac{1}{2} & 0 & 0 & -\frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -\frac{1}{2} & 0 & 0 & \frac{1}{2} \end{pmatrix}$$

$$\ket{\Psi^+} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{1} + \ket{1}\ket{0}\big) = \begin{pmatrix} 0 \\ \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix} \Rightarrow \Psi^+ = \ket{\Psi^+}\bra{\Psi^+} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$$\ket{\Psi^-} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{1} - \ket{1}\ket{0}\big) = \begin{pmatrix} 0 \\ \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \\ 0 \end{pmatrix} \Rightarrow \Psi^- = \ket{\Psi^-}\bra{\Psi^-} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & -\frac{1}{2} & 0 \\ 0 & -\frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

Add up: $\Phi^+ + \Phi^- + \Psi^+ + \Psi^- = $

$$\begin{pmatrix} \frac{1}{2} & 0 & 0 & \frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \frac{1}{2} & 0 & 0 & \frac{1}{2} \end{pmatrix} + \begin{pmatrix} \frac{1}{2} & 0 & 0 & -\frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -\frac{1}{2} & 0 & 0 & \frac{1}{2} \end{pmatrix} + \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & -\frac{1}{2} & 0 \\ 0 & -\frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \blacksquare$$

## Page 5

## ② Superdense Coding

✱ **Teleportation**: using entanglement + classical information to transmit quantum information.

✱ We can also use entanglement to transmit classical information!

- **Superdense coding**: using entanglement + 1 qubit to transmit 2 classical bits.

[Diagram: Alice and Bob share entangled state $\ket{\Phi^+}_{AB}$. Alice's qubit (red line) goes through gates $X^x$ then $Z^z$ (boxed: "Encoding bits $z, x$ into one qubit."), with classical control inputs $x$ and $z$. The qubit is then sent to Bob, who performs a Bell Measurement on both qubits, obtaining outcome $(x, z)$.]

(1) • To encode $(0,0)$: $\underbrace{(Z^0 X^0 \otimes \mathbb{1})}_{=\mathbb{1}}\ket{\Phi^+}_{AB} = \ket{\Phi^+}_{AB}$  (Alice does nothing).
$\quad\;\;(z, x)$

- To encode $(0,1)$: $\underbrace{(Z^0 X^1 \otimes \mathbb{1})}_{=X}\ket{\Phi^+}_{AB} = (X \otimes \mathbb{1}) \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B)$

(Alice applies $X$ to her qubit.) 
$\qquad\qquad\qquad\qquad\quad = \tfrac{1}{\sqrt{2}}(X\ket{0}_A\ket{0}_B + X\ket{1}_A\ket{1}_B)$

$\qquad\qquad\qquad\qquad\quad = \tfrac{1}{\sqrt{2}}(\ket{1}_A\ket{0}_B + \ket{0}_A\ket{1}_B)$

$\qquad\qquad\qquad\qquad\quad = \ket{\Psi^+}_{AB}$

- To encode $(1,0)$: $\underbrace{(Z^1 X^0 \otimes \mathbb{1})}_{=Z}\ket{\Phi^+}_{AB} = (Z \otimes \mathbb{1}) \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B)$

## Page 6

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

## Page 7

⚛ The state encoded by Alice is

$$\ket{\Phi_{z,x}} = (Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}. \qquad ((z,x) \in \{0,1\}^2 \text{ are the bits she wants to send to Bob.})$$

$$\left.\begin{aligned}\ket{\Phi_{0,0}} &= \ket{\Phi^+} \\ \ket{\Phi_{0,1}} &= \ket{\Psi^+} \\ \ket{\Phi_{1,0}} &= \ket{\Phi^-} \\ \ket{\Phi_{1,1}} &= \ket{\Psi^-}\end{aligned}\right\}$ ⚛ Bob measures one of these states, but he does not know which one it is. He has to figure that out from the Bell measurement.

⚛ What is the probability that Bob retrieves the bits Alice sent?

We need to determine: $\Pr[\text{Bob gets outcome }(z',x'), \text{ given Alice encoded }(z,x)]$.

This is given by $\mathrm{Tr}\left[\Phi^{z',x'} \Phi^{z,x}\right]$ $\qquad \left(\Phi^{z,x} = \ket{\Phi^{z,x}}\bra{\Phi^{z,x}}.\right)$

$\uparrow \qquad \nwarrow$ Alice's encoded state.
Bob's
measurement

$$\delta_{x,x'} = \begin{cases} 0 & \text{if } x \neq x' \\ 1 & \text{if } x = x' \end{cases}$$

We will show that $\boxed{\mathrm{Tr}\left[\Phi^{z',x'} \Phi^{z,x}\right] = \delta_{z,z'}\,\delta_{x,x'}}$

<u>This means</u>: if Alice sends bits $z,x$, then Bob's measurement outcome is also $z,x$, with probability one $\Rightarrow$ he successfully gets Alice's bits.

<u>Proof</u>: $\mathrm{Tr}\left[\Phi^{z',x'}\Phi^{z,x}\right] = \mathrm{Tr}\Big[\underbrace{(Z^{z'}X^{x'}\otimes\mathbb{1})\ket{\Phi^+}}_{\ket{v_1}}\underbrace{\bra{\Phi^+}(X^{x'}Z^{z'}\otimes\mathbb{1})}_{\bra{v_1}}\underbrace{(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}}_{\ket{v_2}}\underbrace{\bra{\Phi^+}(X^x Z^z \otimes \mathbb{1})}_{\bra{v_2}}\Big]$

$\underbrace{\hphantom{xxxxxxxxxxxxxxxxxxxxx}}_{\Phi^{z',x'}} \quad \underbrace{\hphantom{xxxxxxxxxxxxxxxxxxxxx}}_{\Phi^{z,x}}$

$(M_1 \otimes \mathbb{1})(M_2 \otimes \mathbb{1})$
$= M_1 M_2 \otimes \mathbb{1}$

$= \mathrm{Tr}\big[\ket{v_1}\bra{v_1}\ket{v_2}\bra{v_2}\big] = \underbrace{\braket{v_1|v_2}}_{\text{scalar!}} \mathrm{Tr}\big[\ket{v_1}\bra{v_2}\big] = \braket{v_1|v_2}\underbrace{\braket{v_2|v_1}}_{=\overline{\braket{v_1|v_2}}}$

$\braket{v_1|v_2} = \bra{\Phi^+}(X^{x'}Z^{z'}\otimes\mathbb{1})(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+} = \bra{\Phi^+}(X^{x'}Z^{z'}Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}$

## Page 8

$$= \tfrac{1}{\sqrt{2}}\underbrace{\big(\bra{0}\bra{0}+\bra{1}\bra{1}\big)}_{\sum_{k=0}^{1}\bra{k}\bra{k}} \big(X^{x'}Z^{z'}Z^{z}X^{x}\otimes \mathbb{1}\big) \tfrac{1}{\sqrt{2}}\underbrace{\big(\ket{0}\ket{0}+\ket{1}\ket{1}\big)}_{\sum_{k'=0}^{1}\ket{k'}\ket{k'}}$$

$$= \tfrac{1}{2}\sum_{k,k'=0}^{1} \bra{k}\bra{k}\big(X^{x'}Z^{z'}Z^{z}X^{x}\otimes \mathbb{1}\big)\ket{k'}\ket{k'}$$

$$= \tfrac{1}{2}\sum_{k,k'=0}^{1} \bra{k}X^{x'}Z^{z'}Z^{z}X^{x}\ket{k'}\underbrace{\braket{k|k'}}_{=\delta_{k,k'}} \qquad \color{blue}{\bra{k}\bra{k}(M_1\otimes M_2)\ket{k'}\ket{k'}}$$
$$\color{blue}{= \bra{k}M_1\ket{k'}\bra{k}M_2\ket{k'}}$$

$$= \tfrac{1}{2}\sum_{k=0}^{1}\bra{k}X^{x'}Z^{z'}Z^{z}X^{x}\ket{k} \qquad \color{blue}{\sum_{k}\bra{k}M\ket{k}=\mathrm{Tr}(M)}$$

$$= \tfrac{1}{2}\mathrm{Tr}\!\left[X^{x'}Z^{z'}Z^{z}X^{x}\right] = \tfrac{1}{2}\mathrm{Tr}\!\left[X^{x}X^{x'}Z^{z'}Z^{z}\right] = \underline{\underline{\tfrac{1}{2}\mathrm{Tr}\!\left[X^{x\oplus x'}Z^{z'\oplus z}\right]}}.$$

$\color{blue}{X^{0}=\mathbb{1}}$
$\color{blue}{X^{1}=X}$

$\color{red}{\to x=0,\,x'=0 \;\Rightarrow\; X^{0}X^{0}=\mathbb{1}}$
$\color{red}{\;\;\;\; x=0,\,x'=1 \;\Rightarrow\; X^{0}X^{1}=X}$
$\color{red}{\;\;\;\; x=1,\,x'=0 \;\Rightarrow\; X^{1}X^{0}=X}$
$\color{red}{\;\;\;\; x=1,\,x'=1 \;\Rightarrow\; X^{1}X^{1}=X^{2}=\mathbb{1}}$

$\Rightarrow X^{x}X^{x'} = X^{\underline{\underline{x\oplus x'}}} \quad \oplus$

$\uparrow$ XOR!

$$\begin{pmatrix} 0\oplus 0 = 0 \\ 0\oplus 1 = 1 \\ 1\oplus 0 = 1 \\ 1\oplus 1 = 0 \end{pmatrix}$$

$\color{red}{\text{Same for } Z^{z'}Z^{z}:\; z'=0,\,z=0 \Rightarrow \mathbb{1}}$
$\color{red}{\;\;\;\; z'=0,\,z=1 \Rightarrow Z}$
$\color{red}{\;\;\;\; z'=1,\,z=0 \Rightarrow Z} \;\;\Rightarrow\; Z^{z'}Z^{z} = Z^{z'\oplus z}$
$\color{red}{\;\;\;\; z'=1,\,z=1 \Rightarrow \mathbb{1}}$

Now, we use the fact that $Z$ and $X$ are orthogonal:

$$Z=\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix},\quad X=\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix} \;\Rightarrow\; \mathrm{Tr}[X]=\mathrm{Tr}[Z]=0,\text{ and}$$

$$\mathrm{Tr}[ZX] = \mathrm{Tr}\!\left[\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}\right] = \mathrm{Tr}\!\left[\begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}\right] = 0.$$

## Page 9

Therefore, $\text{Tr}(Z^a X^b) = 2\, \delta_{a,0}\, \delta_{b,0}$. $\quad a, b \in \{0,1\}$

Check: $a=0, b=0 \Rightarrow \text{Tr}(\mathbb{1}) = 2$
$\phantom{Check:}\, a=0, b=1 \Rightarrow \text{Tr}(X) = 0$
$\phantom{Check:}\, a=1, b=0 \Rightarrow \text{Tr}(Z) = 0$
$\phantom{Check:}\, a=1, b=1 \Rightarrow \text{Tr}(ZX) = 0$.

Finally: $\braket{v_1 | v_2} = \frac{1}{2} \text{Tr}\bigl(X^{x \oplus x'} Z^{z' \oplus z}\bigr) = \delta_{x \oplus x', 0}\, \delta_{z' \oplus z, 0}$

[arrows above exponents labeling $a$ and $b$]

But $x \oplus x' = 0 \iff x = x'$ and $z' \oplus z = 0 \iff z' = z$

$\Rightarrow \delta_{x \oplus x', 0} = \delta_{x, x'}$ and $\delta_{z' \oplus z, 0} = \delta_{z', z}$.

So $\braket{v_1 | v_2} = \delta_{x, x'}\, \delta_{z, z'}$.

Similarly $\braket{v_2 | v_1} = \overline{\braket{v_1 | v_2}} = \delta_{x, x'}\, \delta_{z, z'}$.

So $\text{Tr}\bigl(E^{z', x'}\, E^{z, x}\bigr) = \delta_{x, x'}\, \delta_{z, z'}$. ∎

---

❋ <u>Recap</u>: Superdense coding allows Alice to send two bits to Bob using only one qubit — as long as the qubit is already entangled with Bob's qubit.

This worked b/c the 4 Bell states were used to encode the information and do the measurement — and b/c the Bell states are orthogonal, they are perfectly distinguishable.

❋ <u>Why is this interesting?</u>

With just a single (unentangled) qubit, we cannot successfully (w/ prob. 1) transmit more than one bit of information.

## Page 10

In dimension $d$, we can transmit w/ prob. 1 at most $\log_2(d)$ bits.

So $d=2 \implies \log_2(2) = 1$ bit.

With entanglement, the dimension effectively increases to $4 \to \log_2(4) = 2$.
$$(\text{b/c } 4 = 2^2).$$
