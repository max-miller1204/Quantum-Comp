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
