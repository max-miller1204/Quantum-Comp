$$\underline{\text{Check}}: \text{Tr}[\rho] = \sum_{k=1}^{m} p_k \underbrace{\text{Tr}\left[\ket{\psi_k}\bra{\psi_k}\right]}_{=1} = \sum_{k=1}^{m} p_k = 1 \quad \checkmark$$

$$\begin{pmatrix} (M_1+M_2)^\dagger \\ = M_1^\dagger + M_2^\dagger \end{pmatrix} \qquad \underline{\text{Check}}: \rho^\dagger = \sum_{k=1}^{m} p_k \underbrace{\left(\ket{\psi_k}\bra{\psi_k}\right)^\dagger}_{= \ket{\psi_k}\bra{\psi_k}} = \sum_{k=1}^{m} p_k \ket{\psi_k}\bra{\psi_k} = \rho \quad \checkmark$$

$$\left(\ket{v_1}\bra{v_2}\right)^\dagger = \ket{v_2}\bra{v_1}$$

$\underline{\text{Check}}: \rho \succeq 0 \longrightarrow$ Yes, b/c we sum over PSD elements.

$$M_1, M_2 \succeq 0$$

$$\bra{v}(M_1+M_2)\ket{v} = \underbrace{\bra{v}M_1\ket{v}}_{\geq 0} + \underbrace{\bra{v}M_2\ket{v}}_{\geq 0} \geq 0$$

② <u>Quantum Circuits and gates.</u>

- <u>Recap</u>: classical computation: manipulation of bits via <u>logic gates</u> (AND, OR, NOT, XOR)

  For input $x \in \{0,1\}^n$, calculate $f(x)$ for some $f$.
  (How to realize $f$ with a circuit? How many gates / depth is necessary and/or sufficient?)

  ✱ We rarely think about computation in these terms anymore!

  ✱ We program in some <u>high-level language</u> (C++, python, julia) and then the code gets <u>compiled</u> into the machine-level language.

  ✱ Quantum computing is still thought about at the gate level.

  (Although "quantum programming languages" are being developed — qiskit is a simple example.)
