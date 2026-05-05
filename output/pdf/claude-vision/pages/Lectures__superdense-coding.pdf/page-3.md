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
