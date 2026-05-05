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
