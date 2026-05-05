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
