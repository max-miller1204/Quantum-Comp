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
