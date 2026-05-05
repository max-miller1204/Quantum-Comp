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
