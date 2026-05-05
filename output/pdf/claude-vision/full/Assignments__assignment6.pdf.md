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
