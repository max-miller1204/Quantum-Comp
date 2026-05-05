# CS 4134 – Quantum Computation and Information Processing

## Assignment 5

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

**Issue date:** Monday, March 16, 2026

**Due date:** Tuesday, March 24, 2026

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others, but you must write your own solutions, in your own words. Use of AI tools is not prohibited, but be prepared to explain your solutions and demonstrate your understanding to me on the board upon request at any time. Sticking to the deadline is to your benefit, but there is no late penalty. If you would like the assignment to count towards your final grade, then submit it before the final day of class in May. Submit a physical copy in class or an electronic copy via Canvas.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction. You must submit the assignment with at least one problem attempted in order to get a grade. Blank submissions will receive a grade of zero.

---

1. Calculate both $\text{Tr}_A[M_{AB}]$ and $\text{Tr}_B[M_{AB}]$ for the following two-qubit matrix.

$$M_{AB} = \begin{pmatrix} 1-i & 2+3i & -5 & i \\ -4 & 7-2i & 1+2i & 0 \\ 1 & 4i & -2 & 6+3i \\ 2i & 1 & -i & 3-i \end{pmatrix} \tag{1}$$

2. Let $\Phi^-_{AB} = \ket{\Phi^-}\bra{\Phi^-}_{AB}$. Prove that $\text{Tr}_B[\Phi^-_{AB}] = \frac{1}{2}\mathbb{1}_A$ and $\text{Tr}_A[\Phi^-_{AB}] = \frac{1}{2}\mathbb{1}_B$.

3. (a) Describe in words what the quantum teleportation protocol is, i.e., its purpose, what it achieves, and how.

   (b) Draw the quantum circuit for the quantum teleportation protocol. State the definition of every gate and/or measurement you draw in the circuit.

4. (a) State the mathematical definition of a quantum measurement, also known as a "positive operator-valued measure" (POVM).

   (b) Write down an example of a POVM, with justification.

5. (a) State the definition of the Schmidt decomposition of a bipartite state vector $\ket{\psi}_{AB}$.

   (b) Under what condition(s), based on the Schmidt decomposition, is $\ket{\psi}_{AB}$ entangled?

   (c) Based on the Schmidt decomposition, determine (with justification) whether or not the following state vectors are entangled.

   i. $\frac{1}{\sqrt{3}}\ket{0}\ket{+} + \sqrt{\frac{2}{3}}\ket{1}\ket{-}$.

   ii. $\frac{1}{4}\left(3\ket{0,0} - \sqrt{3}\ket{0,1} + \sqrt{3}\ket{1,0} - \ket{1,1}\right)$.

   iii. $\frac{1}{\sqrt{2}}(\ket{1,0} + i\ket{1,1})$.

1
