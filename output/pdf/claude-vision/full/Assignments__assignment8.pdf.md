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
