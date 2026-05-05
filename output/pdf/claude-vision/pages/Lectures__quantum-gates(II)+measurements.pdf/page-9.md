## — Measuring multiple qubits.

- Consider state vector $\ket{\psi}$ of $n$ qubits $\left(\ket{\psi} \in (\mathbb{C}^2)^{\otimes n}\right)$.

- Computational-basis measurement is a $\{\ket{0}, \ket{1}\}$ measurement on each qubit.

- Outcome probabilities: $\Pr[0,0,1] = |\underbrace{\bra{0,0,1}}_{\bra{0}\otimes\bra{0}\otimes\bra{1}}\ket{\psi}|^2$ (for three qubits).

$$\Pr[x_1, x_2, x_3] = |\braket{x_1, x_2, x_3 | \psi}|^2, \quad x_1, x_2, x_3 \in \{0,1\}.$$

- What is the probability that the first qubit is 0?

$$\Pr[1^{st}\text{ qubit } 0] = \Pr[0,0,0] + \Pr[0,0,1] + \Pr[0,1,0] + \Pr[0,1,1].$$

$$\left\{\begin{matrix} 000 \\ 001 \\ 010 \\ 011 \end{matrix}\right. \quad \begin{matrix} 100 \\ 101 \\ 110 \\ 111 \end{matrix}$$

$$\Pr[2^{nd}\text{ qubit } 1] = \Pr[0,1,0] + \Pr[0,1,1] + \Pr[1,1,0] + \Pr[1,1,1].$$

- We can simultaneously measure each qubit in a different basis.

**Example:** measure $1^{st}$ & $3^{rd}$ qubit in Z-basis, $2^{nd}$ in X-basis.

$$\Pr[0, +, 1] = |\underbrace{\bra{0, +, 1}}_{= \bra{0}\otimes\bra{+}\otimes\bra{1}}\ket{\psi}|^2$$
