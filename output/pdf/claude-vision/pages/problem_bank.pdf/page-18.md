# Quantum circuits

1. Let $\alpha, \beta \in \mathbb{C}$. Prove that:
   (a) $XZXZ(\alpha\ket{0} + \beta\ket{1}) = -(\alpha\ket{0} + \beta\ket{1})$.
   (b) $ZXZX(\alpha\ket{0} + \beta\ket{1}) = -(\alpha\ket{0} + \beta\ket{1})$.

2. Let $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$, with $\alpha, \beta \in \mathbb{C}$ and $|\alpha|^2 + |\beta|^2 = 1$. Let $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ be the Hadamard gate. Calculate the following vectors.
   (a) $H\ket{\psi}$.
   (b) $H\ket{-} = \ket{1}$.
   (c) $H\ket{-\mathrm{i}} = \mathrm{e}^{-\mathrm{i}\frac{\pi}{4}}\ket{+\mathrm{i}}$.
   (d) Let $T = \begin{pmatrix} 1 & 0 \\ 0 & \mathrm{e}^{\mathrm{i}\frac{\pi}{4}} \end{pmatrix}$ be the $T$ gate. Calculate $HTHTH\ket{0}$.

3. Draw the state vector $HYTHX\ket{0}$ as a quantum circuit.

4. Consider an operator $U$ that performs the following mapping on the $Z$-basis state vectors:
$$U\ket{0} = \frac{1}{\sqrt{2}}(\ket{0} - \mathrm{i}\ket{1}), \quad U\ket{1} = \frac{1}{\sqrt{2}}(-\mathrm{i}\ket{0} + \ket{1}). \tag{76}$$

   (a) Express $U$ as a linear operator both in abstract bra-ket notation and as a matrix.
   (b) For arbitrary $\alpha, \beta \in \mathbb{C}$, what is $U(\alpha\ket{0} + \beta\ket{1})$?
   (c) Does $U$ represent a valid quantum gate? Explain your reasoning.

5. (a) Does $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & \mathrm{i} \\ \mathrm{i} & -1 \end{pmatrix}$ represent a valid quantum gate? If so, what is $U\ket{0}$ and $U\ket{1}$?
   
   (b) Does $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ \mathrm{i} & -\mathrm{i} \end{pmatrix}$ represent a valid quantum gate? If so, what is $U\ket{0}$ and $U\ket{1}$?

6. Let $\vec{n} \in \mathbb{R}^3$ be a unit vector, let $\vec{\sigma} = (X, Y, Z)$ be the vector of Pauli operators, and let $\varphi \in \mathbb{R}$. Prove that
$$\mathrm{e}^{\mathrm{i}\varphi(\vec{n}\cdot\vec{\sigma})} = \cos(\varphi)\mathbb{1} + \mathrm{i}\sin(\varphi)(\vec{n}\cdot\vec{\sigma}). \tag{77}$$

7. Consider the following quantum circuit:

   [Quantum circuit with three wires: top wire $\ket{a}$ goes through $H$, then control dot, then $H$; middle wire $\ket{b}$ goes through $H$, then control dot, then $H$; bottom wire $\ket{0}$ has two CNOT targets, the first controlled by $\ket{a}$ and the second controlled by $\ket{b}$] (78)

   (a) If $\ket{a} = \ket{+}$ and $\ket{b} = \ket{+}$, then find the resulting state at the end of the circuit.
   (b) If $\ket{a} = \ket{+}$ and $\ket{b} = \ket{-}$, then find the resulting state at the end of the circuit.
   (c) If $\ket{a} = \ket{-}$ and $\ket{b} = \ket{+}$, then find the resulting state at the end of the circuit.

18
