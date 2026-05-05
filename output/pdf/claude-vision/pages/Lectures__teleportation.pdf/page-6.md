$\{\ket{0,0}\bra{0,0}, \ket{0,1}\bra{0,1}, \ket{1,0}\bra{1,0}, \ket{1,1}\bra{1,1}\}$

- <u>Outcome $(0,0)$</u>: $\Pr(0,0) = \text{Tr}\left[(\ket{0,0}\bra{0,0}_{A'A} \otimes \mathbb{1}_B) \ket{\phi}\bra{\phi}_{A'AB}\right]$

$$\downarrow$$

$$= \text{Tr}\left[(\bra{0,0}_{A'A} \otimes \mathbb{1}_B) \ket{\phi}\bra{\phi}_{A'AB} (\ket{0,0}_{A'A} \otimes \mathbb{1}_B)\right]$$

$(\bra{0,0}_{A'A} \otimes \mathbb{1}_B)\ket{\phi}_{A'AB} = (\bra{0,0}_{A'A} \otimes \mathbb{1}_B) \tfrac{1}{2}\Big(\ket{0,0}_{A'A}(\alpha\ket{0}+\beta\ket{1})_B + \ket{0,1}_{A'A}(\alpha\ket{1}+\beta\ket{0})_B$

$$+ \ket{1,0}_{A'A}(\alpha\ket{0}-\beta\ket{1})_B + \ket{1,1}_{A'A}(\alpha\ket{1}-\beta\ket{0})_B\Big)$$

$$\downarrow$$

$$= \tfrac{1}{2}\Big(\underbrace{\braket{0,0|0,0}_{A'A}}_{1}(\alpha\ket{0}+\beta\ket{1})_B + \underbrace{\braket{0,0|0,1}_{A'A}}_{0}(\alpha\ket{1}+\beta\ket{0})_B$$

$$+ \underbrace{\braket{0,0|1,0}_{A'A}}_{0}(\alpha\ket{0}-\beta\ket{1})_B + \underbrace{\braket{0,0|1,1}_{A'A}}_{0}(\alpha\ket{1}-\beta\ket{0})_B\Big)$$

$$\downarrow$$

$$= \tfrac{1}{2}(\alpha\ket{0}_B + \beta\ket{1})$$

$$\downarrow$$

$$= \tfrac{1}{2}\ket{\psi}_B \;\;\Rightarrow\;\; \Pr(0,0) = \text{Tr}\left[\tfrac{1}{2}\ket{\psi}\bra{\psi}\tfrac{1}{2}\right] = \tfrac{1}{4}\underbrace{\text{Tr}[\ket{\psi}\bra{\psi}]}_{=1} = \tfrac{1}{4}.$$

<span style="color:red">State of Bob conditioned on outcome $(0,0)$ is $\ket{\psi}$!  
(Exactly the state Alice wanted to send.)</span>

- <u>Outcome $(0,1)$</u>: $\Pr(0,1) = \text{Tr}\left[(\ket{0,1}\bra{0,1}_{A'A} \otimes \mathbb{1}_B) \ket{\phi}\bra{\phi}_{A'AB}\right]$

$$\downarrow$$

$$= \text{Tr}\left[(\bra{0,1}_{A'A} \otimes \mathbb{1}_B)\ket{\phi}\bra{\phi}_{A'AB}(\ket{0,1}_{A'A}\otimes\mathbb{1}_B)\right].$$

$$\ket{\phi}_{A'AB} = \tfrac{1}{2}\Big(\ket{0,0}_{A'A}(\alpha\ket{0}+\beta\ket{1})_B + \underline{\ket{0,1}_{A'A}(\alpha\ket{1}+\beta\ket{0})_B}$$

$$+ \ket{1,0}_{A'A}(\alpha\ket{0}-\beta\ket{1})_B + \ket{1,1}_{A'A}(\alpha\ket{1}-\beta\ket{0})_B\Big)$$

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$

$X\ket{\psi} = \alpha X\ket{0} + \beta X\ket{1} = \alpha\ket{1} + \beta\ket{0}$

$(\bra{0,1}_{A'A} \otimes \mathbb{1}_B)\ket{\phi}_{A'AB} = \tfrac{1}{2}(\alpha\ket{1}+\beta\ket{0}) = \tfrac{1}{2}X\ket{\psi}_B.$ <span style="color:red">$\to$ Pauli $X$.</span>

$$\text{Tr}\left[\tfrac{1}{2}X\ket{\psi}\bra{\psi}X\tfrac{1}{2}\right] = \tfrac{1}{4}\text{Tr}[X\ket{\psi}\bra{\psi}X] = \tfrac{1}{4}\text{Tr}[\ket{\psi}\bra{\psi}] = \tfrac{1}{4}.$$

$\Rightarrow \Pr(0,1) = \tfrac{1}{4}$  $\qquad\qquad$ <span style="color:blue">$X^2 = \mathbb{1}$</span>
