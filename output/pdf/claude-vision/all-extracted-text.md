# Assignments__assignment1.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Assignment 1

Virginia Tech Department of Computer Science, Spring 2026

Instructor: Sumeet Khatri

**Issue date:** Thursday, January 29, 2026

**Due date:** Thursday, February 5, 2026

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others, but you must write your own solutions, in your own words. Use of AI tools is not prohibited, but be prepared to explain your solutions and demonstrate your understanding to me on the board upon request at any time. Sticking to the deadline is to your benefit, but there is no late penalty. If you would like the assignment to count towards your final grade, then submit it before the final day of class in May. Submit in class or via email.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a four-point deduction.

---

1. Prove the following facts:

   (a) For complex numbers $z_1, z_2 \in \mathbb{C}$, $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$

   (b) If $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$, for any $d \in \{2, 3, \dots\}$, then $\braket{v_1 | v_2} = \overline{\braket{v_2 | v_1}}$.

2. Consider the following two-dimensional vector $\ket{v} \in \mathbb{C}^2$, written with respect to the standard basis $\{\ket{0}, \ket{1}\}$:
$$\ket{v} = \begin{pmatrix} 3 + 2\mathrm{i} \\ 4 + 5\mathrm{i} \end{pmatrix}. \tag{1}$$

   (a) Determine the values $\braket{0|v}$ and $\braket{1|v}$.

   (b) Write the vector $\ket{v}$ in the abstract form $\ket{v} = a\ket{0} + b\ket{1}$, with the appropriate values of $a$ and $b$.

   (c) Is the vector normalized? Say why or why not. If not normalized, then normalize it.

3. Consider the following three-dimensional vector $\ket{v} \in \mathbb{C}^3$, written with respect to the standard basis $\{\ket{0}, \ket{1}, \ket{2}\}$:
$$\ket{v} = \begin{pmatrix} 5 - \mathrm{i} \\ 6 + 3\mathrm{i} \\ 7 - 4\mathrm{i} \end{pmatrix}. \tag{2}$$

   (a) Determine the values $\braket{0|v}$, $\braket{1|v}$, and $\braket{2|v}$.

   (b) Write the vector $\ket{v}$ in the abstract form $\ket{v} = a\ket{0} + b\ket{1} + c\ket{2}$, with the appropriate values of $a$, $b$, and $c$.

   (c) Is the vector normalized? Say why or why not. If not normalized, then normalize it.

4. Calculate the inner products $\braket{v_1 | v_2}$ and $\braket{v_2 | v_1}$ of the following two vectors:
$$\ket{v_1} = (3 + 4\mathrm{i})\ket{0} + (2 - 5\mathrm{i})\ket{1}, \quad \ket{v_2} = \left(\frac{3}{4} + \frac{2\mathrm{i}}{5}\right)\ket{+} + \left(-\frac{7}{6} + \frac{\mathrm{i}}{3}\right)\ket{-}, \tag{3}$$

   where $\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$. Also calculate the norm of $\ket{v_1}$ and $\ket{v_2}$, and then normalize both vectors.

1


# Assignments__assignment2.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Assignment 2

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

**Issue date:** Thursday, February 5, 2026

**Due date:** Tuesday, February 10, 2026

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others, but you must write your own solutions, in your own words. Use of AI tools is not prohibited, but be prepared to explain your solutions and demonstrate your understanding to me on the board upon request at any time. Sticking to the deadline is to your benefit, but there is no late penalty. If you would like the assignment to count towards your final grade, then submit it before the final day of class in May. Submit a physical copy in class or an electronic copy via Canvas.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a four-point deduction.

---

1. (a) State the definition of a $d \times d$ Hermitian matrix in dimension $d \in \{2, 3, \dots\}$.
   (b) Write down the most general form of a $2 \times 2$ Hermitian matrix.
   (c) Prove that every $d \times d$ Hermitian matrix has real eigenvalues.

2. Draw a Bloch sphere and label the following locations.
   (a) Where a qubit is $\ket{0}$ and $\ket{1}$.
   (b) Where a qubit is $\ket{+}$ and $\ket{-}$.
   (c) Where a qubit is $\ket{+\mathrm{i}}$ and $\ket{-\mathrm{i}}$.

3. (a) State the three-part mathematical definition of a density operator, and explain each part of the definition.
   (b) State the mathematical definition of the purity of a quantum state.
   (c) Write down an example of a pure quantum state for one qubit.

1


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


# Assignments__assignment5.pdf

## Page 1

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


# Assignments__assignment6.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Assignment 6

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

---

**Date:** Thursday, April 2, 2026 (in class)

**Due:** End of class!

**Number of problems:** 3 + 1 BONUS problem

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others and ask the instructor for help. Use of AI tools is not prohibited, but remember that the assignments are preparation for the exam — so if you use AI, use it wisely! Use it to learn.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction. You must submit the assignment with at least one problem attempted in order to get a grade. Blank submissions will receive a grade of zero.

---

1. (BONUS, 10 points) Consider the following two-qubit density operator $\rho_{AB}$:

$$\rho_{AB} = (1-p)\ket{\Phi^+}\bra{\Phi^+}_{AB} + \frac{p}{3}\big(\ket{\Phi^-}\bra{\Phi^-}_{AB} + \ket{\Psi^+}\bra{\Psi^+}_{AB} + \ket{\Psi^-}\bra{\Psi^-}_{AB}\big),$$

where we recall the two-qubit Bell state vectors $\ket{\Phi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1})$ and $\ket{\Psi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0})$.

   (a) Suppose both qubits are measured in the Pauli-$Z$ basis. What is the distribution of outcomes? What is the probability that both outcomes are the same?

   (b) Suppose both qubits are measured according to the Bell measurement. What is the distribution of outcomes?

1

## Page 2

2

## Page 3

2. Does $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ represent a valid quantum gate? State why or why not. What is $U\ket{0}$ and $U\ket{1}$?

## Page 4

3. Let us use the following notation for the swap gate:

   [Two-qubit circuit diagram showing the swap gate: two horizontal wires connected by a vertical line with X markers on each wire]

   Show that the swap gate can be written in terms of three CNOT gates as follows:

   [Circuit identity: SWAP gate = three CNOT gates in sequence. First CNOT has control on top wire and target (⊕) on bottom wire. Second CNOT has control on bottom wire and target (⊕) on top wire. Third CNOT has control on top wire and target (⊕) on bottom wire.]

4

## Page 5

4. Consider the following circuit:

   [Two-qubit circuit: Top wire starts at $\ket{0}$, passes through $H$ gate, then acts as control of a controlled-$S$ gate, then a SWAP gate, then into Measurement box. Bottom wire starts at $\ket{0}$, passes through $S$ gate (target of controlled-$S$), then $H$ gate, then SWAP gate, then into Measurement box. Double lines exit the Measurement box as classical outputs.]

   What is the probability of obtaining each outcome when doing the following measurements.

   (a) Pauli-$Z$ measurement on each qubit.
   (b) Pauli-$X$ measurement on each qubit.
   (c) The two-qubit Bell measurement on both qubits.


# Assignments__assignment7.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Assignment 7

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

---

**Name:**

---

**Date:** Thursday, April 9, 2026 (in class)

**Due:** End of class!

**Number of problems:** 3

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others and ask the instructor for help. Use of AI tools is not prohibited, but remember that the assignments are preparation for the exam — so if you use AI, use it wisely! Use it to learn.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction. You must submit the assignment with at least one problem attempted in order to get a grade. Blank submissions will receive a grade of zero.

---

**For the grader only**

| Problem | 1 | 2 | 3 | Final Score |
|---------|---|---|---|-------------|
| Score   |   |   |   |             |

1

## Page 2

1. Show that the controlled-$Z$ gate can be written in terms of the Hadamard gate and the CNOT gate as follows:

[Circuit diagram: On the left, a two-qubit circuit with the top qubit having a control dot connected vertically to a $Z$ gate on the bottom qubit. Equals sign. On the right, a two-qubit circuit with the top qubit having a control dot, and the bottom qubit having an $H$ gate, then a target ($\oplus$) connected to the control, then another $H$ gate.]

2

## Page 3

2. Consider a probability distribution with two outcomes, 0 and 1, and the probabilities defined as follows:

$$\Pr[0] = \frac{1}{2}(1+\alpha), \quad \Pr[1] = \frac{1}{2}(1-\alpha).$$

Suppose that the value of $\alpha$ is unknown. Describe a procedure, based on repeatedly sampling from this probability distribution, that can be used to estimate the value of $\alpha$.

3

## Page 4

3. Consider the circuit below. Prove that this circuit can be used to calculate the imaginary part of the inner product $\braket{\psi|U|\psi}$, namely, $\text{Im}(\braket{\psi|U|\psi})$.

[Quantum circuit diagram: Top wire starts with $\ket{0}$, passes through $H$ gate, then $S^\dagger$ gate, then acts as control for a controlled-$U$ gate, then through another $H$ gate, then a measurement. Bottom wire starts with $\ket{\psi}$ and passes through the target $U$ gate controlled by the top wire.]

4


# Assignments__assignment8.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Assignment 8

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

---

**Name:**

---

**Date:** Thursday, April 23, 2026 (in class)

**Due:** End of class!

**Number of problems:** 3

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others and ask the instructor for help. Use of AI tools is not prohibited, but remember that the assignments are preparation for the exam — so if you use AI, use it wisely! Use it to learn.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction. You must submit the assignment with at least one problem attempted in order to get a grade. Blank submissions will receive a grade of zero.

---

**For the grader only**

| Problem | 1 | 2 | 3 | Final Score |
|---------|---|---|---|-------------|
| Score   |   |   |   |             |

1

## Page 2

1. Consider the following circuit:

   [Three-qubit circuit. Top wire: $\ket{0}$ — H — control — control — H — measurement. Middle wire: $\ket{0}$ — H — control — control — H — measurement. Bottom wire: $\ket{\psi}$ — target (CNOT from top qubit) — S — target (CNOT from middle qubit).]

   The state vector $\ket{\psi}$ is arbitrary, and the final measurement is in the Pauli-$Z$ basis.

   (a) Show that the probability of both measurement outcomes being 0 is $\frac{5}{8}$.
   
   (b) Calculate the state of the third qubit conditioned on each of the four measurement outcomes.

2

## Page 3

3

## Page 4

2. Prove the following circuit identities.

   (a) $\text{CNOT}(X \otimes \mathbb{1}) = (X \otimes X)\text{CNOT}$.

   [Circuit diagram: LHS shows top wire with $X$ gate then control dot, bottom wire with target $\oplus$. RHS shows top wire with control dot then $X$ gate, bottom wire with target $\oplus$ then $X$ gate. The two circuits are equated with $=$.]

   (b) $\text{CNOT}(\mathbb{1} \otimes Z) = (Z \otimes Z)\text{CNOT}$.

   [Circuit diagram: LHS shows top wire with control dot, bottom wire with $Z$ gate then target $\oplus$. RHS shows top wire with control dot then $Z$ gate, bottom wire with target $\oplus$ then $Z$ gate. The two circuits are equated with $=$.]

4

## Page 5

3. Staring from the $\ket{0}$ state vector, describe what gate(s) we would need to apply in order to generate the following state vectors. Provide justification. (*Hint:* Hadamard, rotation gates, and phase gates of the form $S(\theta) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}$, $\theta \in \mathbb{R}$, are sufficient.)

   (a) $\frac{1}{\sqrt{2}}(\ket{0} + \ket{1})$.

   (b) $\frac{1}{\sqrt{2}}(\ket{0} - \ket{1})$.

   (c) $\frac{1}{\sqrt{2}}(\ket{0} - i\ket{1})$.

   (d) $\cos(\theta/2)\ket{0} + \sin(\theta/2)\ket{1}$, for an arbitrary $\theta \in \mathbb{R}$.

   (e) $\frac{1}{\sqrt{2}}(\ket{0} + e^{i\theta}\ket{1})$, for an arbitrary $\theta \in \mathbb{R}$.

5


# Assignments__assignment9.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Assignment 9

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

---

**Name:**

---

**Date:** Thursday, April 30, 2026 (in class)

**Due:** End of class!

**Number of problems:** 3 + 1 BONUS

**Instructions:** Please show all of your work. Your grade will be based not only on getting the correct answer, but having a complete solution. You may work in collaboration with others and ask the instructor for help. Use of AI tools is not prohibited, but remember that the assignments are preparation for the exam — so if you use AI, use it wisely! Use it to learn.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction. You must submit the assignment with at least one problem attempted in order to get a grade. Blank submissions will receive a grade of zero.

---

**For the grader only**

| Problem | 1 | 2 | 3 | 4 | Final Score |
|---------|---|---|---|---|-------------|
| Score   |   |   |   |   |             |

1

## Page 2

1. State the definitions of a pure state and a mixed state. Write down one example of a pure state and one example of a mixed state, with justification.

## Page 3

2. Consider the state vector $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$, where $\alpha, \beta \in \mathbb{C}$ and $|\alpha|^2 + |\beta|^2 = 1$. Determine the outcome probabilities when measuring this state according to the measurement $\{\frac{2}{5}\ket{\psi_k}\bra{\psi_k}\}_{k=0}^{4}$, where $\ket{\psi_k} = \cos\left(\frac{2\pi k}{5}\right)\ket{0} + \sin\left(\frac{2\pi k}{5}\right)\ket{1}$, $k \in \{0, 1, 2, 3, 4\}$.

3

## Page 4

3. (a) Prove that the Pauli operators $X, Y, Z$ anti-commute: $XY = -YX$, $XZ = -ZX$, $YZ = -ZY$.

   (b) Prove that the Pauli operators are orthogonal: $\text{Tr}[XY] = \text{Tr}[XZ] = \text{Tr}[YZ] = 0$.

   (c) Consider an arbitrary operator $M \in \text{L}(\mathbb{C}^2)$ decomposed in terms of the Pauli operators as $M = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$. Verify that $c_0 = \text{Tr}[M]$, $c_1 = \text{Tr}[XM]$, $c_2 = \text{Tr}[YM]$, and $c_3 = \text{Tr}[ZM]$.

   (d) If we represent $M$ as a $2 \times 2$ matrix, $M = \begin{pmatrix} p & q \\ r & s \end{pmatrix}$, then show that $\text{Tr}[XM] = q + r$, $\text{Tr}[YM] = i(q - r)$, and $\text{Tr}[ZM] = p - s$.

4

## Page 5

4. (BONUS, 10 points) Let $\rho$ be an arbitrary single-qubit density operator, and let $X$, $Y$, $Z$ denote the Pauli operators. Prove that
$$\frac{1}{4}\rho + \frac{1}{4}X\rho X + \frac{1}{4}Y\rho Y + \frac{1}{4}Z\rho Z = \frac{1}{2}\mathbb{1}.$$
In other words, apply the gates $\mathbb{1}, X, Y, Z$ uniformly at random to any state makes the state maximally mixed. (*Hint:* What happens to the coordinates of the state in the Bloch sphere? Use the results of Problem 3.)

5


# Exam-2__exam2-cover.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Exam 2

Virginia Tech Department of Computer Science, Spring 2026

Instructor: Sumeet Khatri

---

**Name:**

---

**Date:** Thursday, March 5, 2026

**Number of problems:** 8

**Time allowed:** 75 minutes

**Instructions:** Please show all of your work. Your grade will be based not only on writing down the correct answer, but having a complete solution.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction.

---

**Potentially helpful definitions**

- Pauli matrices:

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

- Bell state vectors:

$$\ket{\Phi^+} = \frac{1}{\sqrt{2}}\big(\ket{0,0} + \ket{1,1}\big), \quad \ket{\Phi^-} = \frac{1}{\sqrt{2}}\big(\ket{0,0} - \ket{1,1}\big),$$

$$\ket{\Psi^+} = \frac{1}{\sqrt{2}}\big(\ket{0,1} + \ket{1,0}\big), \quad \ket{\Psi^-} = \frac{1}{\sqrt{2}}\big(\ket{0,1} - \ket{1,0}\big).$$

- Swap operator:

$$\mathbb{F} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

1


# Exam-3__exam3_cover_CS4134_Spring2026_25March2026-1.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Exam 3

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

---

**Name:**

---

**Date:** Thursday, March 26, 2026

**Number of problems:** 6

**Time allowed:** 75 minutes

**Instructions:** Please show all of your work. Your grade will be based not only on writing down the correct answer, but having a complete solution.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction.

---

**Potentially helpful definitions**

- Pauli matrices:

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

- Pauli-$X$ basis vectors: $\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$.

- Bell state vectors:

$$\ket{\Phi^+} = \frac{1}{\sqrt{2}}\big(\ket{0,0} + \ket{1,1}\big), \quad \ket{\Phi^-} = \frac{1}{\sqrt{2}}\big(\ket{0,0} - \ket{1,1}\big),$$

$$\ket{\Psi^+} = \frac{1}{\sqrt{2}}\big(\ket{0,1} + \ket{1,0}\big), \quad \ket{\Psi^-} = \frac{1}{\sqrt{2}}\big(\ket{0,1} - \ket{1,0}\big).$$

1


# Exam-4__exam4-cover.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Exam 4

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

---

**Name:**

---

**Date:** Thursday, April 16, 2026

**Number of problems:** 6

**Time allowed:** 75 minutes

**Instructions:** Please show all of your work. Your grade will be based not only on writing down the correct answer, but having a complete solution.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction.

---

**Potentially helpful definitions**

- Pauli matrices/gates: $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$

- Hadamard gate: $H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$

- Phase gate: $S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}.$

- Swap gate: $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$

- CNOT gate: $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}.$

---

**For the grader only**

| Problem | 1 | 2 | 3 | 4 | 5 | 6 | Final Score |
|---------|---|---|---|---|---|---|-------------|
| Score   |   |   |   |   |   |   |             |

1


# Exam-5__exam5_cover_CS4134_Spring2026_1May2026.pdf

## Page 1

# CS 4134 – Quantum Computation and Information Processing

## Exam 5

Virginia Tech Department of Computer Science, Spring 2026
Instructor: Sumeet Khatri

---

**Name:**

---

**Date:** Tuesday, May 5, 2026

**Number of problems:** 6

**Time allowed:** 75 minutes

**Instructions:** Please show all of your work. Your grade will be based not only on writing down the correct answer, but having a complete solution.

**Grading:** You will start from a grade of 100%. For every missed step, unclear or unexplained step, and mistake, you will lose two points, with a maximum of 10 points of deduction per problem. Unattempted problems result in a 10-point deduction.

---

**Potentially helpful definitions**

- Pauli matrices/gates: $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$

- Pauli-$X$ eigenvectors: $\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1}).$

- Hadamard gate: $H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$

- Phase gate: $S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}.$

- CNOT gate: $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}.$

**For the grader only**

| Problem | 1 | 2 | 3 | 4 | 5 | 6 | Final Score |
|---------|---|---|---|---|---|---|-------------|
| Score   |   |   |   |   |   |   |             |

1


# Lectures__entanglement(II).pdf

## Page 1

# ① Recap: Entanglement

❋ State vectors of two qubits belong to the tensor-product space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

(a) — A **product state (vector)** has the form:

(State vector) $\ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B$, $\ket{\phi_1} \in \mathbb{C}^{d_1}$, $\ket{\phi_2} \in \mathbb{C}^{d_2}$.

(Density operator). $\rho_{AB} = \sigma_A \otimes \tau_B$, $\sigma_A \in L(\mathbb{C}^{d_A})$ and $\tau_B \in L(\mathbb{C}^{d_B})$ are density operators.

[Diagram: Alice and Bob each with their own atom/system, separated]

$$\rho_{AB} = \sigma_A \otimes \tau_B$$

*Product state*
Alice and Bob individually prepare their systems.

— A **separable state** has the form: $\rho_{AB} = \sum_x p(x)\, \sigma_A^x \otimes \tau_B^x$

↳ Also called "classically correlated"   ↳ probabilities.

[Diagram: Alice and Bob each with their own atom/system, connected by a classical communication channel (double arrows between them)]

$$\rho_{AB} = \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Separable state*
Alice and Bob individually prepare their systems via local operations and classical communication.

## Page 2

- An **entangled state** is NOT a separable state.

[Diagram: Alice (left) and Bob (right) each with an atom symbol, connected by a wavy line representing entanglement]

$$\rho_{AB} \neq \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Entangled state*

Correlations between Alice and Bob are non-local.
State of the individual systems not sufficient to describe the pair.

⊛ The **Bell states**

**Pure States:**
$$\begin{cases} \Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}, & \ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}) \\ \Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}, & \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0}) \end{cases}$$

$$\ket{\Phi^+} = \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}\!\begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Phi^-} = \begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ -\tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Psi^+} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}, \quad \ket{\Psi^-} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ -\tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$$

Observe that $\{\ket{\Phi^\pm}, \ket{\Psi^\pm}\} \longleftrightarrow \{\underbrace{(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}}_{\ket{\Phi_{z,x}}} : z, x \in \{0,1\}\}$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \begin{matrix} Z^0 = \mathbb{1}, & Z^1 = Z \\ X^0 = \mathbb{1}, & X^1 = X \end{matrix}$$

$\quad 0,0 \leftrightarrow \Phi^+$
$\quad 0,1 \leftrightarrow \Psi^+$
$\quad 1,0 \leftrightarrow \Phi^-$
$\quad 1,1 \leftrightarrow \Psi^-$

$\ket{\Phi^-} = (Z \otimes \mathbb{1})\ket{\Phi^+}$
$\ket{\Psi^+} = (X \otimes \mathbb{1})\ket{\Phi^+}$
$\ket{\Psi^-} = (ZX \otimes \mathbb{1})\ket{\Phi^+}$

## Page 3

## ② Determining Entanglement.

✱ Given a state vector $\ket{\psi}$, how to determine if it is entangled or not?

Precisely: $\exists\, \ket{\phi_1}, \ket{\phi_2}$ s.t. $\ket{\psi} = \ket{\phi_1} \otimes \ket{\phi_2}$ ?

(a) $\ket{\psi}_{AB} \in \mathbb{C}^d \otimes \mathbb{C}^d \;\to\; \ket{\psi}_{AB} = \sum_{i,j=0}^{d-1} M_{i,j} \ket{i}_A \otimes \ket{j}_B$

$$\begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} \to \begin{pmatrix} a & c \\ b & d \end{pmatrix}$$

[arrow indicating that the two-index quantity ↔ matrix!]

Let $M = \sum_{i,j=0}^{d-1} M_{i,j} \ket{j}\bra{i} \in L(\mathbb{C}^d)$.

$M\ket{i} = \sum_{j=0}^{d-1} M_{i,j}\ket{j}$

**Lemma:** $\ket{\psi}_{AB} = (\mathbb{1} \otimes M)\ket{\Gamma_d}$, $\quad \ket{\Gamma_d} = \sum_{i=0}^{d-1} \ket{i} \otimes \ket{i}$.

$\left\{ d=2: \ket{\Gamma_2} = \ket{0}\ket{0} + \ket{1}\ket{1} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix} \right.$

**Proof:** $(\mathbb{1} \otimes M)\ket{\Gamma_d} = (\mathbb{1} \otimes M)\left(\sum_{i=0}^{d-1} \ket{i} \otimes \ket{i}\right) = \sum_{i=0}^{d-1} \ket{i} \otimes M\ket{i} = \sum_{i,j=0}^{d-1} M_{i,j}\ket{i} \otimes \ket{j} = \ket{\psi}_{AB}$. ∎

$\mathrm{vec}(M) := (\mathbb{1} \otimes M)\ket{\Gamma_d} \equiv \ket{M}\rangle \;\Rightarrow\;$ Stacking the **columns** into a vector!

**Example:** $d=2$, $M = \begin{matrix} & {\scriptstyle 0} & {\scriptstyle 1} \\ {\scriptstyle 0} & \begin{pmatrix} a & b \\ c & d \end{pmatrix} \end{matrix}$

[colored boxes grouping entries: green box around column 0 $(a,c)$, orange box around column 1 $(b,d)$, with arrows showing them stacked into the vector below]

$\Rightarrow \quad (\mathbb{1} \otimes M)\ket{\Gamma_2} = a\ket{0,0} + c\ket{0,1} + b\ket{1,0} + d\ket{1,1}$

$$= \begin{pmatrix} a \\ c \\ b \\ d \end{pmatrix}$$

✱ For every $\ket{\psi} \in \mathbb{C}^d \otimes \mathbb{C}^d$, $\exists\, M \in L(\mathbb{C}^d)$ such that $\ket{\psi} = \mathrm{vec}(M) = (\mathbb{1} \otimes M)\ket{\Gamma}$.

## Page 4

(b) Every $M \in L(\mathbb{C}^d)$ has a <u>Singular-value decomposition</u>:

$$M = U \Sigma V^\dagger$$

[arrows: $U$ and $V^\dagger$ labeled "unitaries"; $\Sigma$ labeled "matrix of singular values"]

In bra-ket notation: $\boxed{M = \sum_{k=1}^{r} S_k \ket{f_k}\bra{e_k}}$

[arrow to $S_k$: "singular values, $S_k > 0 \;\forall k$. (unique up to ordering)"]

rank $\equiv$ # of singular values $\to$ <u>unique</u>

$\{\ket{f_k}\}_k, \{\ket{e_k}\}_k$ are orthonormal (left and right singular vectors).

$$\Rightarrow \ket{\psi}_{AB} = \mathrm{vec}(M) = (\mathbb{1} \otimes M)\ket{\mathbb{1}_d} = \sum_{k=1}^{r} S_k \,\mathrm{vec}(\ket{f_k}\bra{e_k}) = \sum_{k=1}^{r} S_k \underbrace{\ket{\bar{e}_k}}_{A} \otimes \underbrace{\ket{f_k}}_{B}$$

$$= (\mathbb{1} \otimes \ket{f_k}\bra{e_k})\left(\sum_{i=0}^{d-1} \ket{i} \otimes \ket{i}\right) = \sum_{i=0}^{d-1} \ket{i} \otimes \ket{f_k}\bra{e_k}\ket{i}$$

$$= \underbrace{\sum_{i=0}^{d-1} \ket{i}\bra{i}\ket{\bar{e}_k} \otimes \ket{f_k}}_{\mathbb{1}} = \ket{\bar{e}_k} \otimes \ket{f_k}$$

[Right side:]
$\ket{e_k} = \sum_{i=0}^{d-1} c_i \ket{i}$

$c_i = \braket{i|e_k}$

$= \overline{\braket{i|e_k}} = \braket{i|\bar{e}_k}$ (circled)

$= \sum_{i=0}^{d-1} \bar{c}_i \ket{i}$

---

⊛ $\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{\bar{e}_k}_A \otimes \ket{f_k}_B$ is called the <u>Schmidt decomposition</u> of $\ket{\psi}_{AB}$.

⊛ $\{S_k\}_{k=1}^{r}$ are called <u>Schmidt coefficients</u>. (sometimes $\sqrt{S_k}$).
   $\;\hookrightarrow > 0$

(Normalisation: $\braket{\psi|\psi} = 1 \Rightarrow \sum_{k=1}^{r} S_k^2 = 1$)

$$1 = \braket{\psi|\psi} = \left(\sum_{k=1}^{r} S_k \bra{\bar{e}_k}_A \otimes \bra{f_k}\right)\left(\sum_{k'=1}^{r} S_{k'} \ket{\bar{e}_{k'}} \otimes \ket{f_{k'}}\right) = \sum_{k,k'=1}^{r} S_k S_{k'} \underbrace{\braket{\bar{e}_k|\bar{e}_{k'}}}_{\delta_{k,k'}} \underbrace{\braket{f_k|f_{k'}}}_{\delta_{k,k'}} = \sum_{k=1}^{r} S_k^2$$

## Page 5

> - If $r=1$, then $\ket{\psi} = \ket{e_1} \otimes \ket{f_1} \Rightarrow$ not entangled!
> - If $r>1$, then entangled!  $\quad r \equiv$ **Schmidt rank**.

(c) Observe: $\ket{\psi}_{AB} = \sum_{k=1}^{r} s_k \ket{\overline{e_k}}_A \otimes \ket{f_k}_B$

$$\Rightarrow \mathrm{Tr}_B[\ket{\psi}\bra{\psi}_{AB}] = \mathrm{Tr}_B\left[ \sum_{k,k'=1}^{r} s_k s_{k'} \ket{\overline{e_k}}\bra{\overline{e_{k'}}}_A \otimes \ket{f_k}\bra{f_{k'}}_B \right]$$

$$= \sum_{k,k'=1}^{r} s_k s_{k'} \ket{\overline{e_k}}\bra{\overline{e_{k'}}}_A \underbrace{\mathrm{Tr}[\ket{f_k}\bra{f_{k'}}]}_{=\,\delta_{k,k'}}$$

$$= \sum_{k=1}^{r} s_k^2 \ket{\overline{e_k}}\bra{\overline{e_k}}_A \quad \to \text{ Diagonal!}$$

Also, $\mathrm{Tr}_A[\ket{\psi}\bra{\psi}_{AB}] = \sum_{k=1}^{r} s_k^2 \ket{f_k}\bra{f_k}_B$

$\Rightarrow \mathrm{Tr}_A[\psi_{AB}]$ and $\mathrm{Tr}_B[\psi_{AB}]$ have the same (non-zero) eigenvalues!

(d) Suppose $r=d$, $s_k = \tfrac{1}{\sqrt{d}}\ \forall\ k \in \{1,2,\ldots,d\}$.

We call $\ket{\psi}$ **maximally entangled** (Note that the marginals are maximally mixed.).

(e) Observe: $\dfrac{1}{\sqrt{d}} \sum_{k=1}^{d} \ket{e_k} \otimes \ket{\overline{e_k}} = \dfrac{1}{\sqrt{d}} \sum_{k=1}^{d} \left( \sum_{j=0}^{d-1} \ket{j}\bra{j} \right) \ket{e_k} \otimes \left( \sum_{\ell=0}^{d-1} \ket{\ell}\bra{\ell} \right) \ket{\overline{e_k}}$

## Page 6

$$= \ket{\Phi_d^+}$$

$$= \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k,k}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{k=1}^{d} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \braket{j | e_k} \braket{\ell | \bar{e}_k} \qquad \overline{\braket{e_k|\ell}} = \braket{e_k|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{k=1}^{d} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \braket{j|e_k}\braket{e_k|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \bra{j} \underbrace{\left( \sum_{k=1}^{d} \ket{e_k}\bra{e_k} \right)}_{= \mathbb{1}_d \text{ b/c } \{\ket{e_k}\} \text{ is ONB!}} \ket{\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j,\ell=0}^{d-1} \ket{j,\ell} \braket{j|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j=0}^{d-1} \ket{j,j}$$

$$\downarrow$$
$$= \ket{\Phi_d^+}. \qquad \underline{\underline{\quad}}$$

---

$$\frac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1})$$

$$\frac{1}{\sqrt{2}}(\underbrace{\ket{0}}_{\ket{e_1}}\underbrace{\ket{1}}_{\ket{f_1}} + \underbrace{\ket{1}}_{\ket{e_2}}\underbrace{\ket{0}}_{\ket{f_2}})$$

---

**(f) Vectorized unitaries are maximally entangled**

$$\ket{\gamma}_{AB} = (\mathbb{1} \otimes U)\ket{\Phi_d^+} = \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \underbrace{\ket{k}}_{\equiv \ket{e_k}} \otimes \underbrace{U\ket{k}}_{\equiv \ket{f_k}}$$

(↑ unitary)

Also, 
$$\mathrm{Tr}_A\!\left[\ket{\gamma}\bra{\gamma}_{AB}\right] = \mathrm{Tr}_A\!\left[(\mathbb{1}_A \otimes U_B) \overbrace{\Phi^+_{AB}}^{\ket{\Phi_d^+}\bra{\Phi_d^+}_{AB}} (\mathbb{1}_A \otimes U_B^\dagger)\right]$$

$$\downarrow$$
$$= U\, \mathrm{Tr}_A\!\left[\Phi^+_{AB}\right] U^\dagger \quad (*)$$
$$\qquad \searrow = \frac{\mathbb{1}_B}{d}$$

$$\downarrow$$
$$= \frac{1}{d} U U^\dagger$$

$$\downarrow$$
$$= \frac{1}{d} \mathbb{1}_B \qquad \left(\text{Similar for } \mathrm{Tr}_A[\ket{\gamma}\bra{\gamma}_{AB}]\right).$$

$(M \otimes \mathbb{1})(\mathbb{1} \otimes N)$
$\quad = (\mathbb{1} \otimes N)(M \otimes \mathbb{1})$

$(*):$
$$= \sum_{k=0}^{d-1} (\bra{k}_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes U_B)\Phi^+(\mathbb{1}_A \otimes U_B^\dagger)(\ket{k}_A \otimes \mathbb{1})$$

$$= \sum_{k=0}^{d-1} U_B \bra{k}_A \Phi^+_{AB} \ket{k}_A U_B^\dagger = U_B\, \mathrm{Tr}_A[\Phi^+_{AB}]\, U_B^\dagger$$

## Page 7

<u>Proof of (\*)</u>: $\text{Tr}_A[\Phi^+_{AB}] = \frac{1}{d}\text{Tr}_A\left[\left(\sum_{k=0}^{d-1} \ket{k}_A\ket{k}_B\right)\left(\sum_{k'=0}^{d-1}\bra{k'}_A\bra{k'}_B\right)\right]$

$\ket{\Phi^+}_{AB} = \frac{1}{\sqrt{d}}\sum_{k=0}^{d-1}\ket{k}\ket{k}$

$$= \frac{1}{d}\sum_{k,k'=0}^{d-1}\underbrace{\text{Tr}_A\left[\ket{k}\bra{k'}_A \otimes \ket{k}\bra{k'}_B\right]}_{}$$

$$= \text{Tr}[\ket{k}\bra{k'}_A]\,\ket{k}\bra{k'}_B$$

$$= \delta_{k,k'}\,\ket{k}\bra{k'}_B$$

$$= \frac{1}{d}\sum_{k=0}^{d-1}\ket{k}\bra{k}_B$$

$$= \frac{1}{d}\mathbb{1}_B. \;\blacksquare$$

(g) Mixed-state entanglement is much harder to characterize! (More on this later...).

③ <u>Purification of mixed states</u>

(a) <u>Recall</u>: For qubits, pure states are on the surface of the Bloch sphere; mixed states are inside.

[Bloch sphere diagram with axes $x, y, z$; $\ket{0}$ at top (+z), $\ket{1}$ at bottom (−z), $\ket{+}$ on +x, $\ket{-}$ on −x (shown rotated), $\ket{+i}$ on +y, $\ket{-i}$ on −y]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$
$\alpha, \beta \in \mathbb{C},$
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

Qubit
$\ket{0}$ or $\ket{1}$;
or *superposition*

General mixed states have the form $\rho = \sum_{k=1}^{N} p_k \underbrace{\ket{\psi_k}\bra{\psi_k}}_{\text{pure states}}$.

$p_k \rightarrow$ probabilities.

## Page 8

(b) How do mixed states arise in nature?

1. Lack of knowledge of state preparation.

[Diagram: A box labeled "Source" with arrows pointing to:
- $\ket{\psi_1}$ w/ prob. $p_1$
- $\ket{\psi_2}$ w/ prob. $p_2$
- $\vdots$
- $\ket{\psi_N}$ w/ prob. $p_N$]

✸ Now someone uses the source to prepare a state, but they don't tell you which one it is. How do you describe your knowledge of the system?
$\hookrightarrow$ (They don't mention the label.)

$\rho_{XS}^\dagger = \rho_{XS}$

$\rho_{XS} \geq 0$

$\text{Tr}[\rho_{XS}] = 1$

$$\rho_{XS} = \sum_{k=1}^{N} p_k \underbrace{\ket{k}\bra{k}_X}_{\text{ONB}} \otimes \ket{\psi_k}\bra{\psi_k}_S \qquad \left(\text{This is a } \underline{\text{classical-quantum state}}\right)$$

[Red annotation pointing to $\ket{k}\bra{k}_X$: classical variable/register. ("which state is it"?)]

✸ To figure out what state the system is prepared in, we measure the "classical register" $X$.
(w.r.t. POVM $\{\ket{k}\bra{k}\}_{k=1}^{N}$)

$$\text{Tr}\left[(\ket{k}\bra{k}_X \otimes \mathbb{1}_S)\rho_{XS}\right] = \text{Tr}\left[(\ket{k}\bra{k}_X \otimes \mathbb{1}_S)\underbrace{\sum_{k'=1}^{N} p_{k'} \ket{k'}\bra{k'}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S}_{\rho_{XS}}\right]$$

$$= \sum_{k'=1}^{N} \text{Tr}\left[p_{k'} \underbrace{\ket{k}\braket{k|k'}\bra{k'}_X}_{\delta_{k,k'}} \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right]$$

$$= p_k \checkmark \quad (\text{as expected!})$$

[Brace below: State conditioned on outcome $k$] (i.e., you know what the label is).

## Page 9

$$\frac{\text{Tr}_X\left[\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\rho_{XS}\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\right]}{p_k}$$

$$= \frac{1}{p_k}\sum_{k'=1}^{N} \text{Tr}_X\left[\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\left(p_{k'}\ket{k'}\bra{k'}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right)\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\right]$$

$$\downarrow$$

$$= \frac{1}{p_k}\sum_{k'=1}^{N} p_{k'}\, \underbrace{\text{Tr}_X\left[\ket{k}\braket{k|k'}\braket{k'|k}\bra{k}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right]}_{=\,\delta_{k',k}\,\ket{\psi_{k'}}\bra{\psi_{k'}}}$$

$$\downarrow$$

$$= \frac{1}{p_k}\, p_k \ket{\psi_k}\bra{\psi_k}$$

$$= \ket{\psi_k}\bra{\psi_k} \quad \checkmark \quad (\text{as expected!})$$

✱ But if you don't know the outcome/label? $\rightarrow$ <u>Trace out the register X!</u>

$$\text{Tr}_X(\rho_{XS}) = \text{Tr}_X\left[\sum_{k=1}^{N} p_k \ket{k}\bra{k}_X \otimes \ket{\psi_k}\bra{\psi_k}_S\right]$$

$$\downarrow$$

$$= \sum_{k=1}^{N} p_k\, \underbrace{\text{Tr}_X\left[\ket{k}\bra{k}_X \otimes \ket{\psi_k}\bra{\psi_k}_S\right]}_{=\,\underbrace{\text{Tr}[\ket{k}\bra{k}]}_{=1}\,\ket{\psi_k}\bra{\psi_k}}$$

$$\downarrow$$

$$= \underline{\underline{\sum_{k=1}^{N} p_k \ket{\psi_k}\bra{\psi_k}.}}$$

**2. Measurement on one part of a pure state.**

$$\ket{\psi}_{AB} = \sum_{k=1}^{r} \sqrt{\lambda_k}\,\ket{e_k}_A \otimes \ket{f_k}_B \quad \rightarrow \text{ Measure } A \text{ wrt POVM } \{M_A^x\}_{x \in \mathcal{X}}$$

Conditioned on outcome $x$, state on $B$ is $\quad \dfrac{1}{p_x}\,\text{Tr}_A\left[\left(\sqrt{M_A^x}\otimes \mathbb{1}_B\right)\ket{\psi}\bra{\psi}_{AB}\left(\sqrt{M_A^x}\otimes \mathbb{1}_B\right)\right]$

## Page 10

$$p_x = \text{Tr}\left[(M_A^x \otimes \mathbb{1}_B)\ket{\psi}\bra{\psi}_{AB}\right] = \text{Tr}\left[M_A^x \, \text{Tr}_B\left[\ket{\psi}\bra{\psi}_{AB}\right]\right] = \sum_{k=1}^{r} \lambda_k \text{Tr}\left[M_A^x \ket{e_k}\bra{e_k}_A\right].$$

$$= \text{Tr}_B\left[\sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}} \ket{e_k}\bra{e_{k'}}_A \otimes \ket{f_k}\bra{f_{k'}}_B\right]$$

$$= \sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}} \ket{e_k}\bra{e_{k'}}_A \underbrace{\text{Tr}\left[\ket{f_k}\bra{f_{k'}}_B\right]}_{=\delta_{k,k'}}$$

$$= \sum_{k=1}^{r} \lambda_k \ket{e_k}\bra{e_k}_A$$

$$\text{Tr}_A\left[\left(\sqrt{M_A^x} \otimes \mathbb{1}_B\right)\ket{\psi}\bra{\psi}_{AB}\left(\sqrt{M_A^x} \otimes \mathbb{1}_B\right)\right] = \text{Tr}_A\left[\sum_{k,k'=1}^{r} \sqrt{M_A^x}\ket{e_k}\bra{e_{k'}}_A\sqrt{M_A^x} \otimes \ket{f_k}\bra{f_{k'}}_B\right]$$

$$= \sum_{k,k'=1}^{r} \text{Tr}\left[\sqrt{M_A^x}\ket{e_k}\bra{e_{k'}}_A\sqrt{M_A^x}\right] \ket{f_k}\bra{f_{k'}}_B$$

$$= \sum_{k,k'=1}^{r} \text{Tr}\left[M_A^x \ket{e_k}\bra{e_{k'}}_A\right] \ket{f_k}\bra{f_{k'}}_B \quad \rightarrow \text{Not a pure state in general.}$$

3. **Entanglement with an (unknown) environment.**

   Consider a mixed state $\rho_S = \sum_{k=1}^{r} \lambda_k \ket{\psi_k}\bra{\psi_k}$ (spectral decomposition).
   
   $\uparrow$ <span style="color:red">eigenvalues</span> $\quad$ <span style="color:red">eigenvectors (orthonormal).</span>

   ⊛ <u>Note</u>: $\text{Tr}(\rho_S) = 1 \implies \text{Tr}\left[\sum_{k=1}^{r} \lambda_k \underbrace{\text{Tr}\left[\ket{\psi_k}\bra{\psi_k}\right]}_{=1}\right] = \sum_{k=1}^{r} \lambda_k = 1$ (eigenvalues sum to one).

   ⊛ <u>Note</u>: $\rho_S \geq 0 \implies \lambda_k \geq 0 \;\forall\, k. \implies 0 \leq \lambda_k \leq 1 \;\forall\, k.$

## Page 11

$\circledast$ There exists a pure state $\ket{\psi}_{ES}$ such that $\mathrm{Tr}_E[\ket{\psi}\bra{\psi}_{ES}] = \rho_S$.

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}\underset{\text{\color{red}environment}}{\color{red}\uparrow}$

Proof: (by explicit construction) Consider $\sqrt{\rho_S} = \sum_{k=1}^{r} \sqrt{\lambda_k}\, \ket{\gamma_k}\bra{\gamma_k}$

Then $\ket{\psi}_{ES} = (\mathbb{1}_E \otimes \sqrt{\rho_S})\ket{\Gamma} = \left(\mathbb{1}_E \otimes \sum_{k=1}^{r}\sqrt{\lambda_k}\,\ket{\gamma_k}\bra{\gamma_k}_S\right)\ket{\Gamma}$

$\phantom{xxxxxx}\underset{\color{red}\dim(\mathcal{H}_E) \geq r}{\color{red}\uparrow} \phantom{xxxx} \underset{\color{red}\ket{\Gamma} = \sum_{k=0}^{d-1}\ket{k,k}}{\color{red}\uparrow}$

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}{\color{blue}\underline{\mathrm{vec}(\ket{e_k}\bra{f_k}) = \overline{\ket{f_k}} \otimes \ket{e_k}}}$

$\phantom{xx}= \sum_{k=1}^{r} \sqrt{\lambda_k}\, \underbrace{(\mathbb{1}_E \otimes \ket{\gamma_k}\bra{\gamma_k}_S)\ket{k,k}_{ES}}_{\color{red}\overline{\ket{\gamma_k}}_E \otimes \ket{\gamma_k}_S} = \sum_{k=1}^{r}\sqrt{\lambda_k}\,\overline{\ket{\gamma_k}}_E \otimes \ket{\gamma_k}_S$

- This is a state vector: $\braket{\psi|\psi} = \left(\sum_{k=1}^{r}\sqrt{\lambda_k}\,\bra{\overline{\gamma_k}}_E \otimes \bra{\gamma_k}_S\right)\left(\sum_{k'=1}^{r}\sqrt{\lambda_{k'}}\,\overline{\ket{\gamma_{k'}}}_E \otimes \ket{\gamma_{k'}}_S\right)$

$\phantom{xxxxxxxxxxxxxxxxx} = \sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}}\, \underbrace{\braket{\overline{\gamma_k}|\overline{\gamma_{k'}}}}_{\delta_{k,k'}} \underbrace{\braket{\gamma_k|\gamma_{k'}}}_{\delta_{k,k'}}$

$\phantom{xxxxxxxxxxxxxxxxx} = \sum_{k=1}^{r} \lambda_k$

$\phantom{xxxxxxxxxxxxxxxxx} = 1 \quad \checkmark$

- $\mathrm{Tr}_E[\ket{\psi}\bra{\psi}_{ES}] = \mathrm{Tr}_E\left[(\mathbb{1}_E \otimes \sqrt{\rho_S})\ket{\Gamma}\bra{\Gamma}_{ES}(\mathbb{1}_E \otimes \sqrt{\rho_S})\right]$

$\phantom{xxxxxxxxxxxxxxx} = \sqrt{\rho_S}\, \underbrace{\mathrm{Tr}_E[\ket{\Gamma}\bra{\Gamma}_{ES}]}_{}\, \sqrt{\rho_S}$

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx} {\color{blue}\ket{\Gamma} = \sum_{k=0}^{d-1}\ket{k,k}}$

## Page 12

$$= \sum_{k,k'=0}^{d-1} \mathrm{Tr}_E\left[\ket{k}\bra{k'}_E \otimes \ket{k}\bra{k'}_S\right]$$

$$= \sum_{k,k'=0}^{d-1} \delta_{k,k'} \ket{k}\bra{k'}_S$$

$$= \sum_{k=0}^{d-1} \ket{k}\bra{k}_S = \mathbb{1}_S.$$

$$= \rho_S \checkmark$$

$$\sqrt{\rho_S}\, \mathbb{1}\, \sqrt{\rho_S} = \rho_S$$


# Lectures__entanglement(III).pdf

## Page 1

# ① Determining Entanglement.

(a) Given a state vector $\ket{\psi}_{AB}$, how to determine if it is entangled or not?
Precisely: $\exists\, \ket{\phi_1}_A, \ket{\phi_2}_B$ s.t. $\ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B$ ?

✸ **Theorem (Schmidt Decomposition):** Every state vector $\ket{\psi}_{AB}$ can be written as

$$\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{e_k}_A \otimes \ket{f_k}_B. \qquad \left(\ket{\psi}_{AB} = \sum_{i,j=0}^{d-1} c_{i,j} \ket{i}_A \otimes \ket{j}_B\right)$$

- $r$: Schmidt rank
- $\{S_k\}_{k=1}^{r}$: Schmidt coefficients $S_k > 0\ \forall k$
- $\{\ket{e_k}_A\}_{k=1}^{r}$ and $\{\ket{f_k}_B\}_{k=1}^{r}$ are orthonormal vectors.

(**Proof** (recall): Write the vector $\ket{\psi}_{AB}$ as a matrix, then do the singular value decomposition of the matrix.)

- The Schmidt rank is **unique** — so we get the following criterion:

$$\boxed{\begin{array}{l} \bullet \text{ If } r = 1, \text{ then } \ket{\psi} = \ket{e_1} \otimes \ket{f_1} \Rightarrow \text{not entangled!} \\[4pt] \bullet \text{ If } r > 1, \text{ then entangled!} \qquad \ket{\mathcal{E}^+} = \tfrac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k}_A \ket{k}_B \end{array}}$$

(b) What about mixed states? More complicated!

- **Example:** convex mixtures of Bell states. $\left(\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}),\ \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0})\right)$

$$\rho_{AB} = p_1 \Phi^+_{AB} + p_2 \Phi^-_{AB} + p_3 \Psi^+_{AB} + p_4 \Psi^-_{AB}, \quad \text{probabilities } p_1, p_2, p_3, p_4 \in [0,1]$$

$$\Phi^\pm_{AB} = \ket{\Phi^\pm}\bra{\Phi^\pm}_{AB},\quad \Psi^\pm_{AB} = \ket{\Psi^\pm}\bra{\Psi^\pm}_{AB}. \qquad p_1 + p_2 + p_3 + p_4 = 1$$

## Page 2

- $p_1 = 1, p_2 = p_3 = p_4 = 0 \implies \rho_{AB} = \Phi^+_{AB} \implies$ entangled!

- $p_1 = 0, p_2 = 1, p_3 = p_4 = 0 \implies \rho_{AB} = \Phi^-_{AB} \implies$ entangled!

- $p_1 = p_2 = 0, p_3 = 1, p_4 = 0 \implies \rho_{AB} = \Psi^+_{AB} \implies$ entangled!

- $p_1 = p_2 = p_3 = 0, p_4 = 1 \implies \rho_{AB} = \Psi^-_{AB} \implies$ entangled!

- <u>But</u>: $p_1 = p_2 = p_3 = p_4 = \frac{1}{4} \implies \rho_{AB} = \frac{1}{4}\Phi^+_{AB} + \frac{1}{4}\Phi^-_{AB} + \frac{1}{4}\Psi^+_{AB} + \frac{1}{4}\Psi^-_{AB} = \frac{1}{4}\mathbb{1}_A \otimes \mathbb{1}_B$

  $\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ B/c Bell states form ONB.

  $\implies$ <u>not</u> entangled!

- General criterion: <u>Positive Partial Transpose (PPT) criterion</u>

<u>Recall</u>: Transpose of a matrix (flip rows and columns).

$\quad$ In Bra-ket notation: $\quad M = \sum_{i,j=0}^{d-1} m_{i,j} \ket{i}\bra{j}$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad M^T = \sum_{i,j=0}^{d-1} m_{i,j} \ket{j}\bra{i} \quad \rightsquigarrow (M^T)^T = M.$

$\quad$ For $M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B})$: $\quad M_{AB} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i}\bra{i'}_A \otimes \ket{j}\bra{j'}_B.$

$\quad$ <u>Partial transpose on A</u>: $\quad M_{AB}^{T_A} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i'}\bra{i}_A \otimes \ket{j}\bra{j'}_B.$

$\quad$ <u>Partial transpose on B</u>: $\quad M_{AB}^{T_B} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i}\bra{i'}_A \otimes \ket{j'}\bra{j}_B.$

$\quad$ <u>Full transpose</u>: $M_{AB}^T = M_{AB}^{T_A T_B} \implies M_{AB}^{T_A} = (M_{AB}^{T_B})^T$

$\quad\quad (M_{AB}^{T_A})^{T_A} = M_{AB} \quad\quad (M_{AB}^{T_B})^T = (M_{AB}^{T_B})^{T_A T_B} = M_{AB}^{T_A}$

## Page 3

For $M_{AB} = $

$$\begin{array}{c} \phantom{00}\;\;00\;\;\;\;\;01\;\;\;\;\;10\;\;\;\;\;11 \\ \begin{array}{c}00\\01\\10\\11\end{array}\!\!\left(\begin{array}{cccc} m_1 & m_2 & m_3 & m_4 \\ m_5 & m_6 & m_7 & m_8 \\ m_9 & m_{10} & m_{11} & m_{12} \\ m_{13} & m_{14} & m_{15} & m_{16} \end{array}\right) \end{array}$$

[Purple ovals/arrows indicate swapping pairs: $(m_2 \leftrightarrow m_5)$, $(m_4 \leftrightarrow m_7)$, $(m_{10} \leftrightarrow m_{13})$, $(m_{12} \leftrightarrow m_{15})$]

$$M_{AB}^{T_B} = \begin{array}{c} \phantom{00}\;\;00\;\;\;\;\;01\;\;\;\;\;10\;\;\;\;\;11 \\ \begin{array}{c}00\\01\\10\\11\end{array}\!\!\left(\begin{array}{cccc} m_1 & m_5 & m_3 & m_7 \\ m_2 & m_6 & m_4 & m_8 \\ m_9 & m_{13} & m_{11} & m_{15} \\ m_{10} & m_{14} & m_{12} & m_{16} \end{array}\right) \end{array}$$

---

[Reproductions of two journal article headers:]

**PHYSICAL REVIEW LETTERS**, Volume 77, 19 August 1996, Number 8 — "Separability Criterion for Density Matrices", Asher Peres, Department of Physics, Technion–Israel Institute of Technology, 32 000, Haifa, Israel (Received 8 April 1996)

**PHYSICS LETTERS A** 223 (1996) 1–8, 25 November 1996 — "Separability of mixed states: necessary and sufficient conditions", Michał Horodecki, Paweł Horodecki, Ryszard Horodecki (University of Gdańsk / Technical University of Gdańsk)

---

✸ **Theorem (PPT Criterion):** $\rho_{AB}$ separable $\Rightarrow \rho_{AB}^{T_A} \geq 0,\; \rho_{AB}^{T_B} \geq 0.$

$X \Rightarrow Y$
$\neg Y \Rightarrow \neg X$

✸ **Contrapositive:** $\rho_{AB}^{T_{A/B}} \not\geq 0 \;\Rightarrow\; \rho_{AB}$ entangled

$\Rightarrow$ Just check if $\rho_{AB}^{T_{A/B}}$ has a negative eigenvalue!

✸ **Converse:** $\rho_{AB}^{T_{A/B}} \geq 0 \;\xcancel{\Rightarrow}\; \rho_{AB}\text{ separable}$ $\;\longrightarrow$ NOT true in general!

(There are entangled states w/ positive partial transpose.)

(Example in this paper.)

## Page 4

[Header: Elsevier Physics Letters A 232 (1997) 333–339, "Separability criterion and inseparable mixed states with positive partial transposition" by Paweł Horodecki, 4 August 1997]

**Proof:** $\rho_{AB}$ separable $\Rightarrow \rho_{AB} = \sum_x p(x)\, \tau_A^x \otimes \omega_B^x$

$$\Rightarrow \rho_{AB}^{T_B} = \sum_x p(x)\, \underbrace{\tau_A^x}_{\geq 0} \otimes \underbrace{(\omega_B^x)^T}_{\geq 0} \geq 0$$

$M \geq 0 \Rightarrow M^T \geq 0$ (full transpose does not change eigenvalues.)

$\Rightarrow \rho_{AB}^{T_B} \geq 0. \quad \rho_{AB}^{T_A} = (\rho_{AB}^{T_B})^T \;\;$ ↪ Full transpose. $\;\Rightarrow \rho_{AB}^{T_A} \geq 0.$ ∎

---

[highlighted box:]
※ Converse **is** true for $2\otimes 2$ and $2\otimes 3$!

↳ $\rho_{AB}$ separable $\iff \rho_{AB}^{T_{A/B}} \geq 0.$

---

- **Examples of the PPT criterion:** $\quad \ket{\Phi^+} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0} + \ket{1}\ket{1}).$

$$-\;\rho_{AB} = \Phi_{AB}^+ = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} \Rightarrow \rho_{AB}^{T_B} = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$\underbrace{\hphantom{XXXXXXXXXXXXX}}_{\mathbb{F}_{AB} \;\to\; \text{swap operator.}}$

※ Eigenvalues of $\mathbb{F}_{AB}$ are $\pm 1.$

※ $\mathbb{F}_{AB} = \sum_{i,j=0}^{d-1} \ket{j,i}\bra{i,j} \quad (\mathbb{F}_{AB}\ket{i,j} = \ket{j,i})$

$\ket{j,i}\bra{i,j} \equiv \ket{j}\bra{i}\otimes\ket{i}\bra{j}$

$\mathbb{F}_{AB}\ket{0}\ket{0} = \ket{0}\ket{0}$
$\mathbb{F}_{AB}\ket{0}\ket{1} = \ket{1}\ket{0}$
$\mathbb{F}_{AB}\ket{1}\ket{0} = \ket{0}\ket{1}$
$\mathbb{F}_{AB}\ket{1}\ket{1} = \ket{1}\ket{1}$

## Page 5

(\*) $F_{AB}\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right) = \ket{\chi_2}_A \otimes \ket{\chi_1}_B.$

<u>Proof</u>: $F_{AB}\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right) = \left(\sum_{i,j=0}^{d-1} \ket{j}\bra{i}_A \otimes \ket{i}\bra{j}_B\right)\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right)$

$$= \sum_{i,j=0}^{d-1} \ket{j}\braket{i|\chi_1} \otimes \ket{i}\braket{j|\chi_2}$$

$$= \sum_{i,j=0}^{d-1} \ket{j}\braket{j|\chi_2} \otimes \ket{i}\braket{i|\chi_1}$$

$$= \underbrace{\left(\sum_{j=0}^{d-1} \ket{j}\bra{j}_A\right)}_{=\mathbb{1}_A}\ket{\chi_2}_A \otimes \underbrace{\left(\sum_{i=0}^{d-1} \ket{i}\bra{i}_B\right)}_{=\mathbb{1}_B}\ket{\chi_1}_B$$

$$= \ket{\chi_2}_A \otimes \ket{\chi_1}_B.$$

$p_1 = 1-p$
$p_2 = p_3 = p_4 = \frac{p}{3}.$

– <u>Isotropic state</u>: $\rho_{AB}^{(p)} = (1-p)\,\Phi_{AB}^+ + \frac{p}{3}\left(\Phi_{AB}^- + \Psi_{AB}^+ + \Psi_{AB}^-\right),\quad p \in [0,1].$

$$\rho_{AB}^{(p)} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{array}{cccc} 00 & 01 & 10 & 11 \end{array} \\ \left(\begin{array}{cccc} \frac{1-p}{2}+\frac{p}{6} & 0 & 0 & \frac{1-p}{2}-\frac{p}{6} \\ 0 & \frac{p}{3} & 0 & 0 \\ 0 & 0 & \frac{p}{3} & 0 \\ \frac{1-p}{2}-\frac{p}{6} & 0 & 0 & \frac{1-p}{2}+\frac{p}{6} \end{array}\right)$$

[Purple ovals/arrows indicate swapping the (00,11) anti-diagonal block with the (01,10) block under partial transpose]

$$\left(\rho_{AB}^{(p)}\right)^{T_B} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{array}{cccc} 00 & 01 & 10 & 11 \end{array} \\ \left(\begin{array}{cccc} \frac{1-p}{2}+\frac{p}{6} & 0 & 0 & 0 \\ 0 & \frac{p}{3} & \frac{1-p}{2}-\frac{p}{6} & 0 \\ 0 & \frac{1-p}{2}-\frac{p}{6} & \frac{p}{3} & 0 \\ 0 & 0 & 0 & \frac{1-p}{2}+\frac{p}{6} \end{array}\right)$$

## Page 6

Eigenvalues of $\left(\rho_{AB}^{(p)}\right)^{T_B}$:  $\quad \lambda_1 = \frac{1}{6}(3-2p) \quad$ (multiplicity 3)

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad \lambda_2 = \frac{1}{2}(-1+2p) \quad$ (multiplicity 1).

$\left(\text{\textcolor{purple}{\textasteriskcentered\ We need a negative eigenvalue for entanglement!}}\right)$

[Plot: x-axis labeled $p$ from 0 to 1.0, y-axis from $-0.4$ to $0.4$. Blue line: $\frac{1}{6}(3-2p)$, decreasing from $0.5$ at $p=0$ to about $0.17$ at $p=1$. Orange line: $\frac{1}{2}(-1+2p)$, increasing from $-0.5$ at $p=0$ through $0$ at $p=0.5$ to $0.5$ at $p=1$. Red dashed vertical line at $p=0.5$ marking the boundary. Region $p < 0.5$ labeled "Entangled", region $p > 0.5$ labeled "Separable".]

$$\rho_{AB}^{(p)} = (1-p)\,\Phi_{AB}^{+} + \frac{p}{3}\left(\Phi_{AB}^{-} + \Psi_{AB}^{+} + \Psi_{AB}^{-}\right)$$

\textcolor{red}{\textasteriskcentered\ Observe:} $\operatorname{Tr}\!\left[\rho_{AB}^{(p)}\,\Phi_{AB}^{+}\right] = \bra{\Phi^+}\rho_{AB}^{(p)}\ket{\Phi^+}$

$$= (1-p)\bra{\Phi^+}\Phi_{AB}^{+}\ket{\Phi^+} + \frac{p}{3}\left(\underbrace{\bra{\Phi^+}\Phi_{AB}^{-}\ket{\Phi^+}}_{0} + \underbrace{\bra{\Phi^+}\Psi_{AB}^{+}\ket{\Phi^+}}_{0} + \underbrace{\bra{\Phi^+}\Psi_{AB}^{-}\ket{\Phi^+}}_{0}\right)$$

$$= 1-p \quad\Rightarrow\quad p = 1 - \bra{\Phi^+}\rho_{AB}^{(p)}\ket{\Phi^+}.$$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\hookrightarrow$ This is called the \textbf{\underline{fidelity}}.

\textcolor{red}{\textasteriskcentered\ So $\rho_{AB}^{(p)}$ is entangled if and only if $\quad \bra{\Phi^+}\rho_{AB}^{(p)}\ket{\Phi^+} > \frac{1}{2}$}

---

② **Classical vs. Quantum Correlations: Bell/CHSH Inequality**

- The above criteria for detecting entanglement are purely mathematical.
- In practice, we need to do \underline{measurements} to determine whether or not qubits are entangled.

## Page 7

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

## Page 8

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

## Page 9

- The anti-correlation exists for <u>any</u> basis measurement!

- **Fact**: Let $U$ be an arbitrary $2 \times 2$ unitary matrix. Then
$$(U \otimes U) \ket{\Psi^-}\bra{\Psi^-} (U \otimes U)^\dagger = \ket{\Psi^-}\bra{\Psi^-}.$$

$$\ket{\Psi^-} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{1} - \ket{1}\ket{0})$$

**Proof**: First consider an arbitrary $2 \times 2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $a,b,c,d \in \mathbb{C}$.

$$(M \otimes M)\ket{\Psi^-} = \tfrac{1}{\sqrt{2}}\big(M\ket{0} \otimes M\ket{1} - M\ket{1} \otimes M\ket{0}\big)$$

$\quad M\ket{0} = a\ket{0} + c\ket{1}$
$\quad M\ket{1} = b\ket{0} + d\ket{1}$

$$= \tfrac{1}{\sqrt{2}}\Big( (a\ket{0} + c\ket{1}) \otimes (b\ket{0} + d\ket{1}) - (b\ket{0} + d\ket{1}) \otimes (a\ket{0} + c\ket{1}) \Big)$$

$$= \tfrac{1}{\sqrt{2}}\Big( \cancel{ab\ket{0,0}} + ad\ket{0,1} + cb\ket{1,0} + \cancel{cd\ket{1,1}} - \cancel{ab\ket{0,0}} - cb\ket{1,0} - ad\ket{1,0}\!\!\!\!\!^{\,0,1} - \cancel{cd\ket{1,1}} \Big)$$

Wait — re-doing carefully:

$$= \tfrac{1}{\sqrt{2}}\Big( (ad - bc)\ket{0,1} - (ad - bc)\ket{1,0} \Big)$$

$$= \tfrac{1}{\sqrt{2}}(ad - bc)\big(\ket{0,1} - \ket{1,0}\big)$$

$$= (ad - bc)\,\tfrac{1}{\sqrt{2}}\big(\ket{0,1} - \ket{1,0}\big)$$

$$= \underline{\det(M)}\,\ket{\Psi^-}. \quad \to \underline{\text{determinant of } M!}$$

So for any matrix $M$: $\;(M \otimes M)\ket{\Psi^-}\bra{\Psi^-}(M \otimes M)^\dagger = |\det(M)|^2 \ket{\Psi^-}\bra{\Psi^-}.$

Determinant is product of the eigenvalues.

Let $U = \sum_{k=1}^{d} \lambda_k \ket{\gamma_k}\bra{\gamma_k}$ be the spectral decomposition of a unitary.

Then $U^\dagger = \sum_{k=1}^{d} \overline{\lambda_k} \ket{\gamma_k}\bra{\gamma_k} \;\Rightarrow\; UU^\dagger = \sum_{k=1}^{d} |\lambda_k|^2 \ket{\gamma_k}\bra{\gamma_k} = \mathbb{1}$ (by unitarity) $\quad \lambda_k = re^{i\theta}$

Also, $\sum_{k=1}^{d} \ket{\gamma_k}\bra{\gamma_k} = \mathbb{1} \;\Rightarrow\; |\lambda_k|^2 = 1 \;\forall\, k \;\Rightarrow\; \lambda_k = e^{i\theta_k} \;\Rightarrow\;$ eigenvalues of

## Page 10

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


# Lectures__linear-algebra(II).pdf

## Page 1

## ① Recap

[Left: Bit diagram — vertical line with two dots labeled 0 (top) and 1 (bottom)]

**Bit**
0 or 1;
or probabilistic mixture

[Right: Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ on front, $\ket{-}$ on back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$
$\alpha, \beta \in \mathbb{C},$
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

---

✱ States of live on the surface of the **Bloch sphere**. — they are described by 2-dimensional **state vectors**.

$$\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad \alpha, \beta \in \mathbb{C}, \quad \underbrace{|\alpha|^2}_{\Pr[0]} + \underbrace{|\beta|^2}_{\Pr[1]} = 1. \quad \longrightarrow \quad \ket{\psi} = \alpha\ket{0} + \beta\ket{1}$$

$$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

(States **inside** the sphere are also possible — they are described by **density matrices**. We will see this later...)

## ② Complex Vector Spaces

$$\ket{v} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \longrightarrow \ket{v} = \sum_{k=1}^{d} a_k \ket{e_k}, \quad \ket{e_1} = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \ket{e_2} = \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, \ldots, \ket{e_d} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}$$

[Note in red: "Complex numbers!" pointing to $a_k$]

$$\bra{v} = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix} \longrightarrow \bra{v} = \sum_{k=1}^{d} \bar{a}_k \bra{e_k}.$$

$$\ket{v} = \sum_{k=0}^{d-1} a_k \ket{k}, \quad \ket{u} = \sum_{k=0}^{d-1} b_k \ket{k}$$

$$\braket{v|u} = \left( \sum_{k=0}^{d-1} \bar{a}_k \bra{k} \right) \left( \sum_{k'=0}^{d-1} b_{k'} \ket{k'} \right)$$

## Page 2

$$\ket{v} = \sum_{k=0}^{d-1} a_k \ket{k} \;\to\; \braket{k'|v} = \bra{k'}\left(\sum_{k=0}^{d-1} a_k \ket{k}\right)$$

$$= \sum_{k=0}^{d-1} a_k \underbrace{\braket{k'|k}}_{\delta_{k,k'}}$$

$$= a_{k'}$$

$$= \sum_{k,k'=0}^{d-1} \overline{a_k}\, b_{k'} \underbrace{\braket{k|k'}}_{\delta_{k,k'}}$$

$$= \sum_{k=0}^{d-1} \overline{a_k}\, b_k$$

## Page 3

※ <u>Notation</u>: $\ket{e_1} \equiv \ket{0}, \ket{e_2} \equiv \ket{1}, \ldots, \ket{e_d} \equiv \ket{d-1}$ → The "standard basis" or "computational basis".

For a qubit: $\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \alpha\ket{0} + \beta\ket{1}.$

$$\alpha = \braket{0|\psi}, \quad \beta = \braket{1|\psi}$$

- Addition of vectors:

$$\ket{v_1} = \sum_{k=0}^{d-1} a_k \ket{k}, \quad \ket{v_2} = \sum_{k=0}^{d-1} b_k \ket{k} \implies \ket{v_1} + \ket{v_2} = \sum_{k=0}^{d-1} (a_k + b_k)\ket{k}.$$

- Inner product of vectors is given by $\braket{v_1|v_2}$.

$$\ket{v_1} = \sum_{k=0}^{d-1} a_k \ket{k}, \quad \ket{v_2} = \sum_{k=0}^{d-1} b_k \ket{k} \longrightarrow \braket{v_1|v_2} = \underbrace{\left(\sum_{k=0}^{d-1} \bar{a}_k \bra{k}\right)}_{\bra{v_1}} \underbrace{\left(\sum_{k'=0}^{d-1} b_{k'} \ket{k'}\right)}_{\ket{v_2}}$$

$$\delta_{k,k'} = \begin{cases} 1 & \text{if } k = k' \\ 0 & \text{if } k \neq k' \end{cases} \qquad = \sum_{k,k'=0}^{d-1} \bar{a}_k b_{k'} \underbrace{\braket{k|k'}}_{=\delta_{k,k'}} = \sum_{k=0}^{d-1} \bar{a}_k b_k.$$

- The <u>norm</u> of a vector is $\| \ket{v} \| = \sqrt{\braket{v|v}} = \left(\sum_{k=0}^{d-1} |a_k|^2\right)^{1/2}.$

$$\left( \ket{v} = \sum_{k=0}^{d-1} a_k \ket{k} \right) \qquad \qquad \downarrow \\ \qquad \qquad \qquad a_k \cdot \bar{a}_k$$

We call a vector "normalized" if $\| \ket{v} \| = 1.$

※ To normalize a vector, just divide by its norm!

$$\ket{v} = \sum_{k=0}^{d-1} a_k \ket{k} \rightarrow \| \ket{v} \| = \left(\sum_{k=0}^{d-1} |a_k|^2\right)^{1/2} \implies \ket{\tilde{v}} = \frac{1}{\| \ket{v} \|} \cdot \ket{v} = \frac{1}{\| \ket{v} \|} \sum_{k=0}^{d-1} a_k \ket{k}$$

$$= \sum_{k=0}^{d-1} \frac{a_k}{\| \ket{v} \|} \ket{k}$$

<u>Check</u>: $\braket{\tilde{v}|\tilde{v}} = \left(\frac{1}{\| \ket{v} \|} \sum_{k=0}^{d-1} \bar{a}_k \bra{k}\right) \left(\frac{1}{\| \ket{v} \|} \sum_{k'=0}^{d-1} a_{k'} \ket{k'}\right)$

## Page 4

$$= \frac{1}{\||v\rangle\|^2} \underbrace{\sum_{k=0}^{d-1} |a_k|^2}_{= \||v\rangle\|^2}$$

$$= \frac{1}{\||v\rangle\|^2} \cdot \||v\rangle\|^2$$

$$= 1 \checkmark$$

- **Tensor product of vectors**: Used to describe the state of multiple qubits. (and entanglement!).

  - One qubit: 2-dimensional vector: $|\psi\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$.

  - If qubit 1 has state $|\psi_1\rangle$ and qubit 2 has state $|\psi_2\rangle$, then the **joint state** is given by

$$|\psi_1\rangle \otimes |\psi_2\rangle = \underbrace{\begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}}_{|\psi_1\rangle} \otimes \underbrace{\begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix}}_{|\psi_2\rangle} = \begin{pmatrix} \alpha_1 \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix} \\ \beta_1 \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} \alpha_1 \alpha_2 \\ \alpha_1 \beta_2 \\ \beta_1 \alpha_2 \\ \beta_1 \beta_2 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

(4-dimensional vector!)

$\underset{\color{red}\text{tensor/Kronecker product}}{\color{red}\uparrow}$

⊛ **Abstract notation**: $|\psi_1\rangle = \alpha_1|0\rangle + \beta_1|1\rangle,\ |\psi_2\rangle = \alpha_2|0\rangle + \beta_2|1\rangle$

$$\Rightarrow |\psi_1\rangle \otimes |\psi_2\rangle = \big(\alpha_1|0\rangle + \beta_1|1\rangle\big) \otimes \big(\alpha_2|0\rangle + \beta_2|1\rangle\big)$$

[red arrows indicate distributing the tensor product across all four cross-terms]

$$= \alpha_1\alpha_2 |0\rangle\otimes|0\rangle + \alpha_1\beta_2 |0\rangle\otimes|1\rangle + \beta_1\alpha_2 |1\rangle\otimes|0\rangle + \beta_1\beta_2 |1\rangle\otimes|1\rangle$$

**Recall:** $|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\ |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \Rightarrow \underline{|0\rangle\otimes|0\rangle} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix};\ \underline{|0\rangle\otimes|1\rangle} = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$

## Page 5

$\ket{1}\otimes\ket{0} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}$, $\ket{1}\otimes\ket{1} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$ → This defines the vector space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

✲ $\{\ket{0}\otimes\ket{0}, \ket{0}\otimes\ket{1}, \ket{1}\otimes\ket{0}, \ket{1}\otimes\ket{1}\}$ is the standard/computational basis for $\mathbb{C}^2 \otimes \mathbb{C}^2$. (Just all two-bit strings!)

✲ Probabilities: $\Pr[0,0] = |\alpha_1\alpha_2|^2$, $\Pr[0,1] = |\alpha_1\beta_2|^2$, $\Pr[1,0] = |\beta_1\alpha_2|^2$, $\Pr[1,1] = |\beta_1\beta_2|^2$.

✲ This extends to any dimension!

For $\mathbb{C}^{d_1} \otimes \mathbb{C}^{d_2}$, basis is $\{\ket{k_1}\otimes\ket{k_2} : k_1 \in \{0,1,\ldots,d_1-1\}, k_2 \in \{0,1,\ldots,d_2-1\}\}$
Dimension is $d_1 \cdot d_2$.

✲ Shorthand notation: $\ket{k_1}\otimes\ket{k_2} \equiv \ket{k_1}\ket{k_2} \equiv \ket{k_1, k_2}$.

– Tensor product of three vectors:

$$\ket{\psi_1} = \begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}, \quad \ket{\psi_2} = \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix}, \quad \ket{\psi_3} = \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix}$$

$$\Rightarrow \ket{\psi_1}\otimes\ket{\psi_2}\otimes\ket{\psi_3} = \big(\ket{\psi_1}\otimes\ket{\psi_2}\big)\otimes\ket{\psi_3} = \ket{\psi_1}\otimes\big(\ket{\psi_2}\otimes\ket{\psi_3}\big).$$

$$= \begin{pmatrix} \alpha_1\alpha_2 \\ \alpha_1\beta_2 \\ \beta_1\alpha_2 \\ \beta_1\beta_2 \end{pmatrix} \otimes \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} = \begin{pmatrix} \alpha_1\alpha_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \alpha_1\beta_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \beta_1\alpha_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \beta_1\beta_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} \alpha_1\alpha_2\alpha_3 \\ \alpha_1\alpha_2\beta_3 \\ \alpha_1\beta_2\alpha_3 \\ \alpha_1\beta_2\beta_3 \\ \beta_1\alpha_2\alpha_3 \\ \beta_1\alpha_2\beta_3 \\ \beta_1\beta_2\alpha_3 \\ \beta_1\beta_2\beta_3 \end{pmatrix} \begin{matrix} 000 \\ 001 \\ 010 \\ 011 \\ 100 \\ 101 \\ 110 \\ 111 \end{matrix}$$

✲ The resulting vector has dimension $8 = 2 \cdot 2 \cdot 2 = 2^3$!

✲ The vector space is $\mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^2$.

## Page 6

✻ **Abstract notation:** $\ket{\psi_1} = \alpha_1\ket{0} + \beta_1\ket{1}$, $\ket{\psi_2} = \alpha_2\ket{0} + \beta_2\ket{1}$, $\ket{\psi_3} = \alpha_3\ket{0} + \beta_3\ket{1}$

$$\Rightarrow \ket{\psi_1} \otimes \ket{\psi_2} \otimes \ket{\psi_3} = \big(\alpha_1\ket{0} + \beta_1\ket{1}\big) \otimes \big(\alpha_2\ket{0} + \beta_2\ket{1}\big) \otimes \big(\alpha_3\ket{0} + \beta_3\ket{1}\big)$$

$$= \big(\alpha_1\alpha_2\ket{0,0} + \alpha_1\beta_2\ket{0,1} + \beta_1\alpha_2\ket{1,0} + \beta_1\beta_2\ket{1,1}\big) \otimes \big(\alpha_3\ket{0} + \beta_3\ket{1}\big)$$

$$= \alpha_1\alpha_2\alpha_3\ket{0,0,0} + \alpha_1\alpha_2\beta_3\ket{0,0,1} + \alpha_1\beta_2\alpha_3\ket{0,1,0} + \alpha_1\beta_2\beta_3\ket{0,1,1}$$
$$+ \beta_1\alpha_2\alpha_3\ket{1,0,0} + \beta_1\alpha_2\beta_3\ket{1,0,1} + \beta_1\beta_2\alpha_3\ket{1,1,0} + \beta_1\beta_2\beta_3\ket{1,1,1}$$

— **Arbitrary number of tensor products:**

$$\ket{\psi_j} = \sum_{k=0}^{1} C_{j,k}\ket{k} = C_{j,0}\ket{0} + C_{j,1}\ket{1}$$

$$\rightarrow \underbrace{\ket{\psi_1} \otimes \ket{\psi_2} \otimes \cdots \otimes \ket{\psi_n}}_{\text{vector in } (\mathbb{C}^2)^{\otimes n}} = \bigotimes_{j=1}^{n}\ket{\psi_j} = \sum_{k_1,k_2,\ldots,k_n=0}^{1} C_{1,k_1} C_{2,k_2} \cdots C_{n,k_n} \ket{k_1, k_2, \ldots, k_n}$$

✻ **Generalizes to arbitrary dimension!** $\ket{\psi_j} = \sum_{k=0}^{d_j-1} C_{j,k}\ket{k}$

$$\Rightarrow \underbrace{\bigotimes_{j=1}^{n} \ket{\psi_j}}_{\text{Vector in } \mathbb{C}^{d_1} \otimes \mathbb{C}^{d_2} \otimes \cdots \otimes \mathbb{C}^{d_n}} = \sum_{k_1=0}^{d_1-1} \sum_{k_2=0}^{d_2-1} \cdots \sum_{k_n=0}^{d_n-1} C_{1,k_1} C_{2,k_2} \cdots C_{n,k_n} \ket{k_1, k_2, \ldots, k_n}$$

— **Basis of $n$-qubit space $(\mathbb{C}^2)^{\otimes n}$ is labeled by all $n$-bit strings.**

$$(\mathbb{C}^2)^{\otimes n} = \mathrm{span}\big\{\ket{\vec{x}} : \underbrace{\vec{x} \in \{0,1\}^n}_{\text{Set of all $n$-bit strings.}}\big\}$$

**Notation:** $\vec{x} \in \{0,1\}^n \Rightarrow \vec{x} = (x_1, x_2, \ldots, x_n)$, $x_i \in \{0,1\}$

$$\ket{\vec{x}} = \ket{x_1, x_2, \ldots, x_n} \equiv \ket{x_1} \otimes \ket{x_2} \otimes \cdots \otimes \ket{x_n}$$

## Page 7

- **Example:** $n=2 \to \{\ket{0,0}, \ket{0,1}, \ket{1,0}, \ket{1,1}\}$

  $n=3 \to \{\ket{0,0,0}, \ket{0,0,1}, \ket{0,1,0}, \ket{0,1,1}, \ket{1,0,0}, \ket{1,0,1}, \ket{1,1,0}, \ket{1,1,1}\}.$

- Tensor product and inner product.

  By definition: $(\bra{v_1} \otimes \bra{v_2})(\ket{u_1} \otimes \ket{u_2}) = \braket{v_1|u_1} \cdot \braket{v_2|u_2}.$

  $$\braket{0,1,0|1,1,0} = \underbrace{\braket{0|1}}_{=0}\underbrace{\braket{1|1}}_{=1}\underbrace{\braket{0|0}}_{=1}$$

- **Example:** for basis vectors,
  $$\braket{0,1,0|1,0,1} = \underbrace{\braket{0|1}}_{=0} \cdot \underbrace{\braket{1|0}}_{=0} \cdot \underbrace{\braket{0|1}}_{=0} = 0.$$

  In general: for basis vectors $\ket{\vec{x}}, \ket{\vec{y}}$, $\vec{x} = (x_1, x_2, \ldots, x_n) \in \{0,1\}^n$
  $$\vec{y} = (y_1, y_2, \ldots, y_n) \in \{0,1\}^n$$

  $$\braket{\vec{x}|\vec{y}} = \delta_{\vec{x},\vec{y}} = \delta_{x_1,y_1}\,\delta_{x_2,y_2}\cdots \delta_{x_n,y_n}$$

- Probabilities: For a state of $n$ qubits given by

  $$\ket{\psi} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}} \to \text{Normalization condition is } \sum_{\vec{x} \in \{0,1\}^n} |c_{\vec{x}}|^2 = 1.$$

  Probabilities are: $\Pr[\vec{x}] = |c_{\vec{x}}|^2 = \braket{\vec{x}|\psi}$

## ③ Matrices: Linear Transformations of Vectors

(✱) Matrices will be used to define and describe states inside the Bloch sphere (i.e., mixed states) and the gates we can apply to qubits on a quantum computer.

## Page 8

⊛ We also call matrices <u>linear operators / transformations</u>.

– <u>2×2 matrices</u>:  $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $a,b,c,d \in \mathbb{C}$.

- Multiplying a matrix with a vector: $\ket{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$

$$M\ket{v} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} av_1 + bv_2 \\ cv_1 + dv_2 \end{pmatrix}$$

- Matrices act linearly as follows:  $M(\alpha \ket{v_1} + \beta \ket{v_2}) = \underline{\alpha M \ket{v_1} + \beta M \ket{v_2}}$

$$= \begin{pmatrix} \alpha a & \alpha b \\ \alpha c & \alpha d \end{pmatrix}$$

- Matrix multiplication: $M_1 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix}$, $M_2 = \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix}$

$$M_1 \cdot M_2 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix} \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} = \begin{pmatrix} a_1 a_2 + b_1 c_2 & a_1 b_2 + b_1 d_2 \\ c_1 a_2 + d_1 c_2 & c_1 b_2 + d_1 d_2 \end{pmatrix}$$

- Abstract notation from vectors extends to matrices!

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} + d\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

⊛ <u>Recall</u>:  $\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ → $\bra{0} = (1\ 0)$, $\bra{1} = (0\ 1)$

⊛ <u>Observe</u>: $\ket{0}\bra{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}(1\ 0) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $\ket{0}\bra{1} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}(0\ 1) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$

$\underbrace{\phantom{xx}}_{2\times 1}\underbrace{\phantom{xx}}_{1\times 2}$

## Page 9

$$\ket{1}\bra{0} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad \ket{1}\bra{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

Then $\;M = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}\quad$ $\begin{aligned} a &= \braket{0|M|0}, & c &= \braket{1|M|0} \\ b &= \braket{0|M|1}, & d &= \braket{1|M|1} \end{aligned}$

This makes multiplication easier! (No need to remember matrix multiplication rules).

$$M\ket{v} = \big(a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}\big)\big(v_1\ket{0} + v_2\ket{1}\big)$$

$$= av_1\underbrace{\ket{0}\braket{0|0}}_{1} + av_2\ket{0}\underbrace{\braket{0|1}}_{0} + bv_1\ket{0}\underbrace{\braket{1|0}}_{0} + bv_2\underbrace{\ket{0}\braket{1|1}}_{1}$$

$$\quad + cv_1\underbrace{\ket{1}\braket{0|0}}_{1} + cv_2\ket{1}\underbrace{\braket{0|1}}_{0} + dv_1\ket{1}\underbrace{\braket{1|0}}_{0} + dv_2\underbrace{\ket{1}\braket{1|1}}_{1}$$

$$= (av_1 + bv_2)\ket{0} + (cv_1 + dv_2)\ket{1}$$

$$= \begin{pmatrix} av_1 + bv_2 \\ cv_1 + dv_2 \end{pmatrix} \checkmark \quad (\text{just as before!})$$

- **Arbitrary $d \times d$ matrices:**

$$M = \sum_{i,j=0}^{d-1} M_{i,j}\,\ket{i}\bra{j}$$

$\uparrow$ entry in the $i^{\text{th}}$ row and $j^{\text{th}}$ column. (complex number)

$$\braket{k|M|\ell} = \bra{k}\left(\sum_{i,j=0}^{d-1} M_{i,j}\,\ket{i}\bra{j}\right)\ket{\ell}$$

$$= \sum_{i,j=0}^{d-1} M_{i,j}\,\underbrace{\braket{k|i}}_{\delta_{k,i}}\underbrace{\braket{j|\ell}}_{\delta_{j,\ell}} = M_{k,\ell}$$

$$M_1 = \sum_{i,j=0}^{d-1} M^{(1)}_{i,j}\,\ket{i}\bra{j} \qquad M_2 = \sum_{i,j=0}^{d-1} M^{(2)}_{i,j}\,\ket{i}\bra{j}$$

$$M_1 \cdot M_2 = \left(\sum_{i_1,j_1=0}^{d-1} M^{(1)}_{i_1,j_1}\,\ket{i_1}\bra{j_1}\right)\left(\sum_{i_2,j_2=0}^{d-1} M^{(2)}_{i_2,j_2}\,\ket{i_2}\bra{j_2}\right)$$

$$= \sum_{i_1,j_1=0}^{d-1}\sum_{i_2,j_2=0}^{d-1} M^{(1)}_{i_1,j_1} M^{(2)}_{i_2,j_2}\,\ket{i_1}\underbrace{\braket{j_1|i_2}}_{\delta_{j_1,i_2}}\bra{j_2} = \sum_{i_1,j_2=0}^{d-1}\left(\sum_{j_1=0}^{d-1} M^{(1)}_{i_1,j_1} M^{(2)}_{j_1,j_2}\right)\ket{i_1}\bra{j_2}$$


# Lectures__linear-algebra(III)+quantum-gates.pdf

## Page 1

# ① Quantum States

[Left diagram: vertical line segment with two dots labeled 0 (top) and 1 (bottom)]

**Bit**
0 or 1;
or probabilistic mixture

[Right diagram: Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ in front, $\ket{-}$ in back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$$
$$\alpha, \beta \in \mathbb{C},$$
$$|\alpha|^2 + |\beta|^2 = 1$$

$$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$$
$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

---

✱ States of live on the surface of the **Bloch sphere**. — they are described by 2-dimensional **state vectors**.

$\{\ket{k}\}_{k=0}^{d-1}$    $\{\ket{e_k}\}_{k=1}^{d}$

$$\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad \alpha,\beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1. \qquad \ket{\psi} = \alpha\ket{0} + \beta\ket{1}, \;\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

(States **inside** the sphere are also possible — they are described by **density matrices**. We will see this today!)

---

② **Matrices** (aka "linear operators")

$$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \ket{0}\bra{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$$

→ column indices

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad a,b,c,d \in \mathbb{C}. \quad \rightarrow \quad M = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}$$

[row/column labels: rows indexed 0,1; columns indexed 0,1]

↗ row indices

$$a = \bra{0}M\ket{0}, \quad b = \bra{0}M\ket{1}, \quad c = \bra{1}M\ket{0},$$
$$d = \bra{1}M\ket{1}.$$

– General $d\times d$ matrix: $\displaystyle M = \sum_{i,j=0}^{d-1} m_{ij}\ket{i}\bra{j}, \quad m_{ij} = \bra{i}M\ket{j}$

→ matrix elements.

## Page 2

⊛ <u>Notation</u>: $L(\mathbb{C}^d) \equiv$ set of all matrices/linear operators acting on $\mathbb{C}^d$ (i.e., $d \times d$ matrices) (dimension is $d^2$.)

- For any vector $\ket{v} \in \mathbb{C}^d$, $\ket{v}\bra{v} \in L(\mathbb{C}^d)$ is a $d \times d$ matrix.

$$\ket{v} = \sum_{k=0}^{d-1} v_k \ket{k} \implies \ket{v}\bra{v} = \left(\sum_{k=0}^{d-1} v_k \ket{k}\right)\left(\sum_{k'=0}^{d-1} \overline{v_{k'}} \bra{k'}\right) = \sum_{k,k'=0}^{d-1} v_k \overline{v_{k'}} \ket{k}\bra{k'}.$$

- <u>Identity matrix</u>: $\mathbb{1} \to \mathbb{1}\ket{v} = \ket{v}$ for all $\ket{v} \in \mathbb{C}^d$.

$$\mathbb{1} = \begin{pmatrix} 1 & & 0 \\ & 1 & \\ & & \ddots \\ 0 & & & 1 \end{pmatrix} = \sum_{k=0}^{d-1} \ket{k}\bra{k} \quad \overset{M_{ij} = \delta_{ij}}{\to} \quad \text{For any orthonormal basis } \{\ket{e_k}\}_{k=1}^d : \mathbb{1} = \sum_{k=1}^d \ket{e_k}\bra{e_k}.$$

- <u>Trace of a Matrix</u>: Sum of the diagonal elements.

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \to \text{Tr}[M] = a + d = \bra{0}M\ket{0} + \bra{1}M\ket{1}.$$

In general: $M = \sum_{i,j=0}^{d-1} M_{ij} \ket{i}\bra{j} \implies \text{Tr}[M] = \sum_{i=0}^{d-1} M_{i,i} = \sum_{i=0}^{d-1} \bra{i}M\ket{i}.$

⊛ Consider a state vector $\ket{\psi} = \alpha\ket{0} + \beta\ket{1} \implies \bra{\psi} = \overline{\alpha}\bra{0} + \overline{\beta}\bra{1}$, $|\alpha|^2 + |\beta|^2 = 1$.

$$\implies \ket{\psi}\bra{\psi} = (\alpha\ket{0} + \beta\ket{1})(\overline{\alpha}\bra{0} + \overline{\beta}\bra{1}) = \alpha\overline{\alpha}\ket{0}\bra{0} + \alpha\overline{\beta}\ket{0}\bra{1} + \beta\overline{\alpha}\ket{1}\bra{0} + \beta\overline{\beta}\ket{1}\bra{1}$$

$$= |\alpha|^2 \ket{0}\bra{0} + \alpha\overline{\beta}\ket{0}\bra{1} + \beta\overline{\alpha}\ket{1}\bra{0} + |\beta|^2 \ket{1}\bra{1} = \begin{pmatrix} |\alpha|^2 & \alpha\overline{\beta} \\ \beta\overline{\alpha} & |\beta|^2 \end{pmatrix}$$

$\hookrightarrow |\alpha|^2 = \Pr[0]$
$\quad\;\; |\beta|^2 = \Pr[1]$

Now take the trace: $\text{Tr}[\ket{\psi}\bra{\psi}] = |\alpha|^2 + |\beta|^2 = 1.$

In general: $\text{Tr}[\ket{v}\bra{v}] = \braket{v|v}$ for all $\ket{v} \in \mathbb{C}^d$.

## Page 3

**Proof:** Just use the definition!

$$\mathrm{Tr}(\ket{v}\bra{v}) = \sum_{k=0}^{d-1} \bra{k}\ket{v}\bra{v}\ket{k} = \sum_{k=0}^{d-1} \braket{v|k}\braket{k|v} = \bra{v}\left(\sum_{k=0}^{d-1} \ket{k}\bra{k}\right)\ket{v} = \braket{v|v}. \blacksquare$$

[annotation: $\bra{v}\mathbb{1}\ket{v}$, with $\sum_{k=0}^{d-1}\ket{k}\bra{k} = \mathbb{1}$]

**Similarly:** $\mathrm{Tr}\big[M\ket{v_1}\bra{v_2}\big] = \braket{v_2|M|v_1}$ for all $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$, $M \in L(\mathbb{C}^d)$.

**Proof:** 
$$\mathrm{Tr}\big[M\ket{v_1}\bra{v_2}\big] = \sum_{k=0}^{d-1}\bra{k}M\ket{v_1}\braket{v_2|k} = \sum_{k=0}^{d-1}\braket{v_2|k}\bra{k}M\ket{v_1} = \bra{v_2}\left(\sum_{k=0}^{d-1}\ket{k}\bra{k}\right)M\ket{v_1}$$

$$= \braket{v_2|M|v_1}. \blacksquare \qquad\qquad = \bra{v_2}\underbrace{\mathbb{1}\cdot M}_{=M}\ket{v_1}$$

[annotation: $\mathbb{1}\ket{v} = \ket{v}$, $\mathbb{1}\cdot M = M$]

---

- **Transpose of a matrix:** flip the rows and columns.

- $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \;\rightarrow\; M^T = \begin{pmatrix} a & c \\ b & d \end{pmatrix}$

- ⊛ **Note:** $\big(\ket{i}\bra{j}\big)^T = \ket{j}\bra{i}.$ $\qquad \underline{(M_1 + M_2)^T = M_1^T + M_2^T}$

- **In general:** $M = \sum_{i,j=0}^{d-1} m_{i,j}\ket{i}\bra{j} \;\Rightarrow\; M^T = \sum_{i,j=0}^{d-1} m_{i,j}\ket{j}\bra{i}$

$$M^T = \left(\sum_{i,j=0}^{d-1} m_{i,j}\ket{i}\bra{j}\right)^T = \sum_{i,j=0}^{d-1} m_{i,j}\big(\ket{i}\bra{j}\big)^T$$

- ⊛ A matrix $M$ is called **symmetric** if $M^T = M$.

$$M^T = M \;\rightarrow\; m_{i,j} = m_{j,i}$$

## Page 4

- <u>Conjugate Transpose of a Matrix:</u>

  - Recall for vectors: $\ket{v} = \begin{pmatrix} v_0 \\ v_1 \\ \vdots \\ v_{d-1} \end{pmatrix} \;\Rightarrow\; \bra{v} = \begin{pmatrix} \bar{v}_0 & \bar{v}_1 & \cdots & \bar{v}_{d-1} \end{pmatrix}$

    OR: $\ket{v} = \sum_{k=0}^{d-1} v_k \ket{k} \;\Rightarrow\; \bra{v} = \sum_{k=0}^{d-1} \bar{v}_k \bra{k}$.

  - Similar for matrices! $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \;\Rightarrow\; M^{\dagger} = \begin{pmatrix} \bar{a} & \bar{c} \\ \bar{b} & \bar{d} \end{pmatrix}$.   ($\dagger$ = "dagger")

  - In general: $M = \sum_{i,j=0}^{d-1} M_{i,j} \ket{i}\bra{j} \;\Rightarrow\; M^{\dagger} = \sum_{i,j=0}^{d-1} \overline{M_{i,j}} \ket{j}\bra{i}$

  $\circledast$ <u>Note:</u> $\big( \ket{i}\bra{j} \big)^{\dagger} = \ket{j}\bra{i}$.

  $\circledast$ A matrix $M$ is called <mark>Hermitian</mark> if $M^{\dagger} = M$.   $\;\to\; M_{i,j} = \overline{M_{j,i}}$

  $\quad M = \begin{pmatrix} a & b \\ \bar{b} & d \end{pmatrix}$, $\;\bar{a} = a,\; \bar{d} = d \;\;(a, d \in \mathbb{R})$

- <u>Inner Product and Orthonormal Bases of Matrices.</u>

  - Recall vector inner product: $\ket{u} = \sum_{k=0}^{d-1} u_k \ket{k}, \;\; \ket{v} = \sum_{k=0}^{d-1} v_k \ket{k}$

    $\Rightarrow \;\braket{u|v} = \Big( \sum_{k=0}^{d-1} \bar{u}_k \bra{k} \Big) \Big( \sum_{k=0}^{d-1} v_k \ket{k} \Big) = \sum_{k=0}^{d-1} \bar{u}_k v_k$

  - Matrix inner product: $\langle M_1, M_2 \rangle = \mathrm{Tr}\big[ M_1^{\dagger} M_2 \big]$, $\;\; \langle M_2, M_1 \rangle = \overline{\langle M_1, M_2 \rangle}$

    From this, we define a <u>norm for matrices</u>: $\| M \|_2 = \sqrt{\langle M, M \rangle} = \sqrt{\mathrm{Tr}[ M^{\dagger} M ]}$

  - Matrices $M_1, M_2$ are <u>orthogonal</u> if $\langle M_1, M_2 \rangle = 0$.

## Page 5

- We have bases for matrices as well! $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

Example: $d=2$, recall $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}.$

$\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$

The set $\{\ket{0}\bra{0}, \ket{0}\bra{1}, \ket{1}\bra{0}, \ket{1}\bra{1}\}$ is an orthonormal basis for $L(\mathbb{C}^2)$.

↳ Observe: there are $4 = 2^2$ elements! $\quad \langle B_i, B_j \rangle = \delta_{i,j}$

Check: take inner products!

$\langle \ket{0}\bra{0}, \ket{0}\bra{1} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{0})^\dagger (\ket{0}\bra{1}) \right] = \mathrm{Tr}\left[ \ket{0}\underbrace{\braket{0|0}}_{=1}\bra{1} \right] = \mathrm{Tr}\left[ \ket{0}\bra{1} \right] = \braket{1|0} = 0.$

$\langle \ket{0}\bra{1}, \ket{1}\bra{0} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{1})^\dagger \ket{1}\bra{0} \right] = \mathrm{Tr}\left[ \ket{1}\underbrace{\braket{0|1}}_{=0}\bra{0} \right] = 0.$

$\langle \ket{0}\bra{0}, \ket{0}\bra{0} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{0})^\dagger \ket{0}\bra{0} \right] = \mathrm{Tr}\left[ \ket{0}\underbrace{\braket{0|0}}_{=1}\bra{0} \right] = \mathrm{Tr}\left[ \ket{0}\bra{0} \right] = \braket{0|0} = 1$

In general: $\langle \ket{i}\bra{j}, \ket{k}\bra{\ell} \rangle = \mathrm{Tr}\left[ (\ket{i}\bra{j})^\dagger \ket{k}\bra{\ell} \right] = \mathrm{Tr}\left[ \ket{j}\underbrace{\braket{i|k}}_{=\delta_{i,k}}\bra{\ell} \right]$

$= \delta_{i,k}\, \mathrm{Tr}\left[ \ket{j}\bra{\ell} \right] = \delta_{i,k} \braket{\ell|j} = \delta_{i,k}\, \delta_{j,\ell}$

(★) Holds for arbitrary dimension! $\{\ket{i}\bra{j} : i,j \in \{0,1,\ldots,d-1\}\}$ is an orthonormal basis for $L(\mathbb{C}^d)$.

- Special basis for $d=2$: <u>Pauli Matrices</u> (aka Pauli gates).

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$\mathrm{Tr}[X] = \mathrm{Tr}[Y] = \mathrm{Tr}[Z] = 0$

↳ <u>Bit-flip matrix</u>: $X\ket{0} = \ket{1}, \; X\ket{1} = \ket{0}.$

$X^2 = \mathbb{1}, \; Y^2 = \mathbb{1}, \; Z^2 = \mathbb{1}.$

$\mathrm{Tr}(X^\dagger X) = 2 = \mathrm{Tr}[Y^\dagger Y] = \mathrm{Tr}[Z^\dagger Z]$

## Page 6

They are Hermitian: $X^\dagger = X$, $Y^\dagger = Y$, $Z^\dagger = Z$.

They are orthogonal: $\langle X, Y \rangle = 0$, $\langle X, Z \rangle = 0$, $\langle Z, Y \rangle = 0$.

$\{\mathbb{1}, X, Y, Z\}$ forms orthogonal basis for $L(\mathbb{C}^2)$!

$$\text{Tr}(X^\dagger Y) = \text{Tr}\left[\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\right] = \text{Tr}\left[\begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}\right] = 0$$

$\Rightarrow$ Any $M \in L(\mathbb{C}^2)$ can be written as $M = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$.

$\quad c_0, c_1, c_2, c_3 \in \mathbb{C}$.

## ③ Quantum States as Density Matrices

– We have seen state vectors:

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}, \quad \alpha,\beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1.$$

[Bloch sphere diagram with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ at front, $\ket{-}$ at back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$,
$\alpha, \beta \in \mathbb{C}$,
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

Qubit
$\ket{0}$ or $\ket{1}$;
or *superposition*

– Consider the matrix $\rho = \ket{\psi}\bra{\psi}$.
It has the following properties:

**(1)** $\rho = \rho^\dagger$ (Hermitian).

$\ket{\psi}\bra{\psi} = (\alpha\ket{0} + \beta\ket{1})(\bar{\alpha}\bra{0} + \bar{\beta}\bra{1})$
$= |\alpha|^2 \ket{0}\bra{0} + \alpha\bar{\beta}\ket{0}\bra{1} + \beta\bar{\alpha}\ket{1}\bra{0} + |\beta|^2 \ket{1}\bra{1}$

$(M_1 + M_2)^\dagger = M_1^\dagger + M_2^\dagger$

$(\ket{\psi}\bra{\psi})^\dagger = |\alpha|^2 (\ket{0}\bra{0})^\dagger + \overline{\alpha\bar{\beta}}(\ket{0}\bra{1})^\dagger + \overline{\beta\bar{\alpha}}(\ket{1}\bra{0})^\dagger + |\beta|^2 (\ket{1}\bra{1})^\dagger$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\downarrow \quad\quad\quad\quad\quad\quad\downarrow$
$\quad\quad\quad\quad\quad = \bar{\alpha}\cdot\bar{\bar{\beta}} = \bar{\alpha}\beta \quad = \bar{\beta}\cdot\bar{\bar{\alpha}} = \bar{\beta}\alpha$

$\left(\overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2\right)$
$\bar{\bar{z}} = z$

$= |\alpha|^2 \ket{0}\bra{0} + \bar{\alpha}\beta \ket{1}\bra{0} + \bar{\beta}\alpha\ket{0}\bra{1} + |\beta|^2 \ket{1}\bra{1}$

$= \ket{\psi}\bra{\psi}\ \checkmark$

## Page 7

(2) $\text{Tr}(\rho) = 1$ (unit trace).

$$\text{Tr}\big[\ket{\psi}\bra{\psi}\big] = \braket{\psi|\psi} = |\alpha|^2 + |\beta|^2 = 1 \quad \checkmark$$

(from above!)

(3) $\rho \geq 0$ (Positive Semi-definite).

❋ A Hermitian matrix $M \in L(\mathbb{C}^d)$ is called **positive semi-definite** (denoted $M \geq 0$) if $\braket{v|M|v} \geq 0 \;\; \forall \; \ket{v} \in \mathbb{C}^d$.

This is equivalent to: all **eigenvalues** are **non-negative**.

❋ Recall **eigenvalues and eigenvectors**: $M\ket{v} = \lambda\ket{v}$, $M = U D U^\dagger$, $U^\dagger U = \mathbb{1}$.

[Annotations: $\ket{v}$ → Eigenvector, $\lambda$ → Eigenvalue, $D$ → diagonal matrix, $U$ → unitary]

Eigenvalue (Spectral) decomposition: $M = \sum_{k=1}^{r} \lambda_k \ket{v_k}\bra{v_k}$

❋ For $\rho = \ket{\psi}\bra{\psi} \to \braket{v|\rho|v} = \braket{v|\psi}\braket{\psi|v} = |\braket{\psi|v}|^2 \geq 0 \;\; \forall \; \ket{v} \;\; \checkmark$

- Any matrix satisfying (1), (2), (3) is called a **density matrix/operator**.

❋ **Axiom of Quantum Mechanics**: The state of any quantum system is mathematically by a density matrix. (arbitrary dimension).

- The density matrix $\rho = \ket{\psi}\bra{\psi}$ describes a **pure state**. (on the surface of the Bloch sphere.)

## Page 8

- What about more general density matrices? Consider $d=2$.

We can write $\rho = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$ (b/c $\{\mathbb{1}, X, Y, Z\}$ is a basis).

We want this to satisfy: (1) $\rho^\dagger = \rho$; (2) $\text{Tr}(\rho) = 1$; (3) $\rho \geq 0$.

(1) $\rho^\dagger = \frac{1}{2}(\bar{c_0}\mathbb{1}^\dagger + \bar{c_1} X^\dagger + \bar{c_2} Y^\dagger + \bar{c_3} Z^\dagger)$  $\quad (\mathbb{1}^\dagger = \mathbb{1},\ X^\dagger = X,\ Y^\dagger = Y,\ Z^\dagger = Z)$

$\quad \downarrow$

$\quad = \frac{1}{2}(\bar{c_0}\mathbb{1} + \bar{c_1} X + \bar{c_2} Y + \bar{c_3} Z)$

$\quad \overset{(!)}{=} \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z) \iff c_0 = \bar{c_0},\ c_1 = \bar{c_1},\ c_2 = \bar{c_2},\ c_3 = \bar{c_3}$ (b/c $\{\mathbb{1}, X, Y, Z\}$ is a basis).

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ (all are real numbers).

(2) $\rho = \frac{1}{2}(r_0 \mathbb{1} + r_1 X + r_2 Y + r_3 Z),\ r_0, r_1, r_2, r_3 \in \mathbb{R}$.

$\text{Tr}(\rho) = \frac{1}{2}\big(r_0 \underbrace{\text{Tr}(\mathbb{1})}_{=2} + r_1 \underbrace{\text{Tr}(X)}_{=0} + r_2 \underbrace{\text{Tr}(Y)}_{=0} + r_3 \underbrace{\text{Tr}(Z)}_{=0}\big) \overset{(!)}{=} 1 \iff \underline{\underline{r_0 = 1}}$

(3) $\rho = \frac{1}{2}(\mathbb{1} + r_1 X + r_2 Y + r_3 Z) \to$ Find the eigenvalues!

$\left(\begin{array}{c}
\circledast\ \underline{\text{Observe}}: \cdot \langle X, \rho \rangle = \text{Tr}(X\rho) = \text{Tr}\big[X \cdot \tfrac{1}{2}(\mathbb{1} + r_1 X + r_2 Y + r_3 Z)\big] \\
\quad\quad\quad\quad = \tfrac{1}{2}\big(\underbrace{\text{Tr}(X)}_{=0} + r_1 \underbrace{\text{Tr}(X^2)}_{=2} + r_2 \underbrace{\text{Tr}(XY)}_{=0} + r_3 \underbrace{\text{Tr}(XZ)}_{=0}\big) \\
\quad\quad\quad\quad\quad \downarrow \\
\quad\quad\quad\quad\quad = r_1 \\
\quad\quad \cdot \langle Y, \rho \rangle = r_2 \\
\quad\quad \cdot \langle Z, \rho \rangle = r_3.
\end{array}\right.$

## Page 9

$$\rho = \frac{1}{2}\begin{pmatrix} 1+r_z & r_x - i r_y \\ r_x + i r_y & 1 - r_z \end{pmatrix} \implies \lambda_\pm = \frac{1}{2}\left(1 \pm \sqrt{r_x^2 + r_y^2 + r_z^2}\right) \geq 0.$$

Need $\lambda_- \geq 0 \implies \frac{1}{2}\left(1 - \sqrt{r_x^2 + r_y^2 + r_z^2}\right) \geq 0 \implies \boxed{r_x^2 + r_y^2 + r_z^2 \leq 1}$

$$\vec{r} = (r_x, r_y, r_z) \in \mathbb{R}^3 \text{ inside the unit sphere!}$$

Observe: $\|\rho\|_2^2 = \text{Tr}[\rho^2] = \frac{1}{2}\left(1 + r_x^2 + r_y^2 + r_z^2\right) \leq 1$
$$\underbrace{\phantom{r_x^2+r_y^2+r_z^2}}_{\leq 1}$$

$\rho = \frac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)$

[Bloch sphere diagram: z-axis up with $\ket{0}$ at top, $\ket{1}$ at bottom; x-axis with $\ket{+}$ and $\ket{-}$ marked; y-axis with $\ket{+i}$ and $\ket{-i}$ marked]

For a pure state $\rho = \ket{\psi}\bra{\psi}$, $\rho^2 = \ket{\psi}\underbrace{\braket{\psi|\psi}}_{=1}\bra{\psi} = \ket{\psi}\bra{\psi} \implies \text{Tr}[\rho^2] = 1$
$\rho^2 = \rho$

$\implies r_x^2 + r_y^2 + r_z^2 = 1 \implies$ pure states are on the surface of the unit sphere!

✻ We call $\text{Tr}[\rho^2]$ the **purity** of $\rho \to \rho$ pure if and only if $\text{Tr}[\rho^2] = 1$.

✻ <u>Origin</u>, $\vec{r} = (0,0,0)$ contains the **maximally-mixed state**: $\frac{\mathbb{1}}{2}$.

$\frac{\mathbb{1}}{2} = \frac{1}{2}(\ket{0}\bra{0} + \ket{1}\bra{1})$

✻ <u>Points on the X-axis</u>: $\vec{r} = (\pm 1, 0, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm X) = \ket{\pm}\bra{\pm}$, $\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$$= \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ \pm 1 \end{pmatrix}$$

These are eigenstates of $X$! $X\ket{\pm} = \pm \ket{\pm}$.

✻ <u>Points on the Y-axis</u>: $\vec{r} = (0, \pm 1, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm Y) = \ket{\pm i}\bra{\pm i}$,
$$\ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1}) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ \pm i \end{pmatrix}$$

These are eigenstates of $Y$! $Y\ket{\pm i} = \pm \ket{\pm i}$.

✻ <u>Points on the Z-axis</u>: $\vec{r} = (0, 0, \pm 1) \to \rho = \frac{1}{2}(\mathbb{1} \pm Z) \begin{matrix} \xrightarrow{(+)} \ket{0}\bra{0} \\ \xrightarrow{(-)} \ket{1}\bra{1} \end{matrix}$  $\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$
$\ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

These are eigenstates of $Z$! $Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$.


# Lectures__linear-algebra.pdf

## Page 1

# 1. What is a qubit?

[Diagram: A vertical line segment labeled "Bit" with 0 at top and 1 at bottom, representing classical bit values or probabilistic mixture in between.]

**Bit**
0 or 1;
or probabilistic mixture

[Diagram: Bloch sphere labeled "Qubit" with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ at front, $\ket{-}$ at back, $\ket{+i}$ on right, $\ket{-i}$ on left.]

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$$
$$\alpha, \beta \in \mathbb{C},$$
$$|\alpha|^2 + |\beta|^2 = 1$$

$$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$$
$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

---

✱ A <u>bit</u> takes a value either 0 or 1 — or any point in between

→ Probabilistic bit:
- Value is 0 with probability $p_0$.
- Value is 1 with probability $p_1$.

✱ $p_0 + p_1 = 1.$

→ So the <u>state</u> of a (probabilistic) bit is just a number b/w 0 and 1!

✱ The <u>state</u> of a qubit is a <u>point on the sphere</u> ← **Bloch sphere** — or any point inside the sphere. (We will understand the reasons for this later...).

→ We have to describe this using <u>vectors</u> of <u>complex numbers</u>.

→ $\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$, $\alpha, \beta \in \mathbb{C}$ (complex numbers).

&nbsp;&nbsp;&nbsp;&nbsp;↑
&nbsp;"ket"

$|\alpha|^2 = \alpha \cdot \bar{\alpha}$ : probability of 0
$|\beta|^2 = \beta \cdot \bar{\beta}$ : probability of 1.
&nbsp;&nbsp;&nbsp;&nbsp;↳ complex conjugate.

✱ In quantum mechanics, probabilities are "generated" by complex numbers.

## Page 2

## ② Complex Numbers

- A complex number is a number $z \in \mathbb{C}$ (← Set of complex numbers) with a <u>real part</u> and <u>imaginary part</u>

$$z = x + yi, \quad i^2 = -1 \qquad \text{Example: } z = 3 + 2i$$

where $x$ is the **Real part** and $y$ is the **Imaginary part**.

✱ Initially conceived in the 1500s for solving polynomial equations.

- Can be represented in a 2D plane. (the "complex plane").

[Diagram: Complex plane with horizontal axis labeled $\text{Re}(z)$ ← real axis, vertical axis labeled $\text{Im}(z)$ ← Imaginary axis. A vector from origin to point $z = x + iy$, with horizontal component $x$ and vertical component $y$.]

Example: $z = 3 + 2i$

$\text{Re}(z) = 3, \quad \text{Im}(z) = 2.$

✱ We can represent this as a vector: 
$$\vec{v} = \begin{pmatrix} x \\ y \end{pmatrix}.$$

- <u>Complex conjugate</u>: flip the sign of the imaginary part.

$$z = x + yi \;\Rightarrow\; \bar{z} = z^* = x - yi \qquad \text{Example: } z = 3 + 2i \;\Rightarrow\; \bar{z} = 3 - 2i.$$

- <u>Modulus (or magnitude)</u>: 
$$|z|^2 = z \cdot \bar{z} = (x + yi)(x - yi)$$

$$= x^2 - xyi + yxi + y^2 \underbrace{(i)(-i)}_{= +1} \qquad i^2 = -1$$

$$= x^2 + y^2$$

$$\Rightarrow |z| = \sqrt{x^2 + y^2}$$

## Page 3

⊛ This is just the **length** of the vector in the complex plane!

also called **norm**: $\| \ket{v} \| = \sqrt{x^2 + y^2}$.

- <u>Polar form</u>:

[Diagram: complex plane with horizontal axis labeled Re(z) ← real axis, vertical axis labeled Im(z) ← Imaginary axis. A purple vector from origin to point $z = x+iy$, with length $r$ and angle $\theta$ from real axis. Dotted lines drop to $x$ on real axis and $y$ on imaginary axis.]

$$z = re^{i\theta}, \quad r = \sqrt{x^2+y^2} = |z|.$$
$$\theta = \tan^{-1}\left(\frac{y}{x}\right)$$

⊛ $e^{i\theta} = \sum_{k=0}^{\infty} \frac{1}{k!}(i\theta)^k = \cos(\theta) + i\sin(\theta).$

$$\Rightarrow x = \underset{=\text{Re}(z)}{r\cos(\theta)}, \quad y = \underset{=\text{Im}(z)}{r\sin(\theta)}.$$

<u>Example</u>: $z = 3 + 2i \Rightarrow r = \sqrt{3^2 + 2^2} = \sqrt{9+4} = \sqrt{13}, \quad \theta = \tan^{-1}\left(\frac{2}{3}\right) \approx 33.69°.$

- <u>Addition and multiplication</u>:

$z_1 = x_1 + y_1 i, \quad z_2 = x_2 + y_2 i \;\rightarrow\; z_1 + z_2 = (x_1 + x_2) + (y_1 + y_2)i$

$z_1 + z_2 = x_1 + y_1 i + x_2 + y_2 i$
$\quad\;\;\, = (x_1 + x_2) + (y_1 + y_2)i$

$\begin{pmatrix} \text{Re}(z_1 + z_2) = \text{Re}(z_1) + \text{Re}(z_2) \\ \text{Im}(z_1 + z_2) = \text{Im}(z_1) + \text{Im}(z_2). \end{pmatrix}$

$z_1 \cdot z_2 = (x_1 + y_1 i)\cdot(x_2 + y_2 i) = x_1 x_2 + x_1 y_2 i + y_1 x_2 i + y_1 y_2 \underbrace{(i \cdot i)}_{=-1}$

$\qquad\quad = (x_1 x_2 - y_1 y_2) + i(x_1 y_2 + y_1 x_2).$

$z_1 = r_1 e^{i\theta_1}, \quad z_2 = r_2 e^{i\theta_2} \;\Rightarrow\; z_1 z_2 = r_1 \cdot r_2\, e^{i\theta_1} e^{i\theta_2} = r_1 \cdot r_2\, e^{i(\theta_1 + \theta_2)}$

## Page 4

## ③ Complex Vector Spaces

- Recall 2D and 3D vectors from linear algebra

[Diagram: 2D coordinate system with x and y axes, showing a vector from origin to point $(a, b)$ with dotted lines indicating components $a$ on x-axis and $b$ on y-axis]

$$\vec{v} = \begin{pmatrix} a \\ b \end{pmatrix}, \quad a, b \in \mathbb{R} \quad \text{\textcolor{red}{$\rightarrow$ real numbers}}$$

- We write $\vec{v} \in \mathbb{R}^2$ $\rightarrow$ all 2D vectors of real numbers.

\textcolor{red}{(Note: this is basically the same as the complex plane!)}

[Diagram: 3D coordinate system with x, y, z axes, showing a vector from origin to point $(a, b, c)$ with dotted lines indicating components]

- In 3D, vectors have three components.

$$\vec{v} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}; \quad a, b, c \in \mathbb{R}.$$

- We write $\underline{\vec{v} \in \mathbb{R}^3}$.

- For any dimension $d \in \{2, 3, \ldots\}$, we have $\vec{v} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix}$, $a_k \in \mathbb{R}$.

and we write $\vec{v} \in \mathbb{R}^d$. The $\underline{\text{norm}}$ (magnitude) of $\vec{v}$ is $\|\vec{v}\| = \sqrt{a_1^2 + a_2^2 + \cdots + a_d^2}$.

- We add (and subtract) vectors component-wise

$$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \quad \vec{v}_2 = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} \implies \vec{v}_1 + \vec{v}_2 = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ \vdots \\ a_d + b_d \end{pmatrix}.$$

## Page 5

- We can take the <u>dot product</u> of two vectors.

$$\vec{V}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \qquad \vec{V}_2 = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} \implies \vec{V}_1 \cdot \vec{V}_2 = a_1 b_1 + a_2 b_2 + \cdots + a_d b_d = \sum_{k=1}^{d} a_k b_k$$

⊛ <u>Observe</u>: $\vec{V}_1 \cdot \vec{V}_1 = a_1^2 + a_2^2 + \cdots + a_d^2 = \|\vec{V}\|^2.$

Geometric interpretation in 2D:

[Diagram: 2D coordinate axes with $x$ and $y$ labeled. Two vectors $\vec{V}_1$ and $\vec{V}_2$ drawn from the origin, with angle $\theta$ between them.]

$$\vec{V}_1 \cdot \vec{V}_2 = \|\vec{V}_1\| \cdot \|\vec{V}_2\| \cdot \cos\theta$$

⊛ So the dot product tells us how much the two vectors overlap.

- <u>Complex vectors</u> are similar!

$$\vec{V} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \longrightarrow \text{but now each } \underline{\underline{a_k \in \mathbb{C}}}! \quad \text{[Each } a_k \text{ is a complex number.]}$$

with $a_k = x_k + y_k i$

⊛ <u>We write $\vec{V} \in \mathbb{C}^d$.</u>

- Addition as before: $\vec{V}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \quad \vec{V}_2 = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} \implies \vec{V}_1 + \vec{V}_2 = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ \vdots \\ a_d + b_d \end{pmatrix}.$

- But dot product changes! And we call it "<u>inner product</u>" instead:

$$\vec{V}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \quad \vec{V}_2 = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} \implies \langle \vec{V}_1, \vec{V}_2 \rangle = \bar{a}_1 b_1 + \bar{a}_2 b_2 + \cdots + \bar{a}_d b_d.$$

## Page 6

- Conjugate transpose of a vector:

$$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \rightarrow \vec{v}_1^\dagger = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix}$$

$$\vec{v}^T = \begin{pmatrix} a_1 & a_2 & \cdots & a_d \end{pmatrix}$$

✱ Observe: $\vec{v}_1^\dagger \vec{v}_2 = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix} \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_d \end{pmatrix} = \bar{a}_1 b_1 + \bar{a}_2 b_2 + \cdots + \bar{a}_d b_d = \langle \vec{v}_1, \vec{v}_2 \rangle.$

We will use this fact all the time in quantum computing!

✱ Norm of a complex vector is $\|\vec{v}\| = \sqrt{|a_1|^2 + |a_2|^2 + \cdots + |a_d|^2} = \sqrt{\langle \vec{v}, \vec{v} \rangle}$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad \underbrace{\phantom{xxx}}_{a_i \cdot \bar{a}_i}$

— <u>Basis</u> of a vector space.

- We can write a vector as

$$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} = \begin{pmatrix} a_1 \\ 0 \\ \vdots \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ a_2 \\ \vdots \\ 0 \end{pmatrix} + \cdots + \begin{pmatrix} 0 \\ 0 \\ \vdots \\ a_d \end{pmatrix}$$

$$= a_1 \underbrace{\begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}}_{\vec{e}_1} + a_2 \underbrace{\begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}}_{\vec{e}_2} + \cdots + a_d \underbrace{\begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}}_{\vec{e}_d}$$

$$= \sum_{k=1}^{d} a_k \vec{e}_k \quad \longrightarrow \text{The "standard" basis}$$

✱ $\{\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_d\}$ are <u>basis vectors</u>. Every vector can be written as a <u>linear combination</u> of these basis vectors.

## Page 7

✺ These basis vectors are __orthonormal__

Two parts to this term:

1. __Orthogonal__: $\langle \vec{e}_i, \vec{e}_j \rangle = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$

   $\equiv \delta_{i,j} \rightarrow$ "Kronecker delta"

2. __Normalised__: $\|\vec{e}_k\| = \sqrt{\langle \vec{e}_k, \vec{e}_k \rangle} = 1$ for all $k$.

[Right side, in blue:]
$d = 3 \rightarrow \vec{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix},\ \vec{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$

$\vec{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

$\langle \vec{e}_1, \vec{e}_2 \rangle = (1\ 0\ 0) \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = 0$

$\langle \vec{e}_1, \vec{e}_1 \rangle = (1\ 0\ 0) \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = 1$

✺ We can extract the components of a vector in this basis using the inner product:

$$\langle \vec{e}_k, \vec{v} \rangle = \left\langle \vec{e}_k, \sum_{\ell=1}^{d} a_\ell \vec{e}_\ell \right\rangle = \sum_{\ell=1}^{d} \underbrace{\langle \vec{e}_k, \vec{e}_\ell \rangle}_{\delta_{k,\ell}} a_\ell = a_k.$$

[Right side, in blue:]
$\langle \vec{e}_1, a_1 \vec{e}_1 + a_2 \vec{e}_2 \rangle$
$= a_1 \underbrace{\langle \vec{e}_1, \vec{e}_1 \rangle}_{=1} + a_2 \underbrace{\langle \vec{e}_1, \vec{e}_2 \rangle}_{=0}$
$= a_1$

— __Bra-ket notation__: very important, used throughout quantum information and quantum computing.

$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \rightarrow \vec{v}_1^\dagger = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix}$

[Blue annotations:]
$|v_1\rangle$, $|v_1\rangle = \sum_{k=1}^{d} a_k |e_k\rangle$, $|e_1\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$

[Red annotations:]
relabel as $|v_1\rangle \rightarrow$ call it a "ket".

relabel as $\langle v_1 | \rightarrow$ call it "bra"

- Then the inner product is $\langle \vec{v}_1, \vec{v}_2 \rangle = \vec{v}_1^\dagger \vec{v}_2 = \langle v_1 | v_2 \rangle$

  [Red:] "bra-ket"

[Bottom right:] $\delta_{k,k'}$

## Page 8

- We write the basis vectors as $\ket{e_k}$

$$\rightarrow \ket{v} = \sum_{k=1}^{d} a_k \ket{e_k} \quad \rightarrow \quad \bra{v} = \sum_{k=1}^{d} \bar{a}_k \bra{e_k} \quad \rightarrow \quad \braket{v|v} = \sum_{k=1}^{d} \bar{a}_k \cdot a_k = \sum_{k=1}^{d} |a_k|^2 = \| \ket{v} \|^2$$

$$\left( \sum_{k=1}^{d} \bar{a}_k \bra{e_k} \right) \left( \sum_{k'=1}^{d} a_{k'} \ket{e_{k'}} \right) = \sum_{k,k'=1}^{d} \bar{a}_k a_{k'} \braket{e_k | e_{k'}}$$

⊛ With this abstract notation, we do not have to explicitly write column vectors! (Helpful for large vectors — for $n$ qubits the size of the vectors is $2^n$!)


# Lectures__measurements(II).pdf

## Page 1

# ① Recap: Measurements

- To extract classical information from a qubit, we must <u>measure</u> it
- <u>Recall</u>: $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$ → Probability of 0: $|\alpha|^2$
  Probability of 1: $|\beta|^2$

  ⊛ <u>Axiom of quantum mechanics!</u> (aka "Born Rule")

  ⊛ <u>Note</u>: $|\alpha|^2 = |\braket{0|\psi}|^2$, $|\beta|^2 = |\braket{1|\psi}|^2$

  <u>Also</u>: $|\braket{0|\psi}|^2 = \braket{0|\psi}\braket{\psi|0} = \mathrm{Tr}[\ket{0}\bra{0}\ket{\psi}\bra{\psi}]$
  $\quad\quad\quad \equiv P_r[0]$

  $\quad\quad\quad$ → "Measurement operators"

  $|\braket{1|\psi}|^2 = \braket{1|\psi}\braket{\psi|1} = \mathrm{Tr}[\ket{1}\bra{1}\ket{\psi}\bra{\psi}]$
  $\quad\quad\quad \equiv P_r[1]$

  $$P_r[0] + P_r[1] = \mathrm{Tr}\big[\underbrace{(\ket{0}\bra{0} + \ket{1}\bra{1})}_{\mathbb{1}}\rho\big] = \mathrm{Tr}[\rho] = 1$$

- For a density matrix $\rho$: $P_r[0] = \mathrm{Tr}[\ket{0}\bra{0}\rho]$, $P_r[1] = \mathrm{Tr}[\ket{1}\bra{1}\rho]$.

⊛ This is often called a "computational-basis measurement" or a "$\{\ket{0}, \ket{1}\}$-basis measurement".

⊛ Recall that $\{\ket{0}, \ket{1}\}$ is also the eigenvectors of Pauli-Z:

$Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$. → So we also sometimes say "<u>Pauli-Z measurement</u>"

⊛ <u>Circuit symbol</u>: $\ket{\psi} \!-\!\boxed{x}\!=$

- <u>Pauli-X measurement</u>: measure along x-axis; equivalent to measuring in basis $\{\ket{+}, \ket{-}\}$ → $\ket{+}\bra{+} + \ket{-}\bra{-} = \mathbb{1}$

  ⊛ Recall: $\ket{+} = H\ket{0}$, $\ket{-} = H\ket{1}$, $H \equiv$ Hadamard gate
  $\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

  ⊛ $H$ unitary $\Rightarrow \{\ket{+}, \ket{-}\}$ is a basis!

[Bloch sphere on right: z-axis up with $\ket{0}$ at top, $\ket{1}$ at bottom; y-axis with $\ket{-i}$ and $\ket{+i}$; x-axis with $\ket{+}$ and $\ket{-}$]

## Page 2

✸ For a state vector $\ket{\psi}$: $\Pr[+] = |\braket{+|\psi}|^2 = \braket{+|\psi}\braket{\psi|+} = \mathrm{Tr}[\ket{+}\bra{+}\ket{\psi}\bra{\psi}]$.

$\Pr[-] = |\braket{-|\psi}|^2 = \braket{-|\psi}\braket{\psi|-} = \mathrm{Tr}[\ket{-}\bra{-}\ket{\psi}\bra{\psi}]$

✸ <u>For a density operator $\rho$</u>: $\Pr[+] = \mathrm{Tr}[\ket{+}\bra{+}\rho]$, $\Pr[-] = \mathrm{Tr}[\ket{-}\bra{-}\rho]$.

  <span style="color:red">↑ Measurement operators. ↑</span>

✸ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{H} - \boxed{X} \!=\!\!=$

[Bloch sphere: $\ket{0}$ at top (+z), $\ket{1}$ at bottom, $\ket{+}$ on +x (front), $\ket{-}$ on −x, $\ket{+i}$ on +y, $\ket{-i}$ on −y. Axes labeled $z, y, x$.]

- <u>Pauli-Y measurement</u>: measure along $y$-axis; equivalent to measuring in basis $\{\ket{+i}, \ket{-i}\}$

✸ <span style="color:red">Recall: $\ket{+i} = SH\ket{0}$, $\ket{-i} = SH\ket{1}$, $H \equiv$ Hadamard gate</span>

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$S \equiv$ phase gate
$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

✸ <span style="color:red">$SH$ is unitary $\Rightarrow \{\ket{+i}, \ket{-i}\}$ is a basis!</span>

✸ For a state vector $\ket{\psi}$: $\Pr[+i] = |\braket{+i|\psi}|^2 = \braket{+i|\psi}\braket{\psi|+i} = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}]$.

$\ket{+i}\bra{+i} + \ket{-i}\bra{-i} = \mathbb{1}$.

$\Pr[-i] = |\braket{-i|\psi}|^2 = \braket{-i|\psi}\braket{\psi|-i} = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$

✸ <u>For a density operator $\rho$</u>: $\Pr[+i] = \mathrm{Tr}[\ket{+i}\bra{+i}\rho]$, $\Pr[-i] = \mathrm{Tr}[\ket{-i}\bra{-i}\rho]$.

  <span style="color:red">↑ Measurement operators. ↑</span>

— <u>Measuring multiple qubits</u>.

- Consider state vector $\ket{\psi}$ of $n$ qubits $\big(\ket{\psi} \in (\mathbb{C}^2)^{\otimes n}\big)$. → or density matrix $\rho$.

- Computational-basis measurement is a $\{\ket{0}, \ket{1}\}$ measurement on each qubit

- Outcome probabilities: $\Pr[0,0,1] = |\braket{0,0,1|\psi}|^2$ (for three qubits).
  
  with $\braket{0,0,1} = \bra{0}\otimes\bra{0}\otimes\bra{1}$
  
  $\Pr[x_1, x_2, x_3] = |\braket{x_1, x_2, x_3|\psi}|^2$, $x_1, x_2, x_3 \in \{0,1\}$.
  
  $= \mathrm{Tr}[\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3}\ket{\psi}\bra{\psi}]$

$\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3} = \ket{x_1}\bra{x_1} \otimes \ket{x_2}\bra{x_2} \otimes \ket{x_3}\bra{x_3}$

✸ For a density operator $\rho$: $\mathrm{Tr}[\ket{x_1,x_2,x_3}\bra{x_1,x_2,x_3}\rho]$.

## Page 3

## Expectation Value of an Observable.

**❋ Axiom of Quantum Mechanics:** Observables are described mathematically by **Hermitian operators**. $H^\dagger = H$.

- **Recall:** Hermitian operators have a *spectral/eigenvalue decomposition*:

$$H\ket{\chi_k} = \lambda_k \ket{\chi_k}$$

$$H = \sum_{k=1}^{d} \lambda_k \ket{\chi_k}\bra{\chi_k}$$

  ↑ eigenvectors.
  eigenvalues (real numbers).

**❋ Examples:** the Pauli operators!

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \ket{+}\bra{+} - \ket{-}\bra{-}$$

$$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \ket{+i}\bra{+i} - \ket{-i}\bra{-i}$$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \ket{0}\bra{0} - \ket{1}\bra{1}.$$

- Eigenvectors are orthonormal basis ⇒ they define a measurement!

$$\sum_{k=1}^{d} \ket{\chi_k}\bra{\chi_k} = \mathbb{1}.$$

For a density operator $\rho$:
$$\Pr[k] = \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big) \to \text{The associated ``observed'' value is } \lambda_k.$$

(Example: $k \equiv$ energy level of a molecule, $\lambda_k \equiv$ the energy value).

$$\sum_{k=1}^{d} \Pr(k) = \sum_{k=1}^{d} \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big) = \mathrm{Tr}\Big(\underbrace{\Big(\sum_{k=1}^{d}\ket{\chi_k}\bra{\chi_k}\Big)}_{=\,\mathbb{1}}\rho\Big) = \mathrm{Tr}(\rho) = 1.$$

- The expected (aka "mean" or "average") value of an observable, given a state $\rho$, is

$$\sum_{k=1}^{d} \Pr(k)\cdot \lambda_k = \sum_{k=1}^{d} \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big)\cdot \lambda_k$$

$$= \mathrm{Tr}\Big(\underbrace{\Big(\sum_{k=1}^{d}\lambda_k\ket{\chi_k}\bra{\chi_k}\Big)}_{H}\rho\Big) = \underline{\underline{\mathrm{Tr}(H\rho)}}$$

$$\left(\begin{array}{l}\text{❋ Recall: for a}\\ \text{random variable } X,\\ \mathbb{E}(X) = \sum_x \Pr(X=x)\cdot x\end{array}\right)$$

## Page 4

② <u>Partial Measurements: Measuring Only Some Qubits</u>

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ enter from the left. Three layers of two-qubit gates (boxes) are applied. After the 3rd layer, the 1st, 3rd, and 5th qubits are measured (shown as red measurement boxes outputting $x$). Dashed vertical lines separate 1st layer, 2nd layer, 3rd layer. Time axis points to the right.]

$(x_1, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

✺ Suppose we only measure the 1st, 3rd, and 5th qubits.

— To get the measurement outcome probabilities, we apply the measurement operators only on the relevant qubits.

✺ <u>Notation</u>: States and operators for multiple qubits and qudits.

- For two qubits, the standard basis is $\{\ket{0}\otimes\ket{0}, \ket{0}\otimes\ket{1}, \ket{1}\otimes\ket{0}, \ket{1}\otimes\ket{1}\}$
  
  $\equiv \ket{0,0}, \equiv \ket{0,1}, \equiv \ket{1,0}, \equiv \ket{1,1}$
  
  [arrows pointing to first factor: "1st qubit"; second factor: "2nd qubit"]

  We often <u>label</u> the qubits by $A, B, C, \dots$

  So we write $\ket{0,0}_{AB} \equiv \ket{0}_A \otimes \ket{0}_B$.
  
  ["qubit A", "qubit B"]
  
  $\rightarrow$ For state vector $\ket{\psi}_{AB} \in \mathbb{C}^2 \otimes \mathbb{C}^2$
  
  [arrows: "qubit A", "qubit B"]

  $\ket{\psi}_{AB} = a\ket{0,0}_{AB} + b\ket{0,1}_{AB} + c\ket{1,0}_{AB} + d\ket{1,1}_{AB}$.

- Similar for three or more qubits: $\ket{\psi}_{ABC} = \sum_{\vec{x} \in \{0,1\}^3} c_{\vec{x}} \ket{\vec{x}}_{ABC}$
  
  $\ket{\vec{x}}_{ABC} \equiv \ket{x_1, x_2, x_3}_{ABC}$

## Page 5

For $n$ qubits: $\ket{\psi}_{A_1 A_2 \cdots A_n} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}}_{A_1 A_2 \cdots A_n}$

$$\hookrightarrow \equiv \ket{x_1, x_2, \ldots, x_n}_{A_1 A_2 \cdots A_n}$$
$$\equiv \ket{x_1}_{A_1} \otimes \ket{x_2}_{A_2} \otimes \cdots \otimes \ket{x_n}_{A_n}$$

- We do the same for linear operators (including density operators)

$M \in L(\mathbb{C}^d) \quad M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}) \to (d_A \cdot d_B) \times (d_A \cdot d_B)$ matrix

System $A$ has dimension $d_A$; $B$ has dimension $d_B$.

$$M_{AB} = \sum_{i,j=0}^{d_A - 1} \sum_{k,\ell=0}^{d_B - 1} M_{i,k;j,\ell} \, \ket{i,k}\bra{j,\ell}_{AB}$$

$$\hookrightarrow \equiv \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B \to \text{These form a basis for } L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}).$$

$$M_{A_1 A_2 \cdots A_n} \in L(\mathbb{C}^{d_{A_1}} \otimes \mathbb{C}^{d_{A_2}} \otimes \cdots \otimes \mathbb{C}^{d_{A_n}}) \to (d_{A_1} \cdot d_{A_2} \cdots d_{A_n}) \times (d_{A_1} \cdot d_{A_2} \cdots d_{A_n}) \text{ matrix.}$$

— Suppose we have a two-qubit density operator $\rho_{AB}$, and we measure the qubit $A$ in the computational basis.

Measurement operators are $\ket{0}\bra{0}$ and $\ket{1}\bra{1}$.

Probabilities are: 
$$\Pr[0] = \mathrm{Tr}\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B)\, \rho_{AB}\right]$$

$$\Pr[1] = \mathrm{Tr}\left[\underbrace{(\ket{1}\bra{1}_A \otimes \mathbb{1}_B)}_{\uparrow}\, \rho_{AB}\right]$$

We measure qubit $A$ only, so we apply the measurement operator only on $A$; we apply identity ("do nothing") on $B$.

## Page 6

If we measure only $B$, then: $\Pr[x] = \text{Tr}\left[(\mathbb{1}_A \otimes \ket{x}\bra{x}_B)\rho_{AB}\right]$, $x \in \{0,1\}$.

If we measure both $A$ & $B$, then: $\Pr[x_1, x_2] = \text{Tr}\left[\underbrace{(\ket{x_1}\bra{x_1}_A \otimes \ket{x_2}\bra{x_2}_B)}_{\ket{x_1, x_2}\bra{x_1, x_2}_{AB}}\rho_{AB}\right]$.

- Suppose we only measure the 1$^{st}$, 3$^{rd}$, and 5$^{th}$ qubits.

[Circuit diagram: 6 qubit lines labeled $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ from top to bottom. Three layers of two-qubit gates separated by dashed vertical lines (1$^{st}$ layer, 2$^{nd}$ layer, 3$^{rd}$ layer). At the end, measurement boxes labeled $x$ on qubits 1, 3, and 5 (drawn in red). Time axis points to the right.]

$(x_1, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

- Let the state before measurement be given by the density operator $\rho_{A_1 A_2 \cdots A_6}$

- The probability distribution is given by:

$$\Pr[x_1, x_2, x_3] = \text{Tr}\left[\left(\ket{x_1}\bra{x_1}_{A_1} \otimes \mathbb{1}_{A_2} \otimes \ket{x_2}\bra{x_2}_{A_3} \otimes \mathbb{1}_{A_4} \otimes \ket{x_3}\bra{x_3}_{A_5} \otimes \mathbb{1}_{A_6}\right) \rho_{A_1 \cdots A_6}\right].$$

$x_1, x_2, x_3 \in \{0,1\}$.

## ③ The Partial Trace

- When we only measure parts of a quantum system, we only need to know the state of that <u>subsystem</u> — we can "ignore" the rest of the system.

- The partial trace describes how (mathematically) to describe ignoring/discarding parts of a system.

## Page 7

- For a linear operator $M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B})$, the (full) trace is:

$$\text{Tr}[M_{AB}] = \sum_{k=0}^{d_A-1} \sum_{\ell=0}^{d_B-1} \braket{k,\ell|_{AB} M_{AB} | k,\ell}_{AB}. \quad \text{\color{red}(sum of the diagonal elements).}$$

<span style="color:red">(Recall that $\{\ket{k,\ell} : k \in \{0,1,\ldots,d_A-1\}, \ell \in \{0,1,\ldots,d_B-1\}\}$ is a basis.)</span>

<span style="color:blue">$\text{Tr}[M] = \sum_{k=0}^{d-1} \braket{k|M|k}$</span>

$$\text{Tr}[M_{AB}] = \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \big(\bra{k}_A \otimes \bra{\ell}_B\big) M_{AB} \big(\ket{k}_A \otimes \ket{\ell}_B\big).$$

- <u>Partial trace over B</u>: $\text{Tr}_B[M_{AB}] = \cancel{\sum_{k=0}^{d_A-1}}\sum_{\ell=0}^{d_B-1} \big(\cancel{\bra{k}_A}^{\;\mathbb{1}_A} \otimes \bra{\ell}_B\big) M_{AB} \big(\cancel{\ket{k}_A}^{\;\mathbb{1}_A} \otimes \ket{\ell}_B\big).$

  $$\downarrow$$
  $$= \sum_{\ell=0}^{d_B-1} \big(\mathbb{1}_A \otimes \bra{\ell}_B\big) M_{AB} \big(\mathbb{1}_A \otimes \ket{\ell}_B\big).$$

  ⊛ <u>Note</u>: the outcome is an operator! Not a scalar, like the full trace.

- <u>Partial trace over A</u>: $\text{Tr}_A[M_{AB}] = \sum_{k=0}^{d_A-1}\cancel{\sum_{\ell=0}^{d_B-1}} \big(\bra{k}_A \otimes \cancel{\bra{\ell}_B}^{\;\mathbb{1}_B}\big) M_{AB} \big(\ket{k}_A \otimes \cancel{\ket{\ell}_B}^{\;\mathbb{1}_B}\big).$

  $$\downarrow$$
  $$= \sum_{k=0}^{d_A-1} \big(\bra{k}_A \otimes \mathbb{1}_B\big) M_{AB} \big(\ket{k}_A \otimes \mathbb{1}_B\big).$$

  ⊛ <u>Note</u>: the outcome is an operator! Not a scalar, like the full trace.

- Some Properties:

(1) $\text{Tr}_A[M_A \otimes N_B] = \sum_{k=0}^{d_A-1} \big(\bra{k}_A \otimes \mathbb{1}_B\big)\big(M_A \otimes N_B\big)\big(\ket{k}_A \otimes \mathbb{1}_B\big).$

<span style="color:blue">$= \big(\bra{k}_A M_A \otimes \mathbb{1}_B \cdot N_B\big) = \bra{k}_A M_A \otimes N_B.$</span>

$$\downarrow$$
$$= \sum_{k=0}^{d_A-1} \braket{k|_A M_A | k}_A \, N_B$$
$$= \text{Tr}[M_A]\, N_B.$$

$$\left(\begin{array}{l} \circledast \text{ Property of tensor product:} \\ (M_1 \otimes M_2)(N_1 \otimes N_2) = M_1 N_1 \otimes M_2 N_2 \end{array}\right)$$

(2) $\text{Tr}_B[M_A \otimes N_B] = \text{Tr}[N_B]\, M_A.$

<span style="color:blue">$\big(\bra{k}_A M_A \otimes N_B\big)\big(\ket{k}_A \otimes \mathbb{1}_B\big) = \braket{k|M_A|k} \cdot N_B.$</span>

## Page 8

$M_{AB} \in L(\mathbb{C}^2 \otimes \mathbb{C}^2) \quad \to \quad M_{AB} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array} \begin{array}{c} \begin{matrix} 00 & 01 & 10 & 11 \end{matrix} \\ \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix} \end{array}$

[The matrix entries are grouped by 2×2 blocks: green circles $a_{11}, a_{22}$; purple $a_{13}, a_{24}$; pink $a_{31}, a_{42}$; orange $a_{33}, a_{44}$.]

$$= \sum_{i,j=0}^{1} \sum_{k,\ell=0}^{1} M_{i,k;j,\ell} \, \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B.$$

$$\mathrm{Tr}_B[M_{AB}] = \sum_{i,j=0}^{1} \sum_{k,\ell=0}^{1} M_{i,k;j,\ell} \, \underbrace{\mathrm{Tr}_B\!\left[\ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B\right]}_{=\,\ket{i}\bra{j}\,\cdot\,\underbrace{\mathrm{Tr}[\ket{k}\bra{\ell}]}_{\delta_{k,\ell}}} = \sum_{i,j=0}^{1} \sum_{k=0}^{1} M_{i,k;j,k} \, \ket{i}\bra{j}_A$$

$$\mathrm{Tr}_B[M_{AB}] = \begin{array}{c} \\ 0 \\ 1 \end{array} \begin{array}{c} \begin{matrix} 0 & \quad 1 \end{matrix} \\ \begin{pmatrix} a_{11}+a_{22} & a_{13}+a_{24} \\ a_{31}+a_{42} & a_{33}+a_{44} \end{pmatrix} \end{array}$$

## Page 9

- Recall: for a computational-basis measurement on qubit $A$ of two-qudit system $AB$ in state $\rho_{AB}$: $\Pr[x] = \text{Tr}\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B) \rho_{AB} \big)$

  $\{\ket{k,\ell}: k \in \{0,1,\ldots,d_A-1\},\ \ell \in \{0,1,\ldots,d_B-1\}\}$ is a basis

  $\quad \xrightarrow{\ \ } \underline{= \text{Tr}\big[ \ket{x}\bra{x}_A \,\text{Tr}_B(\rho_{AB}) \big]}.$

$$\Rightarrow \text{Tr}\big[ (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big] = \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \bra{k,\ell}_{AB}\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big)\ket{k,\ell}_{AB}.$$

(This is a sum over the diagonal elements.)

$$= \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} (\bra{k}_A \otimes \bra{\ell}_B)\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big)(\ket{k}_A \otimes \ket{\ell}_B).$$

$\left( \circledast \text{ Property of tensor product:} \atop (M_1 \otimes M_2)(N_1 \otimes N_2) = M_1 N_1 \otimes M_2 N_2 \right)$

$$= \bra{k}_A (\mathbb{1}_A \otimes \bra{\ell}_B)(\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$\left( \circledast\ (\mathbb{1}_A \otimes M_B)(N_A \otimes \mathbb{1}_B) \atop = N_A \otimes M_B \atop = (N_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes M_B). \right)$

$$= \bra{k}_A \ket{x}\bra{x}_A (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$$= \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \bra{k}_A \ket{x}\bra{x}_A (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$$= \sum_{k=0}^{d_A-1} \bra{k}_A \ket{x}\bra{x}_A \left( \underbrace{\sum_{\ell=0}^{d_B-1} (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)}_{\equiv\, \text{Tr}_B(\rho_{AB})\ \to\ \text{the partial trace!}} \right) \ket{k}_A$$

## Page 10

Compare with the full trace:

$$\mathrm{Tr}(\rho_{AB}) = \sum_{k=0}^{d_A-1} \sum_{\ell=0}^{d_B-1} \left(\bra{k}_A \otimes \bra{\ell}_B\right) \rho_{AB} \left(\ket{k}_A \otimes \ket{\ell}_B\right).$$

$$= \mathrm{Tr}\left[\ket{x}\bra{x}_A \underbrace{\mathrm{Tr}_B(\rho_{AB})}_{=\rho_A}\right]$$

For measurement of $B$ instead: $\Pr(x) = \mathrm{Tr}\left[\left(\mathbb{1}_A \otimes \ket{x}\bra{x}_B\right)\rho_{AB}\right] = \mathrm{Tr}\left[\ket{x}\bra{x}_B \underbrace{\mathrm{Tr}_A(\rho_{AB})}_{=\rho_B}\right].$


# Lectures__measurements(III)+entanglement.pdf

## Page 1

# 1. Measurements

- Every orthonormal basis $\{\ket{e_k}\}_{k=1}^{d}$ in dimension $d$ defines a __measurement__: operators $\{\ket{e_k}\bra{e_k}\}_{k=1}^{d}$ such that $\sum_{k=1}^{d} \ket{e_k}\bra{e_k} = \mathbb{1}_d$.

For a state $\rho$:  $\Pr(k) = \mathrm{Tr}\big[\ket{e_k}\bra{e_k}\rho\big] = \braket{e_k|\rho|e_k}$  ("Born rule")

$$\sum_{k=1}^{d} \Pr(k) = \mathrm{Tr}\Big[\underbrace{\Big(\sum_{k=1}^{d} \ket{e_k}\bra{e_k}\Big)}_{=\,\mathbb{1}_d}\rho\Big] = \mathrm{Tr}(\rho) = 1.$$

⊛ __Example__: For the state $\rho = \frac{\mathbb{1}}{d}$ (the "maximally-mixed" state), the outcomes are completely random in every basis! (i.e., $\Pr(k) = \frac{1}{d}\ \forall\, k$).

- For a bipartite state $\rho_{AB} \rightarrow$ measuring $A$ only: $\Pr(k) = \mathrm{Tr}\big[(\ket{e_k}\bra{e_k}_A \otimes \mathbb{1}_B)\,\rho_{AB}\big]$

This is equal to $\Pr(k) = \mathrm{Tr}\big[\ket{e_k}\bra{e_k}_A\, \mathrm{Tr}_B(\rho_{AB})\big]$
$$\uparrow$$
$$\text{\underline{Partial trace}}$$

⊛ For an operator $M_{AB} = \displaystyle\sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,j;\,k,\ell}\, \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B.$

$$\mathrm{Tr}_B(X_A \otimes Y_B) = X_A \cdot \mathrm{Tr}(Y_B)$$

$$\mathrm{Tr}_B(M_{AB}) = \sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,k;\,j,\ell}\, \ket{i}\bra{j}_A\, \underbrace{\mathrm{Tr}(\ket{k}\bra{\ell}_B)}_{\delta_{k,\ell}}$$

$$= \sum_{i,j=0}^{d_A-1}\Big(\sum_{k=0}^{d_B-1} M_{i,k;\,j,k}\Big)\ket{i}\bra{j}_A$$

$$\mathrm{Tr}_A(M_{AB}) = \sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,j;\,k,\ell}\, \underbrace{\mathrm{Tr}(\ket{i}\bra{j}_A)}_{\delta_{i,j}}\ket{k}\bra{\ell}_B = \sum_{k,\ell=0}^{d_B-1}\Big(\sum_{i=0}^{d_A-1} M_{i,k;\,i,\ell}\Big)\ket{k}\bra{\ell}_B.$$

## Page 2

For a two-qubit operator: 
$$M_{AB} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{pmatrix} \overset{00}{a_{11}} & \overset{01}{a_{12}} & \overset{10}{a_{13}} & \overset{11}{a_{14}} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}$$

$$\mathrm{Tr}_B(M_{AB}) = \mathrm{Tr}_B\!\left[\begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}\right] = \begin{pmatrix} a_{11}+a_{22} & a_{13}+a_{24} \\ a_{31}+a_{42} & a_{33}+a_{44} \end{pmatrix}$$

[The 4×4 matrix is partitioned into 2×2 blocks; within each block, the diagonal entries are summed to produce the corresponding entry of the reduced 2×2 matrix. Color-coding: $a_{11},a_{22}$ (orange) → top-left; $a_{13},a_{24}$ (pink) → top-right; $a_{31},a_{42}$ (purple) → bottom-left; $a_{33},a_{44}$ (red) → bottom-right.]

$$\mathrm{Tr}_A(M_{AB}) = \mathrm{Tr}_A\!\left[\begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}\right] = \begin{pmatrix} a_{11}+a_{33} & a_{12}+a_{34} \\ a_{21}+a_{43} & a_{22}+a_{44} \end{pmatrix}$$

[Color-coding: $a_{11},a_{33}$ (orange) → top-left; $a_{12},a_{34}$ (pink) → top-right; $a_{21},a_{43}$ (purple) → bottom-left; $a_{22},a_{44}$ (red) → bottom-right.]

— The most general form of a measurement is given by a <u>positive operator-valued measure (POVM)</u>: a (finite) set $\{M_x\}_{x \in \mathcal{X}}$ ← outcome labels.

(1) $M_x \geq 0 \quad \forall\, x \in \mathcal{X}$

(2) $\sum_x M_x = \mathbb{1}$.

- Probabilities are given by $\Pr(x) = \mathrm{Tr}(M_x \rho)$

❋ <u>Check</u>: $\sum_{x \in \mathcal{X}} \Pr(x) = \sum_{x \in \mathcal{X}} \mathrm{Tr}(M_x \rho) = \mathrm{Tr}\!\left[\underbrace{\left(\sum_x M_x\right)}_{=\mathbb{1}}\rho\right] = \mathrm{Tr}(\rho) = 1.$ ✓

## Page 3

- Measurements of the form $\{\ket{e_k}\bra{e_k}\}_{k=1}^{d}$, for an orthonormal basis $\{\ket{e_k}\}_{k=1}^{d}$, are known as <u>projective measurements</u>, b/c $M_k \equiv \ket{e_k}\bra{e_k}$ are <u>projectors</u>.

> ✱ A <u>projector</u> is an operator/matrix satisfying $P^2 = P$.
>
> <u>Check</u>: $\big(\ket{e_k}\bra{e_k}\big)^2 = \ket{e_k}\underbrace{\braket{e_k|e_k}}_{=1}\bra{e_k} = \ket{e_k}\bra{e_k}\ \checkmark$

- A <u>general projective measurement</u> has the form $\{\Pi_x\}_{x \in X}$:

  (1) $\Pi_x \geq 0 \quad \forall x \in X$

  (2) $\Pi_x^2 = \Pi_x \quad \forall x \in X$

  (3) $\sum_{x \in X} \Pi_x = \mathbb{1}$.

- <u>Theorem</u>: Every general (POVM) measurement can be written as a projective measurement on a larger system.

  <u>Proof</u>: Consider a system $S$; we want to measure it via a probe $P$.

  [Circuit diagram: top wire labeled $\rho_S$ entering box $U$; bottom wire labeled $\ket{0}$ entering box $U$; bottom output of $U$ goes into a measurement box labeled $x$, $\{\Pi_x\}_x$ ← Projective measurement of the probe.]

  ↑ <span style="color:red">Unitary interaction of system and probe.</span>

$$\rho_S \otimes \ket{0}\bra{0}_P \;\mapsto\; U(\rho_S \otimes \ket{0}\bra{0})U^\dagger \;\mapsto\; \underline{\Pr[x] = \mathrm{Tr}\!\left[(\mathbb{1}_S \otimes \Pi_x)\, U(\rho_S \otimes \ket{0}\bra{0})U^\dagger\right]}$$

✱ We can write this in the form $\mathrm{Tr}[M_x \rho_S]$.

## Page 4

$$\text{Tr}\left[(\mathbb{1}_S \otimes \Pi_x) U (\rho_S \otimes \ket{0}\bra{0}_p) U^\dagger\right] = \text{Tr}\left[(\rho_S \otimes \ket{0}\bra{0}) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$\text{Tr}[ABC] = \text{Tr}[BCA] = \text{Tr}[CAB].$

$(X_A \otimes Y_B) = (X_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes Y_B)$

$\text{Tr}\left[(\rho_A \otimes \mathbb{1}_B) M_{AB}\right] = \text{Tr}\left[\rho_A \, \text{Tr}_B[M_{AB}]\right]$

$$= \text{Tr}\left[(\rho_S \otimes \mathbb{1}_p)(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$$= \text{Tr}\left[\rho_S \, \underbrace{\text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]}_{\equiv M_x}\right]$$

Let us show that $\{M_x\}_{x \in \mathcal{X}}$ is a POVM.

(1) Check that $M_x \geq 0.$  $\quad \langle v | M_x | v \rangle \geq 0 \;\; \forall \ket{v}$

For an arbitrary vector $\ket{v}$:

$$\langle v | M_x | v \rangle = \langle v | \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right] | v \rangle$$

$\text{Tr}[M \ket{v_1}\bra{v_2}]$
$= \langle v_2 | M | v_1 \rangle$

$$= \text{Tr}\left[(\ket{v}\bra{v}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$$= \underbrace{(\bra{v}_S \otimes \bra{0}_p) U^\dagger}_{\equiv \bra{v'}} (\mathbb{1}_S \otimes \Pi_x) \underbrace{U (\ket{v}_S \otimes \ket{0}_p)}_{\equiv \ket{v'}}$$

$$= \langle v' | (\mathbb{1}_S \otimes \Pi_x) | v' \rangle$$

$\geq 0$ b/c $\Pi_x \geq 0$ and $\mathbb{1}_S \geq 0 \Rightarrow \mathbb{1}_S \otimes \Pi_x \geq 0.$

So $M_x \geq 0 \;\checkmark\; \forall x$

(2) Check that $\sum_{x \in \mathcal{X}} M_x = \mathbb{1}.$

$$\sum_{x \in \mathcal{X}} M_x = \sum_{x \in \mathcal{X}} \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right] = \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \underbrace{\sum_{x \in \mathcal{X}} \Pi_x}_{=\mathbb{1}_p \text{ by assumption}}) U\right]$$

$$= \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) \underbrace{U^\dagger (\mathbb{1}_S \otimes \mathbb{1}_p) U}_{\mathbb{1}_S \otimes \mathbb{1}_p}\right] \quad \rightarrow U^\dagger U = \mathbb{1}$$

## Page 5

$$\downarrow$$
$$= \mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_P)(\mathbb{1}_S \otimes \mathbb{1}_P)\right]$$
$$= \mathrm{Tr}_P\left[\mathbb{1}_S \otimes \ket{0}\bra{0}_P\right]$$
$$= \mathbb{1}_S. \checkmark$$

We also prove the converse: given a POVM $\{M_x\}_{x \in X}$, the measurement can be realised by a unitary b/w system and probe and measurement of the probe.

Define $V = \sum_{x \in X} \sqrt{M_x} \otimes \underbrace{\ket{x}_P}_{\text{some orthonormal vectors.}}$

$\quad\left(\circledast \underline{\text{Note}}: M_x \text{ is Hermitian, so it has spectral decomposition}\right.$
$\quad\left. M_x = \sum_{k=1}^{r} \lambda_k \ket{\varphi_k}\bra{\varphi_k}. \text{ Then the square root is } \sqrt{M_x} = \sum_{k=1}^{r} \sqrt{\lambda_k} \ket{\varphi_k}\bra{\varphi_k}.\right)$

$\circledast$ $V$ is an isometry: it satisfies
$V^\dagger V = \mathbb{1}$ (but not necessarily $VV^\dagger = \mathbb{1}$.)

$\underline{\text{Check}}: V^\dagger V = \left(\sum_x \sqrt{M_x} \otimes \bra{x}_P\right)\left(\sum_{x' \in X} \sqrt{M_{x'}} \otimes \ket{x'}_P\right)$
$$\downarrow$$
$$= \sum_{x,x' \in X} \sqrt{M_x}\sqrt{M_{x'}} \underbrace{\braket{x|x'}}_{=\delta_{x,x'}} = \sum_{x \in X} M_x = \mathbb{1} \checkmark$$

Now note that $\mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{x}\bra{x}_{P}) VV^\dagger\right] = \mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{x}\bra{x})\left(\sum_{x_1 \in X} \sqrt{M_{x_1}} \otimes \ket{x_1}\right)\left(\sum_{x_2 \in X} \sqrt{M_{x_2}} \otimes \bra{x_2}\right)\right]$

$$\downarrow$$
$$= \sum_{x_1, x_2 \in X} \mathrm{Tr}_P\left[\sqrt{M_{x_1}}\sqrt{M_{x_2}} \otimes \underbrace{\ket{x}\braket{x|x_1}\bra{x_2}}_{=\delta_{x,x_1}}\right]$$

$$\downarrow$$
$$= \sum_{x_1, x_2 \in X} \sqrt{M_{x_1}}\sqrt{M_{x_2}}\, \delta_{x,x_1} \underbrace{\braket{x_2|x}}_{=\delta_{x,x_2}}$$

$$\downarrow$$
$$= M_x.$$

## Page 6

So for any state $\rho$:
$$\text{Tr}[M_x \rho] = \text{Tr}\left[\text{Tr}_P\left[(\mathbb{1}_S \otimes \ket{x}\bra{x}_P) VV^\dagger\right]\rho\right]$$

$$= \text{Tr}\left[(\mathbb{1}_S \otimes \ket{x}\bra{x}_P) VV^\dagger (\rho_S \otimes \mathbb{1}_P)\right]$$

$$= \text{Tr}\left[V^\dagger(\rho_S \otimes \mathbb{1}_P) V (\mathbb{1}_S \otimes \underbrace{\ket{x}\bra{x}_P})\right]$$

<span style="color:red">This defines a projective measurement b/c $\{\ket{x}\}$ is an ONB.</span>

<span style="color:red">⊛ **Fact:** for every isometry $V_{S \to SP}$, there exists a unitary $U_{SP}$ such that $V_{S \to SP} = U_{SP}(\mathbb{1}_S \otimes \ket{0}_P)$.</span>

$$= \text{Tr}\left[U^\dagger(\rho_S \otimes \ket{0}\bra{0}_P) U (\mathbb{1}_S \otimes \ket{x}\bra{x}_P)\right]$$

---

— <u>Post-measurement state after a partial measurement</u>: If we have a bipartite state $\rho_{AB}$, and we measure the A part, what is the resulting state on the B part?

- Consider measurement POVM $\{M_A^{(x)}\}_{x \in X}$.

- The probabilities are $\Pr[x] = \text{Tr}\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]$

- Conditioned on the outcome $x$, the state of B is

$$\rho_B^{(x)} = \frac{\text{Tr}_A\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]}{\text{Tr}\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]} \quad \color{red}{\} \Pr[x]}$$

⊛ Check that $\rho_B^{(x)}$ has all of the required properties of a density matrix.

$$\text{Tr}[\rho_B^{(x)}] = \frac{\text{Tr}\left[\text{Tr}_A\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]\right]}{\color{blue}{\Pr[x]}} = \frac{\text{Tr}\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]}{\color{blue}{\Pr[x]}} = 1 \checkmark$$

## Page 7

# 2. Entanglement

**※** State vectors of two qubits belong to the tensor-product space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

(a) — A **product state (vector)** has the form:

(State vector) $\quad \ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B, \quad \ket{\phi_1} \in \mathbb{C}^{d_1}, \quad \ket{\phi_2} \in \mathbb{C}^{d_2}.$

(Density operator). $\quad \rho_{AB} = \sigma_A \otimes \tau_B, \quad \sigma_A \in L(\mathbb{C}^{d_A})$ and $\tau_B \in L(\mathbb{C}^{d_B})$ are density operators.

[Diagram: Alice with her atom on the left, Bob with his atom on the right, no connection between them]

$$\rho_{AB} = \sigma_A \otimes \tau_B$$

*Product state*
Alice and Bob individually prepare their systems.

— A **separable state** has the form: $\quad \rho_{AB} = \sum_x p(x) \, \sigma_A^x \otimes \tau_B^x$

↳ Also called "classically correlated" $\qquad$ ↳ probabilities.

[Diagram: Alice with her atom on the left connected via classical communication lines (double arrows) to Bob with his atom on the right]

$$\rho_{AB} = \sum_{x \in \mathcal{X}} p(x)\, \sigma_A^x \otimes \tau_B^x$$

*Separable state*
Alice and Bob individually prepare their systems via local operations and classical communication.

## Page 8

⊛ **Example:** $\rho_{AB} = \frac{1}{2}\left(\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B + \ket{1}\bra{1}_A \otimes \ket{1}\bra{1}_B\right) = \frac{1}{2}\left(\ket{0,0}\bra{0,0}_{AB} + \ket{1,1}\bra{1,1}_{AB}\right)$

This state is <u>diagonal</u> in the tensor-product basis

$$\{\ket{0}_A \otimes \ket{0}_B,\ \ket{0}_A \otimes \ket{1}_B,\ \ket{1}_A \otimes \ket{0}_B,\ \ket{1}_A \otimes \ket{1}_B\}$$

$$\rho_{AB} = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

[column labels: 00, 01, 10, 11]

⊛ **If Alice and Bob both measure in the $\{\ket{0}, \ket{1}\}$ basis, then their outcomes will be correlated!**

- If Alice gets outcome "0", then so will Bob. Same with outcome "1".

$$\text{Tr}_A\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B)\rho_{AB}\right] = \frac{1}{2}\ket{0}\bra{0}_B \rightarrow \rho_B^{(0)} = \ket{0}\bra{0}_B.\ \text{Also,}\ \rho_B^{(1)} = \ket{1}\bra{1}.$$

$$= \text{Tr}_A\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B) \cdot \frac{1}{2}\left(\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B + \ket{1}\bra{1}_A \otimes \ket{1}\bra{1}_B\right)\right]$$

$$= \frac{1}{2}\left(\text{Tr}_A\left[\ket{0}\bra{0}\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B\right] + \text{Tr}_A\left[\underbrace{\ket{0}\bra{0}\ket{1}\bra{1}}_{=\,0}{}_A \otimes \ket{1}\bra{1}_B\right]\right)$$

$$= \frac{1}{2}\text{Tr}_A\left[\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B\right]$$

$$= \frac{1}{2}\ket{0}\bra{0}_B$$

## Page 9

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

## Page 10

- An <mark>entangled state</mark> is NOT a separable state.

[Diagram: Alice (left) and Bob (right) each holding a box containing an atom, connected by a wavy line representing entanglement]

$$\rho_{AB} \neq \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Entangled state*

Correlations between Alice and Bob are non-local.
State of the individual systems not sufficient to describe the pair.

$Z\ket{0} = \ket{0}$
$Z\ket{1} = -\ket{1}$

(b) <u>Examples</u>:

1. The <mark>Bell states</mark>

$$\ket{\Phi_{0,0}} = \ket{\Phi^+}, \quad (Z \otimes \mathbb{1})\ket{\Phi^+} = \tfrac{1}{\sqrt{2}}(Z\ket{0}\ket{0} + Z\ket{1}\ket{1})$$
$$= \tfrac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1}) \quad\quad = \tfrac{1}{\sqrt{2}}(\ket{0,0} - \ket{1,1})$$
$$= \ket{\Phi^-}$$

$$\Phi^{\pm} = \ket{\Phi^{\pm}}\bra{\Phi^{\pm}}, \quad \ket{\Phi^{\pm}} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1})$$

$$\Psi^{\pm} = \ket{\Psi^{\pm}}\bra{\Psi^{\pm}}, \quad \ket{\Psi^{\pm}} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0})$$

Observe that $\{\ket{\Phi^{\pm}}, \ket{\Psi^{\pm}}\} \longleftrightarrow \{\underbrace{(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}}_{\ket{\Phi_{z,x}}} : z, x \in \{0,1\}\}$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Z^0 = \mathbb{1},\ Z^1 = Z$$
$$X^0 = \mathbb{1},\ X^1 = X$$

$0,0 \leftrightarrow \Phi^+$
$0,1 \leftrightarrow \Psi^+$
$1,0 \leftrightarrow \Phi^-$
$1,1 \leftrightarrow \Psi^-$

→ <u>In $d$ dimensions</u>: $\ket{\Phi_d^+} := \tfrac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k,k} \quad (d=3) \ \tfrac{1}{\sqrt{3}}(\ket{0}\ket{0} + \ket{1}\ket{1} + \ket{2}\ket{2})$

(See later for the other $d$-dimensional Bell states.)

$$\ket{\Phi^+} = \begin{pmatrix} 00 \\ 01 \\ 10 \\ 11 \end{pmatrix}\!\!\begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Phi^-} = \begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ -\tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Psi^+} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}, \quad \ket{\Psi^-} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ -\tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$$

## Page 11

$$(X \otimes I)\ket{\Phi^+} = \frac{1}{\sqrt{2}}\left(\underbrace{X\ket{0}}_{\ket{1}}\ket{0} + \underbrace{X\ket{1}}_{\ket{0}}\ket{1}\right) = \frac{1}{\sqrt{2}}\left(\ket{1}\ket{0} + \ket{0}\ket{1}\right) = \ket{\Psi^+}$$

$$(ZX \otimes I)\ket{\Phi^+} = \frac{1}{\sqrt{2}}\left(ZX\ket{0}\ket{0} + ZX\ket{1}\ket{1}\right) = \frac{1}{\sqrt{2}}\left(-\ket{1}\ket{0} + \ket{0}\ket{1}\right) = \ket{\Psi^-}$$

$$\begin{aligned} Z\ket{1} &= -\ket{1} & Z\ket{0} &= \ket{0} \end{aligned}$$

## Page 12

✳️ $\ket{\psi_1} = \alpha_1 \ket{0} + \beta_1 \ket{1}, \quad \ket{\psi_2} = \alpha_2 \ket{0} + \beta_2 \ket{1}$

$\ket{\psi_1} \otimes \ket{\psi_2} = \alpha_1 \alpha_2 \ket{0,0} + \alpha_1 \beta_2 \ket{0,1} + \beta_1 \alpha_2 \ket{1,0} + \beta_1 \beta_2 \ket{1,1} \neq \tfrac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1})$

There does not exist values of $\alpha_1, \alpha_2, \beta_1, \beta_2$ such that $\ket{\psi_1} \otimes \ket{\psi_2} = \ket{\Phi^+}$.

---

✳️ $\{\ket{\Phi_{z,x}} : z, x \in \{0,1\}\}$ is an ONB for $\mathbb{C}^2 \otimes \mathbb{C}^2$

$$\underbrace{U \ket{z, x}}_{} = \ket{\Phi_{z,x}}$$

↳ $U$ is a **unitary matrix**: $U^\dagger U = \mathbb{1} = U U^\dagger \iff U^\dagger = U^{-1}$
   (change-of-basis matrix)

$\Rightarrow \{\ket{\Phi_{z,x}}\bra{\Phi_{z',x'}} : z, x, z', x' \in \{0,1\}\}$ is an ONB for $L(\mathbb{C}^2 \otimes \mathbb{C}^2)$

$\Rightarrow \rho_{AB} = \displaystyle\sum_{\substack{z,x \in \{0,1\} \\ z',x' \in \{0,1\}}} \underbrace{C_{z,x,z',x'}}_{\in \mathbb{C}} \, \ket{\Phi_{z,x}}\bra{\Phi_{z',x'}}_{AB}$

---

✳️ $\displaystyle\sum_{z,x \in \{0,1\}} \mathbb{P}^{z,x}_{AB} = \mathbb{1}_{AB} \longrightarrow$ Bell states form a **measurement** (POVM)

   ↳ Important ingredient in teleportation.


# Lectures__quantum-algorithms(I).pdf

## Page 1

# ① Recap: Swap test

- **Goal:** given two pure states given by $\ket{\psi}$ and $\ket{\phi}$, find out how close they are.

[Circuit diagram: top wire starts in $\ket{0}$, applies $H$, then control to SWAP gate, then $H$, then Pauli-Z measurement (denoted by $X$ box). Middle wire is $\ket{\psi}$ entering SWAP. Bottom wire is $\ket{\phi}$ entering SWAP. Annotation: "Pauli-Z measurement $\{\ket{0}\bra{0}, \ket{1}\bra{1}\}$".]

$$\Pr[0] = \tfrac{1}{2}\left(1 + |\braket{\psi|\phi}|^2\right)$$

$$\Pr[1] = \tfrac{1}{2}\left(1 - |\braket{\psi|\phi}|^2\right)$$

$H\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1}) = \ket{+}$

$H\ket{1} = \tfrac{1}{\sqrt{2}}(\ket{0}-\ket{1}) = \ket{-}$

$$\begin{aligned}
\ket{0}\ket{0} &\mapsto \ket{0}\ket{0} \\
\ket{0}\ket{1} &\mapsto \ket{1}\ket{0} \\
\ket{1}\ket{0} &\mapsto \ket{0}\ket{1} \\
\ket{1}\ket{1} &\mapsto \ket{1}\ket{1}
\end{aligned}$$

$\to$ This means that $\text{SWAP}(\ket{\psi}\ket{\phi}) = \ket{\phi}\ket{\psi}$

- The quantity $|\braket{\psi|\phi}|^2$ quantifies the closeness of $\ket{\psi}$ and $\ket{\phi}$ — it is called the **fidelity** of $\ket{\psi}$ and $\ket{\phi}$.

$$\{M_x\}_x,\quad M_x \geq 0,\quad \sum_x M_x = \mathbb{1}.$$

(★) Observe that $\{\ket{\phi}\bra{\phi},\ \mathbb{1} - \ket{\phi}\bra{\phi}\}$ is a measurement (POVM).

**Check:** $\braket{v|\phi}\braket{\phi|v} = |\braket{v|\phi}|^2 \geq 0$ ✓

Also, from the Cauchy–Schwarz inequality: $|\braket{v|\phi}|^2 \leq \braket{v|v} \cdot \underbrace{\braket{\phi|\phi}}_{=1}$

$\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad = \braket{v|v} = \||v\rangle\|^2$

Therefore, $\braket{v|(\mathbb{1} - \ket{\phi}\bra{\phi})|v} = \braket{v|v} - \underbrace{|\braket{v|\phi}|^2}_{\leq \braket{v|v}} \geq 0$ ✓

Finally, $\ket{\phi}\bra{\phi} + \mathbb{1} - \ket{\phi}\bra{\phi} = \mathbb{1}$ ✓

So $\{\ket{\phi}\bra{\phi},\ \mathbb{1} - \ket{\phi}\bra{\phi}\}$ satisfies the definition of a quantum measurement (POVM).

## Page 2

(\*) $\{\ket{\phi}\bra{\phi}, \mathbb{1}-\ket{\phi}\bra{\phi}\}$ is a measurement that tells us whether or not a given state is equal to $\ket{\phi}\bra{\phi}$.

It has two outcomes (b/c the set has two operators).

- $\ket{\phi}\bra{\phi} \equiv$ "yes, the state is $\ket{\phi}\bra{\phi}$"
- $\mathbb{1} - \ket{\phi}\bra{\phi} \equiv$ "no, the state is not $\ket{\phi}\bra{\phi}$".

(\*) For a given state $\rho$, $\Pr[\phi] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\rho\right]$  $\quad$ <span style="color:blue">Born Rule: $\{M_x\}$ POVM<br>State $\rho \to \Pr(x) = \text{Tr}(M_x \rho)$.</span>

$$\Pr[\text{not } \phi] = \text{Tr}\!\left[(\mathbb{1} - \ket{\phi}\bra{\phi})\rho\right] = \text{Tr}(\rho) - \text{Tr}\!\left[\ket{\phi}\bra{\phi}\rho\right] = 1 - \Pr[\phi].$$

- If $\rho = \ket{\phi}\bra{\phi}$ itself, then $\Pr[\phi] = \text{Tr}\!\left[\underbrace{\ket{\phi}\braket{\phi|\phi}\bra{\phi}}_{=1}\right] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\right] = \braket{\phi|\phi} = 1.$ ✓

  $\Pr[\text{not } \phi] = 1 - \Pr[\phi] = 0$

- If $\rho = \ket{\gamma}\bra{\gamma}$, then $\Pr[\phi] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\ket{\gamma}\bra{\gamma}\right] = |\braket{\phi|\gamma}|^2 \to$ fidelity!

(\*) So the swap test allows us to do the measurement $\{\ket{\phi}\bra{\phi}, \mathbb{1} - \ket{\phi}\bra{\phi}\}$ and estimate the fidelity — without even knowing what $\ket{\phi}$ is!

## ② <u>Statistical Estimation from a Quantum Computer.</u>

- When we run a quantum algorithm and do the measurement at the end, the outcomes will generally be probabilistic.

- To extract the relevant information, we have to run the algorithm many times.

## Page 3

(a) From the swap test, we know that $\Pr(0) = \frac{1}{2}(1+\alpha)$, $\quad \alpha = |\braket{\psi|\phi}|^2$.

$$\Pr(1) = \frac{1}{2}(1-\alpha)$$

Running this many times will give us a bunch of "0"s and "1"s.

How do we use the "0"s and "1"s to estimate $\alpha$?

(b) <u>Procedure</u>: For $i = 1, 2, \ldots, N$ ($N \equiv$ number of samples)

- Each time we get outcome "0" $\to$ record $x_i = 1$
- Each time we get outcome "1" $\to$ record $x_i = -1$

$\circledast$ This defines a <u>random variable</u> $X$:

$$\Pr[X = \pm 1] = \frac{1}{2}(1 \pm \alpha)$$

- Do this $N$ times, then take the <u>sample mean/average</u>: $\hat{x}_N = \frac{1}{N} \sum_{i=1}^{N} x_i$

This defines a random variable $\hat{X}_N = \frac{1}{N}\sum_{i=1}^{N} X_i$. $\hat{X}_N$ is an <u>unbiased estimator</u> of $X$:

$$\mathbb{E}[\hat{X}_N] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X_i] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X] = \mathbb{E}[X].$$

$\quad = \mathbb{E}[X]\ \forall i$, b/c all samples are independent and identical.

$$\mathbb{E}[X] = (+1)\cdot \Pr[X = +1] + (-1)\cdot \Pr[X = -1] = \frac{1}{2}(1+\alpha) - \frac{1}{2}(1-\alpha) = \alpha.$$

- As $N \to \infty$, $\hat{X}_N \to \mathbb{E}[X] = |\braket{\psi|\phi}|^2$ (<u>law of large numbers</u>).

$\circledast$ So the sample average approaches the true (unknown) value of $\alpha$!

## Page 4

③ <u>Hadamard Test</u>: Estimating $\braket{\psi|U|\psi}$, where $U$ is a unitary and $\ket{\psi}$ is a state vector.

[Circuit diagram: top wire $\ket{0}$ — H — •(control) — H — measurement (Pauli-Z); bottom wire $\ket{\psi}$ — U(target) —. The measurement is annotated "Pauli-Z measurement".]

$\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$

$$\ket{\psi_{init}} = \ket{0}\ket{\psi} \mapsto \ket{+}\ket{\psi} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{\psi} + \ket{1}\ket{\psi}\big) \mapsto \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{\psi} + \ket{1}U\ket{\psi}\big)$$

$$\mapsto \tfrac{1}{2}\big(\ket{+}\ket{\psi} + \ket{-}U\ket{\psi}\big) = \tfrac{1}{\sqrt{2}}\Big(\ket{0}\tfrac{1}{\sqrt{2}}(\ket{\psi}+U\ket{\psi}) + \ket{1}\tfrac{1}{\sqrt{2}}(\ket{\psi} - U\ket{\psi})\Big) = \ket{\psi_{final}}$$

$$\Pr[0] = \mathrm{Tr}\Big[\big(\ket{0}\bra{0} \otimes \mathbb{1}\big)\ket{\psi_{final}}\bra{\psi_{final}}\Big] \qquad \tfrac{1}{2}(\ket{\psi}+U\ket{\psi})^{\dagger} = \tfrac{1}{2}(\bra{\psi} + \bra{\psi}U^{\dagger})$$

$$= \tfrac{1}{4}\Big(\big(\bra{\psi} + \bra{\psi}U^{\dagger}\big)\big(\ket{\psi} + U\ket{\psi}\big)\Big)$$

$$= \tfrac{1}{4}\Big(\underbrace{\braket{\psi|\psi}}_{=\braket{\psi|\psi}=1} + \braket{\psi|U|\psi} + \underbrace{\braket{\psi|U^{\dagger}|\psi}}_{= \overline{\braket{\psi|U|\psi}}} + \underbrace{\braket{\psi|U^{\dagger}U|\psi}}_{=\mathbb{1}}\Big) \qquad \begin{matrix} z = x+yi \\ \bar{z} = x-yi \end{matrix} \Bigg\} \to z + \bar z = 2x$$

$$\hspace{8cm} x = \mathrm{Re}(z).$$

$$= \tfrac{1}{2}\Big(1 + \mathrm{Re}\big(\braket{\psi|U|\psi}\big)\Big)$$
$$\hspace{2cm}\underbrace{\phantom{\mathrm{Re}\braket{\psi|U|\psi}}}_{\alpha}$$

$$\Pr[1] = \tfrac{1}{2}\Big(1 - \underbrace{\mathrm{Re}\big(\braket{\psi|U|\psi}\big)}_{\alpha}\Big)$$

$\to$ Then same procedure as above to estimate $\alpha$!
$\Pr[0] = \tfrac{1}{2}(1+\alpha), \quad \Pr[1] = \tfrac{1}{2}(1-\alpha).$

✱ For the imaginary part → include the S gate!

[Circuit diagram: top wire $\ket{0}$ — H — S† — •(control) — H — measurement (Pauli-Z); bottom wire $\ket{\psi}$ — U(target) —.]

$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \implies S^{\dagger} = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$$

$S^{\dagger}\ket{0} = \ket{0}$
$S^{\dagger}\ket{1} = -i\ket{1}$

$$\ket{0}\ket{\psi} \mapsto \ket{+}\ket{\psi} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{\psi} + \ket{1}\ket{\psi}\big) \mapsto \tfrac{1}{\sqrt{2}}\big(\underbrace{\ket{0}}_{S^{\dagger}\ket{0}}\ket{\psi} - i\underbrace{\ket{1}}_{S^{\dagger}\ket{1}}\ket{\psi}\big)$$

$$\mapsto \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{\psi} - i\ket{1}U\ket{\psi}\big) \mapsto \tfrac{1}{\sqrt{2}}\big(\ket{+}\ket{\psi} - i\ket{-}U\ket{\psi}\big)$$

[curly brace gathering the final lines]

## Page 5

$$= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{\psi} - i\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})U\ket{\psi}\right)$$

$$= \frac{1}{2}\left(\ket{0}\ket{\psi} + \ket{1}\ket{\psi} - i\ket{0}U\ket{\psi} + i\ket{1}U\ket{\psi}\right)$$

$$= \frac{1}{2}\left(\ket{0}(\ket{\psi}-iU\ket{\psi}) + \ket{1}(\ket{\psi}+iU\ket{\psi})\right) \longrightarrow (\ket{\psi}-iU\ket{\psi})^\dagger = \bra{\psi} + i\bra{\psi}U^\dagger$$

$$\Rightarrow \Pr[0] = \frac{1}{4}\left(\bra{\psi}+i\bra{\psi}U^\dagger\right)\left(\ket{\psi}-iU\ket{\psi}\right) = \frac{1}{4}\Big(\underbrace{\braket{\psi|\psi}}_{=1} - i\braket{\psi|U|\psi} + i\braket{\psi|U^\dagger|\psi}$$

$$+ \underbrace{\braket{\psi|U^\dagger U|\psi}}_{\substack{=\mathbb{1}\\=1}}\Big)$$

$$= \frac{1}{4}\Big(1 - i\underbrace{\braket{\psi|U|\psi}}_{z} + i\underbrace{\overline{\braket{\psi|U|\psi}}}_{\bar z} + 1\Big) \qquad \left(z - \bar z = x+iy - x+iy = 2iy\right)$$

$$= \frac{1}{4}\left(2 - i\underbrace{\left(\braket{\psi|U|\psi} - \overline{\braket{\psi|U|\psi}}\right)}_{= 2i\,\mathrm{Im}(\braket{\psi|U|\psi})}\right)$$

$$= \frac{1}{2}\Big(1 + \underbrace{\mathrm{Im}(\braket{\psi|U|\psi})}_{\alpha}\Big)$$

$$\Pr[1] = \frac{1}{2}\Big(1 - \underbrace{\mathrm{Im}(\braket{\psi|U|\psi})}_{\alpha}\Big)$$

$\rightarrow$ Then same procedure as above to estimate $\alpha$!
$$\Pr[0] = \tfrac{1}{2}(1+\alpha), \quad \Pr[1] = \tfrac{1}{2}(1-\alpha).$$


# Lectures__quantum-algorithms(II).pdf

## Page 1

① <u>Recap</u>: Quantum Circuits

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left. 

1st layer: $U_1$ acts on qubits 1,2; $U_2$ acts on qubits 3,4; $U_3$ acts on qubits 5,6.
2nd layer: $U_4$ acts on qubits 2,3; $U_5$ acts on qubits 4,5.
3rd layer: $U_6$ on qubits 1,2; $U_7$ on qubits 3,4; $U_8$ on qubits 5,6.

Each output line ends with a measurement (D) producing $x_1', x_2', x_3', x_4', x_5', x_6'$.]

$(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

1st layer | 2nd layer | 3rd layer  →  time

(✱) The circuit elements/gates are <u>unitaries</u>.
$$\left( U : U^\dagger U = U U^\dagger = \mathbb{1} \right)$$

Measurement / read-out:
$$\{\ket{0}\bra{0}, \ket{1}\bra{1}\} \rightarrow \begin{array}{l} \text{Pauli-}Z \\ \text{Computational} \\ \text{Basis.} \end{array}$$

---

(a) <u>Pauli gates</u>:

$-\boxed{X}- \quad \rightarrow \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \left( X\ket{0} = \ket{1},\ X\ket{1} = \ket{0} \right)$

$-\boxed{Y}- \quad \rightarrow \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \left( Y\ket{0} = i\ket{1},\ Y\ket{1} = -i\ket{0} \right)$

$-\boxed{Z}- \quad \rightarrow \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \quad \left( Z\ket{0} = \ket{0},\ Z\ket{1} = -\ket{1} \right)$

(b) <u>Hadamard gate</u>:

$-\boxed{H}- \quad \rightarrow \quad H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

$$H\ket{0} = \ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0} + \ket{1})$$
$$H\ket{1} = \ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0} - \ket{1}).$$

## Page 2

(c) <u>Phase gate</u>: $\;-\boxed{S}-\;\longrightarrow\; S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}\quad\begin{array}{l} S\ket{0} = \ket{0} \\ S\ket{1} = i\ket{1}\end{array}$

$$\ket{0} = \begin{pmatrix}1\\0\end{pmatrix},\;\ket{1}=\begin{pmatrix}0\\1\end{pmatrix}$$

$$S\ket{0} = \begin{pmatrix}1 & 0 \\ 0 & i\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}1\\0\end{pmatrix} = \ket{0}$$

(d) <u>T-gate</u>: $\;-\boxed{T}-\;\longrightarrow\; T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4}\end{pmatrix}$

(e) <u>CNOT / CX gate</u>:    "controlled-X"

[Circuit diagram: top wire is control (•), bottom wire is target with X box; or equivalent diagram with ⊕ symbol on target]

$\circledast\;\;\ket{a,b}\mapsto \ket{a,\,a\oplus b}$

$$\text{CNOT} = \begin{array}{c c} & \begin{array}{cccc} 00 & 01 & 10 & 11 \end{array} \\ \begin{array}{c} 00 \\ 01 \\ 10 \\ 11 \end{array} & \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \end{array}$$

$$\begin{aligned} \ket{0}\ket{0} &\mapsto \ket{0}\ket{0} \\ \ket{0}\ket{1} &\mapsto \ket{0}\ket{1} \\ \ket{1}\ket{0} &\mapsto \ket{1}\,X\ket{0} = \ket{1}\ket{1} \\ \ket{1}\ket{1} &\mapsto \ket{1}\,X\ket{1} = \ket{1}\ket{0} \end{aligned}$$

B/c of linearity, this determines the action on <u>any</u> state!

$$\ket{\gamma} = a\ket{0,0} + b\ket{0,1} + c\ket{1,0} + d\ket{1,1} \;\mapsto\; a\ket{0,0} + b\ket{0,1} + c\ket{1,1} + d\ket{1,0}$$

(f) <u>Controlled Unitary</u>

[Circuit diagram: top wire control (•), bottom wire with U box]

$$\begin{aligned} \ket{0}\ket{0} &\mapsto \ket{0}\ket{0} \\ \ket{0}\ket{1} &\mapsto \ket{0}\ket{1} \\ \ket{1}\ket{0} &\mapsto \ket{1}\,U\ket{0} \\ \ket{1}\ket{1} &\mapsto \ket{1}\,U\ket{1} \end{aligned}$$

$$cU = \begin{pmatrix} \mathbb{1} & 0 \\ 0 & U \end{pmatrix} = \ket{0}\bra{0}\otimes \mathbb{1} + \ket{1}\bra{1}\otimes U.$$

## Page 3

- **Example: Teleportation**

[Diagram: Alice (top) holds $\ket{\psi}_{A'}$ and one half of $\ket{\Phi^+}_{AB}$. She performs a Bell measurement, obtaining classical bits $z, x$ which are sent to Bob. Bob applies $X^x$ then $Z^z$ to his half of the entangled pair, recovering $\ket{\psi}_B$.]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}.$

(✱) **If Alice and Bob are not spatially separated, then the algorithm can be modified as follows:**

[Circuit diagram: Three wires labeled $\ket{\psi}_{A'}$, $\ket{0}_A$, $\ket{0}_B$. The red box on left contains: $H$ on $\ket{0}_A$, then CNOT from $A$ (control) to $B$ (target) — this prepares $\ket{\Phi^+}_{AB}$. Then CNOT with $A'$ as control and $A$ as target, $H$ on $A'$. Blue box on right: CNOT from $A$ to $B$ ($X$ correction), then controlled-$Z$ from $A'$ to $B$, output $\ket{\psi}_B$.]

$\ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0} + \ket{1})$

$$\ket{0}_A\ket{0}_B \mapsto \ket{+}_A\ket{0}_B = \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{0}_B) \mapsto \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B) = \ket{\Phi^+}$$

$$\ket{\psi}_{A'}\ket{0}_A\ket{0}_B \mapsto \ket{\psi}_{A'} \otimes \ket{\Phi^+}_{AB} = \tfrac{1}{\sqrt{2}}\big(\ket{\psi}_{A'}\ket{0}_A\ket{0}_B + \ket{\psi}_{A'}\ket{1}_A\ket{1}_B\big)$$

$\ket{\psi}_{A'} = \alpha\ket{0} + \beta\ket{1}$

$$= \tfrac{1}{\sqrt{2}}\big(\alpha\ket{0}_{A'}\ket{0}_A\ket{0}_B + \beta\ket{1}_{A'}\ket{0}_A\ket{0}_B$$
$$+ \alpha\ket{0}_{A'}\ket{1}_A\ket{1}_B + \beta\ket{1}_{A'}\ket{1}_A\ket{1}_B\big).$$

$$\xmapsto{\text{CNOT}_{A'A}} \tfrac{1}{\sqrt{2}}\big(\alpha\ket{0}_{A'}\ket{0}_A\ket{0}_B + \beta\ket{1}_{A'}\ket{1}_A\ket{0}_B$$
$$+ \alpha\ket{0}_{A'}\ket{1}_A\ket{1}_B + \beta\ket{1}_{A'}\ket{0}_A\ket{1}_B\big).$$

## Page 4

$\downarrow$

$\xmapsto{H_{A'}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{0}_B - \beta \ket{1}_{A'} \ket{1}_A \ket{0}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{1}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big).$

$\xmapsto{\text{CNOT}_{AB}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{0}_B \qquad {\color{blue} Z\ket{1} = -\ket{1}}$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big). \qquad {\color{blue} Z\ket{0} = \ket{0}}$

$\xmapsto{CZ_{A'B}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{1}_B + \beta \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B + \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big).$

$= \frac{1}{2} \Big( \ket{0}_{A'} \ket{0}_A \underbrace{\big( \alpha \ket{0}_B + \beta \ket{1}_B \big)}_{\color{blue}\ket{\psi}}$
$\qquad + \ket{0}_{A'} \ket{1}_A \underbrace{\big( \alpha \ket{0}_B + \beta \ket{1}_B \big)}_{\to \ket{\psi}}$
$\qquad + \ket{1}_{A'} \ket{0}_A \big( \alpha \ket{0}_B + \beta \ket{1}_B \big)$
$\qquad + \ket{1}_{A'} \ket{1}_A \big( \alpha \ket{0}_B + \beta \ket{1}_B \big) \Big)$

$= \frac{1}{2} \big( \ket{0}_{A'} \ket{0}_A + \ket{0}_{A'} \ket{1}_A + \ket{1}_{A'} \ket{0}_A + \ket{1}_{A'} \ket{1}_A \big) \ket{\psi}_B$

$\underline{\underline{= \ket{+}_{A'} \ket{+}_A \ket{\psi}_B}}$

## Page 5

- **Example**: Superdense coding: using entanglement + 1 qubit to transmit 2 classical bits.

[Diagram: Alice and Bob share entangled state $\ket{\Phi^+}_{AB}$. Alice applies $X^x$ then $Z^z$ on her qubit (boxed: "Encoding bits z, x into one qubit."), then sends to Bob who performs a Bell measurement to recover $(x,z)$.]

② **The Swap test**

✻ How do we estimate the inner product of two (unknown) states on a quantum computer?

- **The swap gate**:

[Circuit: $\ket{\psi}$ and $\ket{\phi}$ enter a SWAP box; outputs are $\ket{\phi}$ and $\ket{\psi}$.]

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{1}\ket{0}$$
$$\ket{1}\ket{0} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}\ket{1}$$

As a matrix:

$$\begin{array}{c|cccc} & 00 & 01 & 10 & 11 \\ \hline 00 & 1 & 0 & 0 & 0 \\ 01 & 0 & 0 & 1 & 0 \\ 10 & 0 & 1 & 0 & 0 \\ 11 & 0 & 0 & 0 & 1 \end{array}$$

- **Circuit for the SWAP test**

[Circuit: top wire $\ket{0} - H - \bullet - H - X -$ (measurement); middle wire $\ket{\psi}$ and bottom wire $\ket{\phi}$ enter a SWAP gate controlled by the top qubit.]

## Page 6

$$\ket{\psi_{\text{init}}} = \ket{0}\ket{\psi}\ket{\phi} \xmapsto{H} \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{\psi}\ket{\phi} + \ket{1}\ket{\psi}\ket{\phi}\right)$$

$H\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$

$$\xmapsto{\text{CSWAP}} \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{\psi}\ket{\phi} + \ket{1}\ket{\phi}\ket{\psi}\right)$$

$$\xmapsto{H} \tfrac{1}{2}\left(\ket{+}\ket{\psi}\ket{\phi} + \ket{-}\ket{\phi}\ket{\psi}\right) \qquad \ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\pm\ket{1})$$

$\{\ket{0}\bra{0}, \ket{1}\bra{1}\}.$

$$\ket{\psi_{\text{final}}} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\tfrac{1}{\sqrt{2}}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}) + \ket{1}\tfrac{1}{\sqrt{2}}(\ket{\psi}\ket{\phi}-\ket{\phi}\ket{\psi})\right)$$

$$= \tfrac{1}{2}\ket{0}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}) + \tfrac{1}{2}\ket{1}(\ket{\psi}\ket{\phi}-\ket{\phi}\ket{\psi})$$

Now measure — what is the probability of getting zero? (Recall partial measurements).

$\Pr[0] = \mathrm{Tr}\left[(\ket{0}\bra{0}\otimes \mathbb{1}\otimes \mathbb{1})\ket{\psi_{\text{final}}}\bra{\psi_{\text{final}}}\right].$

$\underbrace{\phantom{xxxxxxxxxx}}_{= \tfrac{1}{2}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi})}$

$$= \tfrac{1}{4}\mathrm{Tr}\left[\underbrace{(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi})(\bra{\psi}\bra{\phi}+\bra{\phi}\bra{\psi})}_{\ket{v}}\right] \qquad \mathrm{Tr}[\ket{v}\bra{v}] = \braket{v|v}$$

$$= \tfrac{1}{4}\left(\bra{\psi}\bra{\phi}+\bra{\phi}\bra{\psi}\right)\left(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}\right)$$

$$= \tfrac{1}{4}\Big(\underbrace{\braket{\psi|\psi}\braket{\phi|\phi}}_{=1} + \underbrace{\braket{\psi|\phi}\braket{\phi|\psi}}_{=|\braket{\psi|\phi}|^2} + \braket{\phi|\psi}\braket{\psi|\phi} + \underbrace{\braket{\phi|\phi}\braket{\psi|\psi}}_{=1}\Big)$$

$$\boxed{\Pr[0] = \tfrac{1}{2}\left(1 + |\braket{\psi|\phi}|^2\right)}$$

$$\Pr[1] = \tfrac{1}{2}\left(1 - |\braket{\psi|\phi}|^2\right)$$

❋ The probabilities contain the inner product!
   So how do we extract the value of the inner product?
   <u>We run the algorithm many times!</u>

- Each time we get outcome "0" → record $x_i = 1$  ⎫  ❋ This defines a <u>random</u>
- Each time we get outcome "1" → record $x_i = -1$ ⎭     <u>variable</u> $X$:
- Do this $N$ times, then take the <u>sample</u>
  <u>mean / average</u>: $\hat{x}_N = \tfrac{1}{N}\sum_{i=1}^{N} x_i$

$\Pr[X = \pm 1] = \tfrac{1}{2}\left(1 \pm |\braket{\psi|\phi}|^2\right).$

## Page 7

This defines a random variable $\hat{X}_N = \frac{1}{N}\sum_{i=1}^{N} X_i$. $\hat{X}_N$ is an <u>unbiased estimator</u> of $X$:

$$\mathbb{E}[\hat{X}_N] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X_i] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X] = \mathbb{E}[X].$$

$\qquad\qquad\quad = \mathbb{E}[X] \;\forall i$, b/c all samples are independent and identical.

$$\mathbb{E}[X] = \sum_x x\, \Pr[X=x]$$

$$\mathbb{E}[X] = (+1)\cdot \Pr[X=+1] + (-1)\cdot \Pr[X=-1] = \tfrac{1}{2}\left(1 + |\braket{\gamma|\phi}|^2\right) - \tfrac{1}{2}\left(1 - |\braket{\gamma|\phi}|^2\right) = |\braket{\gamma|\phi}|^2$$

- As $N \to \infty$, $\hat{X}_N \to \mathbb{E}[X] = |\braket{\gamma|\phi}|^2$  (<u>law of large numbers</u>).

⊛ So the sample average approaches the true (unknown) inner product!

```python
[89]: import numpy as np
      import matplotlib.pyplot as plt

      inner_product=0.8
      # Parameters
      p = (1/2)*(1-inner_product)        # probability of original "1"
      n_samples = 20000

      # Step 1: sample Bernoulli (0 or 1)
      samples = np.random.binomial(1, p, size=n_samples)

      # Step 2: map to +1 / -1
      mapped = 1 - 2 * samples   # 0 -> 1, 1 -> -1

      # Step 3: running average
      running_avg = np.cumsum(mapped) / np.arange(1, n_samples + 1)

      # True mean of the new variable
      true_mean = 1 - 2*p

      # Plot
      plt.figure()
      plt.plot(running_avg)#, label="Running average")
      plt.axhline(true_mean, linestyle='--', label="True inner product")

      plt.xlabel("Number of samples")
      plt.ylabel("Sample average")
      plt.title("Inner product estimation (swap test)")
      plt.legend()
      plt.show()
```

[Plot titled "Inner product estimation (swap test)". X-axis: "Number of samples" from 0 to 20000. Y-axis: "Sample average" from 0.60 to 1.00. A blue curve representing the running sample average starts with high variance near the origin (oscillating between ~0.60 and ~1.00) and quickly converges to ~0.80. A dashed horizontal line at 0.80 labeled "True inner product".]


# Lectures__quantum-algorithms(III).pdf

## Page 1

① <u>Recap: Hadamard Test.</u>

Estimating $\bra{\psi}U\ket{\psi}$, where $U$ is a unitary and $\ket{\psi}$ is a state vector.

[Circuit diagram: top wire $\ket{0}$ — H — •  — H — $\pi$ (Pauli-Z measurement); bottom wire $\ket{\psi}$ — U (controlled by top wire) — ]

$$\Pr[0] = \tfrac{1}{2}\bigl(1 + \mathrm{Re}(\bra{\psi}U\ket{\psi})\bigr), \quad \Pr[1] = \tfrac{1}{2}\bigl(1 - \mathrm{Re}(\bra{\psi}U\ket{\psi})\bigr).$$

$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \;\Rightarrow\; S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$$

For the imaginary part:

[Circuit diagram: top wire $\ket{0}$ — H — $S^\dagger$ — • — H — $\pi$ ; bottom wire $\ket{\psi}$ — U (controlled) — ]

$$\Pr[0] = \tfrac{1}{2}\bigl(1 + \mathrm{Im}(\bra{\psi}U\ket{\psi})\bigr)$$

$$\Pr[1] = \tfrac{1}{2}\bigl(1 - \mathrm{Im}(\bra{\psi}U\ket{\psi})\bigr).$$

✱ In both cases, we have $\Pr[0] = \tfrac{1}{2}(1+\alpha)$, $\Pr[1] = \tfrac{1}{2}(1-\alpha)$, where $\alpha$ is unknown. To <u>estimate</u> $\alpha$, we do the following <u>procedure</u>:

For $i = 1, 2, \ldots, N$ ($N \equiv \#$ of samples / # of times we run the quantum circuit).

- Each time we get outcome "0" → record $x_i = 1$
- Each time we get outcome "1" → record $x_i = -1$

✱ This defines a random <u>variable</u> $X$:

$$\Pr[X = \pm 1] = \tfrac{1}{2}(1 \pm \alpha)$$

- Do this $N$ times, then take the <u>sample mean/average</u>: $\hat{X}_N = \tfrac{1}{N} \sum_{i=1}^{N} x_i$ ← sample mean

This defines a random variable $\hat{X}_N = \tfrac{1}{N}\sum_{i=1}^{N} X_i$. $\hat{X}_N$ is an <u>unbiased estimator</u> of $X$:

$$\mathbb{E}[\hat{X}_N] = \tfrac{1}{N}\sum_{i=1}^{N}\mathbb{E}[X_i] = \tfrac{1}{N}\sum_{i=1}^{N}\mathbb{E}[X] = \mathbb{E}[X].$$

↑ True mean

$\mathbb{E}[X_i] = \mathbb{E}[X]\;\forall i$, b/c all samples are independent and identical.

## Page 2

$$\mathbb{E}[X] = (+1) \cdot \Pr[X=+1] + (-1) \cdot \Pr[X=-1] = \tfrac{1}{2}(1+\alpha) - \tfrac{1}{2}(1-\alpha) = \alpha.$$

- As $N \to \infty$, $\hat{X}_N \to \mathbb{E}[X] = \alpha$  $\quad$ (law of large numbers).

✱ So the sample average approaches the true (unknown) value of $\alpha$!

② <u>Motivation: Expectation values</u>

- Why do we care about quantities of the form $\braket{\psi|U|\psi}$?

  B/c they can be used to compute <u>expectation values</u> of <u>observables</u>.

- <u>Observable</u>: Any Hermitian operator ( <u>recall</u>: $M$ Hermitian $\iff M^\dagger = M$ )

  ✱ <u>Fact from linear algebra</u>: Every Hermitian operator can be <u>diagonalized</u>.

  $$M = \sum_{i=1}^{d} \lambda_i \ket{v_i}\bra{v_i}, \quad \text{where:} \quad \lambda_i : \text{eigenvalues (real numbers)}. \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
  $$\boxed{\sum_{i=1}^{d} \ket{v_i}\bra{v_i} = \mathbb{1}} \qquad \ket{v_i}: \text{orthonormal eigenvectors.} \quad = \ket{0}\bra{0} - \ket{1}\bra{1}$$

  ✱ <u>Axiom of quantum mechanics</u>: every physical quantity corresponds to a Hermitian operator. (e.g., position, momentum, energy...).

  The eigenvalues are the possible values of the quantity.

  We get the value of the quantity through measurement.

- For an observable / Hermitian operator $M$, the corresponding measurement is given by the eigenvectors. ($\{\ket{v_i}\bra{v_i}\}$ is the POVM.)

- For a state $\rho$, the probability that it has value $\lambda_i$ is

## Page 3

$$\Pr[i] = \text{Tr}\left[\ket{v_i}\bra{v_i}\rho\right] \quad \text{(Born rule)} \quad = \bra{v_i}\rho\ket{v_i}$$

The <u>expected value</u> of the observable is:

$$\langle M \rangle_\rho = \sum_{i=1}^{\hat{n}} \lambda_i \Pr[i] = \sum_{i=1}^{\hat{n}} \lambda_i \text{Tr}\left[\ket{v_i}\bra{v_i}\rho\right] = \text{Tr}\left[\underbrace{\left(\sum_{i=1}^{\hat{n}} \lambda_i \ket{v_i}\bra{v_i}\right)}_{M}\rho\right] = \text{Tr}[M\rho].$$

[Red annotation pointing to the "=" sign: "Definition of expectation value!"]

- If we don't know the eigenvectors (b/c they are hard to get for large matrices!), but we know that $M$ can be written as

$$M = \sum_{j=1}^{k} c_j \underbrace{U_j}_{\text{unitaries}}, \quad \text{then} \quad \langle M \rangle_\gamma = \text{Tr}(M\ket{\gamma}\bra{\gamma})$$

$$= \sum_{j=1}^{k} c_j \text{Tr}(U_j \ket{\gamma}\bra{\gamma})$$

$$= \sum_{j=1}^{k} c_j \underbrace{\bra{\gamma}U_j\ket{\gamma}}_{\text{Estimate using Hadamard test!}}$$

So we estimate each term individually using the Hadamard test and then add to get an overall estimate of the expectation value.

## Page 4

## ③ Quantum Fourier Transform

(a) <u>Recap</u>: discrete Fourier transform (DFT).

- Used in a lot of places!
    - Signal processing — identifying frequency components of a signal. (audio and video processing)
    - Machine learning — feature extraction
    - Scientific Computing — solving differential equations numerically.

- <u>Definition</u>: for a signal $\{x_k\}_{k=0}^{N-1}$, its DFT is

$$y_k = \frac{1}{\sqrt{N}} \sum_{k'=0}^{N-1} x_{k'}\, e^{\frac{2\pi i k' k}{N}} \qquad \left( e^{2\pi i x} = \cos(2\pi x) + i\sin(2\pi x) \right)$$

- <u>Example</u>: consider a signal of two sine waves put together:

$$x(t) = \sin(2\pi f_1 t) + \tfrac{1}{2}\sin(2\pi f_2 t)$$

with $f_1, f_2$ marked as <span style="color:purple">frequencies</span>.

- $f_1 = 5$ Hz
- $f_2 = 15$ Hz
- Sampling rate: $f_s = 100$ Hz $\Rightarrow$ 100 samples total (in 1 sec.)

[Three plots side by side:
1. "Time-Domain Signal" — continuous oscillating waveform, amplitude between -1 and 1, time 0 to 1 s.
2. "Time-Domain Signal (sampled)" — same waveform shown as discrete sample points connected by lines.
3. "Frequency-Domain Spectrum ($|y_k|$)" — magnitude vs frequency [Hz], with a tall spike of magnitude 1.0 at 5 Hz and a smaller spike of magnitude 0.5 at 15 Hz.]

## Page 5

(b) <u>The Quantum Version!</u>   (Quantum Fourier Transform $\equiv$ QFT).

- $Y_k = \frac{1}{\sqrt{N}} \sum_{k'=0}^{N-1} x_{k'} \, e^{\frac{2\pi i k' k}{N}} \quad \longrightarrow \quad Q\ket{k} = \frac{1}{\sqrt{d}} \sum_{k'=0}^{d-1} e^{\frac{2\pi i k k'}{d}} \ket{k'}$   (action on basis vectors).

$$\underbrace{\phantom{Q\ket{k}}}_{\text{QFT matrix}}$$

$\ket{x} = \sum_{k=0}^{d-1} x_k \ket{k} \quad \Longrightarrow \quad Q\ket{x} = \sum_{k=0}^{d-1} x_k \, Q\ket{k} = \sum_{k=0}^{d-1} x_k \, \frac{1}{\sqrt{d}} \sum_{k'=0}^{d-1} e^{\frac{2\pi i k k'}{d}} \ket{k'}$

$$= \sum_{k'=0}^{d-1} \underbrace{\left( \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} x_k \, e^{\frac{2\pi i k k'}{d}} \right)}_{\equiv\, Y_{k'}} \ket{k'} = \ket{\tilde{x}}$$

- The QFT matrix is unitary! Let $\omega = e^{\frac{2\pi i}{d}}, \quad \overline{\omega} = e^{-\frac{2\pi i}{d}} = \omega^{-1}$  $\quad d = 2^n$

$$\cos\!\left(\tfrac{2\pi}{d}\right) + i\sin\!\left(\tfrac{2\pi}{d}\right)$$

$$Q = \frac{1}{\sqrt{d}} \sum_{k,k'=0}^{d-1} \omega^{k k'} \ket{k}\bra{k'}$$

$\omega = e^{\frac{2\pi i}{d}} = \cos\!\left(\tfrac{2\pi}{d}\right) + i\sin\!\left(\tfrac{2\pi}{d}\right)$

$\overline{\omega} = \cos\!\left(\tfrac{2\pi}{d}\right) - i\sin\!\left(\tfrac{2\pi}{d}\right)$

$\quad = e^{-\frac{2\pi i}{d}}$

$\quad = \omega^{-1}$

$$Q Q^\dagger = \left( \frac{1}{\sqrt{d}} \sum_{k,k'=0}^{d-1} \omega^{k k'} \ket{k}\bra{k'} \right) \left( \frac{1}{\sqrt{d}} \sum_{j,j'=0}^{d-1} \omega^{-j j'} \ket{j'}\bra{j} \right)$$

$$= \frac{1}{d} \sum_{k,k'=0}^{d-1} \sum_{j,j'=0}^{d-1} \omega^{k k'} \, \omega^{-j j'} \ket{k} \underbrace{\braket{k'|j'}}_{=\,\delta_{j',k'}} \bra{j}$$

$$= \frac{1}{d} \sum_{k,k'=0}^{d-1} \sum_{j=0}^{d-1} \omega^{k k'} \, \omega^{-j k'} \ket{k}\bra{j}$$

$$= \sum_{k,j=0}^{d-1} \underbrace{\left( \frac{1}{d} \sum_{k'=0}^{d-1} \omega^{k'(k-j)} \right)}_{\phantom{xxx}} \ket{k}\bra{j}$$

## Page 6

$$\downarrow \quad \rightarrow \delta_{j,k}$$

$$= \frac{1}{d}\sum_{k'=0}^{d-1} e^{\frac{2\pi i}{d} k'(k-j)}$$

with $\underbrace{(k-j)}_{\equiv x}$

[Sketch: sine and cosine waves over $[0, 2\pi]$ on the same axis]

① If $x = 0 \rightarrow \dfrac{1}{d}\sum_{k'=0}^{d-1}(1) = 1$

② If $x \neq 0 \rightarrow \dfrac{1}{d}\sum_{k'=0}^{d-1} \omega^{k'x} \rightarrow (\omega^x)^{k'}$

$$(\omega^x)^d = e^{\frac{2\pi i}{d}\cdot d \cdot x} = e^{2\pi i x} = \underbrace{\cos(2\pi x)}_{=1\,\forall x} + i\underbrace{\sin(2\pi x)}_{=0\,\forall x}$$

$$\omega = e^{\frac{2\pi i}{d}}, \qquad \omega^x = e^{\frac{2\pi i x}{d}}, \qquad \omega^{xd} = e^{2\pi i x} = 1$$

$$= \underbrace{\frac{1}{d}\sum_{k'=0}^{d-1}(\omega^x)^{k'}}_{\text{Finite geometric series!}} = \frac{1}{d}\left(\frac{1-(\omega^x)^d}{1-\omega}\right) = 0.$$

$$\sum_{k=0}^{d-1} r^{k'} = \frac{1-r^d}{1-r}$$

③ So $\dfrac{1}{d}\sum_{k'=0}^{d-1} \omega^{k'(k-j)} = \delta_{j-k,\,0} = \delta_{j,k}$

$$\Rightarrow \;\; QQ^\dagger = \sum_{k,j=0}^{d-1} \underbrace{\left(\frac{1}{d}\sum_{k'=0}^{d-1}\omega^{k'(k-j)}\right)}_{\delta_{k,j}} \ket{k}\bra{j} = \mathbb{1} \;\checkmark$$

Similarly, $Q^\dagger Q = \mathbb{1}$.

$$Q = \frac{1}{\sqrt{d}}\begin{pmatrix} 1 & 1 & 1 & \cdots & 1 \\ 1 & \omega & \omega^2 & \cdots & \omega^{d-1} \\ 1 & \omega^2 & \omega^4 & \cdots & \omega^{2(d-1)} \\ \vdots & \vdots & & & \vdots \\ 1 & \omega^{d-1} & \omega^{2(d-1)} & \cdots & \omega^{(d-1)^2} \end{pmatrix}$$

## Page 7

<u>Note</u>: for $d=2$, $\omega = e^{\frac{2\pi i}{2}} = e^{\pi i} = -1 \;\Rightarrow\; Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & \omega \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \to$ Hadamard!

— Let $d = 2^n$, $\omega = e^{\frac{2\pi i}{2^n}} \to$ <u>What is a circuit representation of QFT?</u>

Use the binary representation of $0, 1, 2, \ldots, 2^n - 1$

e.g., $n = 3$:

$$
\begin{aligned}
0 &\to 000 \\
1 &\to 001 \\
2 &\to 010 \\
3 &\to 011 \\
4 &\to 100 \\
5 &\to 101 \\
6 &\to 110 \\
7 &\to 111
\end{aligned}
\quad\Rightarrow\quad
\begin{array}{l}
\in \{0,1,2,\ldots,7\} \\
k \to (k_1, k_2, k_3) \\[4pt]
k = k_1 \cdot 4 + k_2 \cdot 2 + k_3 \cdot 1 \\[6pt]
\circledast \text{ In general: } k = \sum_{\ell=1}^{n} 2^{n-\ell} k_\ell
\end{array}
$$

$$Q\ket{j} = \frac{1}{\sqrt{2^n}} \sum_{k=0}^{2^n - 1} e^{\frac{2\pi i j k}{2^n}} \ket{k}$$

$$\Rightarrow Q\ket{j_1, j_2, \ldots, j_n} = \frac{1}{\sqrt{2^n}} \sum_{k_1, k_2, \ldots, k_n \in \{0,1\}} e^{\frac{2\pi i}{2^n} j (k_1 2^{n-1} + k_2 2^{n-2} + \cdots + k_n)} \ket{k_1, k_2, \ldots, k_n}$$

$$= \frac{1}{\sqrt{2^n}} \sum_{k_1 \in \{0,1\}} \sum_{k_2 \in \{0,1\}} \cdots \sum_{k_n \in \{0,1\}} e^{\frac{2\pi i}{2^n} j k_1 2^{n-1}} \, e^{\frac{2\pi i}{2^n} j k_2 2^{n-2}} \cdots e^{\frac{2\pi i}{2^n} j k_n} \ket{k_1, k_2, \ldots, k_n}$$

$$= \left( \frac{1}{\sqrt{2}} \sum_{k_1 \in \{0,1\}} e^{\frac{2\pi i}{2^n} j k_1 2^{n-1}} \ket{k_1} \right) \left( \frac{1}{\sqrt{2}} \sum_{k_2 \in \{0,1\}} e^{\frac{2\pi i}{2^n} j k_2 2^{n-2}} \ket{k_2} \right) \cdots \left( \frac{1}{\sqrt{2}} \sum_{k_n \in \{0,1\}} e^{\frac{2\pi i}{2^n} j k_n} \ket{k_n} \right)$$

$$= \left( \frac{1}{\sqrt{2}} \sum_{k_1 \in \{0,1\}} e^{2\pi i k_1 \frac{j}{2}} \ket{k_1} \right) \left( \frac{1}{\sqrt{2}} \sum_{k_2 \in \{0,1\}} e^{2\pi i k_2 \frac{j}{2^2}} \ket{k_2} \right) \cdots \left( \frac{1}{\sqrt{2}} \sum_{k_n \in \{0,1\}} e^{2\pi i k_n \frac{j}{2^n}} \ket{k_n} \right)$$

## Page 8

Consider $n=3$: $\mathcal{Q}\ket{j_1, j_2, j_3} = \left(\frac{1}{\sqrt{2}}\sum_{k_1 \in \{0,1\}} e^{2\pi i k_1 \frac{j}{2}}\ket{k_1}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_2 \in \{0,1\}} e^{2\pi i k_2 \frac{j}{2^2}}\ket{k_2}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_3 \in \{0,1\}} e^{2\pi i k_3 \frac{j}{2^3}}\ket{k_3}\right)$

$$j = 4j_1 + 2j_2 + j_3 \implies \frac{j}{2} = 2j_1 + j_2 + \frac{j_3}{2}$$

$$\frac{j}{2^2} = \frac{j}{4} = j_1 + \frac{j_2}{2} + \frac{j_3}{4}$$

$$\frac{j}{2^3} = \frac{j}{8} = \frac{j_1}{2} + \frac{j_2}{4} + \frac{j_3}{8}$$

$$\implies e^{2\pi i k_1 \frac{j}{2}} = \underbrace{e^{2\pi i k_1 (2j_1)}}_{=1} \underbrace{e^{2\pi i k_1 j_2}}_{=1} e^{2\pi i k_1 \frac{j_3}{2}} = e^{\pi i k_1 j_3} = (-1)^{k_1 j_3}$$

$$e^{2\pi i k_2 \frac{j}{4}} = \underbrace{e^{2\pi i k_2 j_1}}_{=1} \underbrace{e^{2\pi i k_2 (\frac{j_2}{2})}}_{=(-1)^{k_2 j_2}} \underbrace{e^{2\pi i k_2 (\frac{j_3}{4})}}_{= e^{\frac{2\pi i}{4} k_2 j_3}}$$

$$e^{2\pi i k_3 \frac{j}{8}} = \underbrace{e^{\frac{2\pi i}{2} k_3 j_1}}_{(-1)^{k_3 j_1}} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3}$$

Therefore: $\mathcal{Q}\ket{j_1, j_2, j_3} = \left(\frac{1}{\sqrt{2}}\sum_{k_1 \in \{0,1\}} (-1)^{k_1 j_3} \ket{k_1}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_2 \in \{0,1\}} (-1)^{k_2 j_2} e^{\frac{2\pi i}{4} k_2 j_3} \ket{k_2}\right)$

$$\left(\frac{1}{\sqrt{2}}\sum_{k_3 \in \{0,1\}} (-1)^{k_3 j_1} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3} \ket{k_3}\right)$$

$$= \frac{1}{\sqrt{2^3}} \sum_{k_1, k_2, k_3 \in \{0,1\}} (-1)^{k_1 j_3} (-1)^{k_2 j_2} (-1)^{k_3 j_1} e^{\frac{2\pi i}{4} k_2 j_3} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3} \ket{k_1, k_2, k_3}$$

$$= \widetilde{\mathcal{Q}} \ket{j_3, j_2, j_1}$$

$R_z(\theta) = e^{i\frac{\theta}{2} Z} = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}$ [illegible: factor]

✱ Define the rotation gate $R_k = \begin{pmatrix} 1 & 0 \\ 0 & e^{\frac{2\pi i}{2^k}} \end{pmatrix}$ $\quad R_2 = \begin{pmatrix} 1 & 0 \\ 0 & e^{\frac{2\pi i}{4}} \end{pmatrix}$

[Quantum circuit diagram enclosed in dashed purple box, labeled $\widetilde{\mathcal{Q}}$ below:
- Top wire $\ket{j_3}$: passes through control, then $R_3$ gate, then $R_2$ gate, then $H$
- Middle wire $\ket{j_2}$: $R_2$ gate, then control, then $H$, then control
- Bottom wire $\ket{j_1}$: $H$, then control, then control
]

$\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$

$e^{\frac{\pi i}{2}} = i$

## Page 9

So $\quad U \ket{j_1, j_2, j_3} = \tilde{U} \ket{j_3, j_2, j_1} = \tilde{U} S \ket{j_1, j_2, j_3}$

$\qquad\qquad\qquad\qquad\qquad\qquad\quad \uparrow$
$\qquad\qquad\qquad\qquad\qquad$ <span style="color:purple">Permutation of the qubits!</span>

★ In general, $\tilde{U}$ is given by the following circuit:

[Quantum circuit diagram with $n$ qubit lines, top to bottom labeled $\ket{j_n}, \ket{j_{n-1}}, \ldots, \ket{j_4}, \ket{j_3}, \ket{j_2}, \ket{j_1}$.

- Bottom wire $\ket{j_1}$: starts with $H$, then acts as control for a sequence of controlled rotation gates $R_2, R_3, R_4, \ldots, R_n$ applied to wires $\ket{j_2}, \ket{j_3}, \ket{j_4}, \ldots, \ket{j_n}$ respectively.
- Next wire $\ket{j_2}$: after the $R_2$ gate from $\ket{j_1}$, has an $H$, then controls $R_2, R_3, \ldots, R_{n-1}$ on the wires above.
- Wire $\ket{j_3}$: has $R_3$ (controlled from $\ket{j_1}$), then later $R_2$ (from $\ket{j_2}$), then $H$, etc.
- Wire $\ket{j_4}$: has $R_4$ (from $\ket{j_1}$), $R_3$ (from $\ket{j_2}$), then $H$ later.
- $\vdots$
- Top wire $\ket{j_n}$: receives $R_n, R_{n-1}, \ldots, R_2$ controlled rotations, then ends with $H$.]


# Lectures__quantum-gates(II)+measurements.pdf

## Page 1

① <u>Recap: Quantum Gates</u>

- Quantum gates describe how the states of qubits evolve — Similar to classical logic gates like AND, OR, NOT.

- Composing gates leads to <u>circuits</u>, which are used to describe quantum computations.

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left, passing through 3 layers of gates (1st layer, 2nd layer, 3rd layer) separated by dashed vertical lines, ending in measurement read-outs $D \rightsquigarrow x_1', x_2', x_3', x_4', x_5', x_6'$ on the right. Below: $(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$. Arrow labeled "time" pointing right. The measurements are labeled "Measurement/read-out".]

- Mathematically, quantum gates are described by <u>unitary matrices/operators</u> $U^\dagger U = U U^\dagger = \mathbb{1}$. They are <u>norm and trace preserving</u>. They describe <u>basis changes</u>.

  $\ket{\psi} \to U\ket{\psi} \to \|U\ket{\psi}\| = \|\ket{\psi}\|$  $\quad \{U\ket{k}\}_{k=0}^{d-1}$

  $\rho \to U\rho U^\dagger \to \mathrm{Tr}(U\rho U^\dagger) = \mathrm{Tr}(\rho)$.

- <u>Examples</u>:

  - <u>Pauli gates</u>:
  
    $-\boxed{X}- \quad \to \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \left( X\ket{0} = \ket{1},\ X\ket{1} = \ket{0} \right)$

    $-\boxed{Y}- \quad \to \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \left( Y\ket{0} = i\ket{1},\ Y\ket{1} = -i\ket{0} \right)$

    $-\boxed{Z}- \quad \to \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \quad \left( Z\ket{0} = \ket{0},\ Z\ket{1} = -\ket{1} \right)$

## Page 2

- **Hadamard gate:** $-\boxed{H}-$  $\rightarrow H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

$$H\ket{0} = \ket{+} = \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})$$
$$H\ket{1} = \ket{-} = \frac{1}{\sqrt{2}}(\ket{0}-\ket{1})$$

- **Phase gate:** $-\boxed{S}-$ $\rightarrow S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$

- **T-gate:** $-\boxed{T}-$ $\rightarrow T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$

- **CNOT / CX gate:**  *"controlled-X"*

[Circuit diagram: control wire with dot connected vertically to target wire with X box; alternatively shown with $\oplus$ symbol on target]
  - top wire = control
  - bottom wire (with X) = target

$$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}X\ket{0} = \ket{1}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}X\ket{1} = \ket{1}\ket{0}$$

- **Rotation Gates:**

$$R_X(\theta) = e^{-i\frac{\theta}{2}X} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)X \quad \rightarrow \text{rotation around X-axis by angle } \theta.$$

$$R_Y(\theta) = e^{-i\frac{\theta}{2}Y} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Y \quad \rightarrow \text{rotation around Y-axis by angle } \theta.$$

$$R_Z(\theta) = e^{-i\frac{\theta}{2}Z} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Z \quad \rightarrow \text{rotation around Z-axis by angle } \theta.$$

## Page 3

② <u>Translating b/w circuit diagrams and math.</u>

[Circuit: $\ket{\psi}$ — [U] —]   $\leftrightarrow$   $U\ket{\psi}$

[Circuit: $\ket{\psi}$ — [$U_1$] — [$U_2$] —]   $\leftrightarrow$   $U_2 U_1 \ket{\psi}$

[Arrows indicating $U_1$ then $U_2$ applied in order]

<span style="color:red">↑ state vector (representing pure state).</span>

[Circuit: $\rho$ — [U] —]   $\leftrightarrow$   $U \rho U^\dagger$    $\quad$  $\rho = \ket{\psi}\bra{\psi} \;\to\; U\ket{\psi}\bra{\psi}U^\dagger$

<span style="color:red">↑ density operator (representing mixed state).</span>

[Circuit: $\rho$ — [$U_1$] — [$U_2$] —]   $\leftrightarrow$   $U_2 U_1 \rho U_1^\dagger U_2^\dagger$

[Dashed arrow at intermediate point: $U_1 \rho U_1^\dagger$]

[Two-qubit circuit:
 line 1: — [$U_1$] —
 line 2: — [$U_2$] — ]
$\leftrightarrow$   $U_1 \otimes U_2$

<span style="color:red">↑ tensor product of matrices.</span>

<span style="color:red">$U_1$ acts on qubit 1<br>
$U_2$ acts on qubit 2.</span>

## Page 4

<u>Recall</u>: $\ket{V_1} = \begin{pmatrix} a_1 \\ b_1 \end{pmatrix}$, $\ket{V_2} = \begin{pmatrix} a_2 \\ b_2 \end{pmatrix}$ $\Rightarrow$ $\ket{V_1} \otimes \ket{V_2} = \begin{pmatrix} a_1 a_2 \\ a_1 b_2 \\ b_1 a_2 \\ b_1 b_2 \end{pmatrix} = \begin{pmatrix} a_1 \begin{pmatrix} a_2 \\ b_2 \end{pmatrix} \\ b_1 \begin{pmatrix} a_2 \\ b_2 \end{pmatrix} \end{pmatrix}$

$M_1 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix}$, $M_2 = \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix}$ $\Rightarrow$ $M_1 \otimes M_2 = \begin{pmatrix} a_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} & b_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} \\ c_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} & d_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} \end{pmatrix}$

$= \begin{pmatrix} a_1 a_2 & a_1 b_2 & b_1 a_2 & b_1 b_2 \\ a_1 c_2 & a_1 d_2 & b_1 c_2 & b_1 d_2 \\ c_1 a_2 & c_1 b_2 & d_1 a_2 & d_1 b_2 \\ c_1 c_2 & c_1 d_2 & d_1 c_2 & d_1 d_2 \end{pmatrix}$

$\text{Tr}[M \otimes N] = \text{Tr}[N]\,\text{Tr}[M].$

$\langle M_1 \otimes M_2,\, N_1 \otimes N_2 \rangle = \langle M_1, N_1 \rangle \langle M_2, N_2 \rangle$

$\langle M, N \rangle = \text{Tr}(M^\dagger N).$

[Circuit diagram: three parallel wires labeled 1, 2, 3, each passing through a single-qubit gate $U_1$, $U_2$, $U_3$ respectively]  $\longleftrightarrow$  $U_1 \otimes U_2 \otimes U_3.$

[Circuit diagram: three input states $\ket{\psi_1}$, $\ket{\psi_2}$, $\ket{\psi_3}$ each entering gates $U_1$, $U_2$, $U_3$ respectively]  $\longleftrightarrow$  $(U_1 \otimes U_2 \otimes U_3)(\ket{\psi_1} \otimes \ket{\psi_2} \otimes \ket{\psi_3})$

$\qquad\qquad = U_1\ket{\psi_1} \otimes U_2\ket{\psi_2} \otimes U_3\ket{\psi_3}.$

## Page 5

- **Tracking the State of qubits through a circuit**

$$\ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$$

$$\ket{+}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{0}$$

[Circuit: top qubit $\ket{0}$ through $H$, then control of CNOT; bottom qubit $\ket{0}$ is target. Red arrows mark stages ① and ②.]

$$\ket{0}\ket{0} \xmapsto{\;①\;} H\ket{0}\ket{0} = \ket{+}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{0})$$

$$\xmapsto{\;②\;} \tfrac{1}{\sqrt{2}}\big(\underbrace{\text{CNOT}\ket{0}\ket{0}}_{\ket{0}\ket{0}} + \underbrace{\text{CNOT}\ket{1}\ket{0}}_{\ket{1}\ket{1}}\big)$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{1})$$

$$\ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0}-\ket{1})$$

[Circuit: top qubit $\ket{1}$ through $H$, then control of CNOT; bottom qubit $\ket{0}$ target. Stages ① and ②.]

$$\ket{1}\ket{0} \xmapsto{\;①\;} H\ket{1}\ket{0} = \ket{-}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{0})$$

$$\xmapsto{\;②\;} \tfrac{1}{\sqrt{2}}\big(\text{CNOT}\ket{0}\ket{0} - \text{CNOT}\ket{1}\ket{0}\big)$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{1})$$

---

[Three-qubit circuit: qubit 1 $\ket{0}$ — $H$ — • — — — $H$; qubit 2 $\ket{0}$ — $H$ — — • — $H$; qubit 3 $\ket{0}$ — — ⊕ — ⊕ — . Red arrows mark stages ①, ②, ③, ④.]

$$\ket{0}\ket{0}\ket{0} \xmapsto{\;①\;} \ket{+}\ket{+}\ket{0}$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\,\tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{0}$$

$$= \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{0} + \ket{1}\ket{0}\ket{0} + \ket{1}\ket{1}\ket{0}\big)$$

$$\xmapsto{\;②\;} \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{0} + \ket{1}\ket{0}\ket{1} + \ket{1}\ket{1}\ket{1}\big)$$

$$\xmapsto{\;③\;} \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{1} + \ket{1}\ket{0}\ket{1} + \ket{1}\ket{1}\ket{0}\big)$$

$$\xmapsto{\;④\;} \tfrac{1}{2}\big(\ket{+}\ket{+}\ket{0} + \ket{+}\ket{-}\ket{1} + \ket{-}\ket{+}\ket{1} + \ket{-}\ket{-}\ket{0}\big)$$

$$= \tfrac{1}{2}\Big(\underbrace{(\ket{+}\ket{+}+\ket{-}\ket{-})}_{(a)}\ket{0} + \underbrace{(\ket{+}\ket{-}+\ket{-}\ket{+})}_{(b)}\ket{1}\Big)$$

$$= \tfrac{1}{\sqrt{2}}\Big(\tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{1})\ket{0} + \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{1})\ket{1}\Big)$$

(a) $\tfrac{1}{2}\big(\ket{0}\ket{0}+\ket{0}\ket{1}+\ket{1}\ket{0}+\ket{1}\ket{1}$
$\quad\quad +\ket{0}\ket{0}-\ket{0}\ket{1}-\ket{1}\ket{0}+\ket{1}\ket{1}\big)$
$= \ket{0}\ket{0} + \ket{1}\ket{1}$

(b) $\tfrac{1}{2}\big(\ket{0}\ket{0}-\ket{0}\ket{1}+\ket{1}\ket{0}-\ket{1}\ket{1}$
$\quad\quad +\ket{0}\ket{0}+\ket{0}\ket{1}-\ket{1}\ket{0}-\ket{1}\ket{1}\big)$
$= \ket{0}\ket{0} - \ket{1}\ket{1}$

## Page 6

## ③ Measurements

- To extract classical information from a qubit, we must <u>measure</u> it

- <u>Recall</u>: $\ket{\psi} = \alpha\ket{0} + \beta\ket{1} \rightarrow$ Probability of 0: $|\alpha|^2$  ⊛ <span style="color:red">Axiom of quantum mechanics! (aka "Born Rule")</span>
  
  $\alpha = \braket{0|\psi}, \;\beta = \braket{1|\psi}$  Probability of 1: $|\beta|^2$

  ⊛ <u>Note</u>: $|\alpha|^2 = |\braket{0|\psi}|^2,\; |\beta|^2 = |\braket{1|\psi}|^2$

  <u>Also</u>: $\underbrace{|\braket{0|\psi}|^2}_{\equiv \,\Pr(0)} = \braket{0|\psi}\braket{\psi|0} = \mathrm{Tr}\big[\ket{0}\bra{0}\,\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad\qquad\qquad\qquad\quad \braket{v_1|M|v_2} = \mathrm{Tr}\big[M\ket{v_2}\bra{v_1}\big]$

  $\underbrace{|\braket{1|\psi}|^2}_{\equiv \,\Pr(1)} = \braket{1|\psi}\braket{\psi|1} = \mathrm{Tr}\big[\ket{1}\bra{1}\,\ket{\psi}\bra{\psi}\big]$

  <u>Check</u>: $\Pr(0) + \Pr(1) = \mathrm{Tr}\big[\ket{0}\bra{0}\ket{\psi}\bra{\psi}\big] + \mathrm{Tr}\big[\ket{1}\bra{1}\ket{\psi}\bra{\psi}\big]$

  $\mathrm{Tr}[M_1 + M_2] = \mathrm{Tr}[M_1] + \mathrm{Tr}[M_2]$
  
  $\mathrm{Tr}\big[\ket{0}\bra{0}\ket{\psi}\bra{\psi} + \ket{1}\bra{1}\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad = \mathrm{Tr}\Big[\big(\underbrace{\ket{0}\bra{0} + \ket{1}\bra{1}}_{=\,\mathbb{1}}\big)\ket{\psi}\bra{\psi}\Big]$
  
  $\qquad\qquad = \mathrm{Tr}\big[\ket{\psi}\bra{\psi}\big]$
  
  $\qquad\qquad = \braket{\psi|\psi}$
  
  $\qquad\qquad = 1\;\checkmark$

  ⊛ This is often called a "<u>computational-basis measurement</u>"
  or a "$\{\ket{0},\ket{1}\}$-<u>basis measurement</u>".

  ⊛ Recall that $\{\ket{0},\ket{1}\}$ is also the eigenvectors of Pauli-Z:
  
  $Z\ket{0} = \ket{0},\; Z\ket{1} = -\ket{1}. \rightarrow$ So we also sometimes say "<u>Pauli-Z measurement</u>"

  ⊛ <u>Circuit symbol</u>:  $\ket{\psi}\!-\!\boxed{Z}\!=$

## Page 7

⊛ <u>Observe</u>: If $\ket{\psi} = \ket{0}$, then $\Pr(0) = 1$, $\Pr(1) = 0$.
If $\ket{\psi} = \ket{1}$, then $\Pr(0) = 0$, $\Pr(1) = 1$.

— We can measure with respect to other Pauli operators too!

[Bloch sphere diagram with $\ket{0}$ at top (+z), $\ket{1}$ at bottom, $\ket{+}$ on +x axis, $\ket{-}$ on −x, $\ket{+i}$ on +y, $\ket{-i}$ on −y]

- <u>Pauli-X measurement</u>: measure along x-axis; equivalent to measuring in basis $\{\ket{+}, \ket{-}\}$

⊛ Recall: $\ket{+} = H\ket{0}$, $\ket{-} = H\ket{1}$, $H \equiv$ Hadamard gate
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

⊛ $H$ unitary $\Rightarrow \{\ket{+}, \ket{-}\}$ is a basis!

⊛ For a state vector $\ket{\psi}$:
$$\Pr(+) = |\braket{+|\psi}|^2 = \braket{+|\psi}\braket{\psi|+} = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big]$$
$$\Pr(-) = |\braket{-|\psi}|^2 = \braket{-|\psi}\braket{\psi|-} = \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big]$$

$\ket{+} = H\ket{0}$
$\ket{-} = H\ket{1}$

<u>Check</u>: $\Pr(+) + \Pr(-) = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big] + \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big]$

$$= \mathrm{Tr}\Big[\underbrace{\big(\ket{+}\bra{+} + \ket{-}\bra{-}\big)}_{\downarrow}\ket{\psi}\bra{\psi}\Big] = \mathrm{Tr}\big[\ket{\psi}\bra{\psi}\big] = 1 \;\checkmark$$

$$= H\ket{0}\bra{0}H^\dagger + H\ket{1}\bra{1}H^\dagger = H\ket{0}\bra{0}H + H\ket{1}\bra{1}H$$
$$= H\underbrace{\big(\ket{0}\bra{0} + \ket{1}\bra{1}\big)}_{=\,\mathbb{1}}H$$
$$= HH = \mathbb{1}$$

⊛ <u>Observe</u>: $\Pr(+) = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[H\ket{0}\bra{0}H\,\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[\ket{0}\bra{0}\,\underline{H\ket{\psi}\bra{\psi}H}\big]$

$\quad\;\; \Pr(-) = \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[H\ket{1}\bra{1}H\,\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[\ket{1}\bra{1}\,\underline{H\ket{\psi}\bra{\psi}H}\big]$

[with $\ket{\psi'}$ labeled above $H\ket{\psi}\bra{\psi}H$]

$\Rightarrow$ Apply $H$ gate to $\ket{\psi}$, then measure in $\{\ket{0}, \ket{1}\}$ basis!

$X\ket{+} = \ket{+},\; X\ket{-} = -\ket{-}$

## Page 8

⊛ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{H} - \boxed{X} \models$

$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

[Bloch sphere with $\ket{0}$ at top (z-axis), $\ket{1}$ at bottom, $\ket{+}$ and $\ket{-}$ on x-axis, $\ket{+i}$ and $\ket{-i}$ on y-axis]

- <u>Pauli-Y measurement</u>: measure along $y$-axis; equivalent to measuring in basis $\{\ket{+i}, \ket{-i}\}$

⊛ <span style="color:red">Recall: $\ket{+i} = SH\ket{0}$, $\ket{-i} = SH\ket{1}$, $H \equiv$ Hadamard gate</span>

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

⊛ <span style="color:red">$SH$ unitary $\Rightarrow \{\ket{+i}, \ket{-i}\}$ is a basis!</span>

$S \equiv$ phase gate
$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

⊛ For a state vector $\ket{\psi}$:

$$P_r(+i) = |\braket{+i|\psi}|^2 = \braket{+i|\psi}\braket{\psi|+i} = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}]$$

$$P_r(-i) = |\braket{-i|\psi}|^2 = \braket{-i|\psi}\braket{\psi|-i} = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$$

<u>Check</u>: $P_r(+i) + P_r(-i) = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}] + \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$

$$= \mathrm{Tr}\big[(\ket{+i}\bra{+i} + \ket{-i}\bra{-i})\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}[\ket{\psi}\bra{\psi}] = 1 \checkmark$$

<span style="color:blue">$\ket{+i} = SH\ket{0}$
$\ket{-i} = SH\ket{1}$</span>

$$= SH\ket{0}\bra{0}HS^\dagger + SH\ket{1}\bra{1}HS^\dagger = SH\ket{0}\bra{0}HS^\dagger + SH\ket{1}\bra{1}HS^\dagger$$

$$= SH\big(\ket{0}\bra{0} + \ket{1}\bra{1}\big)HS^\dagger$$
$$\quad\quad\quad\quad\quad\quad = \mathbb{1}$$
$$= SH \cdot HS^\dagger = SS^\dagger = \mathbb{1}$$
$$\quad\;\; = \mathbb{1}$$

⊛ <u>Observe</u>: $P_r(+i) = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}] = \mathrm{Tr}[SH\ket{0}\bra{0}HS^\dagger \underbrace{\ket{\psi}\bra{\psi}}_{}] = \mathrm{Tr}[\ket{0}\bra{0}HS^\dagger\ket{\psi}\bra{\psi}SH]$

$P_r(-i) = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}] = \mathrm{Tr}[SH\ket{1}\bra{1}HS^\dagger\ket{\psi}\bra{\psi}] = \mathrm{Tr}[\ket{1}\bra{1}\underline{HS^\dagger\ket{\psi}}\bra{\psi}SH]$

$\Rightarrow$ Apply $S^\dagger$, then $H$ gate to $\ket{\psi}$, then measure in $\{\ket{0}, \ket{1}\}$ basis!

⊛ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{S^\dagger} - \boxed{H} - \boxed{X} \models$

## Page 9

## — Measuring multiple qubits.

- Consider state vector $\ket{\psi}$ of $n$ qubits $\left(\ket{\psi} \in (\mathbb{C}^2)^{\otimes n}\right)$.

- Computational-basis measurement is a $\{\ket{0}, \ket{1}\}$ measurement on each qubit.

- Outcome probabilities: $\Pr[0,0,1] = |\underbrace{\bra{0,0,1}}_{\bra{0}\otimes\bra{0}\otimes\bra{1}}\ket{\psi}|^2$ (for three qubits).

$$\Pr[x_1, x_2, x_3] = |\braket{x_1, x_2, x_3 | \psi}|^2, \quad x_1, x_2, x_3 \in \{0,1\}.$$

- What is the probability that the first qubit is 0?

$$\Pr[1^{st}\text{ qubit } 0] = \Pr[0,0,0] + \Pr[0,0,1] + \Pr[0,1,0] + \Pr[0,1,1].$$

$$\left\{\begin{matrix} 000 \\ 001 \\ 010 \\ 011 \end{matrix}\right. \quad \begin{matrix} 100 \\ 101 \\ 110 \\ 111 \end{matrix}$$

$$\Pr[2^{nd}\text{ qubit } 1] = \Pr[0,1,0] + \Pr[0,1,1] + \Pr[1,1,0] + \Pr[1,1,1].$$

- We can simultaneously measure each qubit in a different basis.

**Example:** measure $1^{st}$ & $3^{rd}$ qubit in Z-basis, $2^{nd}$ in X-basis.

$$\Pr[0, +, 1] = |\underbrace{\bra{0, +, 1}}_{= \bra{0}\otimes\bra{+}\otimes\bra{1}}\ket{\psi}|^2$$

## Page 10

## ④ Observables

- In quantum mechanics, measurement outcomes are not deterministic — they occur with some probability.

- What is the *expected* outcome of a measurement?

- Recall: For a probability mass function $p_X(x)$, $\quad \left( \begin{array}{l} p_X(x) \in [0,1] \;\; \forall x \in \mathcal{X} \\ \sum_{x \in \mathcal{X}} p_X(x) = 1 \end{array} \right)$

  [Red annotation: $X$ is a Random variable $\to \Pr(X = x) = p_X(x)$.]

  the expected value is

$$\mathbb{E}(X) = \sum_x p_X(x) \cdot x$$

- We can measure w.r.t. any orthonormal basis — consider basis $\{\ket{e_k}\}_{k=1}^{d}$.

  Outcomes are labeled by $k$
  Outcome $k$ is associated with value $\lambda_k$. $\leftrightarrow$ random variable $X$

  For a state vector $\ket{\psi} \in \mathbb{C}^d$, the probability distribution is

$$\Pr(k) = |\braket{e_k|\psi}|^2 \equiv \Pr(X = \lambda_k)$$

  The expected value of $X$ is:

  [Blue annotation: $\braket{v_1 | M | v_2} = \mathrm{Tr}\left[ M \ket{v_2}\bra{v_1} \right]$.]

$$\mathbb{E}(X) = \sum_{k=1}^{d} \Pr(X = \lambda_k) \cdot \lambda_k = \sum_{k=1}^{d} |\braket{e_k|\psi}|^2 \cdot \lambda_k = \sum_{k=1}^{d} \braket{e_k | \psi}\braket{\psi | e_k} \cdot \lambda_k$$

$$= \sum_{k=1}^{d} \mathrm{Tr}\!\left( \ket{e_k}\bra{e_k} \psi \rangle\langle \psi \right) \cdot \lambda_k = \mathrm{Tr}\!\left[ \left( \sum_{k=1}^{d} \lambda_k \ket{e_k}\bra{e_k} \right) \ket{\psi}\bra{\psi} \right] = \mathrm{Tr}\!\left[ H \ket{\psi}\bra{\psi} \right].$$

$$H \ket{e_{k'}} = \sum_{k=1}^{d} \lambda_k \ket{e_k}\underbrace{\braket{e_k|e_{k'}}}_{\delta_{k,k'}} = \lambda_{k'} \ket{e_{k'}}$$

[Red annotation: $H \to$ Hermitian operator.]


# Lectures__quantum-gates.pdf

## Page 1

① <u>Recap: Density Matrices</u>

- A <u>density matrix</u> in dimension $d \in \{2,3,\ldots\}$ is a $d \times d$ matrix $\rho \in L(\mathbb{C}^d)$ satisfying the following properties:

    (1) <u>Hermitian</u>: $\rho^\dagger = \rho$  $\quad \dagger \equiv$ conjugate transpose.

    (2) <u>Unit Trace</u>: $\text{Tr}[\rho] = 1$ $\quad$ (Recall: Tr ≡ trace ≡ sum of diagonal elements of a matrix)

    (3) <u>Positive Semi-definite</u>: $\rho \geq 0$

    ✱ This means that $\langle v | \rho | v \rangle \geq 0 \;\; \forall \; |v\rangle \in \mathbb{C}^d$.
    Equivalently: all the <u>eigenvalues</u> of $\rho$ are non-negative.
    $\hookrightarrow M|v\rangle = \lambda |v\rangle$

✱ <u>Axiom of Quantum Mechanics</u>: The state of any quantum system is mathematically described by a density matrix. (arbitrary dimension).
State vector: $|\psi\rangle \to \||\psi\rangle\| = 1 \to \rho = |\psi\rangle\langle\psi|$

- For $d=2$ (qubits), density matrices are synonymous with points on and inside the unit sphere.

[Bloch sphere diagram: sphere with $|0\rangle$ at top (+z), $|1\rangle$ at bottom (-z), $|+\rangle$ and $|-\rangle$ on x-axis, $|+i\rangle$ and $|-i\rangle$ on y-axis. Labeled "(Bloch sphere)".]

→ Point $\vec{r} \in \mathbb{R}^3$ (real 3D space)
$\vec{r} = (r_x, r_y, r_z)$, $\rho = \frac{1}{2}(\mathbb{1} + r_x \underline{X} + r_y \underline{Y} + r_z \underline{Z})$.

$r_x^2 + r_y^2 + r_z^2 \leq 1$, $r_x = \text{Tr}[\rho X]$, $r_y = \text{Tr}[\rho Y]$, $r_z = \text{Tr}[\rho Z]$.

$\text{Tr}[\rho X] = \text{Tr}\left[\frac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z) X\right]$
$\quad = \frac{1}{2}(\text{Tr}[X] + r_x \text{Tr}[\mathbb{1}] + r_y \text{Tr}[YX] + r_z \text{Tr}[ZX])$
$\quad = r_x.$

- $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$, $Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (<u>Pauli matrices</u>).

- If $r_x^2 + r_y^2 + r_z^2 = 1$, then $\rho$ is a <u>pure state</u>: it can be written as $\rho = |\psi\rangle\langle\psi|$, where $|\psi\rangle \in \mathbb{C}^2$ is a <u>state vector</u>; $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$.

## Page 2

- ✻ <u>Origin</u>, $\vec{r} = (0,0,0) \to \rho = \frac{1}{2}(\ket{0}\bra{0} + \ket{1}\bra{1}) \to$ the <u>maximally-mixed state</u>  $\quad |\alpha|^2 + |\beta|^2 = 1$
  
  (A completely random state). $\quad = \frac{\mathbb{1}}{2}$

- ✻ <u>Points on the X-axis</u>: $\vec{r} = (\pm 1, 0, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm X) = \ket{\pm}\bra{\pm}, \quad \ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$

  These are eigenvectors of $X$! $\quad X\ket{\pm} = \pm\ket{\pm}. \to X\ket{+} = \ket{+}$
  (Eigenvalues of $X$ are $\pm 1$.) $\hspace{6cm} X\ket{-} = -\ket{-}$

- ✻ <u>Points on the Y-axis</u>: $\vec{r} = (0, \pm 1, 0) \to \rho = \frac{1}{2}(\mathbb{1} \pm Y) = \ket{\pm i}\bra{\pm i}, \quad \ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

  These are eigenvectors of $Y$! $\quad Y\ket{\pm i} = \pm \ket{\pm i}. \quad Y\ket{+i} = \ket{+i}$
  (Eigenvalues of $Y$ are $\pm 1$.) $\hspace{6cm} Y\ket{-i} = -\ket{-i}$

- ✻ <u>Points on the Z-axis</u>: $\vec{r} = (0, 0, \pm 1) \to \rho = \frac{1}{2}(\mathbb{1} \pm Z) \begin{matrix} ^{(+)}\to \ket{0}\bra{0} \\ _{(-)}\to \ket{1}\bra{1} \end{matrix}$

  These are eigenvectors of $Z$! $\quad Z\ket{0} = \ket{0}, \; Z\ket{1} = -\ket{1}.$ (Eigenvalues of $Z$ are $\pm 1$.)

- For higher dimensions, we don't have such a nice representation.

- We can still check if a state is pure using the <u>purity</u>:

  For density matrix $\rho$ in dimension $d$, $\quad \underline{\text{Tr}[\rho^2] \equiv \text{purity}}$

  The state $\rho$ is pure if and only if $\text{Tr}[\rho^2] = 1$.

- ✻ Every pure state is represented by a density matrix of the form $\rho = \ket{\psi}\bra{\psi}$, where $\ket{\psi} \in \mathbb{C}^d$ is a state vector ($\|\ket{\psi}\| = 1$).

  If a state is not pure, then we call it a <mark>mixed state.</mark>

- ✻ <u>Important fact</u>: Every mixed state can be written as a <u>convex combination</u> of pure states:
  
  $$\rho = \sum_{k=1}^{M} p_k \ket{\psi_k}\bra{\psi_k}, \quad p_k \in [0,1], \quad \sum_{k=1}^{M} p_k = 1.$$
  
  $\hspace{3cm}\uparrow$ probabilities.

## Page 3

$$\underline{\text{Check}}: \text{Tr}[\rho] = \sum_{k=1}^{m} p_k \underbrace{\text{Tr}\left[\ket{\psi_k}\bra{\psi_k}\right]}_{=1} = \sum_{k=1}^{m} p_k = 1 \quad \checkmark$$

$$\begin{pmatrix} (M_1+M_2)^\dagger \\ = M_1^\dagger + M_2^\dagger \end{pmatrix} \qquad \underline{\text{Check}}: \rho^\dagger = \sum_{k=1}^{m} p_k \underbrace{\left(\ket{\psi_k}\bra{\psi_k}\right)^\dagger}_{= \ket{\psi_k}\bra{\psi_k}} = \sum_{k=1}^{m} p_k \ket{\psi_k}\bra{\psi_k} = \rho \quad \checkmark$$

$$\left(\ket{v_1}\bra{v_2}\right)^\dagger = \ket{v_2}\bra{v_1}$$

$\underline{\text{Check}}: \rho \succeq 0 \longrightarrow$ Yes, b/c we sum over PSD elements.

$$M_1, M_2 \succeq 0$$

$$\bra{v}(M_1+M_2)\ket{v} = \underbrace{\bra{v}M_1\ket{v}}_{\geq 0} + \underbrace{\bra{v}M_2\ket{v}}_{\geq 0} \geq 0$$

② <u>Quantum Circuits and gates.</u>

- <u>Recap</u>: classical computation: manipulation of bits via <u>logic gates</u> (AND, OR, NOT, XOR)

  For input $x \in \{0,1\}^n$, calculate $f(x)$ for some $f$.
  (How to realize $f$ with a circuit? How many gates / depth is necessary and/or sufficient?)

  ✱ We rarely think about computation in these terms anymore!

  ✱ We program in some <u>high-level language</u> (C++, python, julia) and then the code gets <u>compiled</u> into the machine-level language.

  ✱ Quantum computing is still thought about at the gate level.

  (Although "quantum programming languages" are being developed — qiskit is a simple example.)

## Page 4

- **Classical logic circuits:**

  [Circuit diagram: input $x_1$ goes into a NOT gate; inputs $x_2, x_3$ go into an OR gate; the NOT output and OR output feed into an AND gate; the AND output and another signal feed into a final OR gate.]

  - For every logic gate, we have a truth table (how 0 + 1 are transformed by the gate.)

  [Gate symbols shown: OR, AND, XOR, NOR, NAND, NOT]

  | A | NOT A |
  |---|-------|
  | 0 | 1     |
  | 1 | 0     |

  | A | B | A AND B |
  |---|---|---------|
  | 0 | 0 | 0       |
  | 0 | 1 | 0       |
  | 1 | 0 | 0       |
  | 1 | 1 | 1       |

  | A | B | A OR B |
  |---|---|--------|
  | 0 | 0 | 0      |
  | 0 | 1 | 1      |
  | 1 | 0 | 1      |
  | 1 | 1 | 1      |

  | A | B | A XOR B |
  |---|---|---------|
  | 0 | 0 | 0       |
  | 0 | 1 | 1       |
  | 1 | 0 | 1       |
  | 1 | 1 | 0       |

  | A (control bit) | B (target bit) | A CNOT B |
  |-----------------|----------------|----------|
  | 0               | 0              | 0  0     |
  | 0               | 1              | 0  1     |
  | 1               | 0              | 1  1     |
  | 1               | 1              | 1  0     |

  ⊛ Reversible version of XOR gate.

  $$A, B \mapsto A,\; A \oplus B. \quad \oplus$$

  - For a given circuit, we use these truth tables, combining them to get the truth table of the whole circuit.

## Page 5

- **Quantum Circuits and Gates**: very similar! But the gates act on the complex vector space $(\mathbb{C}^2)^{\otimes n}$ of $n$ qubits ⟶ they are represented by <mark>unitary matrices</mark>. ⟶ matrix $U \in L(\mathbb{C}^d)$ satisfying $U^\dagger U = U U^\dagger = \mathbb{1}$.

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left, passing through 3 layers of gate boxes (1st layer, 2nd layer, 3rd layer separated by dashed vertical lines), with measurement/read-out on the right giving outputs $\sim x_1', x_2', x_3', x_4', x_5', x_6'$. Time flows left to right. Inputs satisfy $(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$.]

- ✸ Each box represents a gate / unitary matrix.
- ✸ Multiply the gates to get a unitary matrix for the full circuit.

✸ Why unitary matrix? Comes from quantum physics (Schrödinger equation).

✸ To understand what the circuit does, we just have to know how it acts on basis vectors!

<u>Recall</u>: any state vector of $n$ qubits can be represented as

$$\ket{\psi} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}}, \quad c_{\vec{x}} \in \mathbb{C}, \quad \sum_{\vec{x} \in \{0,1\}^n} |c_{\vec{x}}|^2 = 1.$$

$$\left( \begin{array}{l} \vec{x} \equiv (x_1, x_2, \ldots, x_n), \; x_i \in \{0,1\} \\ \ket{\vec{x}} \equiv \ket{x_1, x_2, \ldots, x_n} \\ \quad\quad = \ket{x_1} \otimes \ket{x_2} \otimes \cdots \otimes \ket{x_n} \end{array} \right)$$

↳ input state of the quantum circuit.

$$\Rightarrow U \ket{\psi} = U \left( \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}} \right) = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \, \underline{U \ket{\vec{x}}}.$$

$\left( \text{✸ Linearity of matrices: } M(\alpha \ket{v_1} + \beta \ket{v_2}) = \alpha M \ket{v_1} + \beta M \ket{v_2} \right).$

## Page 6

- From calculating $U\ket{\vec{x}}$ for all $\vec{x}$, we get something like the "truth table" of the quantum circuit.

✱ Elementary quantum gates (building blocks of larger circuits).

- **Pauli gates:** $-\boxed{X}-\ \rightarrow\ X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\ \left(X\ket{0}=\ket{1},\ X\ket{1}=\ket{0}\right)$

  $X^\dagger = X$,
  $X^\dagger X = X^2 = \mathbb{1}$

  $\quad\quad\quad\quad\quad\quad\ \  -\boxed{Y}-\ \rightarrow\ Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\ \left(Y\ket{0}=i\ket{1},\ Y\ket{1}=-i\ket{0}\right)$

  $\quad\quad\quad\quad\quad\quad\ \  -\boxed{Z}-\ \rightarrow\ Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\ \left(Z\ket{0}=\ket{0},\ Z\ket{1}=-\ket{1}\right)$

- **Hadamard gate:** $-\boxed{H}-\ \rightarrow\ H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

  $H^\dagger = H \rightarrow H^2 = \mathbb{1}$.

  $H\ket{0} = \ket{+} = \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})$
  $H\ket{1} = \ket{-} = \frac{1}{\sqrt{2}}(\ket{0}-\ket{1})$.

- **Phase gate:** $-\boxed{S}-\ \rightarrow\ S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \rightarrow S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$

- **T-gate:** $-\boxed{T}-\ \rightarrow\ T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$

  $\underbrace{\phantom{e^{i\pi/4}}}_{\downarrow}$

  $e^{i\pi/4} = \cos\left(\frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{4}\right)$
  $\quad\quad = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}i$

## Page 7

- **CNOT / CX gate:** "controlled-X"

[Circuit: two horizontal wires, top wire has a control dot (labeled "control"), bottom wire has an X box (labeled "target")]   or   [equivalent circuit with control dot on top wire and ⊕ symbol on bottom wire]

$$\text{CNOT} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{pmatrix} \overset{00}{1} & \overset{01}{0} & \overset{10}{0} & \overset{11}{0} \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}X\ket{0} = \ket{1}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}X\ket{1} = \ket{1}\ket{0}$$

B/c of linearity, this determines the action on **any** state!

$$\ket{\psi} = a\ket{0,0} + b\ket{0,1} + c\ket{1,0} + d\ket{1,1} \mapsto a\ket{0,0} + b\ket{0,1} + c\ket{1,1} + d\ket{1,0}$$

---

- **Controlled-Z / CZ gate:**

[Circuit: top wire control dot, bottom wire Z box]   OR   [Circuit: control dot on both wires connected by vertical line — symmetric notation]

$$CZ = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{pmatrix} \overset{00}{1} & \overset{01}{0} & \overset{10}{0} & \overset{11}{0} \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$$

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}Z\ket{0} = \ket{1}\ket{0}$$
$$\ket{1}\ket{1} \mapsto \ket{1}Z\ket{1} = -\ket{1}\ket{1}$$

---

- **Controlled Unitary**

[Circuit: top wire control dot, bottom wire U box]

$$cU = \begin{pmatrix} \mathbb{1} & 0 \\ 0 & U \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ \hline 0 & 0 & & \\ 0 & 0 & \multicolumn{2}{c}{U} \end{pmatrix}$$

$$\underbrace{\phantom{xxx}}_{\text{2×2 unitary}}$$

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}U\ket{0}$$
$$\ket{1}\ket{1} \mapsto \ket{1}U\ket{1}$$

## Page 8

- **Rotation Gates:**

$$R_X(\theta) = e^{-i\frac{\theta}{2}X} \quad \rightarrow \text{rotation around X-axis by angle } \theta.$$

$$R_Y(\theta) = e^{-i\frac{\theta}{2}Y} \quad \rightarrow \text{rotation around Y-axis by angle } \theta.$$

$$R_Z(\theta) = e^{-i\frac{\theta}{2}Z} \quad \rightarrow \text{rotation around Z-axis by angle } \theta.$$

[Bloch sphere diagram with axes labeled $x$, $y$, $z$; points marked $\ket{+}$ on +x axis and $\ket{+i}$ on +y axis]

$$e^M := \sum_{k=0}^{\infty} \frac{1}{k!} M^k \quad (\text{matrix exponential})$$

$$\Rightarrow \quad e^{-i\frac{\theta}{2}X} = \sum_{k=0}^{\infty} \frac{1}{k!}\left(-i\frac{\theta}{2}X\right)^k$$

$$\left(\begin{array}{l} X^2 = \mathbb{1} \\ \Rightarrow X^k = \mathbb{1},\ k \text{ even} \\ \quad\ X^k = X,\ k \text{ odd} \end{array}\right)$$

$X^3 = \underbrace{X^2}_{\mathbb{1}} \cdot X = X \qquad X^4 = \underbrace{X^2 \cdot X^2}_{} = \mathbb{1}$

$$= \sum_{k=0}^{\infty} \frac{1}{(2k)!}\left(-i\frac{\theta}{2}X\right)^{2k} + \sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\left(-i\frac{\theta}{2}X\right)^{2k+1}$$

$$\underbrace{\phantom{xxxxxxxxxxxx}}_{0,2,4,6,\ldots} \qquad \underbrace{\phantom{xxxxxxxxxxxx}}_{1,3,5,7,\ldots}$$

$$= \sum_{k=0}^{\infty} \frac{1}{(2k)!}\left(\frac{\theta}{2}\right)^{2k}(-i)^{2k}\,\mathbb{1} + \sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\left(\frac{\theta}{2}\right)^{2k+1}(-i)^{2k+1} X$$

$$i \cdot i = i^2 = -1$$

$(-i)^1 = -i \quad (k=0)$

$(-i)^3 = \underbrace{-i \cdot -i}_{-1} \cdot -i = i \quad (k=1)$

$(-i)^5 = -i \qquad\qquad (k=2)$

$\vdots$

$(-i)^{2k+1} = -i(-1)^k$

$(-i)^2 = -i \cdot -i = -1 \quad (k=1)$

$(-i)^4 = ((-i)^2)^2 = 1 \quad (k=2)$

$(-i)^6 = -1 \qquad\qquad (k=3)$

$\vdots$

$(-i)^{2k} = (-1)^k$

## Page 9

$$= \underbrace{\sum_{k=0}^{\infty} \frac{1}{(2k)!} \left(\frac{\theta}{2}\right)^{2k} (-1)^k}_{\cos(\frac{\theta}{2})} \mathbb{1} \;-\; i \underbrace{\sum_{k=0}^{\infty} \frac{1}{(2k+1)!} \left(\frac{\theta}{2}\right)^{2k+1} (-1)^k}_{\sin(\frac{\theta}{2})} X$$

$$= \cos\left(\tfrac{\theta}{2}\right) \mathbb{1} - i \sin\left(\tfrac{\theta}{2}\right) X$$

(✱) Similar argument to show $R_y(\theta) = e^{-i\frac{\theta}{2} Y} = \cos(\tfrac{\theta}{2}) \mathbb{1} - i \sin(\tfrac{\theta}{2}) Y$

$$R_z(\theta) = e^{-i\frac{\theta}{2} Z} = \cos(\tfrac{\theta}{2}) \mathbb{1} - i \sin(\tfrac{\theta}{2}) Z$$

- **Important properties of Unitaries.**

  - <u>Unitaries preserve norm</u>: For $U \in L(\mathbb{C}^d)$ unitary, $\ket{v} \in \mathbb{C}^d$ arbitrary,

  $$\ket{\tilde{v}} = U\ket{v} \;\rightarrow\; \| \ket{\tilde{v}} \|^2 = \braket{\tilde{v}|\tilde{v}} = \braket{v | \underbrace{U^\dagger U}_{=\mathbb{1}} | v} = \braket{v|v}$$

  $$\left( (M_1 M_2)^\dagger = M_2^\dagger M_1^\dagger \right)$$

  $$\bra{\tilde{v}} = (\ket{\tilde{v}})^\dagger = (U\ket{v})^\dagger = \bra{v} U^\dagger$$

  - <u>Unitaries preserve states</u>: let $\rho$ be a density operator representing a mixed quantum state. Then the transformed state is given by

  $$\tilde{\rho} = U \rho U^\dagger \;\rightarrow\; \text{This is still a density matrix!}$$

  Check: (1) $\tilde{\rho}^\dagger = (U \rho U^\dagger)^\dagger = (U^\dagger)^\dagger \rho^\dagger U^\dagger = U \rho U^\dagger$ ✓
  
  $\;\;\;\;\underbrace{\;\;\;}_{\tilde{\rho}} \quad \underbrace{\;\;\;}_{=U} \underbrace{\;\;\;}_{=\rho} \underbrace{\;\;\;}_{\tilde{\rho}}$

  $$\left( (M_1 M_2 M_3)^\dagger = M_3^\dagger M_2^\dagger M_1^\dagger \right)$$

  (2) $\text{Tr}[\tilde{\rho}] = \text{Tr}[U \rho U^\dagger] = \text{Tr}[U^\dagger U \rho] = \text{Tr}[\rho] = 1$ ✓

  $$\left( \text{(✱) Cyclicity of trace: } \text{Tr}[M_1 M_2 M_3] = \text{Tr}[M_2 M_3 M_1] = \text{Tr}[M_3 M_2 M_1] \right)$$

## Page 10

(3) For arbitrary $\ket{v} \in \mathbb{C}^d$, $\bra{v} \tilde{\rho} \ket{v} = \underbrace{\bra{v} U}_{\bra{\tilde{v}}} \rho \underbrace{U^\dagger \ket{v}}_{\ket{\tilde{v}}}$

$$= \bra{\tilde{v}} \rho \ket{\tilde{v}} \geq 0 \quad \text{b/c } \rho \geq 0 \text{ by assumption}$$

$\Rightarrow$ So $\tilde{\rho} \geq 0$ ✓

---

— **Product of unitaries is a unitary:** if $U_1, U_2$ are unitaries, then $U = U_1 U_2$ is also a unitary.

Check: $U^\dagger U = (U_1 U_2)^\dagger U_1 U_2 = U_2^\dagger \underbrace{U_1^\dagger U_1}_{= \mathbb{1}} U_2 = U_2^\dagger U_2 = \mathbb{1}$ ✓

$U U^\dagger = (U_1 U_2)(U_1 U_2)^\dagger = U_1 \underbrace{U_2 U_2^\dagger}_{= \mathbb{1}} U_1^\dagger = U_1 U_1^\dagger = \mathbb{1}$ ✓


# Lectures__superdense-coding.pdf

## Page 1

# ① Recap: Quantum teleportation

- A method to send arbitrary quantum information using entanglement and two bits of classical information.

[Diagram: Alice holds $\ket{\psi}_{A'}$ and one half of the entangled pair $\ket{\Phi^+}_{AB}$. She performs a Bell measurement on her two qubits, obtaining outcomes $x \in \{0,1\}$ and $z \in \{0,1\}$. These two classical bits are sent to Bob, who applies $X^x$ then $Z^z$ to his half of $\ket{\Phi^+}_{AB}$ to recover $\ket{\psi}_B$.]

- If $x=0$, do nothing; if $x=1$, apply $X$.
- If $z=0$, do nothing; if $z=1$, apply $Z$.

✱ Teleportation is **not** instantaneous / faster than light — it only works if Bob gets Alice's measurement outcomes → this takes time!

- The **Bell measurement** is a critical component.
  It is given by the POVM $\{\Phi^+, \Phi^-, \Psi^+, \Psi^-\}$, $\Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}$, $\Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}$,
  
  $$\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0} \pm \ket{1}\ket{1}), \qquad \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{1} \pm \ket{1}\ket{0}).$$

Circuit implementation:

[Circuit: two qubit lines. The top line goes through $H$ then a Pauli-$Z$ measurement. The bottom line is the target of a CNOT (control = top qubit) before the $H$, and is then measured in the $Z$ basis. The boxed region containing the two $Z$-measurements is labeled "Pauli-$Z$ measurement".]

$$\ket{0}\ket{0} \mapsto \ket{0}\ket{0}$$
$$\ket{0}\ket{1} \mapsto \ket{0}\ket{1}$$
$$\ket{1}\ket{0} \mapsto \ket{1}\ket{1}$$
$$\ket{1}\ket{1} \mapsto \ket{1}\ket{0}$$

**Proof:** Let $\rho_{AB}$ be the initial state.

Let $U = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$ be the CNOT gate, and $H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ the Hadamard gate.

$H\ket{0} = \ket{+}$
$H\ket{1} = \ket{-}$
$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$

## Page 2

[Circuit diagram: Input $\rho_{AB}$ on two qubits A (top) and B (bottom). A CNOT gate with A as control and B as target, then a Hadamard H on qubit A, then Pauli-Z measurement boxes (labeled X) on both qubits.]

$\rho_{AB} \mapsto U\rho_{AB}U^\dagger \mapsto (H\otimes \mathbb{1})U\rho_{AB}U^\dagger(H^\dagger \otimes \mathbb{1})$

↑ Pauli-Z measurement.   ↓ State just before measurement.

Now do a Pauli-Z measurement on each qubit.

The POVM is $\{|0,0\rangle\langle 0,0|, |0,1\rangle\langle 0,1|, |1,0\rangle\langle 1,0|, |1,1\rangle\langle 1,1|\}$.

Outcome probabilities:

$\Pr(z,x) = \mathrm{Tr}\big[|z,x\rangle\langle z,x|_{AB}\,(H\otimes\mathbb{1})\,U\rho_{AB}U^\dagger\,(H^\dagger\otimes\mathbb{1})\big]$

$\qquad \mathrm{Tr}\big[|z,x\rangle\langle z,x|\,\sigma\big]$

$\mathrm{Tr}[ABC] = \mathrm{Tr}[CAB] = \mathrm{Tr}[BCA]$

$= \mathrm{Tr}\big[(H^\dagger\otimes\mathbb{1})|z,x\rangle\langle z,x|_{AB}(H\otimes\mathbb{1})\,U\rho_{AB}U^\dagger\big]$  (cyclicity of trace)

$= \mathrm{Tr}\big[\underbrace{U^\dagger(H^\dagger\otimes\mathbb{1})|z,x\rangle\langle z,x|_{AB}(H\otimes\mathbb{1})U}_{M_{z,x}}\,\rho_{AB}\big]$  (cyclicity of trace again).

$U^\dagger = U$ (b/c CNOT is Hermitian)

$H^\dagger = H$ (b/c Hadamard is also Hermitian). $\Rightarrow M_{z,x} = U(H\otimes\mathbb{1})|z,x\rangle\langle z,x|(H\otimes\mathbb{1})U$

(1) $U(H\otimes\mathbb{1})|0,0\rangle = \mathrm{CNOT}|+,0\rangle = \mathrm{CNOT}\tfrac{1}{\sqrt{2}}(|0\rangle|0\rangle + |1\rangle|0\rangle)$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(\mathrm{CNOT}|0\rangle|0\rangle + \underbrace{\mathrm{CNOT}|1\rangle|0\rangle}_{=|1\rangle|1\rangle})$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(|0\rangle|0\rangle + |1\rangle|1\rangle)$

$\qquad\qquad = |\Phi^+\rangle$

$\Rightarrow M_{0,0} = \Phi^+$

$|+\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$

(2) $U(H\otimes\mathbb{1})|0,1\rangle = \mathrm{CNOT}|+,1\rangle = \mathrm{CNOT}\tfrac{1}{\sqrt{2}}(|0\rangle|1\rangle + |1\rangle|1\rangle)$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(\mathrm{CNOT}|0\rangle|1\rangle + \mathrm{CNOT}|1\rangle|1\rangle)$

## Page 3

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

## Page 4

$$\Rightarrow \Phi^+ = \ket{\Phi^+}\bra{\Phi^+} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \frac{1}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{2}} & 0 & 0 & \frac{1}{\sqrt{2}} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & 0 & 0 & \frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \frac{1}{2} & 0 & 0 & \frac{1}{2} \end{pmatrix}$$

$$\ket{\Phi^-} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{0} - \ket{1}\ket{1}\big) = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ 0 \\ -\frac{1}{\sqrt{2}} \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

$$\Rightarrow \Phi^- = \ket{\Phi^-}\bra{\Phi^-} = \begin{pmatrix} \frac{1}{2} & 0 & 0 & -\frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -\frac{1}{2} & 0 & 0 & \frac{1}{2} \end{pmatrix}$$

$$\ket{\Psi^+} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{1} + \ket{1}\ket{0}\big) = \begin{pmatrix} 0 \\ \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix} \Rightarrow \Psi^+ = \ket{\Psi^+}\bra{\Psi^+} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$$\ket{\Psi^-} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{1} - \ket{1}\ket{0}\big) = \begin{pmatrix} 0 \\ \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \\ 0 \end{pmatrix} \Rightarrow \Psi^- = \ket{\Psi^-}\bra{\Psi^-} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & -\frac{1}{2} & 0 \\ 0 & -\frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

Add up: $\Phi^+ + \Phi^- + \Psi^+ + \Psi^- = $

$$\begin{pmatrix} \frac{1}{2} & 0 & 0 & \frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \frac{1}{2} & 0 & 0 & \frac{1}{2} \end{pmatrix} + \begin{pmatrix} \frac{1}{2} & 0 & 0 & -\frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -\frac{1}{2} & 0 & 0 & \frac{1}{2} \end{pmatrix} + \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & -\frac{1}{2} & 0 \\ 0 & -\frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \blacksquare$$

## Page 5

## ② Superdense Coding

✱ **Teleportation**: using entanglement + classical information to transmit quantum information.

✱ We can also use entanglement to transmit classical information!

- **Superdense coding**: using entanglement + 1 qubit to transmit 2 classical bits.

[Diagram: Alice and Bob share entangled state $\ket{\Phi^+}_{AB}$. Alice's qubit (red line) goes through gates $X^x$ then $Z^z$ (boxed: "Encoding bits $z, x$ into one qubit."), with classical control inputs $x$ and $z$. The qubit is then sent to Bob, who performs a Bell Measurement on both qubits, obtaining outcome $(x, z)$.]

(1) • To encode $(0,0)$: $\underbrace{(Z^0 X^0 \otimes \mathbb{1})}_{=\mathbb{1}}\ket{\Phi^+}_{AB} = \ket{\Phi^+}_{AB}$  (Alice does nothing).
$\quad\;\;(z, x)$

- To encode $(0,1)$: $\underbrace{(Z^0 X^1 \otimes \mathbb{1})}_{=X}\ket{\Phi^+}_{AB} = (X \otimes \mathbb{1}) \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B)$

(Alice applies $X$ to her qubit.) 
$\qquad\qquad\qquad\qquad\quad = \tfrac{1}{\sqrt{2}}(X\ket{0}_A\ket{0}_B + X\ket{1}_A\ket{1}_B)$

$\qquad\qquad\qquad\qquad\quad = \tfrac{1}{\sqrt{2}}(\ket{1}_A\ket{0}_B + \ket{0}_A\ket{1}_B)$

$\qquad\qquad\qquad\qquad\quad = \ket{\Psi^+}_{AB}$

- To encode $(1,0)$: $\underbrace{(Z^1 X^0 \otimes \mathbb{1})}_{=Z}\ket{\Phi^+}_{AB} = (Z \otimes \mathbb{1}) \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B)$

## Page 6

(Alice applies $Z$ to her qubit.)

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$$= \tfrac{1}{\sqrt{2}}\left( Z\ket{0}_A \ket{0}_B + Z\ket{1}_A \ket{1}_B \right)$$

$$= \tfrac{1}{\sqrt{2}}\left( \ket{0}_A \ket{0}_B - \ket{1}_A \ket{1}_B \right)$$

$$= \ket{\Phi^-}_{AB}$$

- <u>To encode $(1,1)$</u>: $(Z^1 X^1 \otimes \mathbb{1})\ket{\Phi^+}_{AB} = (ZX \otimes \mathbb{1})\tfrac{1}{\sqrt{2}}\left( \ket{0}_A \ket{0}_B + \ket{1}_A \ket{1}_B \right)$

$$= ZX$$

$$= \tfrac{1}{\sqrt{2}}\left( ZX\ket{0}_A \ket{0}_B + ZX\ket{1}_A \ket{1}_B \right)$$

$$\quad\quad = Z\ket{1} = -\ket{1} \qquad = Z\ket{0} = \ket{0}$$

$$= \tfrac{1}{\sqrt{2}}\left( -\ket{1}_A \ket{0}_B + \ket{0}_A \ket{1}_B \right)$$

$$= \ket{\Psi^-}_{AB}.$$

⊛ <u style="color:red">Observation</u>: <span style="color:red">These encoded states are the same as the measurement operators of the Bell measurement!</span>

(2) After encoding, Alice sends her qubit to Bob.

(3) Then Bob does a Bell measurement on both qubits.

⊛ <u>Recall</u>: the outcome of the Bell measurement is two bits of information.
  Outcome $\Phi^+ \leftrightarrow (0,0)$
  Outcome $\Psi^+ \leftrightarrow (0,1)$
  Outcome $\Phi^- \leftrightarrow (1,0)$
  Outcome $\Psi^- \leftrightarrow (1,1)$

  Each one of these outcomes occurs with some probability, depending on the state: if the state being measured is $\rho$, then:

  $$\Pr[\Phi^+] = \mathrm{Tr}[\rho\, \Phi^+], \quad \Pr[\Phi^-] = \mathrm{Tr}[\rho\, \Phi^-], \quad \Pr[\Psi^+] = \mathrm{Tr}[\rho\, \Psi^+], \quad \Pr[\Psi^-] = \mathrm{Tr}[\rho\, \Psi^-]$$

## Page 7

⚛ The state encoded by Alice is

$$\ket{\Phi_{z,x}} = (Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}. \qquad ((z,x) \in \{0,1\}^2 \text{ are the bits she wants to send to Bob.})$$

$$\left.\begin{aligned}\ket{\Phi_{0,0}} &= \ket{\Phi^+} \\ \ket{\Phi_{0,1}} &= \ket{\Psi^+} \\ \ket{\Phi_{1,0}} &= \ket{\Phi^-} \\ \ket{\Phi_{1,1}} &= \ket{\Psi^-}\end{aligned}\right\}$ ⚛ Bob measures one of these states, but he does not know which one it is. He has to figure that out from the Bell measurement.

⚛ What is the probability that Bob retrieves the bits Alice sent?

We need to determine: $\Pr[\text{Bob gets outcome }(z',x'), \text{ given Alice encoded }(z,x)]$.

This is given by $\mathrm{Tr}\left[\Phi^{z',x'} \Phi^{z,x}\right]$ $\qquad \left(\Phi^{z,x} = \ket{\Phi^{z,x}}\bra{\Phi^{z,x}}.\right)$

$\uparrow \qquad \nwarrow$ Alice's encoded state.
Bob's
measurement

$$\delta_{x,x'} = \begin{cases} 0 & \text{if } x \neq x' \\ 1 & \text{if } x = x' \end{cases}$$

We will show that $\boxed{\mathrm{Tr}\left[\Phi^{z',x'} \Phi^{z,x}\right] = \delta_{z,z'}\,\delta_{x,x'}}$

<u>This means</u>: if Alice sends bits $z,x$, then Bob's measurement outcome is also $z,x$, with probability one $\Rightarrow$ he successfully gets Alice's bits.

<u>Proof</u>: $\mathrm{Tr}\left[\Phi^{z',x'}\Phi^{z,x}\right] = \mathrm{Tr}\Big[\underbrace{(Z^{z'}X^{x'}\otimes\mathbb{1})\ket{\Phi^+}}_{\ket{v_1}}\underbrace{\bra{\Phi^+}(X^{x'}Z^{z'}\otimes\mathbb{1})}_{\bra{v_1}}\underbrace{(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}}_{\ket{v_2}}\underbrace{\bra{\Phi^+}(X^x Z^z \otimes \mathbb{1})}_{\bra{v_2}}\Big]$

$\underbrace{\hphantom{xxxxxxxxxxxxxxxxxxxxx}}_{\Phi^{z',x'}} \quad \underbrace{\hphantom{xxxxxxxxxxxxxxxxxxxxx}}_{\Phi^{z,x}}$

$(M_1 \otimes \mathbb{1})(M_2 \otimes \mathbb{1})$
$= M_1 M_2 \otimes \mathbb{1}$

$= \mathrm{Tr}\big[\ket{v_1}\bra{v_1}\ket{v_2}\bra{v_2}\big] = \underbrace{\braket{v_1|v_2}}_{\text{scalar!}} \mathrm{Tr}\big[\ket{v_1}\bra{v_2}\big] = \braket{v_1|v_2}\underbrace{\braket{v_2|v_1}}_{=\overline{\braket{v_1|v_2}}}$

$\braket{v_1|v_2} = \bra{\Phi^+}(X^{x'}Z^{z'}\otimes\mathbb{1})(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+} = \bra{\Phi^+}(X^{x'}Z^{z'}Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}$

## Page 8

$$= \tfrac{1}{\sqrt{2}}\underbrace{\big(\bra{0}\bra{0}+\bra{1}\bra{1}\big)}_{\sum_{k=0}^{1}\bra{k}\bra{k}} \big(X^{x'}Z^{z'}Z^{z}X^{x}\otimes \mathbb{1}\big) \tfrac{1}{\sqrt{2}}\underbrace{\big(\ket{0}\ket{0}+\ket{1}\ket{1}\big)}_{\sum_{k'=0}^{1}\ket{k'}\ket{k'}}$$

$$= \tfrac{1}{2}\sum_{k,k'=0}^{1} \bra{k}\bra{k}\big(X^{x'}Z^{z'}Z^{z}X^{x}\otimes \mathbb{1}\big)\ket{k'}\ket{k'}$$

$$= \tfrac{1}{2}\sum_{k,k'=0}^{1} \bra{k}X^{x'}Z^{z'}Z^{z}X^{x}\ket{k'}\underbrace{\braket{k|k'}}_{=\delta_{k,k'}} \qquad \color{blue}{\bra{k}\bra{k}(M_1\otimes M_2)\ket{k'}\ket{k'}}$$
$$\color{blue}{= \bra{k}M_1\ket{k'}\bra{k}M_2\ket{k'}}$$

$$= \tfrac{1}{2}\sum_{k=0}^{1}\bra{k}X^{x'}Z^{z'}Z^{z}X^{x}\ket{k} \qquad \color{blue}{\sum_{k}\bra{k}M\ket{k}=\mathrm{Tr}(M)}$$

$$= \tfrac{1}{2}\mathrm{Tr}\!\left[X^{x'}Z^{z'}Z^{z}X^{x}\right] = \tfrac{1}{2}\mathrm{Tr}\!\left[X^{x}X^{x'}Z^{z'}Z^{z}\right] = \underline{\underline{\tfrac{1}{2}\mathrm{Tr}\!\left[X^{x\oplus x'}Z^{z'\oplus z}\right]}}.$$

$\color{blue}{X^{0}=\mathbb{1}}$
$\color{blue}{X^{1}=X}$

$\color{red}{\to x=0,\,x'=0 \;\Rightarrow\; X^{0}X^{0}=\mathbb{1}}$
$\color{red}{\;\;\;\; x=0,\,x'=1 \;\Rightarrow\; X^{0}X^{1}=X}$
$\color{red}{\;\;\;\; x=1,\,x'=0 \;\Rightarrow\; X^{1}X^{0}=X}$
$\color{red}{\;\;\;\; x=1,\,x'=1 \;\Rightarrow\; X^{1}X^{1}=X^{2}=\mathbb{1}}$

$\Rightarrow X^{x}X^{x'} = X^{\underline{\underline{x\oplus x'}}} \quad \oplus$

$\uparrow$ XOR!

$$\begin{pmatrix} 0\oplus 0 = 0 \\ 0\oplus 1 = 1 \\ 1\oplus 0 = 1 \\ 1\oplus 1 = 0 \end{pmatrix}$$

$\color{red}{\text{Same for } Z^{z'}Z^{z}:\; z'=0,\,z=0 \Rightarrow \mathbb{1}}$
$\color{red}{\;\;\;\; z'=0,\,z=1 \Rightarrow Z}$
$\color{red}{\;\;\;\; z'=1,\,z=0 \Rightarrow Z} \;\;\Rightarrow\; Z^{z'}Z^{z} = Z^{z'\oplus z}$
$\color{red}{\;\;\;\; z'=1,\,z=1 \Rightarrow \mathbb{1}}$

Now, we use the fact that $Z$ and $X$ are orthogonal:

$$Z=\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix},\quad X=\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix} \;\Rightarrow\; \mathrm{Tr}[X]=\mathrm{Tr}[Z]=0,\text{ and}$$

$$\mathrm{Tr}[ZX] = \mathrm{Tr}\!\left[\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}\right] = \mathrm{Tr}\!\left[\begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}\right] = 0.$$

## Page 9

Therefore, $\text{Tr}(Z^a X^b) = 2\, \delta_{a,0}\, \delta_{b,0}$. $\quad a, b \in \{0,1\}$

Check: $a=0, b=0 \Rightarrow \text{Tr}(\mathbb{1}) = 2$
$\phantom{Check:}\, a=0, b=1 \Rightarrow \text{Tr}(X) = 0$
$\phantom{Check:}\, a=1, b=0 \Rightarrow \text{Tr}(Z) = 0$
$\phantom{Check:}\, a=1, b=1 \Rightarrow \text{Tr}(ZX) = 0$.

Finally: $\braket{v_1 | v_2} = \frac{1}{2} \text{Tr}\bigl(X^{x \oplus x'} Z^{z' \oplus z}\bigr) = \delta_{x \oplus x', 0}\, \delta_{z' \oplus z, 0}$

[arrows above exponents labeling $a$ and $b$]

But $x \oplus x' = 0 \iff x = x'$ and $z' \oplus z = 0 \iff z' = z$

$\Rightarrow \delta_{x \oplus x', 0} = \delta_{x, x'}$ and $\delta_{z' \oplus z, 0} = \delta_{z', z}$.

So $\braket{v_1 | v_2} = \delta_{x, x'}\, \delta_{z, z'}$.

Similarly $\braket{v_2 | v_1} = \overline{\braket{v_1 | v_2}} = \delta_{x, x'}\, \delta_{z, z'}$.

So $\text{Tr}\bigl(E^{z', x'}\, E^{z, x}\bigr) = \delta_{x, x'}\, \delta_{z, z'}$. ∎

---

❋ <u>Recap</u>: Superdense coding allows Alice to send two bits to Bob using only one qubit — as long as the qubit is already entangled with Bob's qubit.

This worked b/c the 4 Bell states were used to encode the information and do the measurement — and b/c the Bell states are orthogonal, they are perfectly distinguishable.

❋ <u>Why is this interesting?</u>

With just a single (unentangled) qubit, we cannot successfully (w/ prob. 1) transmit more than one bit of information.

## Page 10

In dimension $d$, we can transmit w/ prob. 1 at most $\log_2(d)$ bits.

So $d=2 \implies \log_2(2) = 1$ bit.

With entanglement, the dimension effectively increases to $4 \to \log_2(4) = 2$.
$$(\text{b/c } 4 = 2^2).$$


# Lectures__teleportation.pdf

## Page 1

# ① Recap of the course so far.

## (a) What is a qubit?

[Diagram on left: A bit, shown as two points labeled 0 (top) and 1 (bottom) connected by a line.]

**Bit**
0 or 1;
or probabilistic mixture

[Diagram on right: Bloch sphere with $\ket{0}$ at top (z-axis), $\ket{1}$ at bottom, $\ket{+}$ and $\ket{-}$ on x-axis, $\ket{+i}$ and $\ket{-i}$ on y-axis.]

$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$$
$$\alpha, \beta \in \mathbb{C},$$
$$|\alpha|^2 + |\beta|^2 = 1$$

$$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$$
$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

---

- The state of a qubit is given by a <u>density matrix/operator</u>:

  (1) $\rho^\dagger = \rho$ (Hermitian) → **Conjugate transpose**

  (2) $\rho \geq 0$ (positive semi-definite ⇔ non-negative eigenvalues)

  (3) $\text{Tr}[\rho] = 1$ → **Sum of the diagonal elements.**

- Points on the surface of the Bloch sphere are given by state vectors; they are called <u>pure states</u>: $\rho = \ket{\psi}\bra{\psi}$, $\ket{\psi} \in \mathbb{C}^2$, $\|\ket{\psi}\|_2 = 1$.
  
  [arrow pointing to $\ket{\psi}$:] **State vector.**

- Points inside the Bloch sphere are <u>mixed states</u>:

$$\rho = \sum_{k=1}^{r} g_k \underbrace{\ket{\psi_k}\bra{\psi_k}}_{\text{pure states}}, \quad g_k \in [0,1], \quad \sum_{k=1}^{r} g_k = 1.$$

- <u>Quantum gates</u> are used to describe operations/computations on qubits. They are defined by <u>unitary matrices</u>: $U \in L(\mathbb{C}^d)$, $U^\dagger U = U U^\dagger = \mathbb{1}$.

## Page 2

(b) How to extract information from a qubit? <u>Measurements</u>!

- A <u>measurement</u> (aka "positive operator-valued measure") is defined by $\rightarrow$ (POVM) a set of operators $\{M_x\}_{x \in \mathcal{X}}$ (some finite set $\mathcal{X}$), such that:

  (1) $M_x \geq 0 \;\; \forall x \in \mathcal{X}$. ($M_x \in L(\mathbb{C}^d) \to d \times d$ matrix for arbitrary dimension $d$.)

  (2) $\sum_{x \in \mathcal{X}} M_x = \mathbb{1}$

- For any state $\rho$, the outcome probabilities are given by
  $$\Pr(x) = \mathrm{Tr}[M_x \rho] \;\; \forall x \in \mathcal{X}.$$

- Examples of measurements:

  (1) Pauli-$Z$ / computational basis: $\{\underbrace{\ket{0}\bra{0}}_{M_0}, \underbrace{\ket{1}\bra{1}}_{M_1}\}$ &nbsp;&nbsp; $\ket{0}\bra{0} + \ket{1}\bra{1} = \mathbb{1}$. &nbsp;&nbsp; $Z\ket{0} = \ket{0}$, $Z\ket{1} = -\ket{1}$

  (2) Pauli-$X$: $\{\ket{+}\bra{+}, \ket{-}\bra{-}\}$, $\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$, $X\ket{\pm} = \pm\ket{\pm}$

  (3) Any basis: for any unitary $U$, $\{U\ket{0}\bra{0}U^\dagger, U\ket{1}\bra{1}U^\dagger\}$.

  $$\left(\underline{\text{Check}}: U\ket{0}\bra{0}U^\dagger + U\ket{1}\bra{1}U^\dagger = U\underbrace{(\ket{0}\bra{0} + \ket{1}\bra{1})}_{=\mathbb{1}}U^\dagger = UU^\dagger = \mathbb{1} \;\checkmark\right)$$

(c) <u>Entanglement</u>: One of the key distinguishing characteristics of quantum vs. classical.

- A state vector $\ket{\psi}_{AB}$ is entangled if it <u>cannot</u> be written as $\ket{\psi}_{AB} = \ket{\psi}_A \otimes \ket{\psi}_B$.
  $$\downarrow \text{ product state}$$

- Every state vector $\ket{\psi}_{AB}$ has a <u>Schmidt decomposition</u>:

  (1) $\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{e_k}_A \otimes \ket{f_k}_B$

  $\ket{\Phi^+} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0} + \ket{1}\ket{1})$.

  (2) $S_k$: Schmidt coefficients $(S_k > 0)$

  $\{\ket{e_k}_A\}_{k=1}^{r}$ and $\{\ket{f_k}_B\}_{k=1}^{r}$ are orthonormal vectors.
  $$\braket{e_k | e_{k'}} = \delta_{k,k'} = \begin{cases} 0 & \text{if } k \neq k' \\ 1 & \text{if } k = k' \end{cases}$$

## Page 3

$r$: Schmidt rank.

(3) $\ket{\psi}_{AB}$ is entangled if and only if $\underline{r > 1}$.

- Entanglement of mixed states is more complicated!

  A mixed state (density operator) $\rho_{AB}$ is entangled it $\underline{\text{cannot}}$ be written as

  $$\rho_{AB} = \sum_{x \in \mathcal{X}} \underbrace{p(x)}_{\text{probabilities}} \tau_A^{(x)} \otimes \omega_B^{(x)} \rightarrow \text{This is } \underline{\text{Separable}}.$$

- ✱ If A & B are qubits, then $\rho_{AB}$ is separable if and only if $\rho_{AB}^{T_B} \geq 0$. $\quad$ <span style="color:red">↙ partial transpose</span>

## ② Teleportation

- A method to transfer the state of a qubit from Alice to Bob using entanglement and classical communication only.

- <u>Given</u>: (1) State vector that Alice wants to send to Bob.
  (2) Shared entangled state b/w Alice and Bob.

- <u>Goal</u>: Transfer the state of qubit $A'$ to Bob's qubit.

[Teleportation circuit diagram: Alice has qubit $\ket{\psi}_{A'}$ which together with her half of $\ket{\Phi^+}_{AB}$ goes into a Bell Measurement, producing classical bits $x \in \{0,1\}$ and $z \in \{0,1\}$. Bob's qubit (the other half of $\ket{\Phi^+}_{AB}$) has $X^x$ then $Z^z$ applied conditioned on the classical bits, yielding $\ket{\psi}_B$.]

- If $x=0$, do nothing. If $x=1$, apply $X$.
- If $z=0$, do nothing. If $z=1$, apply $Z$.

## Page 4

(a) Key ingredient: the two-qubit __Bell measurement__

- POVM is $\{\Phi^+, \Phi^-, \Psi^+, \Psi^-\}$, $\quad \Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}$, $\Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}$.

$$\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{0} \pm \ket{1}\ket{1}\right)$$
$$\ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{1} \pm \ket{1}\ket{0}\right)$$

- Circuit description of the measurement:

[Circuit diagram: Two wires labeled $A'$ (top, source) and $A$ (bottom, target). A CNOT gate with control on $A'$ and target on $A$, followed by a Hadamard gate $H$ on the $A'$ wire, then $z$-basis measurements ($\ket{x}$ boxes) on both wires.]

Hadamard gate: $H\ket{0} = \ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$
$H\ket{1} = \ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0}-\ket{1})$

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$z$-basis measurement.

CNOT gate (source $\to$ target):
$$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

$\text{CNOT}\ket{0,0} = \ket{0,0}$
$\text{CNOT}\ket{0,1} = \ket{0,1}$
$\text{CNOT}\ket{1,0} = \ket{1,1}$
$\text{CNOT}\ket{1,1} = \ket{1,0}$

---

(b) __Protocol analysis__

$\ket{\psi}_{A'} = \alpha \ket{0}_{A'} + \beta \ket{1}_{A'} \quad \to$ State Alice wants to send to Bob. $\quad (|\alpha|^2 + |\beta|^2 = 1)$

$\ket{\Phi^+}_{AB} = \tfrac{1}{\sqrt{2}}\left(\ket{0,0}_{AB} + \ket{1,1}_{AB}\right) \to$ Shared entanglement.

(1) Joint initial state: 
$$\ket{\psi}_{A'} \otimes \ket{\Phi^+}_{AB} = \left(\alpha\ket{0}_{A'} + \beta\ket{1}_{A'}\right) \otimes \tfrac{1}{\sqrt{2}}\left(\ket{0,0}_{AB} + \ket{1,1}_{AB}\right)$$
$$= \tfrac{1}{\sqrt{2}}\Big(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB} + \beta\ket{1,0,0}_{A'AB} + \beta\ket{1,1,1}_{A'AB}\Big)$$

## Page 5

(2) $\text{CNOT}_{A'A}$: $\frac{1}{\sqrt{2}}(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB}$
$\qquad\qquad\qquad +\beta\underset{\color{red}1,1}{\ket{1,0,0}}_{A'AB} + \beta\underset{\color{red}1,0}{\ket{1,1,1}}_{A'AB})$

$\downarrow$

$\frac{1}{\sqrt{2}}(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB}$
$\qquad +\beta\ket{1,1,0}_{A'AB} + \beta\ket{1,0,1}_{A'AB})$

(3) Hadamard on $A'$: $\frac{1}{\sqrt{2}}(\alpha\underset{\color{red}\ket{+}}{\ket{0,0,0}}_{A'AB} + \alpha\underset{\color{red}\ket{+}}{\ket{0,1,1}}_{A'AB}$
$\qquad\qquad\qquad\qquad +\beta\underset{\color{red}\ket{-}}{\ket{1,1,0}}_{A'AB} + \beta\underset{\color{red}\ket{-}}{\ket{1,0,1}}_{A'AB})$

$\color{blue}H\ket{0} = \ket{+}$
$\color{blue}H\ket{1} = \ket{-}$

$\downarrow$

$\frac{1}{\sqrt{2}}(\alpha\ket{+,0,0}_{A'AB} + \alpha\ket{+,1,1}_{A'AB}$
$\qquad +\beta\ket{-,1,0}_{A'AB} + \beta\ket{-,0,1}_{A'AB})$

(4) Measure $A'A$ in the $Z$-basis / computational basis / $\{\ket{0},\ket{1}\}$ basis:

- **Four outcomes**: $00, 01, 10, 11 = (z,x)$

$\frac{1}{\sqrt{2}}(\alpha\ket{+,0,0}_{A'AB} + \alpha\ket{+,1,1}_{A'AB} + \beta\ket{-,1,0}_{A'AB} + \beta\ket{-,0,1}_{A'AB})$

$= \frac{1}{\sqrt{2}}\Big(\alpha\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})_{A'}\ket{0,0}_{AB} + \alpha\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})_{A'}\ket{1,1}_{AB}$
$\qquad + \beta\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})_{A'}\ket{1,0}_{AB} + \beta\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})_{A'}\ket{0,1}_{AB}\Big)$

$\downarrow$

$\ket{\phi}_{A'AB} = \Big(\ket{0,0}_{A'A}\frac{1}{2}(\alpha\ket{0}+\beta\ket{1})_B + \ket{0,1}_{A'A}\frac{1}{2}(\alpha\ket{1}+\beta\ket{0})_B$
$\qquad\qquad + \ket{1,0}_{A'A}\frac{1}{2}(\alpha\ket{0}-\beta\ket{1})_B + \ket{1,1}_{A'A}\frac{1}{2}(\alpha\ket{1}-\beta\ket{0})_B\Big)$

## Page 6

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

## Page 7

⇒ State of Bob conditioned on Alice's outcome is $X\ket{\psi}$.

- <u>Outcome (1,0)</u>: $\Pr(1,0) = \text{Tr}\Big[ \big(\bra{1,0}_{A'A} \otimes \mathbb{I}_B\big) \ket{\phi}\bra{\phi}_{A'AB} \big(\ket{1,0}_{A'A} \otimes \mathbb{I}_B\big) \Big]$

$$\ket{\phi}_{A'AB} = \tfrac{1}{2}\Big( \ket{0,0}_{A'A}\big(\alpha\ket{0}+\beta\ket{1}\big)_B + \ket{0,1}_{A'A}\big(\alpha\ket{1}+\beta\ket{0}\big)_B$$
$$+ \ket{1,0}_{A'A}\big(\alpha\ket{0}-\beta\ket{1}\big)_B + \ket{1,1}_{A'A}\big(\alpha\ket{1}-\beta\ket{0}\big)_B \Big)$$

$\ket{\psi} = \alpha\ket{0}+\beta\ket{1}$
$Z\ket{\psi} = \alpha Z\ket{0} + \beta Z\ket{1}$, $\quad Z\ket{1}=-\ket{1}$
$\quad\quad = \alpha\ket{0} - \beta\ket{1}$.

$\big(\bra{1,0}_{A'A} \otimes \mathbb{I}_B\big)\ket{\phi}_{A'AB} = \tfrac{1}{2}\big(\alpha\ket{0}-\beta\ket{1}\big) = \tfrac{1}{2} Z\ket{\psi}$ → Pauli $Z$

$$\text{Tr}\big[\tfrac{1}{2} Z\ket{\psi}\bra{\psi} Z \tfrac{1}{2}\big] = \tfrac{1}{4}\text{Tr}\big[Z\ket{\psi}\bra{\psi} Z\big] = \tfrac{1}{4}\text{Tr}\big[\ket{\psi}\bra{\psi}\big] = \tfrac{1}{4}.$$

$Z^2 = \mathbb{I}$

$\Rightarrow \Pr(1,0) = \tfrac{1}{4}$

⇒ State of Bob conditioned on Alice's outcome is $Z\ket{\psi}$.

- <u>Outcome (1,1)</u>: $\Pr(1,1) = \text{Tr}\Big[ \big(\bra{1,1}_{A'A} \otimes \mathbb{I}_B\big) \ket{\phi}\bra{\phi}_{A'AB} \big(\ket{1,1}_{A'A} \otimes \mathbb{I}_B\big) \Big]$

$$\ket{\phi}_{A'AB} = \tfrac{1}{2}\Big( \ket{0,0}_{A'A}\big(\alpha\ket{0}+\beta\ket{1}\big)_B + \ket{0,1}_{A'A}\big(\alpha\ket{1}+\beta\ket{0}\big)_B$$
$$+ \ket{1,0}_{A'A}\big(\alpha\ket{0}-\beta\ket{1}\big)_B + \ket{1,1}_{A'A}\big(\alpha\ket{1}-\beta\ket{0}\big)_B \Big)$$

$\big(\bra{1,1}_{A'A} \otimes \mathbb{I}_B\big)\ket{\phi}_{A'AB} = \tfrac{1}{2}\big(\alpha\ket{1}-\beta\ket{0}\big) = \tfrac{1}{2} XZ\ket{\psi}_B$

$$\text{Tr}\big[\tfrac{1}{2} XZ\ket{\psi}\bra{\psi} ZX \tfrac{1}{2}\big] = \tfrac{1}{4}\text{Tr}\big[ZX\ket{\psi}\bra{\psi} XZ\big] = \tfrac{1}{4}\text{Tr}\big[\ket{\psi}\bra{\psi}\big] = \tfrac{1}{4}.$$

$\Rightarrow \Pr(1,1) = \tfrac{1}{4}$

$Z^2 = \mathbb{I},\ X^2 = \mathbb{I}$

⇒ State of Bob conditioned on Alice's outcome is $XZ\ket{\psi}$.

## Page 8

**Summary:**
- $\Pr(0,0) = \tfrac{1}{4} \to$ State $\ket{\psi}$ for Bob.
- $\Pr(0,1) = \tfrac{1}{4} \to$ State $X\ket{\psi}$ for Bob.
- $\Pr(1,0) = \tfrac{1}{4} \to$ State $Z\ket{\psi}$ for Bob.
- $\Pr(1,1) = \tfrac{1}{4} \to$ State $XZ\ket{\psi}$ for Bob.

(5) After the measurement, Alice communicates the outcomes to Bob.

(6) Depending on the outcome, Bob applies a __correction__:

[column labels in red: $z\ \ x$]

$0,0 \to$ No correction

$0,1 \to$ Apply Pauli-$X$  $\quad X(X\ket{\psi}) = \underbrace{X^2}_{=\mathbb{1}}\ket{\psi} = \ket{\psi}$

$1,0 \to$ Apply Pauli-$Z$  $\quad Z(Z\ket{\psi}) = \underbrace{Z^2}_{=\mathbb{1}}\ket{\psi} = \ket{\psi}$

$1,1 \to$ Apply Pauli-$X$, then Pauli-$Z$

Then Bob recovers Alice's state!

⊛ Teleportation is __not__ instantaneous / faster than light — it only works if Bob gets Alice's measurement outcomes ⤳ this takes time!

⊛ The teleported state can also be a mixed state.


# Lectures__universal-gate-sets-noise-in-quantum-computing.pdf

## Page 1

# ① Universal Gate Sets

- We want to use a set of elementary gates to execute <u>arbitrary</u> unitaries on $n$ qubits.

[Diagram: a quantum circuit on 4 wires showing several single-qubit boxes and two-qubit boxes spanning adjacent wires arranged in columns, illustrating decomposition of an arbitrary unitary into elementary gates.]

- <u>Two versions</u>: 
  - Exact  ↓ Requires (uncountably) infinite # of gates in the set.
  - Approximate. → we can allow for some error/deviation in the implementation. → Relevant when we want the set to be finite.

(a) <u>Exact case</u>: CNOT + all single-qubit gates are universal! ( ✱ This set <u>is not finite</u>.)

> **Lemma 4.1.** Every unitary $2\times 2$ matrix can be expressed as
> $$\begin{pmatrix} e^{i\delta} & 0 \\ 0 & e^{i\delta} \end{pmatrix} \begin{pmatrix} e^{i\alpha/2} & 0 \\ 0 & e^{-i\alpha/2} \end{pmatrix} \begin{pmatrix} \cos\theta/2 & \sin\theta/2 \\ -\sin\theta/2 & \cos\theta/2 \end{pmatrix}$$
> $$\times \begin{pmatrix} e^{i\beta/2} & 0 \\ 0 & e^{-i\beta/2} \end{pmatrix},$$
> where $\delta, \alpha, \theta,$ and $\beta$ are real valued. Moreover, any special unitary $2\times 2$ matrix (i.e., with unity determinant) can be expressed as
> $$\begin{pmatrix} e^{i\alpha/2} & 0 \\ 0 & e^{-i\alpha/2} \end{pmatrix} \begin{pmatrix} \cos\theta/2 & \sin\theta/2 \\ -\sin\theta/2 & \cos\theta/2 \end{pmatrix} \begin{pmatrix} e^{i\beta/2} & 0 \\ 0 & e^{-i\beta/2} \end{pmatrix}.$$

✱ Recall the rotation gates!

$$R_x(\theta) = e^{-i\frac{\theta}{2}X} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)X$$

$$R_y(\theta) = e^{-i\frac{\theta}{2}Y} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Y$$

$$R_z(\theta) = e^{-i\frac{\theta}{2}Z} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Z$$

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

<u>Observe</u>: 
$$R_y(\theta) = \begin{pmatrix} \cos(\tfrac{\theta}{2}) & 0 \\ 0 & \cos(\tfrac{\theta}{2}) \end{pmatrix} - i\begin{pmatrix} 0 & -i\sin(\tfrac{\theta}{2}) \\ i\sin(\tfrac{\theta}{2}) & 0 \end{pmatrix} = \begin{pmatrix} \cos(\tfrac{\theta}{2}) & -\sin(\tfrac{\theta}{2}) \\ \sin(\tfrac{\theta}{2}) & \cos(\tfrac{\theta}{2}) \end{pmatrix}$$

## Page 2

$$R_z(\theta) = \begin{pmatrix} \cos(\frac{\theta}{2}) & 0 \\ 0 & \cos(\frac{\theta}{2}) \end{pmatrix} - i \begin{pmatrix} \sin(\frac{\theta}{2}) & 0 \\ 0 & -\sin(\frac{\theta}{2}) \end{pmatrix} \qquad e^{i\varphi} = \cos(\varphi) + i\sin(\varphi)$$

$$= \begin{pmatrix} \cos(\frac{\theta}{2}) - i\sin(\frac{\theta}{2}) & 0 \\ 0 & \cos(\frac{\theta}{2}) + i\sin(\frac{\theta}{2}) \end{pmatrix}$$

$$= \begin{pmatrix} e^{-i\frac{\theta}{2}} & 0 \\ 0 & e^{i\frac{\theta}{2}} \end{pmatrix}$$

★ So every single-qubit gate can be decomposed into rotation gates:

$$U = R_z(\alpha)\, R_y(\theta)\, R_z(\beta), \quad \text{for appropriate angles } \alpha, \beta, \theta.$$

> *Lemma 5.1.* For a unitary $2\times 2$ matrix $W$, a $\wedge_1(W)$ gate can be simulated by a network of the form
>
> [Circuit diagram: controlled-$W$ gate equals a circuit with control line passing through CNOTs interleaved with single-qubit gates $A$, $B$, $C$ on the target line: $-A-\oplus-B-\oplus-C-$, with controls on the top wire.]
>
> where $A$, $B$, and $C \in SU(2)$ if and only if $W \in SU(2)$.

(b) <u>Approximate case</u>: Arises when the # of gates in the set is finite

(B/c the set of unitaries is uncountably infinite, while the set of sequences of gates from a finite set will be countably infinite.)

★ <mark>Theorem:</mark> <u>Clifford gates</u> + <u>one single-qubit non-Clifford gate</u> is universal!

$$\hookrightarrow T \text{ gate!} \quad T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$$

– Recall Pauli operators on $n$ qubits: $\mathcal{P}_n = \{I, X, Y, Z\}^{\otimes n} \to P = I \otimes X \otimes Y \otimes X \otimes Z$
$$\hookrightarrow 4^n$$

$\to$ Let $\mathcal{P}_n^* = \mathcal{P}_n \setminus \{I^{\otimes n}\}$
$\hookrightarrow$ exclude the identity gate.

## Page 3

- Define the $n$-qubit Clifford group as

$$\mathcal{C}_n := \left\{ U : P \in \pm \mathcal{P}_n^* \Rightarrow UPU^\dagger \in \pm \mathcal{P}_n^* \right\} / U(1) \quad \rightarrow \text{mod out global phase}$$

$\rightarrow$ Transforms Paulis to Paulis (up to sign)

$H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \rightarrow HXH = Z, \; HZH = X$

⊛ <u>Theorem</u>: $\mathcal{C}_n = \langle H_i, S_i, \text{CNOT}_{i,j} \;:\; i,j \in \{1,2,\ldots,n\} \rangle / U(1)$

  ⊛ $H, S, \text{CNOT}$ are <u>generators</u> of the Clifford group!

  ⊛ (Take all possible products of $H, S, \text{CNOT}$, and ignore global phase.)

⊛ <mark><u>Corollary</u>:</mark> $\{H, S, \text{CNOT}, T\}$ is universal $\rightarrow \{H, \text{CNOT}, T\}$ is universal. $(S = T^2)$.

---

② <u>Noise and Errors in Quantum Computing</u>

⊛ In quantum computing, we care about <u>precise control</u> of qubits — but they inevitably <u>interact with their environment</u>! This evolution is unitary.

(<u>ideal case</u>).

[Circuit: $\ket{0} \longrightarrow \boxed{G} \longrightarrow G\ket{0}$]

  $\underbrace{\phantom{\boxed{G}}}_{\text{Unitary gate.}}$

(<u>reality</u>) $\rightarrow$ gate noise.

[Circuit:
- System: $\ket{0} \longrightarrow$ [box $\mathcal{N}$] $\longrightarrow \mathcal{N}(\ket{0}\bra{0}) \rightarrow$ "quantum channel"
- Environment: $\ket{0} \longrightarrow$ [into box, traced out]
]

## Page 4

(reality) → decoherence
↓
Qubit state drifts over time.

[Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$, $\ket{-}$, $\ket{+i}$, $\ket{-i}$ on equator. A purple arrow shows the state drifting from near $\ket{0}$ toward the interior, with another arrow pointing to the center labeled:]

Origin: maximally-mixed state $\frac{\mathbb{1}}{2}$.

(a) Any <u>unwanted gate</u> applied to the qubit can be thought of as noise.

<u>Example</u>: Bit flip → Pauli-X gate, $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

$X\ket{0} = \ket{1}$, $X\ket{1} = \ket{0}$ → <span style="color:red">opposite ends of the Bloch sphere!</span>

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1} \to X\ket{\psi} = \alpha\ket{1} + \beta\ket{0}$

→ measurement probabilities get flipped!

[Bloch sphere with $\ket{0}$ and $\ket{1}$ marked in red, indicating the X gate maps between these antipodal points.]

<u>Example</u>: Rotations → $R_x(\theta), R_y(\theta), R_z(\theta)$

✱ Recall teleportation! The state before Bob's correction is precisely a noisy version of the true state Alice wants to send.

(b) <u>Different gates</u> can also be applied <u>randomly</u> to the state

- <u>Example</u>: Apply $X$ with probability $\alpha$, do nothing with probability $1-\alpha$.

## Page 5

If the qubit state is given by a density operator $\rho$, then after the noise it is

$$(1-\alpha)\rho + \alpha X\rho X \quad \rightarrow \text{"Bit-flip channel"}$$

- $(1-\alpha)\rho$: Do nothing with probability $1-\alpha$
- $\alpha X\rho X$: Apply the X gate with probability $\alpha$.

[Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom; vertical blue line connecting them with red dots indicating the mixed state along the z-axis]

$$\ket{0}\bra{0} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \mapsto (1-\alpha)\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \alpha \underbrace{X\ket{0}\bra{0}X}_{=\ket{1}\bra{1}} = \begin{pmatrix} 1-\alpha & 0 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & \alpha \end{pmatrix}$$

$$= \begin{pmatrix} 1-\alpha & 0 \\ 0 & \alpha \end{pmatrix}$$

$$= (1-\alpha)\ket{0}\bra{0} + \alpha\ket{1}\bra{1}.$$

✸ If we measured the initial (noiseless) state, then we would get the outcome "0" with probability 1 → after noise, the state becomes mixed: with probability $1-\alpha$ we get "0" and with probability $\alpha$ we get "1".

✸ So $\alpha$ quantifies the amount of noise! 
- $\alpha = 0 \Rightarrow$ no noise
- $\alpha = \frac{1}{2} \Rightarrow \boxed{\frac{1}{2}\ket{0}\bra{0} + \frac{1}{2}\ket{1}\bra{1}}$

✸ For a general density matrix: recall the form $\rho = \frac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)$

$r_x, r_y, r_z$ → Coordinates in the Bloch sphere.

[Bloch sphere with axes labeled: z-axis up with $\ket{0}$ at top and $\ket{1}$ at bottom; y-axis to the right with $\ket{+i}$, and $\ket{-i}$ on the opposite side; x-axis coming out toward viewer with $\ket{+}$ in front and $\ket{-}$ behind]

How do those coordinates transform after the noise?

$$(r_x, r_y, r_z) \mapsto (r_x', r_y', r_z') \;?$$

## Page 6

$$(1-\alpha)\rho + \alpha X\rho X = \underbrace{(1-\alpha)\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)}_{\rho} + \alpha \underbrace{X\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)X}_{\rho}$$

$$\underline{XY = -YX}$$
$$\underline{XZ = -ZX}$$

$$= \tfrac{1}{2}(X\mathbb{1}X + r_x \underbrace{XXX}_{=X^2 \cdot X = X} + r_y \underbrace{XYX}_{=-X^2 Y = -Y} + r_z \underbrace{XZX}_{=-X^2 Z = -Z})$$
$$\underbrace{= X^2}_{=\mathbb{1}}$$

$$= (1-\alpha)\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z) + \alpha\tfrac{1}{2}(\mathbb{1} + r_x X - r_y Y - r_z Z)$$

$$= \tfrac{1}{2}\Big((1-\alpha+\alpha)\mathbb{1} + ((1-\alpha)r_x + \alpha r_x)X$$
$$\qquad + ((1-\alpha)r_y - \alpha r_y)Y$$
$$\qquad + ((1-\alpha)r_z - \alpha r_z)Z\Big)$$

$$= \tfrac{1}{2}(\mathbb{1} + \underbrace{r_x}_{r'_x = r_x} X + \underbrace{(1-2\alpha)r_y}_{r'_y} Y + \underbrace{(1-2\alpha)r_z}_{r'_z} Z).$$

<u>Check</u>: If $\rho = \ket{0}\bra{0}$, then $r_x = 0$, $r_y = 0$, $r_z = 1 \xrightarrow{\alpha=1} r'_x = 0,\; r'_y = 0,\; r'_z = -1$ ✓

- <u>Example</u>: Phase-flip / dephasing channel

$$\rho \mapsto \underbrace{(1-\alpha)\rho}_{\text{Do nothing with probability } 1-\alpha} + \underbrace{\alpha Z\rho Z}_{\text{Apply Pauli-}Z\text{ with probability }\alpha}.$$

(✱) Now how do the coordinates transform?

$$\rho = \tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z) \longmapsto \rho' = \tfrac{1}{2}(\mathbb{1} + r'_x X + r'_y Y + r'_z Z)$$

$$r'_x = (1-2\alpha) r_x,\quad r'_y = (1-2\alpha) r_y,\quad r'_z = r_z.$$

## Page 7

✻ For this channel, it is useful to see the transformation in the standard basis.

$$\rho = \begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} \mapsto (1-\alpha)\rho + \alpha Z\rho Z = (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

where $a \in [0,1]$, $c \in \mathbb{C}$.

[arrow indicating the last product equals:]
$$= \begin{pmatrix} a & c \\ -\bar{c} & -(1-a) \end{pmatrix}$$

$$= (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} a & c \\ -\bar{c} & -(1-a) \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$$= \begin{pmatrix} a & -c \\ -\bar{c} & 1-a \end{pmatrix}$$

$$= (1-\alpha)\begin{pmatrix} a & c \\ \bar{c} & 1-a \end{pmatrix} + \alpha \begin{pmatrix} a & -c \\ -\bar{c} & 1-a \end{pmatrix} = \begin{pmatrix} a & (1-2\alpha)c \\ (1-2\alpha)\bar{c} & 1-a \end{pmatrix}$$

$\alpha = 0 \Rightarrow$ no noise
$\alpha = \tfrac{1}{2} \Rightarrow$ max. noise

✻ Off-diagonal terms are suppressed!

✻ For $\alpha = \tfrac{1}{2}$, the off-diagonal terms vanish! → superposition is gone!

- **Example:** Depolarizing channel: $\rho \mapsto (1-\alpha)\rho + \tfrac{\alpha}{3}X\rho X + \tfrac{\alpha}{3}Y\rho Y + \tfrac{\alpha}{3}Z\rho Z$

$$\begin{pmatrix} \text{With prob. } 1-\alpha, \text{ do nothing;} \\ \text{with prob. } \alpha, \text{ apply a Pauli} \\ \text{operator uniformly at random.} \end{pmatrix}$$

✻ For $\alpha = 3/4$: $\tfrac{1}{4}\rho + \tfrac{1}{4}X\rho X + \tfrac{1}{4}Y\rho Y + \tfrac{1}{4}Z\rho Z = \mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2}$  (Assignment!)

[underbrace under $\mathrm{Tr}[\rho]$: $=1$]

✻ Using this, we can write the depolarizing channel in an alternative way:

## Page 8

$$\tfrac{1}{4}\rho + \tfrac{1}{4} X\rho X + \tfrac{1}{4} Y\rho Y + \tfrac{1}{4} Z\rho Z = \mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2} \implies X\rho X + Y\rho Y + Z\rho Z = 4\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2} - \rho$$

$$\implies \rho \mapsto (1-\alpha)\rho + \tfrac{\alpha}{3}\left(4\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2} - \rho\right)$$

$$= (1-\alpha)\rho + \tfrac{4\alpha}{3}\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2} - \tfrac{\alpha}{3}\rho$$

$$= \left(1 - \alpha - \tfrac{\alpha}{3}\right)\rho + \tfrac{4\alpha}{3}\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2}$$

$$= \underbrace{\left(1 - \tfrac{4\alpha}{3}\right)\rho}_{\text{"all"}} + \underbrace{\tfrac{4\alpha}{3}\mathrm{Tr}[\rho]\tfrac{\mathbb{1}}{2}}_{\text{"nothing"}} \quad \left(\text{"all or nothing"}\right).$$

"all" (state perfectly intact)

"nothing" (all information about state is lost)

$$\beta = 1 - \tfrac{4\alpha}{3}, \quad \rho \mapsto \beta \cdot \rho + (1-\beta)\tfrac{\mathbb{1}}{2}$$


# Past-Exams__Test1.pdf

## Page 1

1. Consider the complex number $z = 1 + 2i$.
   - (a) Find $\text{Re}(z)$.
   - (b) Find $\text{Im}(z)$.
   - (c) Plot $z$ as a point in the complex plane.
   - (d) Write $z$ in polar form, $z = re^{i\theta}$.
   - (e) Find $\bar{z}$.
   - (f) Find $|z|$.
   - (g) Find $|z|^2$.

a) $\text{Re}(z) = 1$

b) $\text{Im}(z) = 2$

c) [Plot in complex plane: Im axis vertical with marks at $i, 2i, 3i$; Re axis horizontal with marks at 1, 2, 3. An arrow from origin to the point $(1, 2)$ with angle $\theta$ marked from the Re axis.]

d) $r = \sqrt{1^2 + 2^2} = \sqrt{5} \qquad \theta = \tan^{-1}\left(\frac{y}{x}\right) = 63.43^\circ$

   $z = \sqrt{5}\, e^{i(63.43)} \qquad \sqrt{5}\, e^{i\tan^{-1}(2)}$ would be better.

e) $\bar{z} = \overline{1 + 2i} = 1 - 2i$

f) $|z| = \sqrt{1^2 + 2^2} = \sqrt{5}$

g) $|z|^2 = \sqrt{5}^2 = 5$

2

## Page 2

2. (a) State the definition of a $d \times d$ Hermitian matrix, $d \in \{2, 3, \dots\}$.
   (b) Write down the most general form of a $2 \times 2$ Hermitian matrix.

a) $H = \ket{v}\bra{v} + \ket{v}\bra{v}$

A Hermitian matrix is made up of ket $\cdot$ Bra

$\ket{0}\bra{0}, \quad \ket{1}\bra{0}, \quad \ket{0}\bra{1}, \quad \ket{1}\bra{1}$

\* $2 \times 2$ Hermitian Matrix

(-2)

When doing ket $\cdot$ Bra instead of bra $\cdot$ ket;

$2 \times 2$ case: $\begin{pmatrix} a+bi \\ c+di \end{pmatrix} \begin{pmatrix} a-bi & c-di \end{pmatrix}$

(-2)

$\underbrace{2 \times 1 \quad 1 \times 2}_{2 \times 2}$

3

## Page 3

3. Draw a Bloch sphere and label the following locations.

   (a) Where a qubit is $\ket{0}$ and $\ket{1}$.
   (b) Where a qubit is $\ket{+}$ and $\ket{-}$.
   (c) Where a qubit is $\ket{+i}$ and $\ket{-i}$.

[Hand-drawn Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ on front, $\ket{-}$ on back-upper, $\ket{+i}$ on right, $\ket{-i}$ on left. Arrows label the pairs as (a), (b), (c).]

[Grader's note in blue ink:] All are generally in the same area. ✓

4

## Page 4

4. Let $X$ be a random variable, taking values in $\{1, 2, 3, \ldots\}$, whose probability mass function is given as

$$p_X(x) = \begin{cases} \alpha x^2 & x \in \{1, 2, 3, 4\}, \\ 0 & \text{otherwise}. \end{cases}$$

(a) What is the value of $\alpha$?
(b) Compute $\Pr[X = 4]$.
(c) Compute $\Pr[X \leq 2]$.

PMF = 1

a) $P_X(x) = \sum_{x=1}^{4} \alpha x^2 = 1$

$\quad = \alpha(1^2 + 2^2 + 3^2 + 4^2) = 1$

$\quad = \alpha(30) = 1$

$\quad \alpha = \dfrac{1}{30}$

b) $\Pr[X = 4] = P(4) = \alpha(4^2)$

$\quad = \dfrac{1}{30} \cdot 16 = \dfrac{16}{30} = \dfrac{8}{15}$

c) $\Pr[X \leq 2] = P(1) + P(2)$

$\quad = \dfrac{1}{30}(1)^2 + \dfrac{1}{30}(2)^2 = \dfrac{3}{30} = \dfrac{1}{10}$ [illegible: maybe "(-2)= $\tfrac{1}{6}$"]

5

## Page 5

5. (a) State the three-part mathematical definition of a density operator, and explain each part of the definition. **(−4) Not attempted.**
   (b) State the mathematical definition of the purity of a quantum state.
   (c) Write down an example of a pure quantum state for one qubit.

a) Density operator $\braket{V_1 | V_2} = \sum_{k', k = 0}^{d-1} \bar{a}_1 b_2 \, \delta_{kk'}$

   $\longrightarrow \begin{cases} 0 & \text{if } k \neq k' \\ 1 & \text{if } k = k' \end{cases}$

   Orthonormal:

   Orthogonal: $\braket{V_1 | V_2} = 0$

   Normality: $\braket{V_1 | V_1} = 1$
   $\braket{V_2 | V_2} = 1$

   (−2)

c) $\frac{1}{\sqrt{2}} \big[ \ket{0} + \ket{1} \big]$ ✓

## Page 6

6. Let $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$ be arbitrary vectors, and let $M \in L(\mathbb{C}^d)$ be an arbitrary linear operator (i.e., $d \times d$ matrix). Using the definition of the trace of a linear operator, prove the following identities.
   (a) $\text{Tr}\big[\ket{v_1}\bra{v_2}\big] = \braket{v_2|v_1}$
   (b) $\text{Tr}\big[M\ket{v_1}\bra{v_2}\big] = \braket{v_2|M|v_1}$

---

a) $\text{Tr}\big[\ket{V_1}\bra{V_2}\big] = \braket{V_2|V_1}$

$$\bra{e_1} \sum_{k=0}^{d-1} \ket{V_1}\bra{V_2} \ket{e_2} = \braket{V_2|V_1} \underbrace{\sum_{k=0}^{d-1} \braket{e_1|e_2}}_{\text{Identity}} \quad \textcolor{red}{\circled{-2}} \;\textcolor{red}{\times}$$

$$= \braket{V_2|V_1}$$

<div style="color:blue">(-2) Need to show for $d \times d$ matrix. $e_1, e_2$ are not sufficient.</div>

b) $\text{Tr}\big[M\ket{V_1}\bra{V_2}\big] = \braket{V_2|M|V_1}$

$$\bra{e_1} \sum_{k=0}^{d-1} M\ket{V_1}\braket{V_2|e_2}$$

$$\braket{V_2|M|V_1} \cdot \underbrace{\sum_{k=0}^{d-1} \braket{e_1|e_2}}_{\text{Identity}} \quad \textcolor{red}{\times}$$

$$= \braket{V_2|M|V_1}$$

7


# Past-Exams__Test2.pdf

## Page 1

1. (a) Determine whether the following $2 \times 2$ matrices are unitary matrices.

   i. $M = \begin{pmatrix} \frac{3}{5} & \frac{4i}{5} \\ \frac{4i}{5} & \frac{3}{5} \end{pmatrix}$  $\quad C_1 = \begin{pmatrix} 3/5 \\ \frac{4i}{5} \end{pmatrix}$  $\quad C_2 = \begin{pmatrix} \frac{4i}{5} \\ 3/5 \end{pmatrix}$
   
   [marked: $\boxed{-2}$]
   
   $\rightarrow U^T U = I$
   
   $\rightarrow \begin{pmatrix} 3/5 & -\frac{4i}{5} \end{pmatrix} \begin{pmatrix} \frac{4i}{5} \\ 3/5 \end{pmatrix} = \frac{12i}{25} + \text{[...]}$

   ii. $M = \begin{pmatrix} \frac{2+i}{3} & \frac{2i}{3} \\ \frac{2i}{3} & \frac{2-i}{3} \end{pmatrix}$  $\quad C_1 = \begin{pmatrix} \frac{2+i}{3} \\ \frac{2i}{3} \end{pmatrix}$  $\quad C_2 = \begin{pmatrix} \frac{2i}{3} \\ \frac{2-i}{3} \end{pmatrix}$
   
   [marked: $\boxed{-2}$]
   
   $\rightarrow \begin{pmatrix} \frac{2-i}{3} & -\frac{2i}{3} \end{pmatrix} \begin{pmatrix} \frac{2i}{3} \\ \frac{2-i}{3} \end{pmatrix} = \begin{pmatrix} \frac{2-i}{3} \end{pmatrix}\begin{pmatrix} \frac{2i}{3} \end{pmatrix}$

   (b) Calculate the partial trace $\mathrm{Tr}_B[M_{AB}]$ of the following two-qubit matrices.

$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$

   i. $M_{AB} = \begin{pmatrix} \frac{1}{2}-\frac{1}{3}i & \frac{2}{3}+\frac{3}{4}i & -\frac{5}{7} & \frac{1}{2}i \\ -\frac{4}{3} & \frac{7}{5}-\frac{2}{5}i & \frac{1}{9}+\frac{2}{3}i & 0 \\ \frac{1}{8} & \frac{4}{5}i & -\frac{2}{11} & \frac{6}{7}+\frac{3}{8}i \\ \frac{2}{9}i & \frac{1}{6} & -\frac{1}{7}i & \frac{3}{2}-\frac{1}{6}i \end{pmatrix}$
   
   [marked: $\boxed{-2}$]
   
   $\mathrm{Tr}_B(M_{AB}) = \begin{pmatrix} a+d & 0 \\ 0 & a+d \end{pmatrix}$

   ii. $M_{AB} = \begin{pmatrix} \frac{3}{5} & \frac{1}{2}-\frac{1}{4}i & 0 & \frac{1}{3}i \\ \frac{1}{2}+\frac{1}{4}i & \frac{2}{3} & \frac{4}{7}i & 0 \\ 0 & -\frac{4}{7}i & 1 & -\frac{2}{9}+\frac{1}{2}i \\ -\frac{1}{3}i & 0 & -\frac{2}{9}-\frac{1}{2}i & \frac{4}{9} \end{pmatrix}$
   
   [marked: $\boxed{-1}$]
   
   $\mathrm{Tr}_B(M_{a3}) = \begin{pmatrix} \frac{12}{10} & -\frac{8}{15}i \\ & \\ & 0 \end{pmatrix}$

$\mathrm{Tr}_B[M_{AB}] = \begin{pmatrix} \frac{16}{5} & 0 \\ 0 & \frac{13}{9} \end{pmatrix}$

TOTAL: $\boxed{1-7}$

2

## Page 2

TOTAL: $\boxed{-10}$

2. Let $X, Y, Z$ denote the Pauli operators and let $\mathbb{1}_2$ denote the $2 \times 2$ identity matrix. Prove the following identities.

   (a) $\frac{1}{4}(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X - Y \otimes Y + Z \otimes Z) = \ket{\Phi^+}\bra{\Phi^+}$.   $\boxed{-10}$

   (b) $\frac{1}{2}(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X + Y \otimes Y + Z \otimes Z) = \mathbb{F}$.

[Annotation: "Matrix" with checkmark]

$$\frac{1}{4}\left(I_2 \otimes I_2 + X \otimes X - Y \otimes Y + Z \otimes Z\right) = \ket{\phi^+}\bra{\phi^+}$$

$$I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \quad r_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad r_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad r_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$r_x = 2\,\mathrm{Re}(\rho)$

$r_y = -2\,\mathrm{Im}(\rho)$

$r_z = a - b$

$\frac{1}{4}\left(r_x^2 + r_y^2 + r_z^2\right) = 1$

$\frac{1}{4}\left(2^2 + (-1)^2 + 2^2\right) = 1$

$\frac{1}{4}\begin{pmatrix} 9 \end{pmatrix} \neq 1$

$\ket{\phi^+} = \frac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1}) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix}$

$\bra{\phi^+} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 0 & 0 & 1 \end{pmatrix}$

$\ket{\phi^+}\bra{\phi^+} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 0 & 0 & 1 \end{pmatrix}$

[annotations: $4 \times 1$, $1 \times 4$]

$= \frac{1}{\sqrt{2}}\begin{pmatrix} 1+1 & 0 \\ 0 & 1+1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} \sqrt{2} & 0 \\ 0 & \sqrt{2} \end{pmatrix}$

$\frac{1}{2}\Big($

$\mathbb{F} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$

3

## Page 3

**TOTAL: [40]**

3. (a) Given any orthonormal basis $\{\ket{e_k}\}_{k=1}^d$ for $\mathbb{C}^d$, prove that $\mathbb{1}_d = \sum_{k=1}^d \ket{e_k}\bra{e_k}$.

   (b) Let $\{\ket{e_k}\}_{k=1}^d$ and $\{\ket{f_k}\}_{k=1}^d$ be two orthonormal bases for $\mathbb{C}^d$. Prove that $U = \sum_{k=1}^d \ket{e_k}\bra{f_k}$ is a unitary operator.

[-10]

a) orthogonal: $\braket{V_1 | V_2} = 0$

   normal: $\braket{V_1 | V_1} = 1$ OR $\braket{V_2 | V_2} = 1$

   $\braket{0|1} = \begin{pmatrix} 1 & 0 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = 0$

   $\braket{1|1} = \begin{pmatrix} 0 & 1 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = 1$

   $I_d = \sum_{k=1}^d \ket{e_k}\bra{e_k}$

   $I^2 = \bra{e_k} \sum_{k=1}^d \ket{e_k}$

   $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} =$

b) $U^\dagger U = I$

   $U^\dagger = \sum_{k=1}^d \overline{f_k}\ket{e_k}$ \qquad $U = \sum_{k=1}^d \ket{e_k}\bra{f_k}$

   $\sum_{k=1}^d \sum_{k=1}^d \overline{f_k}\ket{f_k} \, \bra{e_k}\ket{e_k} = 1 \cdot I = I$
   
   $\qquad\qquad\qquad\downarrow \qquad\qquad \downarrow$
   $\qquad\qquad\quad = I \qquad\quad = 1$

4

## Page 4

**TOTAL: -10**

4. Let $M_B \in L(\mathbb{C}^{d_B})$, $N_B \in L(\mathbb{C}^{d_B})$, and $P_A \in L(\mathbb{C}^{d_A})$ be arbitrary linear operators. Prove the following facts about the partial trace.

   (a) $\text{Tr}_A[P_A \otimes M_B] = \text{Tr}[P_A] M_B$.   **(-10)**
   (b) $\text{Tr}_B[P_A \otimes M_B] = \text{Tr}[M_B] P_A$.
   (c) $\text{Tr}_A[(\mathbb{1}_A \otimes M_B) H_{AB} (\mathbb{1}_A \otimes N_B)] = M_B \text{Tr}_A[H_{AB}] N_B$.

Let $M_3 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$, $N_3 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$, $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

a) $\text{Tr}_{(A)}[P_A \otimes M_B] = \text{Tr}[P_A] M_B$

$$\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \\ 0 \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \\ 1 \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \end{pmatrix}$$

$\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$

[remainder of page blank / illegible faint marks]

5

## Page 5

TOTAL: [-2]

5. (a) Two qubits are in the state given by the vector

$$\frac{i}{\sqrt{10}}\ket{0,0} + \frac{1-2i}{\sqrt{10}}\ket{0,1} + \frac{e^{i\pi/100}}{\sqrt{10}}\ket{1,0} + \frac{\sqrt{3}}{\sqrt{10}}\ket{1,1}.$$

If we measure the qubits in the two-qubit Z-basis $\{\ket{0,0}, \ket{0,1}, \ket{1,0}, \ket{1,1}\}$, what are the possible measurement outcomes and their associated probabilities? What are the possible measurement outcomes and their associated probabilities if instead we measure in the two-qubit X-basis $\{\ket{+,+}, \ket{+,-}, \ket{-,+}, \ket{-,-}\}$?

(b) Consider the following two state vectors:

$$\ket{v_1} = \frac{\sqrt{3}}{2}\ket{0} + \frac{i}{2}\ket{1}, \quad \ket{v_2} = \frac{i}{2}\ket{0} + \frac{\sqrt{3}}{2}\ket{1}$$

i. Prove that $\ket{v_1}$ and $\ket{v_2}$ are orthonormal, and thus that they define a measurement.

ii. Consider a qubit in the state given by

$$\ket{u} = \frac{1}{2}\ket{0} - \frac{\sqrt{3}}{2}\ket{1}.$$

If we measure the state given by $\ket{u}$ with respect to the measurement defined by $\{\ket{v_1}\bra{v_1}, \ket{v_2}\bra{v_2}\}$, then what are the possible outcomes and their associated probabilities?

---

a) $\quad a\ket{0,0} + b\ket{0,1} + c\ket{1,0} + d\ket{1,1}$

$P_A = |a|^2 = \left|\frac{i}{\sqrt{10}}\right|^2 = \boxed{\frac{1}{10}}$

$P_B = |b|^2 = \left|\frac{(1-2i)}{\sqrt{10}}\right|^2 = \frac{1^2}{10} + \frac{-2i^2}{10} = \frac{1}{10} + \frac{4}{10} = \boxed{\frac{5}{10}}$

$P_C = |c|^2 = \left|\frac{e^{i\pi/100}}{\sqrt{10}}\right|^2 = \frac{10}{10} - \frac{9}{10} = \boxed{\frac{1}{10}}$

$P_D = |d|^2 = \left|\frac{\sqrt{3}}{\sqrt{10}}\right|^2 = \boxed{\frac{3}{10}}$

If X-basis → have to factor in $\frac{1}{\sqrt{2}}$ \quad Need more [-2]

b) Orthonormal → orthogonal: $\braket{v_1|v_2} = 0$ \quad i) first orthogonal → $\begin{pmatrix} \frac{\sqrt{3}}{2} & -\frac{i}{2} \end{pmatrix} \begin{pmatrix} \frac{i}{2} \\ \frac{\sqrt{3}}{2} \end{pmatrix}$

Normal: $\braket{v_1|v_1} = 1$
$\braket{v_2|v_2} = 1$ \qquad $= 0$

ii) $\ket{u} = a\ket{0} + b\ket{1}$ \qquad Normal → $\|\ket{v_1}\| = \sqrt{\left(\frac{\sqrt{3}}{2}\right)^2 + \left(\frac{i}{2}\right)^2} = \sqrt{\frac{3}{4} + \frac{1}{4}} = 1$

$P_a = \left|\frac{1}{2}\right|^2 = \frac{1}{4}$ \quad [-2]

$P_b = \left|-\frac{\sqrt{3}}{2}\right|^2 = \frac{3}{4}$ \qquad $\|\ket{v_2}\| = \sqrt{\left(\frac{i}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2} = \sqrt{\frac{1}{4} + \frac{3}{4}} = 1$

6

## Page 6

TOTAL: $\boxed{-10}$

6. Consider the bipartite state $\rho_{AB} = \frac{1}{2}(\ket{0,1}\bra{0,1}_{AB} + \ket{1,0}\bra{1,0}_{AB})$ of Alice (A) and Bob (B).

   (a) Suppose Alice and Bob both measure in the $\{\ket{0}, \ket{1}\}$ basis.
   
   i. Prove that their outcomes are *anti-correlated*, i.e., $\Pr[0,0] = \Pr[1,1] = 0$ and $\Pr[0,1] = \Pr[1,0] = \frac{1}{2}$.
   
   ii. Calculate the post-measurement states of Bob's qubit conditioned on Alice's two outcomes, and demonstrate that Bob always gets the opposite outcome as Alice.
   
   (b) Now suppose that Alice and Bob both measure in the $\{\ket{+}, \ket{-}\}$ basis.
   
   i. Calculate the probabilities of the possible outcomes: $\Pr[+,+], \Pr[+,-], \Pr[-,+], \Pr[-,-]$.
   
   ii. Prove that their measurement outcomes are now completely uncorrelated: regardless of what outcome Alice gets, Bob's outcomes are completely random.

---

a) i) 
$$\frac{1}{2}\ket{0}\left(\ket{1}\bra{1}\right) = 0 \qquad \frac{1}{2}\ket{0}\left(\ket{0}\bra{1}\right) = \frac{1}{2}$$

$$\frac{1}{2}\ket{1}\left(\ket{0}\bra{0}\right) = 0 \qquad \frac{1}{2}\ket{1}\left(\ket{1}\bra{0}\right) = \frac{1}{2}$$

ii) [circled: $-10$]

b)

## Page 7

**TOTAL: -10**

7. Consider the bipartite quantum state $\ket{\Psi^-}\bra{\Psi^-}_{AB}$ of Alice and Bob. In this problem, we show that Alice and Bob's measurement outcomes are always anti-correlated when they measure in the same basis, regardless of the chosen basis.

   (a) If Alice and Bob both measure in the $\{\ket{0}, \ket{1}\}$ basis, what is the distribution of outcomes? Justify that their outcomes are *anti-correlated*: whenever Alice gets $0/1$, Bob gets $1/0$.

   (b) If instead Alice and Bob measure in the $\{\ket{+}, \ket{-}\}$ basis, then show that their outcomes are still anti-correlated: whenever Alice gets $+/-$, Bob gets $-/+$.

   (c) Let $U$ be an arbitrary $2 \times 2$ unitary matrix. Prove that $(U \otimes U)\ket{\Psi^-}\bra{\Psi^-}(U \otimes U)^\dagger = \ket{\Psi^-}\bra{\Psi^-}$.

   (d) Let $U$ be an arbitrary $2 \times 2$ unitary matrix. Prove that the vectors $U^\dagger\ket{0}$ and $U^\dagger\ket{1}$ define a measurement.

   (e) Using the result from (c), prove that if Alice and Bob both measure with respect to $\{U^\dagger\ket{0}, U^\dagger\ket{1}\}$, with $U$ being an arbitrary $2 \times 2$ unitary matrix, then their measurement outcomes are anti-correlated. Thus, regardless of the basis choice, their measurement outcomes are anti-correlated.

---

a) $\ket{\Psi^-} = \dfrac{1}{\sqrt{2}}\big(\ket{0,1} - \ket{1,0}\big)_A \;=\; \dfrac{1}{\sqrt{2}}\begin{pmatrix} 0 & -c \\ -c & 0 \end{pmatrix}$

$\bra{\Psi^-} = \dfrac{1}{\sqrt{2}}\big(\ket{0,1} + \ket{1,0}\big)_B \;=\; \dfrac{1}{\sqrt{2}}\begin{pmatrix} 0 & c \\ c & 0 \end{pmatrix}$

b)

$\boxed{-10}$

c) $U^\dagger U$

## Page 8

TOTAL: $\boxed{-10}$

8. Consider the following two-qubit density operator $\rho_{AB}$ of Alice and Bob:

$$\rho_{AB} = (1-p)|\Phi^+\rangle\langle\Phi^+|_{AB} + \frac{p}{3}\left(|\Phi^-\rangle\langle\Phi^-|_{AB} + |\Psi^+\rangle\langle\Psi^+|_{AB} + |\Psi^-\rangle\langle\Psi^-|_{AB}\right),$$

where $p \in [0,1]$. Suppose Alice and Bob both measure their qubits with respect to the Pauli-$z$ basis; i.e., the POVM is $\{|0\rangle\langle 0|, |1\rangle\langle 1|\}$. What is the probability that they obtain the same measurement outcome?

$$\rho_{AB} = (1-p)|\Phi^+\rangle\langle\Phi^+|_{AB} + \frac{p}{3}\left[|\Phi^-\rangle\langle\Phi^-|_{AB} + |\Psi^+\rangle\langle\Psi^+|_{AB} + |\Psi^-\rangle\langle\Psi^-|_{AB}\right]$$

[under-brace under first term:] $= 6$

[under-brace under bracketed terms:] $= 1 + 1 = 2$

$$P_{AB} = 2 \cdot \frac{p}{3} = \boxed{\frac{2p}{3}}$$

$\boxed{-10}$


# Past-Exams__Test3.pdf

## Page 1

1. Consider the following three-dimensional vector $\ket{v} \in \mathbb{C}^3$, written with respect to the standard basis $\{\ket{0}, \ket{1}, \ket{2}\}$:

$$\ket{v} = \begin{pmatrix} 5-i \\ 6+3i \\ 7-4i \end{pmatrix}, \quad \rightarrow \quad \ket{0} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \ket{2} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \quad (1)$$

$$\ket{1} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$$

(a) Write the vector $\ket{v}$ in the abstract form $\ket{v} = a\ket{0} + b\ket{1} + c\ket{2}$, with the appropriate values of $a$, $b$, and $c$.

(b) Is the vector normalized? Say why or why not. If not normalized, then normalize it.

---

a) $\ket{v} = (5-i)\ket{0} + (6+3i)\ket{1} + (7-4i)\ket{2}$

b) normalized?

$(5-i)\ket{0} \overset{?}{=} \left| \sqrt{5^2 - i^2} \right| = \sqrt{25+1} = \sqrt{26}$

$(6+3i)\ket{1} = \left| \sqrt{6^2 + (3i)^2} \right| = \sqrt{36 - 9} = \sqrt{25} = 5$

$(7-4i)\ket{2} = \left| \sqrt{7^2 - (4i)^2} \right| = \sqrt{49+16} = \sqrt{65}$

Not normal $\rightarrow$

normalized vector?

2

## Page 2

2. (a) Calculate both $\text{Tr}_A[M_{AB}]$ and $\text{Tr}_B[M_{AB}]$ for the following two-qubit matrix:

$$M_{AB} = \begin{pmatrix} 0 & 5+3i & 1-2i & 2+i \\ -3+2i & 1 & -i & 1+i \\ 2 & -2i & 3+2i & 0 \\ 1 & 5i & -3+2i & 1 \end{pmatrix} \tag{2}$$

(b) Let $\Phi^-_{AB} = \ket{\Phi^-}\bra{\Phi^-}_{AB}$. Prove that $\text{Tr}_B[\Phi^-_{AB}] = \frac{1}{2}\mathbb{1}_A$ and $\text{Tr}_A[\Phi^-_{AB}] = \frac{1}{2}\mathbb{1}_B$.

(c) Consider the three-qubit state vector $\ket{\psi_1}_{ABC} = \frac{1}{\sqrt{2}}(\ket{0,0,0}_{ABC} + \ket{1,1,1}_{ABC})$. Calculate $\text{Tr}_A[\ket{\psi_1}\bra{\psi_1}_{ABC}]$.

---

a) $\text{Tr}_A[M_{AB}] = \begin{pmatrix} \boxed{0} & \boxed{5+3i} & 1-2i & 2+i \\ -3+2i & \boxed{1} & -i & 1+i \\ 2 & -2i & \boxed{3+2i} & \boxed{0} \\ 1 & 5i & -3+2i & \boxed{1} \end{pmatrix} = \begin{pmatrix} 0+3+2i & 5+3i+0 \\ -3+2i + (-3+2i) & 1+1 \end{pmatrix}$

$$\text{Tr}_A[M_{AB}] = \begin{pmatrix} 3+2i & 5+3i \\ -6+4i & 2 \end{pmatrix}$$

$\text{Tr}_B[M_{AB}] = \begin{pmatrix} 0+1 & (1-2i)+(1+i) \\ 2+5i & (3+2i)+1 \end{pmatrix} = \begin{pmatrix} 1 & 2-i \\ 2+5i & 4+2i \end{pmatrix}$

b) $\Phi^- = \frac{1}{\sqrt{2}}(\ket{00} - \ket{11})$

$\ket{\Phi^-}\bra{\Phi^-}_{AB} = \frac{1}{2}(\ket{00} - \ket{11})^2$  → ↗ $(\ket{00}-\ket{11})(\ket{00}-\ket{11})$

$\frac{1}{2}\big[\ket{00}\ket{00} - \ket{00}\ket{11} - \ket{11}\ket{00} + \ket{11}\ket{11}\big]$ ✗

$\text{Tr}_B[\Phi^-_{AB}] = (\quad)_A \,\text{Tr}[\quad]$

c)

3

## Page 3

(+10)

3. (a) State the mathematical definition of a quantum measurement, also known as a "positive operator-valued measure" (POVM).

   (b) Write down an example of a POVM, with justification.

a)  M

4

## Page 4

[−10 circled at top of page]

4. Consider the bipartite quantum state $\ket{\Psi^-}\bra{\Psi^-}_{AB}$ of Alice and Bob.

   (a) If Alice and Bob both measure in the $\{\ket{0}, \ket{1}\}$ basis, what is the distribution of outcomes? Justify that their outcomes are *anti-correlated*: whenever Alice gets $0/1$, Bob gets $1/0$.

   (b) If instead Alice and Bob measure in the $\{\ket{+}, \ket{-}\}$ basis, then show that their outcomes are still anti-correlated: whenever Alice gets $+/-$, Bob gets $-/+$.

$$\ket{\Psi} = \frac{1}{\sqrt{2}}\left(\ket{0,1} - \ket{1,0}\right) \qquad \{\ket{0}, \ket{1}\} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

$$\bra{\Psi} = \frac{1}{\sqrt{2}}\left(\bra{0,1} - \bra{0,1}\right)$$

$$\ket{\Psi}\bra{\Psi}_{AB} = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ \end{pmatrix}$$

[matrix appears incomplete / cut off]

5

## Page 5

[+10]

5. Consider the following two-qubit density operator $\rho_{AB}$ of Alice and Bob:

$$\rho_{AB} = (1-p)\ket{\Phi^+}\bra{\Phi^+}_{AB} + \frac{p}{3}\left(\ket{\Phi^-}\bra{\Phi^-}_{AB} + \ket{\Psi^+}\bra{\Psi^+}_{AB} + \ket{\Psi^-}\bra{\Psi^-}_{AB}\right),$$

where $p \in [0,1]$. Suppose Alice and Bob both measure their qubits with respect to the Pauli-$Z$ basis; i.e., the POVM is $\{\ket{0}\bra{0}, \ket{1}\bra{1}\}$. What is the probability that they obtain the same measurement outcome?

6

## Page 6

[−10]

6. (a) State the definition of a separable state and an entangled state.
   (b) State the definition of the Schmidt decomposition of a bipartite state vector $\ket{\psi}_{AB}$.
   (c) Under what condition(s), based on the Schmidt decomposition, is $\ket{\psi}_{AB}$ entangled?
   (d) Based on the Schmidt decomposition, determine (with justification) whether or not the following state vectors are entangled.
   
   i. $\frac{1}{\sqrt{3}}\ket{0}\ket{+} + \sqrt{\frac{2}{3}}\ket{1}\ket{-}$.
   
   ii. $\frac{1}{4}(3\ket{0,0} - \sqrt{3}\ket{0,1} + \sqrt{3}\ket{1,0} - \ket{1,1})$.

a) Seperable →

7


# Past-Exams__Test4.pdf

## Page 1

1. Does $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ represent a valid quantum gate? State why or why not. What is $U\ket{0}$ and $U\ket{1}$?

Valid: $U^\dagger U = I$

$$U^\dagger = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$$

$$U^\dagger U = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1+1 & i-i \\ -i+i & 1+1 \end{pmatrix}$$

$$= \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$$

Yes, it's a valid quantum gate.

$$U\ket{0} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix} \checkmark$$

[dimensions noted: $2\times 2$, $2\times 1$]

$$U\ket{1} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} i \\ 1 \end{pmatrix}$$

2

## Page 2

2. Draw the quantum circuit for the quantum teleportation protocol. State the definition of every gate and/or measurement you draw in the circuit.

[Hand-drawn quantum circuit with two horizontal wires:
- Top wire: passes through an H (Hadamard) gate, then through a measurement box (labeled with an "X"-like symbol indicating measurement)
- Bottom wire: connected to the top wire by a vertical line at a control point (controlled-Swap), then passes through an H (Hadamard) gate, then through a measurement box
- Arrows label the gates: "Hadamard" pointing to the first H gate, "a measurement" pointing to the first measurement box, "controlled-Swap" pointing to the vertical connection, "Hadamard" pointing to the second H gate]

−10

3

## Page 3

3. Consider the following two state vectors, $\ket{v_1} = \frac{\sqrt{3}}{2}\ket{0} + \frac{i}{2}\ket{1}$ and $\ket{v_2} = \frac{i}{2}\ket{0} + \frac{\sqrt{3}}{2}\ket{1}$.

   (a) Prove that $\ket{v_1}$ and $\ket{v_2}$ are orthonormal.
   (b) Show that $\ket{v_1}\bra{v_1} + \ket{v_2}\bra{v_2} = \mathbb{1}$.
   (c) Consider a qubit in the state given by $\ket{u} = \frac{1}{2}\ket{0} - \frac{\sqrt{3}}{2}\ket{1}$. If we measure this state with respect to the measurement $\{\ket{v_1}\bra{v_1}, \ket{v_2}\bra{v_2}\}$, then what are the possible outcomes and their associated probabilities?

---

orthonormal = orthogonal & normal

a) $\braket{v_1|v_2} = \left| \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{3}}{2} \braket{0|1} + \frac{i}{2} \cdot \frac{i}{2} \braket{1|0} \right| = \frac{3}{4} + \frac{i^2}{4} = 1\;?$

[marked $-5$ in red]

$\braket{v_1|v_1} = \left| \left(\frac{\sqrt{3}}{2}\right)^2 + \left(\frac{i}{2}\right)^2 \right| = \frac{3}{4} + \frac{1}{4} = \frac{4}{4} = 1$

$\braket{v_2|v_2} = \left| \left(\frac{i}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2 \right| = \frac{1}{4} + \frac{3}{4} = \frac{4}{4} = 1$

b) $\ket{v_1}\bra{v_1} = \begin{pmatrix} \frac{\sqrt{3}}{2} \\ \frac{i}{2} \end{pmatrix} \begin{pmatrix} \frac{\sqrt{3}}{2} & -\frac{i}{2} \end{pmatrix} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix}$

[marked $-3$ in blue circle, ✓]

$\ket{v_2}\bra{v_2} = \begin{pmatrix} \frac{i}{2} \\ \frac{\sqrt{3}}{2} \end{pmatrix} \begin{pmatrix} -\frac{i}{2} & \frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix}$

$\ket{v_1}\bra{v_1} + \ket{v_2}\bra{v_2} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix} + \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$

c) $\ket{v_1}\bra{v_1}\ket{u} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix} \begin{pmatrix} \frac{1}{2} \\ -\frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{3}{8} \\ -\frac{\sqrt{3}}{8} \end{pmatrix}$

[marked $-2$]

$\ket{v_2}\bra{v_2}\ket{u} = \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix} \begin{pmatrix} \frac{1}{2} \\ -\frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{1}{8} \\ -\frac{3\sqrt{3}}{8} \end{pmatrix}$

## Page 4

4. Consider a probability distribution with two outcomes defined as follows:

$$\Pr[0] = \frac{1}{2}(1-\alpha), \quad \Pr[1] = \frac{1}{2}(1+\alpha).$$

Suppose that the value of $\alpha$ is unknown. Describe a real-life procedure, based on repeatedly sampling from this probability distribution, that can be used to estimate the value of $\alpha$.

let $n_0$ be $a$ is $0$

$n_1$ be $a$ is $1$

$\hat{\alpha} = \Pr(0) - \Pr(1) \qquad \hat{p} = \frac{1}{2}(1-\alpha)$

$$\boxed{\hat{\alpha} = 1 - 2\left(\frac{n_0}{N}\right)} \qquad 2\hat{p} = 1 - \alpha$$

$$\hat{\alpha} = 1 - 2\hat{p}$$

$\hat{p} = \dfrac{n_0}{N}$

$\angle 10$

5

## Page 5

5. Let us use the following notation for the swap gate:

[Swap gate symbol: two X's connected by a vertical line]

Show that the swap gate can be written in terms of three CNOT gates as follows:

[Circuit equation: SWAP = CNOT (control top, target bottom) · CNOT (control bottom, target top) · CNOT (control top, target bottom)]

CNOT:

$\ket{00} \to \ket{00}$

$\ket{01} \to \ket{01}$

$\ket{10} \to \ket{11}$

$\ket{11} \to \ket{10}$

Swap:

$\ket{00} \to \ket{00}$

$\ket{01} \to \ket{10}$

$\ket{10} \to \ket{01}$

$\ket{11} \to \ket{11}$

for $\ket{00}$:

$\ket{00} \xrightarrow{\text{CNOT 1}} \ket{00} \xrightarrow{\text{CNOT 2}} \ket{00} \xrightarrow{\text{CNOT 3}} \ket{00}$

for $\ket{01}$:

$\ket{01} \xrightarrow{\text{CNOT 1}} \ket{01} \xrightarrow{\text{CNOT 2}} \ket{11} \xrightarrow{\text{CNOT 3}} \ket{10}$

for $\ket{10}$:

$\ket{10} \xrightarrow{\text{CNOT 1}} \ket{11} \xrightarrow{\text{CNOT 2}} \ket{01} \xrightarrow{\text{CNOT 3}} \ket{01}$ ✓

for $\ket{11}$:

$\ket{11} \xrightarrow{\text{CNOT 1}} \ket{10} \xrightarrow{\text{CNOT 2}} \ket{10} \xrightarrow{\text{CNOT 3}} \ket{11}$

6

## Page 6

6. Consider the circuit below. Prove that this circuit can be used to calculate the imaginary part of the inner product $\braket{\psi|U|\psi}$, namely, $\operatorname{Im}(\braket{\psi|U|\psi})$, where $U$ is an arbitrary single-qubit gate and $\ket{\psi}$ is an arbitrary single-qubit state vector. Here, $H$ denotes the Hadamard gate and $S$ denotes the phase gate.

[Circuit diagram: top wire starts with $\ket{0}$, passes through $H$, then $S^\dagger$, then a control dot, then $H$, then a measurement. Bottom wire starts with $\ket{\psi}$, passes through $U$ (controlled by top wire).]

H on $\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})\otimes\ket{\psi}$

$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

$\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\otimes\ket{0} + \ket{1}\otimes\ket{1})\otimes\ket{\psi}$

$S^\dagger$ on $H\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\otimes\ket{0} + i\ket{1}\otimes\ket{1})\otimes\ket{\psi}$

$\ket{00} \rightarrow \ket{00}$

$\ket{01} \rightarrow \ket{01}$

$\ket{10} \rightarrow \ket{10}$ +

$\ket{11} \rightarrow i\ket{11}$

$\;$ [circled: $-6$]

ctrl-$U$ on $\ket{\psi}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\ket{0} + i\ket{1}\ket{1})\otimes U\ket{\psi}$

H on $\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}\cdot\frac{1}{\sqrt{2}}(\ket{0}\ket{0}\otimes\ket{0} + i\ket{1}\ket{1}\otimes\ket{1})\otimes U\ket{\psi}$

by basis $\{\ket{0},\ket{1}\}$

$= \frac{1}{2}\left(\ket{0}\otimes(\ket{00}U\ket{\psi}) + \ket{1}\otimes(U_i\ket{11}\ket{\psi})\right)$

$\Pr_1 = $ squared $= \frac{1}{4}\left( \quad \right)^2$

$\Pr_2 = \frac{1}{4}\left(\text{same as this but w/ minus sign}\right)$


# problem_bank.pdf

## Page 1

# Problem Bank
# CS4134 – Quantum Computation and Information Processing

Sumeet Khatri, Virginia Tech Department of Computer Science, Spring 2026

## Table of Contents

**Linear algebra** &nbsp; 1

**Probability and statistics** &nbsp; 8

**Quantum mechanics** &nbsp; 11

**Entanglement** &nbsp; 16

**Quantum circuits** &nbsp; 18

**Quantum error correction** &nbsp; 22

---

- Questions marked with a ★ are challenging problems that may appear in the exams as *bonus questions*, i.e., they need not be attempted in order to get a full score on the exams.

- You may go the instructor and TA office hours to discuss solutions to the problems.

---

## Linear algebra

1. Consider the complex number $z = 1 + 2i$.
   
   (a) Find $\text{Re}(z)$.
   
   (b) Find $\text{Im}(z)$.
   
   (c) Plot $z$ as a point in the complex plane.
   
   (d) Write $z$ in polar form, $z = r\,e^{i\theta}$.
   
   (e) Find $\bar{z}$.
   
   (f) Find $|z|$.
   
   (g) Find $|z|^2$.

2. Prove the following facts:
   
   (a) For complex numbers $z_1, z_2 \in \mathbb{C}$, $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$.
   
   (b) If $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$, for any $d \in \{2, 3, \dots\}$, then $\braket{v_1|v_2} = \overline{\braket{v_2|v_1}}$.

1

## Page 2

3. Consider the following two-dimensional vector $\ket{v} \in \mathbb{C}^2$, written with respect to the standard basis $\{\ket{0}, \ket{1}\}$:
$$\ket{v} = \begin{pmatrix} 3 + 2i \\ 4 + 5i \end{pmatrix}. \tag{1}$$

   (a) Determine the values $\braket{0|v}$ and $\braket{1|v}$.

   (b) Write the vector $\ket{v}$ in the abstract form $\ket{v} = a\ket{0} + b\ket{1}$, with the appropriate values of $a$ and $b$.

   (c) Is the vector normalized? Say why or why not. If not normalized, then normalize it.

4. Consider the following three-dimensional vector $\ket{v} \in \mathbb{C}^3$, written with respect to the standard basis $\{\ket{0}, \ket{1}, \ket{2}\}$:
$$\ket{v} = \begin{pmatrix} 5 - i \\ 6 + 3i \\ 7 - 4i \end{pmatrix}. \tag{2}$$

   (a) Determine the values $\braket{0|v}$, $\braket{1|v}$, and $\braket{2|v}$.

   (b) Write the vector $\ket{v}$ in the abstract form $\ket{v} = a\ket{0} + b\ket{1} + c\ket{2}$, with the appropriate values of $a$, $b$, and $c$.

   (c) Is the vector normalized? Say why or why not. If not normalized, then normalize it.

5. Calculate the inner products $\braket{v_1|v_2}$ and $\braket{v_2|v_1}$ of the following two vectors:
$$\ket{v_1} = (3 + 4i)\ket{0} + (2 - 5i)\ket{1}, \quad \ket{v_2} = \left(\frac{3}{4} + \frac{2i}{5}\right)\ket{+} + \left(-\frac{7}{6} + \frac{i}{3}\right)\ket{-}, \tag{3}$$

   where $\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$. Also calculate the norm of $\ket{v_1}$ and $\ket{v_2}$, and then normalize both vectors.

6. Consider the vectors $\ket{v_1}$ and $\ket{v_2}$ from (3). Verify that
$$\ket{0} \otimes \ket{v_1} + \ket{1} \otimes \ket{v_2} = \begin{pmatrix} \ket{v_1} \\ \ket{v_2} \end{pmatrix} = \begin{pmatrix} 3 + 4i \\ 2 - 5i \\ \frac{1}{\sqrt{2}}\left(-\frac{5}{12} + \frac{11i}{15}\right) \\ \frac{1}{\sqrt{2}}\left(\frac{23}{12} + \frac{i}{15}\right) \end{pmatrix}. \tag{4}$$

7. Let $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$ be arbitrary vectors, and let $M \in \mathrm{L}(\mathbb{C}^d)$ be an arbitrary linear operator (i.e., $d \times d$ matrix). Using the definition of the trace of a linear operator, prove the following identities.

   (a) $\mathrm{Tr}\big[\ket{v_1}\bra{v_2}\big] = \braket{v_2|v_1}$

   (b) $\mathrm{Tr}\big[M\ket{v_1}\bra{v_2}\big] = \braket{v_2|M|v_1}$

8. Consider the following two state vectors:
$$\ket{v_1} = \frac{\sqrt{3}}{2}\ket{0} + \frac{i}{2}\ket{1}, \tag{5}$$
$$\ket{v_2} = \frac{i}{2}\ket{0} + \frac{\sqrt{3}}{2}\ket{1} \tag{6}$$

2

## Page 3

(a) Prove that $\ket{v_1}$ and $\ket{v_2}$ are orthonormal.

(b) Show that $\ket{v_1}\bra{v_1} + \ket{v_2}\bra{v_2} = \mathbb{1}$.

(c) Consider a qubit in the state given by

$$\ket{u} = \frac{1}{2}\ket{0} - \frac{\sqrt{3}}{2}\ket{1}. \tag{7}$$

Write this state in terms of $\ket{v_1}$ and $\ket{v_2}$.

(d) If we measure the state given by $\ket{u}$ with respect to the measurement $\{\ket{v_1}\bra{v_1}, \ket{v_2}\bra{v_2}\}$, then what are the possible outcomes and their associated probabilities?

9. Consider the vectors

$$\ket{v_1} = \frac{3 + i\sqrt{3}}{4}\ket{0} + \frac{1}{2}\ket{1}, \tag{8}$$

$$\ket{v_2} = \frac{1}{4}\ket{0} + x\ket{1}. \tag{9}$$

(a) Find the value of $x$ so that $\ket{v_1}$ and $\ket{v_2}$ are orthogonal.

(b) Find the value of $x$ so that $\ket{v_2}$ is normalized.

(c) For what values of $x$ (if any) are $\ket{v_1}$ and $\ket{v_2}$ orthonormal?

10. (a) Consider the matrix $H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.

   i. Verify that the vector $\ket{v} = \begin{pmatrix} 1 + \sqrt{2} \\ 1 \end{pmatrix}$ is an eigenvector of $H$ with associated eigenvalue 1.

   ii. Verify that $\ket{v} = \begin{pmatrix} 1 - \sqrt{2} \\ 1 \end{pmatrix}$ is an eigenvector of $H$ with associated eigenvalue $-1$.

   (b) Consider the matrix

$$U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & e^{i\pi/4} & 0 & e^{i\pi/4} \\ 1 & 0 & -1 & 0 \\ 0 & e^{i\pi/4} & 0 & -e^{i\pi/4} \end{pmatrix}. \tag{10}$$

   i. Verify that $U$ is a unitary matrix.

   ii. Verify that $\ket{v} = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \sqrt{2} - 1 \end{pmatrix}$ is an eigenvector of $U$ with associated eigenvalue $e^{i\pi/4}$.

11. Let $M \in \mathrm{L}(\mathbb{C}^d)$ be an arbitrary linear operator. Prove that the conjugate transpose of $M$, i.e., $M^\dagger$, satisfies the following identity:

$$\braket{v_2 | M v_1} = \braket{M^\dagger v_2 | v_1}, \tag{11}$$

for all $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$.

3

## Page 4

12. Let $M \in \mathrm{L}(\mathbb{C}^d)$ be an arbitrary linear operator. Define the vector $|M\rangle\!\rangle$ as follows:
$$|M\rangle\!\rangle \equiv \mathrm{vec}(M) := (\mathbb{1}_d \otimes M)|\Gamma_d\rangle, \tag{12}$$

where
$$|\Gamma_d\rangle := \sum_{k=0}^{d-1} |k\rangle \otimes |k\rangle. \tag{13}$$

(a) Prove that
$$\mathrm{vec}(|v_1\rangle\langle v_2|) = \overline{|v_2\rangle} \otimes |v_1\rangle, \tag{14}$$
where $|v_1\rangle, |v_2\rangle \in \mathbb{C}^d$ are arbitrary and $\overline{|v_2\rangle}$ denotes the complex conjugate of $|v_2\rangle$ with respect to the basis $\{|k\rangle\}_{k=0}^{d-1}$.

(b) If $M \in \mathrm{L}(\mathbb{C}^2)$ is the $2 \times 2$ matrix given by
$$M = \begin{pmatrix} p & q \\ r & s \end{pmatrix}, \quad p, q, r, s \in \mathbb{C}, \tag{15}$$
then show that $|M\rangle\!\rangle$ is the column vector defined by stacking the columns of $M$:
$$|M\rangle\!\rangle = \begin{pmatrix} p \\ r \\ q \\ s \end{pmatrix}. \tag{16}$$

(c) For $M \in \mathrm{L}(\mathbb{C}^d)$ prove that
$$(\mathbb{1}_d \otimes M)|\Gamma_d\rangle = (M^{\mathsf{T}} \otimes \mathbb{1}_d)|\Gamma_d\rangle, \tag{17}$$
where $M^{\mathsf{T}}$ is the transpose of $M$.

(d) For $M \in \mathrm{L}(\mathbb{C}^d)$, prove that
$$\mathrm{Tr}[M] = \langle \Gamma_d|(\mathbb{1}_d \otimes M)|\Gamma_d\rangle. \tag{18}$$

(e) For $K, M, L \in \mathrm{L}(\mathbb{C}^d)$, prove that
$$\mathrm{vec}(KML^\dagger) = (\overline{L} \otimes K)\mathrm{vec}(M). \tag{19}$$

13. Let $M \in \mathrm{L}(\mathbb{C}^d)$ be an arbitrary linear operator. Prove that $M^\dagger M$ is positive semi-definite.

14. ★ Prove that a linear operator $M \in \mathrm{L}(\mathbb{C}^d)$, with $d \in \{1, 2, \dots\}$, is injective if and only if it is surjective.

15. ★ Let $\{|\psi_j\rangle\}_{j=0}^{d-1}$ be a set of $d$ linearly independent vectors in $\mathbb{C}^d$, with $d \in \{2, 3, \dots\}$. By definition, this means that, for all $c_0, c_1, \dots, c_{d-1} \in \mathbb{C}$, the equation $c_0|\psi_0\rangle + c_1|\psi_1\rangle + \cdots + c_{d-1}|\psi_{d-1}\rangle = 0$ implies $c_0 = c_1 = \cdots = c_{d-1} = 0$.

   (a) Let
$$T := \sum_{j=0}^{d-1} |\psi_j\rangle\langle j|. \tag{20}$$

   The operator $T$ can be thought of as a $d \times d$ matrix whose columns are given by the vectors $|\psi_j\rangle$. Prove that $T$ is invertible. (*Hint*: First prove that $T$ is injective, by showing that its kernel contains only the zero vector. Then use the result of the previous problem.)

4

## Page 5

(b) Using (a), prove that $\{\ket{\psi_j}\}_{j=1}^d$ is a basis for $\mathbb{C}^d$. In other words, prove that every vector $\ket{\phi} \in \mathbb{C}^d$ can be written as a unique linear combination of the vectors $\ket{\psi_j}$. We thus have that every set of $d$ linearly independent vectors in $\mathbb{C}^d$ is a basis for $\mathbb{C}^d$.

(c) Prove that if $\sum_{j=1}^d \ket{\psi_j}\bra{\psi_j} = \mathbb{1}_d$, then $\{\ket{\psi}_j\}_{j=1}^d$ is an orthonormal basis for $\mathbb{C}^d$.

By combining this result with (57), we have that a linearly independent set $\{\ket{\psi_j}\}_{j=1}^d$ of vectors in $\mathbb{C}^d$ is an orthonormal basis if and only if $\sum_{j=1}^d \ket{\psi_j}\bra{\psi_j} = \mathbb{1}_d$.

16. ★ Let $\{B_j\}_{j=1}^{d^2}$ be an orthonormal basis for $\mathrm{L}(\mathbb{C}^d)$, with $d \in \{2, 3, \dots\}$.

   (a) Prove that
   $$\sum_{j=1}^{d^2} \overline{B_j} \otimes B_j = \Gamma_d, \tag{21}$$
   where $\Gamma_d = \ket{\Gamma_d}\bra{\Gamma_d} = \sum_{i,j=0}^{d-1} \ket{i,i}\bra{j,j}$. Similarly, prove that
   $$\sum_{j=1}^{d^2} B_j^\dagger \otimes B_j = F, \tag{22}$$
   where $F = \sum_{i,j=0}^{d-1} \ket{i,j}\bra{j,i}$.

   (*Hint*: Start by verifying that $\{\overline{B_j}\}_{j=1}^{d^2}$ is an orthonormal basis for $\mathrm{L}(\mathbb{C}^d)$. Then, use the fact that every linear operator $Z \in \mathrm{L}(\mathbb{C}^d \otimes \mathbb{C}^d)$ can be written as $Z = \sum_{j,k=1}^{d^2} c_{j,k} \overline{B_j} \otimes B_k$ for some coefficients $c_{j,k} \in \mathbb{C}$.)

   (b) Prove that for $M \in \mathrm{L}(\mathbb{C}^d)$,
   $$\sum_{j=1}^{d^2} B_j M B_j^\dagger = \mathrm{Tr}[M] \mathbb{1}_d. \tag{23}$$
   (*Hint*: Use (18), (19), and (21).)

   (c) Prove that $\{\ket{B_j}\!\rangle\}_{j=1}^{d^2}$ is an orthonormal basis for $\mathbb{C}^d \otimes \mathbb{C}^d$.

17. ★ Let $\{\ket{\psi_j}\}_{j=0}^{d-1}$ be a set of linearly independent, normalized, but non-orthogonal vectors in $\mathbb{C}^d$, with $d \in \{2, 3, \dots\}$. We would like to transform these vectors into a new set $\{\ket{\phi_j}\}_{j=0}^{d-1}$ of orthonormal vectors via an invertible linear operator $Q$, such that $\ket{\phi_j} = Q\ket{\psi_j}$ for all $j \in \{0, 1, \dots, d-1\}$.

   (a) Prove that the operator $S$ defined as
   $$S := \sum_{j=0}^{d-1} \ket{\psi_j}\bra{\psi_j} \tag{24}$$
   is invertible and positive definite. (*Hint*: Write $S$ in terms of the operator $T$ defined in (20).)

5

## Page 6

(b) Let
$$\ket{\phi_j} := S^{-\frac{1}{2}}\ket{\psi_j} \tag{25}$$
for all $j \in \{0, 1, \ldots, d-1\}$. Prove that $\{\ket{\phi_j}\}_{j=0}^{d-1}$ is an orthonormal basis for $\mathbb{C}^d$. Also, prove that $\braket{\phi_i|\psi_j} = \bra{i} G^{\frac{1}{2}} \ket{j}$ for all $i, j \in \{0, 1, \ldots, d-1\}$, where $G := T^\dagger T$ and $T := \sum_{j=0}^{d-1} \ket{\psi_j}\bra{j}$.

(c) Let us now show that the vectors defined in (25) are optimal with respect to the Euclidean norm, in the following sense:
$$\inf_Q \left\{ \sum_{j=0}^{d-1} \| \ket{\psi_j} - \ket{\phi_j} \|_2^2 : \ket{\phi_j} = Q\ket{\psi_j},\ \braket{\phi_i|\phi_j} = \delta_{i,j}\ \forall j \in \{0, 1, \ldots, d-1\} \right\} \tag{26}$$
$$= \sum_{j=0}^{d-1} \| \ket{\psi_j} - S^{-\frac{1}{2}} \ket{\psi_j} \|_2^2, \tag{27}$$

where the optimization in (26) is with respect to every invertible linear operator $Q$.

  i. Prove that solving the optimization problem given by (26) can be reduced to solving the optimization problem given by
$$\sup_Q \left\{ \mathrm{Tr}[(Q + Q^\dagger)S] : QSQ^\dagger = \mathbb{1}_d \right\}. \tag{28}$$

  ii. Prove that the constraint $QSQ^\dagger = \mathbb{1}_d$ in (28) implies that $Q = US^{-\frac{1}{2}}$, where $U$ is a unitary operator. (*Hint*: Consider a polar decomposition of $Q$.)
  Hence, show that the optimization problem given by (28) is equivalent to
$$\sup_U \mathrm{Re}\left( \mathrm{Tr}[U S^{\frac{1}{2}}] \right), \tag{29}$$
where the optimization is with respect to unitary operators $U$ acting on $\mathbb{C}^d$.

  iii. Prove that the solution to the optimization problem given by (29) is $U = \mathbb{1}_d$, implying that the optimal $Q$ in (26) is indeed $S^{-\frac{1}{2}}$.

18. Prove that the trace norm can be calculated as $\|M\|_1 = \mathrm{Tr}[\sqrt{M^\dagger M}]$. (*Hint*: Start by writing $M$ in terms of its singular-value decomposition. Then recall how we define the square root of Hermitian operators.)

19. Prove that $\|P\|_1 = \mathrm{Tr}[P]$ for every (Hermitian) positive semi-definite operator $P$.

20. ★ Let $\ket{u}, \ket{v} \in \mathbb{C}^d$, with $d \in \{2, 3, \ldots\}$, be arbitrary vectors (not necessarily unit/state vectors). Prove that
$$\| \ket{u}\bra{u} - \ket{v}\bra{v} \|_1^2 = (\braket{u|u} + \braket{v|v})^2 - 4|\braket{u|v}|^2. \tag{30}$$

21. Let $\ket{\psi} \in \mathbb{C}^d$ be a state vector, with $d \in \{2, 3, \ldots\}$. Prove that
$$\frac{1}{2} \left\| \ket{\psi}\bra{\psi} - \frac{\mathbb{1}_d}{d} \right\|_1 = 1 - \frac{1}{d}. \tag{31}$$

In other words, every pure state is the same trace distance away from the maximally-mixed state.

6

## Page 7

22. Let $\rho$ be a density operator in dimension $d \in \{2, 3, \ldots\}$. Prove that

$$\frac{1}{2}\left\|\rho - \frac{\mathbb{1}_d}{d}\right\|_1 = \frac{1}{2}\sum_{k=1}^{r}\left|\lambda_k - \frac{1}{d}\right| + \frac{1}{2}\left(1 - \frac{r}{d}\right), \tag{32}$$

where $r \in \{1, 2, \ldots, d\}$ is the rank of $\rho$ and $\{\lambda_k\}_{k=1}^{r}$ is the set of non-zero eigenvalues of $\rho$. If $\lambda_k \geq \frac{1}{d}$ for all $k \in \{1, 2, \ldots, r\}$, then conclude that $\frac{1}{2}\|\rho - \frac{\mathbb{1}_d}{d}\|_1 = 1 - \frac{r}{d}$.

23. Prove that $\|M\|_\infty = \sqrt{\lambda_{\max}(M^\dagger M)}$, where $\lambda_{\max}(M^\dagger M)$ denotes the largest eigenvalue of $M^\dagger M$.

24. Prove that $\|U\|_\infty = 1$ for every unitary operator $U$.

7

## Page 8

# Probability and statistics

1. Fifty teams compete in a student programming competition. It has been observed that 60% of the teams use the programming language C while the others use C++, and experience has shown that teams who program in C are twice as likely to win as those who use C++. Furthermore, ten teams who use C++ include a graduate student, while only four of those who use C include a graduate student.
   
   (a) What is the probability that the winning team programs in C?
   
   (b) What is the probability that the winning team programs in C and includes a graduate student?
   
   (c) What is the probability that the winning team includes a graduate student?
   
   (d) Given that the winning team includes a graduate student, what is the probability that team programmed in C?

2. Let $A$ be the event that an odd number of spots comes up when a fair die is thrown, and let $B$ be the event that the number of spots is a prime number. What is $\Pr[A|B]$ and $\Pr[B|A]$?

3. A family has three children. What is the probability that all three children are boys? What is the probability that there are two girls and one boy? Given that at least one of the three is a boy, what is the probability that all three children are boys. You should assume that $\Pr[\text{boy}] = \Pr[\text{girl}] = \frac{1}{2}$.

4. Three cards are placed in a box; one is white on both sides, one is black on both sides, and the third is white on one side and black on the other. One card is chosen at random from the box and placed on a table. The (uppermost) face that shows is white. Explain why the probability that the hidden face is black is equal to $\frac{1}{3}$ and not $\frac{1}{2}$.

5. If $\Pr[A|B] = \Pr[B] = \Pr[A \cup B] = \frac{1}{2}$, are $A$ and $B$ independent?

6. Let $X$ be a random variable, taking values in $\{1, 2, 3, \ldots\}$, whose probability mass function is given as
$$p_X(x) = \begin{cases} \alpha x^2 & x \in \{1, 2, 3, 4\}, \\ 0 & \text{otherwise.} \end{cases} \tag{33}$$

   (a) What is the value of $\alpha$?
   
   (b) Compute $\Pr[X = 4]$.
   
   (c) Compute $\Pr[X \leq 2]$.

7. Let $X$ be a random variable, taking values in $\{1, 2, 3, \ldots\}$, whose probability masss function is given as
$$p_X(x) = \begin{cases} \alpha/x & x \in \{1, 2, 3, 4\} \\ 0 & \text{otherwise} \end{cases} \tag{34}$$

   (a) What is the value of $\alpha$?
   
   (b) Compute $\Pr[X \text{ is odd}]$.
   
   (c) Compute $\Pr[X > 2]$.

8

## Page 9

8. Let $X, Y$, and $Z$ be three discrete random variables for which we have the following probabilities:

$$\Pr[X = 0, Y = 0, Z = 0] = \frac{6}{24}, \tag{35}$$

$$\Pr[X = 0, Y = 1, Z = 0] = \frac{8}{24}, \tag{36}$$

$$\Pr[X = 0, Y = 1, Z = 1] = \frac{6}{24}, \tag{37}$$

$$\Pr[X = 1, Y = 0, Z = -1] = \frac{1}{24}, \tag{38}$$

$$\Pr[X = 1, Y = 0, Z = 1] = \frac{1}{24}, \tag{39}$$

$$\Pr[X = 1, Y = 1, Z = 0] = \frac{2}{24} \tag{40}$$

Let $S$ be a new random variable for which $S = X + Y + Z$.

(a) Find the marginal probability mass function of $X$.

(b) Are $X$ and $Y$ independent?

(c) Are $X$ and $Z$ independent?

(d) Find the marginal probability mass function of $S$.

9. Let $X, Y$, and $Z$ be three discrete random variables for which we have the following probabilities:

$$\Pr[X = 1, Y = 1, Z = 0] = p, \tag{41}$$

$$\Pr[X = 1, Y = 0, Z = 1] = \frac{1}{2}(1-p), \tag{42}$$

$$\Pr[X = 0, Y = 1, Z = 1] = \frac{1}{2}(1-p), \tag{43}$$

where $p \in (0, 1)$.

(a) What is the joint probability mass function of $X$ and $Y$?

(b) Determine the covariance matrix for $X$ and $Y$.

10. The probabilty mass function of a discrete random variable $X$ is as follows:

$$p_X(x) = \begin{cases} 0.2 & x = -2, \\ 0.3 & x = -1, \\ 0.4 & x = 1, \\ 0.1 & x = 2, \\ 0 & \text{otherwise} \end{cases} \tag{44}$$

Find the expectation values of the following functions of $X$:

(a) $Y = 3X - 1$

(b) $Z = -X$

(c) $W = |X|$

11. A coin is tossed 400 times and the number of heads that appear is equal to 225. What is the probability that this coin is biased?

9

## Page 10

12. Messages relayed over a communication channel have probability $p$ of being received correctly. A message that is not received correctly is retransmitted until it is. What value should $p$ have so that the probability of more than one retransmission is less than $0.05$?

13. ★ Consider a discrete-time Markov chain consisting of four states, $a$, $b$, $c$, and $d$, whose transition probability matrix is given by
$$P = \begin{pmatrix} 0 & 0 & 0.8 & 0.2 \\ 0 & 0.4 & 0 & 0.3 \\ 1 & 0.6 & 0.2 & 0 \\ 0 & 0 & 0 & 0.5 \end{pmatrix} \tag{45}$$

   Compute the following probabilities.

   (a) $\Pr[X_4 = c, X_3 = c, X_2 = c, X_1 = c | X_0 = a]$
   (b) $\Pr[X_6 = d, X_5 = c, X_4 = b | X_3 = a]$
   (c) $\Pr[X_5 = c, X_6 = a, X_7 = c, X_8 = c | X_4 = b, X_3 = d]$.

14. ★ A Markov chain with two states, $a$ and $b$, has the following conditional probabilities: if it is in state $a$ at time step $t$, $t \in \{0, 1, 2, \dots\}$, then it stays in state $a$ with probability $\frac{1}{2}(\frac{1}{2})^t$. If it is in state $b$ at time step $t$, then it stays in state $b$ with probability $\frac{3}{4}(\frac{1}{4})^t$.

   (a) Determine the transition probability matrix of the Markov chain.
   (b) If the Markov chain begins in state $a$ at time step $t = 0$, then compute the probabilities of the following sample paths:
   $$a \to b \to a \to b \quad \text{and} \quad a \to a \to b \to b. \tag{46}$$

10

## Page 11

# Quantum mechanics

1. Draw a Bloch sphere and label the following locations:
    (a) Where a qubit is exactly $\ket{0}$.
    (b) Where a qubit is exactly $\ket{1}$.
    (c) Where a qubit is half $\ket{0}$ and half $\ket{1}$.
    (d) Where a qubit is more $\ket{0}$ than $\ket{1}$.
    (e) Where a qubit is more $\ket{1}$ then $\ket{0}$.

2. Prove that the Pauli operators are orthogonal to each other; specifically, $\mathrm{Tr}[XY] = 0$, $\mathrm{Tr}[XZ] = 0$, and $\mathrm{Tr}[YZ] = 0$, where we recall that the Pauli operators are
$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -\mathrm{i} \\ \mathrm{i} & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}. \tag{47}$$

3. Define the Bell state vector
$$\ket{\Phi} = \frac{1}{\sqrt{2}}\big(\ket{0,0} + \ket{1,1}\big) = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \frac{1}{\sqrt{2}} \end{pmatrix}. \tag{48}$$

    Prove that
$$\frac{1}{4}\big(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X - Y \otimes Y + Z \otimes Z\big) = \ket{\Phi}\bra{\Phi} = \begin{pmatrix} \tfrac{1}{2} & 0 & 0 & \tfrac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \tfrac{1}{2} & 0 & 0 & \tfrac{1}{2} \end{pmatrix}. \tag{49}$$

4. Prove that
$$\frac{1}{2}\big(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X + Y \otimes Y + Z \otimes Z\big) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}. \tag{50}$$

5. Consider an operator $M \in \mathrm{L}(\mathbb{C}^2)$ decomposed in the Pauli basis as $M = \tfrac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$.

    (a) Verify that
$$c_0 = \mathrm{Tr}[M], \quad c_1 = \mathrm{Tr}[XM], \quad c_2 = \mathrm{Tr}[YM], \quad c_3 = \mathrm{Tr}[ZM]. \tag{51}$$

    (b) Verify that the Hilbert–Schmidt norm of $M$ is $\|M\|_{\mathrm{HS}} = \sqrt{\tfrac{1}{2}\big(|c_0|^2 + |c_1|^2 + |c_2|^2 + |c_3|^2\big)}$.

6. Consider an arbitrary $2 \times 2$ matrix as follows:
$$M = \begin{pmatrix} p & q \\ r & s \end{pmatrix}, \quad p, q, r, s \in \mathbb{C}. \tag{52}$$

    Show that
$$\mathrm{Tr}[M] = p + s, \quad \mathrm{Tr}[XM] = q + r, \quad \mathrm{Tr}[YM] = \mathrm{i}(q - r), \quad \mathrm{Tr}[ZM] = p - s. \tag{53}$$

11

## Page 12

7. Consider the following state vectors. Determine the probabilities for obtaining the outcomes "0" and "1".

   (a) $\ket{\psi} = \left(\frac{1}{5} + \frac{2i}{3}\right)\ket{0} + \left(\frac{4}{15} + \frac{2i}{3}\right)\ket{1}$
   
   (b) $\ket{\psi} = \left(\frac{1}{3} + \frac{2i}{5}\right)\ket{0} + \left(\frac{8}{15} + \frac{2i}{3}\right)\ket{1}$
   
   (c) $\ket{\psi} = \left(\frac{2}{25} + \frac{8i}{75}\right)\ket{0} + \left(\frac{1}{3} + \frac{14i}{15}\right)\ket{1}$
   
   (d) $\ket{\psi} = \left(\frac{3}{25} + \frac{38i}{75}\right)\ket{0} + \left(\frac{8}{15} + \frac{2i}{3}\right)\ket{1}$

8. Two qubits are in the state given by the vector

$$\frac{i}{\sqrt{10}}\ket{0,0} + \frac{1-2i}{\sqrt{10}}\ket{0,1} + \frac{e^{i\pi/100}}{\sqrt{10}}\ket{1,0} + \frac{\sqrt{3}}{\sqrt{10}}\ket{1,1}. \tag{54}$$

   If we measure the qubits in the two-qubit $Z$-basis $\{\ket{0,0},\ket{0,1},\ket{1,0},\ket{1,1}\}$, what are the possible measurement outcomes and their associated probabilities?

9. Determine whether or not the following density matrices represent pure states. Then, write each density matrix with respect to the Pauli basis, i.e., determine the coefficients $r_X, r_Y, r_Z \in \mathbb{R}$ such that $\rho = \frac{1}{2}(\mathbb{1} + r_X X + r_Y Y + r_Z Z)$.

   (a) $\rho = \begin{pmatrix} \frac{5}{13} & \frac{3+2i}{13} \\ \frac{3-2i}{13} & \frac{8}{13} \end{pmatrix}$
   
   (b) $\rho = \begin{pmatrix} \frac{109}{225} & \frac{112}{225} + \frac{2i}{45} \\ \frac{112}{225} - \frac{2i}{45} & \frac{116}{225} \end{pmatrix}$
   
   (c) $\rho = \begin{pmatrix} \frac{377}{1125} & \frac{2422+824i}{5625} \\ \frac{2422-824i}{5625} & \frac{748}{1125} \end{pmatrix}$
   
   (d) $\rho = \begin{pmatrix} \frac{4}{225} & \frac{142-44i}{1125} \\ \frac{142+44i}{1125} & \frac{221}{225} \end{pmatrix}$

10. Prove that every Hermitian operator has real eigenvalues.

11. Prove that a linear operator $M \in \mathrm{L}(\mathbb{C}^2)$, decomposed as $M = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$ in the Pauli basis, is Hermitian if and only if the coefficients $c_0, c_1, c_2, c_3$ are all real-valued.

12. Let $M \in \mathrm{L}(\mathbb{C}^d)$ be an arbitrary linear operator. Prove that $M$ can be decomposed as follows:

$$M = H_1 + iH_2, \tag{55}$$

    where

$$H_1 = \frac{1}{2}(M + M^\dagger), \quad H_2 = \frac{1}{2i}(M - M^\dagger). \tag{56}$$

    Verify that $H_1$ and $H_2$ are Hermitian.

13. Let $U \in \mathrm{L}(\mathbb{C}^d)$ be a unitary operator, and let $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$ be arbitrary vectors. Prove that $\braket{Uv_1|Uv_2} = \braket{v_1|v_2}$.

12

## Page 13

14. Given any orthonormal basis $\{\ket{e_k}\}_{k=1}^d$ for $\mathbb{C}^d$, prove that

$$\mathbb{1}_d = \sum_{k=1}^d \ket{e_k}\bra{e_k}. \tag{57}$$

15. Let $\{\ket{e_k}\}_{k=1}^d$ and $\{\ket{f_k}\}_{k=1}^d$ be two orthonormal bases for $\mathbb{C}^d$. Prove that

$$U = \sum_{k=1}^d \ket{e_k}\bra{f_k} \tag{58}$$

is a unitary operator.

16. Verify that the following $2 \times 2$ matrices are unitary matrices.

   (a) $U = \begin{pmatrix} \frac{3}{5} & \frac{4i}{5} \\ \frac{4i}{5} & \frac{3}{5} \end{pmatrix}$

   (b) $U = \begin{pmatrix} \frac{2+i}{3} & \frac{2i}{3} \\ \frac{2i}{3} & \frac{2-i}{3} \end{pmatrix}$

   (c) $U = \sqrt{\frac{75}{43}} \begin{pmatrix} \frac{2}{15} + \frac{i}{5} & -\frac{4}{15} + \frac{2i}{3} \\ \frac{4}{15} + \frac{2i}{3} & \frac{2}{15} - \frac{i}{5} \end{pmatrix}$

   (d) $U = \sqrt{\frac{450}{43}} \begin{pmatrix} \frac{1}{10} + \frac{2i}{15} & -\frac{1}{6} + \frac{i}{5} \\ \frac{1}{6} + \frac{i}{5} & \frac{1}{10} - \frac{2i}{15} \end{pmatrix}$

17. Calculate the partial trace $\operatorname{Tr}_B[M_{AB}]$ for the following two-qubit linear operators.

   (a) $M_{AB} = \begin{pmatrix} \frac{1}{3} + \frac{2}{5}i & 0 & 0 & 0 \\ 0 & -\frac{7}{4} - \frac{1}{9}i & 0 & 0 \\ 0 & 0 & \frac{5}{2} + \frac{3}{2}i & 0 \\ 0 & 0 & 0 & -\frac{2}{7} + \frac{1}{8}i \end{pmatrix}$

   (b) $M_{AB} = \begin{pmatrix} \frac{1}{2} - \frac{1}{3}i & \frac{2}{3} + \frac{3}{4}i & -\frac{5}{7} & \frac{1}{2}i \\ -\frac{4}{3} & \frac{7}{5} - \frac{2}{5}i & \frac{1}{9} + \frac{2}{3}i & 0 \\ \frac{1}{8} & \frac{4}{5}i & -\frac{2}{11} & \frac{6}{7} + \frac{3}{8}i \\ \frac{2}{9}i & \frac{1}{6} & -\frac{1}{7}i & \frac{3}{2} - \frac{1}{6}i \end{pmatrix}$

   (c) $M_{AB} = \begin{pmatrix} \frac{3}{5} & \frac{1}{2} - \frac{1}{4}i & 0 & \frac{1}{3}i \\ \frac{1}{2} + \frac{1}{4}i & \frac{2}{3} & \frac{4}{7}i & 0 \\ 0 & -\frac{4}{7}i & 1 & -\frac{2}{9} + \frac{1}{2}i \\ -\frac{1}{3}i & 0 & -\frac{2}{9} - \frac{1}{2}i & \frac{4}{9} \end{pmatrix}$

   (d) $M_{AB} = \begin{pmatrix} 0 & \frac{5}{7} + \frac{3}{11}i & \frac{1}{6} - \frac{2}{5}i & \frac{2}{3} + \frac{1}{4}i \\ -\frac{3}{4} + \frac{2}{7}i & \frac{1}{4} & -\frac{1}{6}i & \frac{1}{9} + \frac{1}{7}i \\ \frac{2}{5} & -\frac{2}{3}i & \frac{3}{8} + \frac{2}{9}i & 0 \\ \frac{1}{10} & \frac{5}{8}i & -\frac{3}{11} + \frac{2}{3}i & \frac{1}{2} \end{pmatrix}$

13

## Page 14

18. Consider the three-qubit state vectors

$$\ket{\psi_1}_{ABC} = \frac{1}{\sqrt{2}}(\ket{0,0,0}_{ABC} + \ket{1,1,1}_{ABC}), \tag{59}$$

$$\ket{\psi_2}_{ABC} = \frac{1}{\sqrt{3}}(\ket{0,0,1}_{ABC} + \ket{0,1,0}_{ABC} + \ket{1,0,0}_{ABC}). \tag{60}$$

Determine the following partial traces.

(a) $\mathrm{Tr}_B\big[\ket{\psi_1}\bra{\psi_1}_{ABC}\big]$.

(b) $\mathrm{Tr}_B\big[\ket{\psi_2}\bra{\psi_2}_{ABC}\big]$.

(c) $\mathrm{Tr}_A\big[p\ket{\psi_1}\bra{\psi_1}_{ABC} + (1-p)\ket{\psi_2}\bra{\psi_2}_{ABC}\big]$, where $p \in [0,1]$.

(d) $\mathrm{Tr}_C\big[p\ket{\psi_1}\bra{\psi_2}_{ABC} + (1-p)\ket{\psi_2}\bra{\psi_1}_{ABC}\big]$, where $p \in [0,1]$.

19. Prove the following identity:

$$\mathrm{Tr}_E[(\mathbb{1}_E \otimes M_S) H_{ES} (\mathbb{1}_E \otimes N_S)] = M_S \, \mathrm{Tr}_E[H_{ES}] N_S, \tag{61}$$

where $H_{ES}$, $M_S$, and $N_S$ are arbitrary linear operators.

20. Consider the following two-qubit density operator $\rho_{AB}$ of Alice and Bob:

$$\rho_{AB} = (1-p)\ket{\Phi^+}\bra{\Phi^+}_{AB} + \frac{p}{3}(\ket{\Phi^-}\bra{\Phi^-}_{AB} + \ket{\Psi^+}\bra{\Psi^+}_{AB} + \ket{\Psi^-}\bra{\Psi^-}_{AB}), \tag{62}$$

where we recall the two-qubit Bell state vectors:

$$\ket{\Phi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}), \tag{63}$$

$$\ket{\Psi^\pm} = \frac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0}). \tag{64}$$

Suppose that Alice and Bob both measure their qubits with respect to the Pauli-$z$ basis; i.e., the POVM is $\{\ket{0}\bra{0}, \ket{1}\bra{1}\}$. What is the probability that they obtain *different* measurement outcomes?

21. Consider the qubit state vectors

$$\ket{\psi_k} = \cos\left(\frac{2\pi k}{5}\right)\ket{0} + \sin\left(\frac{2\pi k}{5}\right)\ket{1}, \quad k \in \{0,1,2,3,4\}. \tag{65}$$

Verify that the set $\left\{\frac{2}{5}\ket{\psi_k}\bra{\psi_k}\right\}_{k=0}^{4}$ is a POVM.

22. Consider the three-qubit state vector $\ket{\psi_1}$ in (59), known as the *GHZ state vector*, and define the following set of eight state vectors:

$$\ket{\psi_{z,x_1,x_2}}_{ABC} := (Z^z \otimes X^{x_1} \otimes X^{x_2})\ket{\psi_1}_{ABC}, \quad z, x_1, x_2 \in \{0,1\}. \tag{66}$$

Prove that the set $\{\ket{\psi_{z,x_1,x_2}}\}_{z,x_1,x_2 \in \{0,1\}}$ is an orthonormal basis for $\mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^2$. Conclude that the set $\{\ket{\psi_{z,x_1,x_2}}\bra{\psi_{z,x_1,x_2}}\}_{z,x_1,x_2 \in \{0,1\}}$ is a POVM.

14

## Page 15

23. Define the $n$-qubit GHZ state vector as follows:

$$|\text{GHZ}_n\rangle := \frac{1}{\sqrt{2}}(|0\rangle^{\otimes n} + |1\rangle^{\otimes n}), \tag{67}$$

for $n \in \{1, 2, \ldots\}$. Then, define

$$|\text{GHZ}_{z,\vec{x}}\rangle := (Z^z \otimes X^{\vec{x}})|\text{GHZ}_n\rangle, \tag{68}$$

for $z \in \{0,1\}$ and $\vec{x} \in \{0,1\}^{n-1}$. Prove that the set $\{|\text{GHZ}_{z,\vec{x}}\rangle\}_{z\in\{0,1\},\,\vec{x}\in\{0,1\}^{n-1}}$ is an orthonormal basis for $(\mathbb{C}^2)^{\otimes n}$, and thereby conclude that the set $\{|\text{GHZ}_{z,\vec{x}}\rangle\langle\text{GHZ}_{z,\vec{x}}|\}_{z\in\{0,1\},\,\vec{x}\in\{0,1\}^{n-1}}$ is a POVM.

24. ★ *Fusing two GHZ state vectors.* Consider a GHZ state of three qubits and a GHZ state of four qubits. We can merge these to create a larger GHZ state of six qubits using the following protocol, which is similar to the teleportation protocol.

   Step 1 Apply the CNOT gate to the third qubit of the first GHZ state (which is the control qubit) and the first qubit of the second GHZ state (which is the target qubit).

   Step 2 Then, measure the target qubit in the $\{|0\rangle, |1\rangle\}$ basis.

   Step 3 If the measurement outcome is "0", do nothing; if the outcome is "1", then apply the Pauli-$X$ gate to all of the remaining qubits of the second GHZ state.

   Prove that, with probability one, this procedure results in the larger GHZ state of six qubits.

25. ★ Let $\rho$ and $\sigma$ be quantum states. Consider a very simple hypothesis testing strategy for guessing whether a given quantum system is in state $\rho$ or $\sigma$: Bob discards the state of the system and guesses "$\rho$" with probability $q$ and "$\sigma$" with probability $1 - q$.

   (a) What is the POVM corresponding to this strategy?
   (b) Evaluate the type-I and type-II error probabilities for this strategy.
   (c) If, in the symmetric setting, the prior probability for being given the state $\rho$ is $p \in [0,1]$, then evaluate the expected error probability for this strategy.

26. ★ Consider states $\rho$ and $\sigma$ along with a POVM $\{M_0, M_1\}$ representing a strategy for hypothesis testing of a single copy of the quantum system, where the outcome "0" corresponds to $\rho$ and the outcome "1" corresponds to $\sigma$. Let $p \in [0,1]$ be the prior probability of being given $\rho$, and let $n \in \{2, 3, \ldots\}$. Construct the POVM $\{M_\rho^{(n)}, M_\sigma^{(n)}\}$ and evaluate the type-I and type-II error probabilities for the following two strategies for hypothesis testing of $n$ copies of the quantum system.

   (a) The *majority-vote* strategy: (1) Measure each system according to the POVM $\{M_0, M_1\}$, and let $N_x$ be the number of times the outcome $x \in \{0, 1\}$ occurs; (2) If $N_0 > N_1$, guess "$\rho$", and if $N_1 > N_0$, guess "$\sigma$". If $n$ is even and $N_0 = N_1$, then guess "$\rho$" with probability $q \in [0,1]$ and "$\sigma$" with probability $1 - q$.

   (b) The *unanimous-vote* strategy: (1) Measure each system according to the POVM $\{M_0, M_1\}$, and let $N_x$ be the number of times the outcome $x \in \{0,1\}$ occurs. (2) If $N_0 = n$, then guess "$\rho$"; otherwise, guess "$\sigma$".

15

## Page 16

# Entanglement

1. Do each of the following state vectors represent a product state or an entangled state? If it represents a product state, give the factorization.
   
   (a) $\frac{1}{\sqrt{3}}\ket{0}\ket{+} + \sqrt{\frac{2}{3}}\ket{1}\ket{-}$.
   
   (b) $\frac{1}{4}\bigl(3\ket{0,0} - \sqrt{3}\ket{0,1} + \sqrt{3}\ket{1,0} - \ket{1,1}\bigr)$.
   
   (c) $\frac{1}{\sqrt{2}}\bigl(\ket{1,0} + i\ket{1,1}\bigr)$.
   
   (d) $\frac{1}{\sqrt{2}}\bigl(\ket{0,1} + \ket{1,0}\bigr)$.

2. Let $\ket{\Phi_d}$ be the state vector
$$\ket{\Phi_d} := \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k,k}. \tag{69}$$
   
   For every unitary operator $U$, prove that
$$(U \otimes \overline{U})\ket{\Phi_d} = \ket{\Phi_d}, \tag{70}$$
   
   where $\overline{U}$ denotes the complex conjugate of $U$.

3. Consider the state vector $\ket{\Psi^-}$ defined in (64). Prove that
$$(U \otimes U)\ket{\Psi^-}\bra{\Psi^-}(U \otimes U)^\dagger = \ket{\Psi^-}\bra{\Psi^-} \tag{71}$$
   
   for every single-qubit unitary $U$.

4. Consider the Bell state vectors as follows:
$$\ket{\Phi^+} = \frac{1}{\sqrt{2}}\bigl(\ket{0,0} + \ket{1,1}\bigr), \tag{72}$$
$$\ket{\Phi^-} = \frac{1}{\sqrt{2}}\bigl(\ket{0,0} - \ket{1,1}\bigr), \tag{73}$$
$$\ket{\Psi^+} = \frac{1}{\sqrt{2}}\bigl(\ket{0,1} + \ket{1,0}\bigr), \tag{74}$$
$$\ket{\Psi^-} = \frac{1}{\sqrt{2}}\bigl(\ket{0,1} - \ket{1,0}\bigr). \tag{75}$$
   
   (a) Show that when the $X$ gate is applied to either qubit of $\ket{\Psi^+}$, the result is $\ket{\Phi^+}$ up to a global phase.
   
   (b) Show that when the $X$ gate is applied to either qubit of $\ket{\Phi^+}$, the result is $\ket{\Psi^+}$ up to a global phase.
   
   (c) Show that when the $X$ gate is applied to either qubit of $\ket{\Psi^-}$, the result is $\ket{\Phi^-}$ up to a global phase.
   
   (d) Show that when the $X$ gate is applied to either qubit of $\ket{\Phi^-}$, the result is $\ket{\Psi^-}$ up to a global phase.

5. By calculating the Schmidt decomposition, and explicitly stating the Schmidt rank, determine whether the following state vectors are entangled.

16

## Page 17

(a) $\ket{\psi}_{AB} = \frac{1}{\sqrt{23/2}}\big(\ket{0,0} + i\ket{0,1} + (\frac{1}{2} - i)\ket{0,2} + (1+i)\ket{1,0} + 2\ket{1,1} + \frac{1}{2}i\ket{2,0} + (1+1i)\ket{2,2}\big)$.

(b) $\ket{\psi}_{AB} = \frac{1}{\sqrt{70}}\big(\ket{0,0} + 2\ket{0,1} + 3\ket{0,2} + i\ket{1,0} + (1+2i)\ket{1,1} + (1+3i)\ket{1,2} + (1+i)\ket{2,0} + (3+2i)\ket{2,1} + (4+3i)\ket{2,2}\big)$.

(c) $\ket{\psi}_{AB} = \frac{1}{\sqrt{98}}\big(\ket{0,0} + 2\ket{0,1} + 3\ket{0,2} + i\ket{1,0} + 2i\ket{1,1} + 3i\ket{1,2} + (2+i)\ket{2,0} + (4+2i)\ket{2,1} + (6+3i)\ket{2,2}\big)$.

6. Prove that in the teleportation protocol, every outcome of Alice's measurement occurs with probability $\frac{1}{4}$, and carry out the calculation to determine the conditional state achieved by Bob (before his correction operation) for each of these measurement outcomes.

17

## Page 18

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

## Page 19

(d) If $\ket{a} = \ket{-}$ and $\ket{b} = \ket{-}$, then find the resulting state at the end of the circuit.

(e) Using your answers to the previous parts, explain why this circuit calculates the parity of the first two qubits in the $X$ basis.

8. Prove that $U_1 := Z^{-1/4} X^{1/4}$ and $U_2 := H^{-1/2} Z^{-1/4} X^{1/4} H^{1/2}$ can be written solely as a product of $H$ and $T$. Recall that $H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ and $T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$.

9. Let us use the following notation for the swap gate:

$$\text{[swap gate symbol: two crosses connected vertically]} \tag{79}$$

Show that the swap gate can be written in terms of three CNOT gates as follows:

$$\text{[swap]} = \text{[CNOT with control on top, target bottom; then CNOT with control bottom, target top; then CNOT with control on top, target bottom]} \tag{80}$$

10. Show that the controlled-$Z$ gate can be written in terms of the Hadamard gate and the CNOT gate as follows:

$$\text{[controlled-Z gate]} = \text{[H on target, then CNOT, then H on target]} \tag{81}$$

11. Show that the control and target qubits of the CNOT gate can be changed by adding Hadamard gates before and after as follows:

$$\text{[CNOT with control on bottom, target on top]} = \text{[H on both wires, then CNOT (control top, target bottom), then H on both wires]} \tag{82}$$

12. Prove the following circuit identities.

(a) $\text{CNOT}(X \otimes \mathbb{1}) = (X \otimes X)\text{CNOT}$.

$$\text{[X on top wire, then CNOT (control top, target bottom)]} = \text{[CNOT, then X on both top and bottom wires]} \tag{83}$$

(b) $\text{CNOT}(\mathbb{1} \otimes X) = (\mathbb{1} \otimes X)\text{CNOT}$.

$$\text{[X on bottom wire, then CNOT]} = \text{[CNOT, then X on bottom wire]} \tag{84}$$

(c) $\text{CNOT}(Z \otimes \mathbb{1}) = (Z \otimes \mathbb{1})\text{CNOT}$.

$$\text{[Z on top wire, then CNOT]} = \text{[CNOT, then Z on top wire]} \tag{85}$$

19

## Page 20

(d) $\text{CNOT}(\mathbb{1} \otimes Z) = (Z \otimes Z)\text{CNOT}$.

$$
\begin{array}{c}
[\text{Circuit: top wire is control (dot), bottom wire has } Z \text{ then target } \oplus] \quad = \quad [\text{Circuit: top wire is control (dot) then } Z; \text{ bottom wire is target } \oplus \text{ then } Z]
\end{array}
\tag{86}
$$

13. Consider the following circuit:

$$
\begin{array}{c}
\ket{0} - H - \bullet - \times - \measuredangle \\
\ket{0} - S - H - \times - \measuredangle
\end{array}
\tag{87}
$$

[Two-qubit circuit: top qubit $\ket{0}$, then $H$, then control of a CZ (vertical line connecting both wires), then SWAP (×), then measurement. Bottom qubit $\ket{0}$, then $S$, then $H$ (after the CZ control acts on top, the controlled gate target is on bottom — actually the vertical line connects the dot on top to bottom wire after $S$), then $H$, then SWAP, then measurement.]

The final measurement is in the Pauli-$Z$ basis. What is the probability of obtaining each outcome?

14. Consider the following circuit:

$$
\begin{array}{c}
\ket{0} - H - \bullet - \bullet - H - \measuredangle \\
\ket{0} - H - \bullet - \bullet - H - \measuredangle \\
\ket{\psi} - \oplus - S - \oplus -
\end{array}
\tag{88}
$$

[Three-qubit circuit. Top qubit: $\ket{0}$, $H$, control, control, $H$, measurement. Middle qubit: $\ket{0}$, $H$, control, control, $H$, measurement. Bottom qubit: $\ket{\psi}$, target $\oplus$ (controlled by both top qubits via Toffoli), $S$, target $\oplus$ (Toffoli again).]

The final measurement is in the Pauli-$Z$ basis.

(a) Show that the probability of both measurement outcomes being 0 is $\frac{5}{8}$.

(b) Show that the circuit applies the gate $R_z(\theta)$ to the third qubit if the measurement outcomes are both 0, where $\theta$ is given by $\cos(\theta) = \frac{3}{5}$; otherwise, the circuit applies $Z$ to the third qubit.

15. Recall the following circuit for the Hadamard test:

$$
\begin{array}{c}
\ket{0} - H - \bullet - H - \measuredangle \\
\ket{\psi} - U -
\end{array}
\tag{89}
$$

Here, $U$ is an arbitrary unitary and can act on an arbitrary number of qubits. Using this circuit, it is possible to determine the real part of $\braket{\psi|U|\psi}$, i.e., $\text{Re}(\braket{\psi|U|\psi})$.

Now, show that by adding the $S$ gate as follows, it is possible to also calculate the imaginary part of the inner product, namely, $\text{Im}(\braket{\psi|U|\psi})$.

$$
\begin{array}{c}
\ket{0} - H - S - \bullet - H - \measuredangle \\
\ket{\psi} - U -
\end{array}
\tag{90}
$$

20

## Page 21

16. The Mølmer–Sørensen (MS) gate is a two-qubit gate that can be naturally implemented on trapped-ion quantum computers. It transforms $Z$-basis states as follows:

$$\ket{0,0} \mapsto \frac{1}{\sqrt{2}}\left(\ket{0,0} + \mathrm{i}\ket{1,1}\right), \tag{91}$$

$$\ket{0,1} \mapsto \frac{1}{\sqrt{2}}\left(\ket{0,1} - \mathrm{i}\ket{1,1}\right), \tag{92}$$

$$\ket{1,0} \mapsto \frac{1}{\sqrt{2}}\left(\ket{1,0} - \mathrm{i}\ket{0,1}\right), \tag{93}$$

$$\ket{1,1} \mapsto \frac{1}{\sqrt{2}}\left(\ket{1,1} + \mathrm{i}\ket{0,0}\right). \tag{94}$$

Write the MS gate as a matrix.

17. The Clifford group generating set, $\{\text{CNOT}, H, S\}$ is not universal for quantum computation. Give three ways to modify the set so that it is universal for quantum computation.

## Page 22

## Quantum error correction

1. A logical qubit is in the state given by the vector $\ket{\psi} = \frac{\sqrt{3}}{2}\ket{0_L} + \frac{1}{2}\ket{1_L}$. We encode the logical qubit into three physical qubits according to $\ket{0_L} = \ket{0,0,0}$ and $\ket{1_L} = \ket{1,1,1}$. You suspect that a partial bit flip has occurred to one of the qubits, so you measure the parity of adjacent qubits.

    (a) If $\mathrm{parity}(q_1, q_2) = 0$ and $\mathrm{parity}(q_0, q_1) = 0$, what quantum gate(s), if any, should you apply to fix the error?

    (b) If $\mathrm{parity}(q_1, q_2) = 0$ and $\mathrm{parity}(q_0, q_1) = 1$, what quantum gate(s), if any, should you apply to fix the error?

    (c) If $\mathrm{parity}(q_1, q_2) = 1$ and $\mathrm{parity}(q_0, q_1) = 0$, what quantum gate(s), if any, should you apply to fix the error? If $\mathrm{parity}(q_1, q_2) = 1$ and $\mathrm{parity}(q_0, q_1) = 1$, what quantum gate(s), if any, should you apply to fix the error?

22
