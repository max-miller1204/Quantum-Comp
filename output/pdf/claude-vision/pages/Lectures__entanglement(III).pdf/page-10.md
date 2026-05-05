a unitary are complex numbers with unit modulus.

$\Rightarrow \det(u) = \lambda_1 \lambda_2 \cdots \lambda_d$ is a complex number with unit modulus.

$\Rightarrow |\det(u)|^2 = 1.$

$\Rightarrow (u \otimes u) \ket{\Psi^-}\bra{\Psi^-} (u \otimes u)^\dagger = |\det(u)|^2 \ket{\Psi^-}\bra{\Psi^-} = \ket{\Psi^-}\bra{\Psi^-}.$ ∎

- The vectors $\{u^\dagger \ket{0}, u^\dagger \ket{1}\}$ define a measurement, with measurement operators $M_0 = u^\dagger \ket{0}\bra{0} u$, $M_1 = u^\dagger \ket{1}\bra{1} u$.

$$M_0 + M_1 = u^\dagger \ket{0}\bra{0} u + u^\dagger \ket{1}\bra{1} u = u^\dagger \underbrace{(\ket{0}\bra{0} + \ket{1}\bra{1})}_{=\mathbb{1}} u = u^\dagger u = \mathbb{1}. \checkmark$$

Probability distribution is:

$$\Pr(i,j) = \mathrm{Tr}\big[ (M_i \otimes M_j) \ket{\Psi^-}\bra{\Psi^-}_{AB} \big] = \mathrm{Tr}\big[ (u^\dagger \ket{i}\bra{i} u \otimes u^\dagger \ket{j}\bra{j} u) \ket{\Psi^-}\bra{\Psi^-}_{AB} \big]$$

$\textcolor{blue}{(X_1 \otimes Y_1)(X_2 \otimes Y_2) = X_1 X_2 \otimes Y_1 Y_2}$

$$= \mathrm{Tr}\big[ (u^\dagger \otimes u^\dagger) \ket{i,j}\bra{i,j} (u \otimes u) \ket{\Psi^-}\bra{\Psi^-}_{AB} \big]$$

$$= \mathrm{Tr}\big[ \ket{i,j}\bra{i,j} \underbrace{(u \otimes u) \ket{\Psi^-}\bra{\Psi^-} (u \otimes u)^\dagger}_{= \ket{\Psi^-}\bra{\Psi^-} \text{ (from above)}} \big]$$

$$= \mathrm{Tr}\big[ \ket{i,j}\bra{i,j} \ket{\Psi^-}\bra{\Psi^-} \big]$$

$\Rightarrow$ Same distribution as the $\{\ket{0}, \ket{1}\}$ basis! So still anti-correlated!

$\textcolor{red}{\circledast \text{ We can formalize this idea into an } \underline{\text{experimental test}} \text{ for entanglement.}}$
