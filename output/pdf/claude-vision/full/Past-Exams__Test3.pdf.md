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
