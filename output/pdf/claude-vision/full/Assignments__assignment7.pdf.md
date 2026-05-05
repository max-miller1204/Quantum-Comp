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
