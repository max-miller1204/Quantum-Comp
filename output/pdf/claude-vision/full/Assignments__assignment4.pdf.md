# Assignments__assignment4.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Assignment 4

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

---

**Issue date:** Tuesday, February 24, 2026

**Due date:** Tuesday, March 3, 2026

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others, but you must write your own solutions, in your own words. Use of AI tools is not prohibited, but be prepared to explain your solutions and demonstrate your understanding to me on the board upon request at any time. Sticking to the deadline is to your benefit, but there is no late penalty. If you would like the assignment to count towards your final grade, then submit it before the final day of class in May. Submit a physical copy in class or an electronic copy via Canvas.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction. You must submit the assignment with at least one problem attempted in order to get a grade. Blank submissions will receive a grade of zero.

---

1. Consider the bipartite state $\rho_{AB} = \frac{1}{2}\big(\ket{0,0}\bra{0,0}_{AB} + \ket{1,1}\bra{1,1}_{AB}\big)$ of Alice ($A$) and Bob ($B$).

   (a) If Alice and Bob both measure in the $\{\ket{0}, \ket{1}\}$ basis, then prove that their outcomes are correlated, i.e., $\Pr[0,0] = \Pr[1,1] = \frac{1}{2}$ and $\Pr[0,1] = \Pr[1,0] = 0$. Calculate the post-measurement states of Bob's qubit conditioned on Alice's two outcomes, and demonstrate that Bob always gets the same outcome as Alice.

   (b) Now suppose that Alice and Bob both measure in the $\{\ket{+}, \ket{-}\}$ basis. Prove that their measurement outcomes are now completely uncorrelated: regardless of what outcome Alice gets, Bob's outcomes are completely random.

2. Consider two arbitrary state vectors, $\ket{\psi_1} = \alpha_1 \ket{0} + \beta_1 \ket{1}$ and $\ket{\psi_2} = \alpha_2 \ket{0} + \beta_2 \ket{1}$, where $\alpha_1, \beta_1, \alpha_2, \beta_2 \in \mathbb{C}$. Prove that there does not exist any choices of $\alpha_1, \beta_1, \alpha_2, \beta_2$ such that $\ket{\psi_1} \otimes \ket{\psi_2} = \ket{\Phi^+} = \frac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1})$. Hence $\ket{\Phi^+}$ is an entangled state vector.

3. For a density operator $\rho \in \mathrm{L}(\mathbb{C}^d)$, consider a spectral/eigenvalue decomposition as follows: $\rho = \sum_{k=1}^{d} \lambda_k \ket{\psi_k}\bra{\psi_k}$, where $\lambda_k$ are the eigenvalues and $\ket{\psi_k}$ are the associated eigenvectors.

   (a) What properties do the eigenvectors and eigenvalues have based on the definition of eigenvalues/eigenvectors and the three-part definition of a density operator?

   (b) Write down the square root of $\rho$, denoted $\sqrt{\rho}$ or $\rho^{1/2}$, in terms of the spectral decomposition given above.

   (c) Prove that $\ket{\psi_\rho} \coloneqq \mathrm{vec}(\sqrt{\rho}) = (\mathbb{1} \otimes \sqrt{\rho})\ket{\Gamma}$ is a purification of $\rho$.

   (d) Show that $\ket{\psi_\rho} = \sum_{k=1}^{d} \sqrt{\lambda_k}\, \overline{\ket{\psi_k}} \otimes \ket{\psi_k}$.

4. Let $X, Y, Z$ denote the Pauli operators. Prove the following identities.

   (a) $\frac{1}{4}\big(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X - Y \otimes Y + Z \otimes Z\big) = \ket{\Phi^+}\bra{\Phi^+}$.

---

1

## Page 2

(b) $\frac{1}{2}\left(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X + Y \otimes Y + Z \otimes Z\right) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$

5. Consider the following two-qubit density operator $\rho_{AB}$ of Alice and Bob:

$$\rho_{AB} = p_1 \ket{\Phi^+}\bra{\Phi^+}_{AB} + p_2 \ket{\Phi^-}\bra{\Phi^-}_{AB} + p_3 \ket{\Psi^+}\bra{\Psi^+}_{AB} + p_4 \ket{\Psi^-}\bra{\Psi^-}_{AB}, \tag{1}$$

where $p_1, p_2, p_3, p_4$ are probabilities ($p_1, p_2, p_3, p_4 \in [0,1]$ and $p_1 + p_2 + p_3 + p_4 = 1$) and we recall the two-qubit Bell state vectors:

$$\ket{\Phi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}), \quad \ket{\Psi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0}). \tag{2}$$

Suppose that Alice and Bob both measure their qubits with respect to the Pauli-$z$ basis; i.e., the POVM is $\{\ket{0}\bra{0}, \ket{1}\bra{1}\}$. What is the probability that they obtain *different* measurement outcomes?

6. Consider the state vector $\ket{\Psi^-}_{AB}$ of Alice and Bob, defined in (2).

   (a) If Alice and Bob both measure in the computational basis, then how are their outcomes correlated?
   
   (b) For every measurement outcome of Alice, calculate the corresponding post-measurement state of Bob.
   
   (c) Let $U \in \mathrm{L}(\mathbb{C}^2)$ be an arbitrary $2 \times 2$ unitary matrix. Prove that $(U \otimes U)\ket{\Psi^-}\bra{\Psi^-}(U \otimes U)^\dagger = \ket{\Psi^-}\bra{\Psi^-}$.
   
   (d) Conclude that if Alice and Bob both do a measurement with respect to the same but arbitrary basis, then their outcomes are always correlated in the same way as in the computational-basis measurement.

2
