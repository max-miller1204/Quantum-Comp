- Marginal distributions are given by the partial trace:
  - Marginal for Alice: $\rho_A = \frac{1}{2}\mathbb{1}_A \Rightarrow \Pr_A[+] = \Pr_A[-] = \frac{1}{2}$
  - Marginal for Bob: $\rho_B = \frac{1}{2}\mathbb{1}_B \Rightarrow \Pr_B[+] = \Pr_B[-] = \frac{1}{2}$
  - Product of the marginals: $\Pr_A[+]\cdot\Pr_B[+] = \frac{1}{4}$, $\Pr_A[+]\cdot\Pr_B[-] = \frac{1}{4}$
  
  $P_{XY} = P_X \cdot P_Y$
  
  $$\Pr_A[-]\cdot\Pr_B[+] = \frac{1}{4}, \quad \Pr_A[-]\cdot\Pr_B[-] = \frac{1}{4}.$$

  This is the same as the joint distribution calculated above!
  So Alice and Bob's random variables are independent $\Rightarrow$ no correlation.

- But for $\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}(\ket{0}_A\ket{1}_B - \ket{1}_A\ket{0}_B)$, the outcomes are still perfectly anti-correlated!

  - $(\bra{+}_A \otimes \bra{+}_B)\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}\big(\underbrace{\braket{+|0}}_{=\frac{1}{\sqrt{2}}}\underbrace{\braket{+|1}}_{\frac{1}{\sqrt{2}}} - \braket{+|1}\braket{+|0}\big) = 0 \Rightarrow \underline{\Pr[+,+] = 0}$
  
  - $(\bra{+}_A \otimes \bra{-}_B)\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}\big(\underbrace{\braket{+|0}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{-|1}}_{-\frac{1}{\sqrt{2}}} - \underbrace{\braket{+|1}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{-|0}}_{\frac{1}{\sqrt{2}}}\big) = \frac{1}{\sqrt{2}}\left(-\frac{1}{2}-\frac{1}{2}\right) = -\frac{1}{\sqrt{2}}$
  
  $$\Rightarrow \underline{\Pr[+,-] = \big|(\bra{+}_A \otimes \bra{-}_B)\ket{\Psi^-}_{AB}\big|^2 = \frac{1}{2}}$
  
  - $(\bra{-}_A \otimes \bra{+}_B)\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}\big(\underbrace{\braket{-|0}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{+|1}}_{\frac{1}{\sqrt{2}}} - \underbrace{\braket{-|1}}_{-\frac{1}{\sqrt{2}}}\underbrace{\braket{+|0}}_{\frac{1}{\sqrt{2}}}\big) = \frac{1}{\sqrt{2}}\left(\frac{1}{2}+\frac{1}{2}\right) = \frac{1}{\sqrt{2}}$
  
  $$\Rightarrow \underline{\Pr[-,+] = \big|(\bra{-}_A \otimes \bra{+}_B)\ket{\Psi^-}_{AB}\big|^2 = \frac{1}{2}}$
  
  - $(\bra{-}_A \otimes \bra{-}_B)\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}\big(\underbrace{\braket{-|0}}_{=\frac{1}{\sqrt{2}}}\underbrace{\braket{-|1}}_{-\frac{1}{\sqrt{2}}} - \underbrace{\braket{-|1}}_{-\frac{1}{\sqrt{2}}}\underbrace{\braket{-|0}}_{\frac{1}{\sqrt{2}}}\big) = 0 \Rightarrow \underline{\Pr[-,-] = 0}.$
