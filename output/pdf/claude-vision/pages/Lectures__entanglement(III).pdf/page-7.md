- <u>Recall example from before</u>: $\rho_{AB} = \frac{1}{2}\left(\ket{0}\bra{0}_A \otimes \ket{1}\bra{1}_B + \ket{1}\bra{1}_A \otimes \ket{0}\bra{0}_B\right)$

  - This state is separable (not entangled).
  - If Alice and Bob both measure in $\{\ket{0}, \ket{1}\}$ basis, then:
    - They both get "0" and "1" w/ probability $\frac{1}{2}$.
      (i.e., locally, it looks completely random, b/c $\rho_A = \text{Tr}_B[\rho_{AB}] = \frac{1}{2}\mathbb{1}_A$ and $\rho_B = \text{Tr}_A[\rho_{AB}] = \frac{1}{2}\mathbb{1}_B$.)
    - But if they compare their measurement outcomes, they will always be the opposite! (Whenever Alice got a "0" or "1", Bob got "1" or "0".) So their outcomes are perfectly <u>anti-correlated</u>.

- But the same thing happens with the maximally-entangled state!

  $\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}(\ket{0}_A\ket{1}_B - \ket{1}_A\ket{0}_B)$ — in the $\{\ket{0}, \ket{1}\}$ basis, the outcomes are
  
  $\quad\quad\quad\quad\quad\;\; \underbrace{\;\;}_{\ket{e_1}}\;\underbrace{\;\;}_{\ket{f_1}}\;\;\underbrace{\;\;}_{\ket{e_2}}\;\underbrace{\;\;}_{\ket{f_2}}$
  
  perfectly anti-correlated!

- So how to distinguish the two? What makes the entangled state special?

- To see the difference, measure in a different basis! Say in the $\{\ket{+}, \ket{-}\}$ basis.

  - For $\rho_{AB} = \frac{1}{2}(\ket{0}\bra{0}_A \otimes \ket{1}\bra{1}_B + \ket{1}\bra{1}_A \otimes \ket{0}\bra{0}_B)$:

    $\Pr[+,+] = \text{Tr}\left[\left(\ket{+}\bra{+}_A \otimes \ket{+}\bra{+}_B\right)\rho_{AB}\right] = \frac{1}{2}\left(\underbrace{\braket{+|0}\braket{0|+}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{+|1}\braket{1|+}}_{\frac{1}{\sqrt{2}}} + \underbrace{\braket{+|1}\braket{1|+}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{+|0}\braket{0|+}}_{\frac{1}{\sqrt{2}}}\right)$

    $\left[\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} + \ket{1})\right]$
    
    $\quad\quad\quad\quad\quad\quad\quad\quad = \frac{1}{2}\left(\frac{1}{4} + \frac{1}{4}\right) = \frac{1}{4}.$

  Similarly: $\Pr[+,-] = \Pr[-,+] = \Pr[-,-] = \frac{1}{4}$.

  So the outcomes are completely <u>uncorrelated</u>!

  Why? B/c the joint distribution is a product of the marginal distributions.
