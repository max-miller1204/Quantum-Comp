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
