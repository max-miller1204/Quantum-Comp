- **But this is not the case for all measurements!**
  If they both measure in $\{\ket{+}, \ket{-}\}$ basis instead, then the outcomes are completely uncorrelated!
  $$\Pr(+,+) = \Pr(+,-) = \Pr(-,+) = \Pr(-,-) = \tfrac{1}{4}.$$

  If Alice gets outcome "+" (happens with probability $\tfrac{1}{2}$), then Bob's state is
  $$\rho_B^{(+)} = \tfrac{1}{1/2} \operatorname{Tr}_A\!\left[(\ket{+}\!\bra{+}_A \otimes \mathbb{1}_B)\rho_{AB}\right] = \tfrac{\mathbb{1}}{2} \rightarrow \text{completely random for Bob!}$$

- So, in this case, the correlations depend on the basis choice!

✱ **Aside**: All states of two probabilistic bits can be expressed as diagonal density matrices in the computational basis.

$$\rho_{AB} = \begin{array}{c} {\scriptstyle 00} \\ {\scriptstyle 01} \\ {\scriptstyle 10} \\ {\scriptstyle 11} \end{array}\!\!\begin{pmatrix} p_{00} & & & 0 \\ & p_{01} & & \\ & & p_{10} & \\ 0 & & & p_{11} \end{pmatrix}$$
$$\quad\quad\,\,\,{\scriptstyle 00\;\;01\;\;10\;\;11}$$

✱ Even one bit!
$$\rho = \begin{pmatrix} p_1 & \\ & p_2 \end{pmatrix} = \tfrac{1}{2}\left(p_1 \ket{0}\!\bra{0} + p_2 \ket{1}\!\bra{1}\right)$$
describes an arbitrary state of one bit!
