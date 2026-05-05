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
