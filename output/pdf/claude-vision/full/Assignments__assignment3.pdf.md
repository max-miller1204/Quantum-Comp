# Assignments__assignment3.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Assignment 3

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

**Issue date:** Tuesday, February 17, 2026

**Due date:** Tuesday, February 24, 2026 (Submit by this date to ensure it is graded and returned to you before the next exam.)

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others, but you must write your own solutions, in your own words. Use of AI tools is not prohibited, but be prepared to explain your solutions and demonstrate your understanding to me on the board upon request at any time. Sticking to the deadline is to your benefit, but there is no late penalty. If you would like the assignment to count towards your final grade, then submit it before the final day of class in May. Submit a physical copy in class or an electronic copy via Canvas.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction. You must submit the assignment with at least one problem attempted in order to get a grade. Blank submissions will receive a grade of zero.

---

1. Two qubits are in the state given by the vector

$$\frac{\mathrm{i}}{\sqrt{10}}\ket{0,0} + \frac{1-2\mathrm{i}}{\sqrt{10}}\ket{0,1} + \frac{\mathrm{e}^{\mathrm{i}\pi/100}}{\sqrt{10}}\ket{1,0} + \frac{\sqrt{3}}{\sqrt{10}}\ket{1,1}. \tag{1}$$

   If we measure the qubits in the two-qubit $Z$-basis $\{\ket{0,0}, \ket{0,1}, \ket{1,0}, \ket{1,1}\}$, what are the possible measurement outcomes and their associated probabilities? What are the possible measurement outcomes and their associated probabilities if instead we measure in the two-qubit $X$-basis $\{\ket{+,+}, \ket{+,-}, \ket{-,+}, \ket{-,-}\}$?

2. Consider the following two state vectors:

$$\ket{v_1} = \frac{\sqrt{3}}{2}\ket{0} + \frac{\mathrm{i}}{2}\ket{1}, \tag{2}$$

$$\ket{v_2} = \frac{\mathrm{i}}{2}\ket{0} + \frac{\sqrt{3}}{2}\ket{1} \tag{3}$$

   (a) Prove that $\ket{v_1}$ and $\ket{v_2}$ are orthonormal.
   (b) Show that $\ket{v_1}\bra{v_1} + \ket{v_2}\bra{v_2} = \mathbb{1}$.
   (c) Consider a qubit in the state given by

$$\ket{u} = \frac{1}{2}\ket{0} - \frac{\sqrt{3}}{2}\ket{1}. \tag{4}$$

   Write this state vector in terms of $\ket{v_1}$ and $\ket{v_2}$.

   (d) If we measure the state given by $\ket{u}$ with respect to the measurement $\{\ket{v_1}\bra{v_1}, \ket{v_2}\bra{v_2}\}$, then what are the possible outcomes and their associated probabilities?

3. Let $X$, $Y$, and $Z$ be three discrete random variables for which we have the following probabilities:

$$\Pr[X=1, Y=1, Z=0] = p, \tag{5}$$

1

## Page 2

$$\Pr[X=1, Y=0, Z=1] = \frac{1}{2}(1-p), \tag{6}$$

$$\Pr[X=0, Y=1, Z=1] = \frac{1}{2}(1-p), \tag{7}$$

where $p \in (0,1)$.

   (a) What is the joint probability mass function of $X$ and $Y$?
   
   (b) Determine the covariance matrix for $X$ and $Y$.

4. Given any orthonormal basis $\{\ket{e_k}\}_{k=1}^d$ for $\mathbb{C}^d$, prove that $\mathbb{1}_d = \sum_{k=1}^d \ket{e_k}\bra{e_k}$.

5. Let $\{\ket{e_k}\}_{k=1}^d$ and $\{\ket{f_k}\}_{k=1}^d$ be two orthonormal bases for $\mathbb{C}^d$. Prove that $U = \sum_{k=1}^d \ket{e_k}\bra{f_k}$ is a unitary operator.

6. Consider the following quantum circuit:

   [Quantum circuit with three wires. Top wire: $\ket{a}$ — H — control dot — H. Middle wire: $\ket{b}$ — H — control dot — H. Bottom wire: $\ket{0}$ — target ($\oplus$) from top control — target ($\oplus$) from middle control. The two CNOTs target the bottom qubit, controlled by the top and middle qubits respectively, between the H gates.] $\tag{8}$

   (a) If $\ket{a} = \ket{+}$ and $\ket{b} = \ket{+}$, then find the resulting state at the end of the circuit.
   
   (b) If $\ket{a} = \ket{+}$ and $\ket{b} = \ket{-}$, then find the resulting state at the end of the circuit.
   
   (c) If $\ket{a} = \ket{-}$ and $\ket{b} = \ket{+}$, then find the resulting state at the end of the circuit.
   
   (d) If $\ket{a} = \ket{-}$ and $\ket{b} = \ket{-}$, then find the resulting state at the end of the circuit.
   
   (e) Using your answers to the previous parts, explain why this circuit calculates the parity of the first two qubits in the $X$ basis.

7. Consider an operator $U$ that performs the following mapping on the $Z$-basis state vectors:

$$U\ket{0} = \frac{1}{\sqrt{2}}(\ket{0} - \mathrm{i}\ket{1}), \quad U\ket{1} = \frac{1}{\sqrt{2}}(-\mathrm{i}\ket{0} + \ket{1}). \tag{9}$$

   (a) Express $U$ as a linear operator both in abstract bra-ket notation and as a matrix.
   
   (b) For arbitrary $\alpha, \beta \in \mathbb{C}$, what is $U(\alpha\ket{0} + \beta\ket{1})$?
   
   (c) Does $U$ represent a valid quantum gate? Explain your reasoning.

8. Let $H_{AB} \in \mathrm{L}(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B})$, $M_B \in \mathrm{L}(\mathbb{C}^{d_B})$, $N_B \in \mathrm{L}(\mathbb{C}^{d_B})$, and $P_A \in \mathrm{L}(\mathbb{C}^{d_A})$ be arbitrary linear operators. Prove the following facts about the partial trace.

   (a) $\mathrm{Tr}_A[P_A \otimes M_B] = \mathrm{Tr}[P_A]M_B$.
   
   (b) $\mathrm{Tr}_B[P_A \otimes M_B] = \mathrm{Tr}[M_B]P_A$.
   
   (c) $\mathrm{Tr}_A[(\mathbb{1}_A \otimes M_B)H_{AB}(\mathbb{1}_A \otimes N_B)] = M_B \mathrm{Tr}_A[H_{AB}]N_B$.

9. Consider an arbitrary linear operator $M_{AB} \in \mathrm{L}(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B})$ and an arbitrary density operator $\rho_A \in \mathrm{L}(\mathbb{C}^{d_A})$. Prove that

$$\mathrm{Tr}[M_{AB}(\rho_A \otimes \ket{0}\bra{0}_B)] = \mathrm{Tr}[M_A' \rho_A], \quad M_A' = (\mathbb{1}_A \otimes \bra{0}_B) M_{AB} (\mathbb{1}_A \otimes \ket{0}_B). \tag{10}$$

2
