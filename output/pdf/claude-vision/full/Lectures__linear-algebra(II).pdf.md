# Lectures__linear-algebra(II).pdf

## Page 1

## ① Recap

[Left: Bit diagram — vertical line with two dots labeled 0 (top) and 1 (bottom)]

**Bit**
0 or 1;
or probabilistic mixture

[Right: Bloch sphere with $\ket{0}$ at top, $\ket{1}$ at bottom, $\ket{+}$ on front, $\ket{-}$ on back, $\ket{+i}$ on right, $\ket{-i}$ on left]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$
$\alpha, \beta \in \mathbb{C},$
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

**Qubit**
$\ket{0}$ or $\ket{1}$;
or *superposition*

---

✱ States of live on the surface of the **Bloch sphere**. — they are described by 2-dimensional **state vectors**.

$$\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad \alpha, \beta \in \mathbb{C}, \quad \underbrace{|\alpha|^2}_{\Pr[0]} + \underbrace{|\beta|^2}_{\Pr[1]} = 1. \quad \longrightarrow \quad \ket{\psi} = \alpha\ket{0} + \beta\ket{1}$$

$$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

(States **inside** the sphere are also possible — they are described by **density matrices**. We will see this later...)

## ② Complex Vector Spaces

$$\ket{v} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \longrightarrow \ket{v} = \sum_{k=1}^{d} a_k \ket{e_k}, \quad \ket{e_1} = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \ket{e_2} = \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, \ldots, \ket{e_d} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}$$

[Note in red: "Complex numbers!" pointing to $a_k$]

$$\bra{v} = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix} \longrightarrow \bra{v} = \sum_{k=1}^{d} \bar{a}_k \bra{e_k}.$$

$$\ket{v} = \sum_{k=0}^{d-1} a_k \ket{k}, \quad \ket{u} = \sum_{k=0}^{d-1} b_k \ket{k}$$

$$\braket{v|u} = \left( \sum_{k=0}^{d-1} \bar{a}_k \bra{k} \right) \left( \sum_{k'=0}^{d-1} b_{k'} \ket{k'} \right)$$

## Page 2

$$\ket{v} = \sum_{k=0}^{d-1} a_k \ket{k} \;\to\; \braket{k'|v} = \bra{k'}\left(\sum_{k=0}^{d-1} a_k \ket{k}\right)$$

$$= \sum_{k=0}^{d-1} a_k \underbrace{\braket{k'|k}}_{\delta_{k,k'}}$$

$$= a_{k'}$$

$$= \sum_{k,k'=0}^{d-1} \overline{a_k}\, b_{k'} \underbrace{\braket{k|k'}}_{\delta_{k,k'}}$$

$$= \sum_{k=0}^{d-1} \overline{a_k}\, b_k$$

## Page 3

※ <u>Notation</u>: $\ket{e_1} \equiv \ket{0}, \ket{e_2} \equiv \ket{1}, \ldots, \ket{e_d} \equiv \ket{d-1}$ → The "standard basis" or "computational basis".

For a qubit: $\ket{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \alpha\ket{0} + \beta\ket{1}.$

$$\alpha = \braket{0|\psi}, \quad \beta = \braket{1|\psi}$$

- Addition of vectors:

$$\ket{v_1} = \sum_{k=0}^{d-1} a_k \ket{k}, \quad \ket{v_2} = \sum_{k=0}^{d-1} b_k \ket{k} \implies \ket{v_1} + \ket{v_2} = \sum_{k=0}^{d-1} (a_k + b_k)\ket{k}.$$

- Inner product of vectors is given by $\braket{v_1|v_2}$.

$$\ket{v_1} = \sum_{k=0}^{d-1} a_k \ket{k}, \quad \ket{v_2} = \sum_{k=0}^{d-1} b_k \ket{k} \longrightarrow \braket{v_1|v_2} = \underbrace{\left(\sum_{k=0}^{d-1} \bar{a}_k \bra{k}\right)}_{\bra{v_1}} \underbrace{\left(\sum_{k'=0}^{d-1} b_{k'} \ket{k'}\right)}_{\ket{v_2}}$$

$$\delta_{k,k'} = \begin{cases} 1 & \text{if } k = k' \\ 0 & \text{if } k \neq k' \end{cases} \qquad = \sum_{k,k'=0}^{d-1} \bar{a}_k b_{k'} \underbrace{\braket{k|k'}}_{=\delta_{k,k'}} = \sum_{k=0}^{d-1} \bar{a}_k b_k.$$

- The <u>norm</u> of a vector is $\| \ket{v} \| = \sqrt{\braket{v|v}} = \left(\sum_{k=0}^{d-1} |a_k|^2\right)^{1/2}.$

$$\left( \ket{v} = \sum_{k=0}^{d-1} a_k \ket{k} \right) \qquad \qquad \downarrow \\ \qquad \qquad \qquad a_k \cdot \bar{a}_k$$

We call a vector "normalized" if $\| \ket{v} \| = 1.$

※ To normalize a vector, just divide by its norm!

$$\ket{v} = \sum_{k=0}^{d-1} a_k \ket{k} \rightarrow \| \ket{v} \| = \left(\sum_{k=0}^{d-1} |a_k|^2\right)^{1/2} \implies \ket{\tilde{v}} = \frac{1}{\| \ket{v} \|} \cdot \ket{v} = \frac{1}{\| \ket{v} \|} \sum_{k=0}^{d-1} a_k \ket{k}$$

$$= \sum_{k=0}^{d-1} \frac{a_k}{\| \ket{v} \|} \ket{k}$$

<u>Check</u>: $\braket{\tilde{v}|\tilde{v}} = \left(\frac{1}{\| \ket{v} \|} \sum_{k=0}^{d-1} \bar{a}_k \bra{k}\right) \left(\frac{1}{\| \ket{v} \|} \sum_{k'=0}^{d-1} a_{k'} \ket{k'}\right)$

## Page 4

$$= \frac{1}{\||v\rangle\|^2} \underbrace{\sum_{k=0}^{d-1} |a_k|^2}_{= \||v\rangle\|^2}$$

$$= \frac{1}{\||v\rangle\|^2} \cdot \||v\rangle\|^2$$

$$= 1 \checkmark$$

- **Tensor product of vectors**: Used to describe the state of multiple qubits. (and entanglement!).

  - One qubit: 2-dimensional vector: $|\psi\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$.

  - If qubit 1 has state $|\psi_1\rangle$ and qubit 2 has state $|\psi_2\rangle$, then the **joint state** is given by

$$|\psi_1\rangle \otimes |\psi_2\rangle = \underbrace{\begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}}_{|\psi_1\rangle} \otimes \underbrace{\begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix}}_{|\psi_2\rangle} = \begin{pmatrix} \alpha_1 \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix} \\ \beta_1 \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} \alpha_1 \alpha_2 \\ \alpha_1 \beta_2 \\ \beta_1 \alpha_2 \\ \beta_1 \beta_2 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

(4-dimensional vector!)

$\underset{\color{red}\text{tensor/Kronecker product}}{\color{red}\uparrow}$

⊛ **Abstract notation**: $|\psi_1\rangle = \alpha_1|0\rangle + \beta_1|1\rangle,\ |\psi_2\rangle = \alpha_2|0\rangle + \beta_2|1\rangle$

$$\Rightarrow |\psi_1\rangle \otimes |\psi_2\rangle = \big(\alpha_1|0\rangle + \beta_1|1\rangle\big) \otimes \big(\alpha_2|0\rangle + \beta_2|1\rangle\big)$$

[red arrows indicate distributing the tensor product across all four cross-terms]

$$= \alpha_1\alpha_2 |0\rangle\otimes|0\rangle + \alpha_1\beta_2 |0\rangle\otimes|1\rangle + \beta_1\alpha_2 |1\rangle\otimes|0\rangle + \beta_1\beta_2 |1\rangle\otimes|1\rangle$$

**Recall:** $|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\ |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \Rightarrow \underline{|0\rangle\otimes|0\rangle} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix};\ \underline{|0\rangle\otimes|1\rangle} = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$

## Page 5

$\ket{1}\otimes\ket{0} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}$, $\ket{1}\otimes\ket{1} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$ → This defines the vector space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

✲ $\{\ket{0}\otimes\ket{0}, \ket{0}\otimes\ket{1}, \ket{1}\otimes\ket{0}, \ket{1}\otimes\ket{1}\}$ is the standard/computational basis for $\mathbb{C}^2 \otimes \mathbb{C}^2$. (Just all two-bit strings!)

✲ Probabilities: $\Pr[0,0] = |\alpha_1\alpha_2|^2$, $\Pr[0,1] = |\alpha_1\beta_2|^2$, $\Pr[1,0] = |\beta_1\alpha_2|^2$, $\Pr[1,1] = |\beta_1\beta_2|^2$.

✲ This extends to any dimension!

For $\mathbb{C}^{d_1} \otimes \mathbb{C}^{d_2}$, basis is $\{\ket{k_1}\otimes\ket{k_2} : k_1 \in \{0,1,\ldots,d_1-1\}, k_2 \in \{0,1,\ldots,d_2-1\}\}$
Dimension is $d_1 \cdot d_2$.

✲ Shorthand notation: $\ket{k_1}\otimes\ket{k_2} \equiv \ket{k_1}\ket{k_2} \equiv \ket{k_1, k_2}$.

– Tensor product of three vectors:

$$\ket{\psi_1} = \begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}, \quad \ket{\psi_2} = \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix}, \quad \ket{\psi_3} = \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix}$$

$$\Rightarrow \ket{\psi_1}\otimes\ket{\psi_2}\otimes\ket{\psi_3} = \big(\ket{\psi_1}\otimes\ket{\psi_2}\big)\otimes\ket{\psi_3} = \ket{\psi_1}\otimes\big(\ket{\psi_2}\otimes\ket{\psi_3}\big).$$

$$= \begin{pmatrix} \alpha_1\alpha_2 \\ \alpha_1\beta_2 \\ \beta_1\alpha_2 \\ \beta_1\beta_2 \end{pmatrix} \otimes \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} = \begin{pmatrix} \alpha_1\alpha_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \alpha_1\beta_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \beta_1\alpha_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \beta_1\beta_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} \alpha_1\alpha_2\alpha_3 \\ \alpha_1\alpha_2\beta_3 \\ \alpha_1\beta_2\alpha_3 \\ \alpha_1\beta_2\beta_3 \\ \beta_1\alpha_2\alpha_3 \\ \beta_1\alpha_2\beta_3 \\ \beta_1\beta_2\alpha_3 \\ \beta_1\beta_2\beta_3 \end{pmatrix} \begin{matrix} 000 \\ 001 \\ 010 \\ 011 \\ 100 \\ 101 \\ 110 \\ 111 \end{matrix}$$

✲ The resulting vector has dimension $8 = 2 \cdot 2 \cdot 2 = 2^3$!

✲ The vector space is $\mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^2$.

## Page 6

✻ **Abstract notation:** $\ket{\psi_1} = \alpha_1\ket{0} + \beta_1\ket{1}$, $\ket{\psi_2} = \alpha_2\ket{0} + \beta_2\ket{1}$, $\ket{\psi_3} = \alpha_3\ket{0} + \beta_3\ket{1}$

$$\Rightarrow \ket{\psi_1} \otimes \ket{\psi_2} \otimes \ket{\psi_3} = \big(\alpha_1\ket{0} + \beta_1\ket{1}\big) \otimes \big(\alpha_2\ket{0} + \beta_2\ket{1}\big) \otimes \big(\alpha_3\ket{0} + \beta_3\ket{1}\big)$$

$$= \big(\alpha_1\alpha_2\ket{0,0} + \alpha_1\beta_2\ket{0,1} + \beta_1\alpha_2\ket{1,0} + \beta_1\beta_2\ket{1,1}\big) \otimes \big(\alpha_3\ket{0} + \beta_3\ket{1}\big)$$

$$= \alpha_1\alpha_2\alpha_3\ket{0,0,0} + \alpha_1\alpha_2\beta_3\ket{0,0,1} + \alpha_1\beta_2\alpha_3\ket{0,1,0} + \alpha_1\beta_2\beta_3\ket{0,1,1}$$
$$+ \beta_1\alpha_2\alpha_3\ket{1,0,0} + \beta_1\alpha_2\beta_3\ket{1,0,1} + \beta_1\beta_2\alpha_3\ket{1,1,0} + \beta_1\beta_2\beta_3\ket{1,1,1}$$

— **Arbitrary number of tensor products:**

$$\ket{\psi_j} = \sum_{k=0}^{1} C_{j,k}\ket{k} = C_{j,0}\ket{0} + C_{j,1}\ket{1}$$

$$\rightarrow \underbrace{\ket{\psi_1} \otimes \ket{\psi_2} \otimes \cdots \otimes \ket{\psi_n}}_{\text{vector in } (\mathbb{C}^2)^{\otimes n}} = \bigotimes_{j=1}^{n}\ket{\psi_j} = \sum_{k_1,k_2,\ldots,k_n=0}^{1} C_{1,k_1} C_{2,k_2} \cdots C_{n,k_n} \ket{k_1, k_2, \ldots, k_n}$$

✻ **Generalizes to arbitrary dimension!** $\ket{\psi_j} = \sum_{k=0}^{d_j-1} C_{j,k}\ket{k}$

$$\Rightarrow \underbrace{\bigotimes_{j=1}^{n} \ket{\psi_j}}_{\text{Vector in } \mathbb{C}^{d_1} \otimes \mathbb{C}^{d_2} \otimes \cdots \otimes \mathbb{C}^{d_n}} = \sum_{k_1=0}^{d_1-1} \sum_{k_2=0}^{d_2-1} \cdots \sum_{k_n=0}^{d_n-1} C_{1,k_1} C_{2,k_2} \cdots C_{n,k_n} \ket{k_1, k_2, \ldots, k_n}$$

— **Basis of $n$-qubit space $(\mathbb{C}^2)^{\otimes n}$ is labeled by all $n$-bit strings.**

$$(\mathbb{C}^2)^{\otimes n} = \mathrm{span}\big\{\ket{\vec{x}} : \underbrace{\vec{x} \in \{0,1\}^n}_{\text{Set of all $n$-bit strings.}}\big\}$$

**Notation:** $\vec{x} \in \{0,1\}^n \Rightarrow \vec{x} = (x_1, x_2, \ldots, x_n)$, $x_i \in \{0,1\}$

$$\ket{\vec{x}} = \ket{x_1, x_2, \ldots, x_n} \equiv \ket{x_1} \otimes \ket{x_2} \otimes \cdots \otimes \ket{x_n}$$

## Page 7

- **Example:** $n=2 \to \{\ket{0,0}, \ket{0,1}, \ket{1,0}, \ket{1,1}\}$

  $n=3 \to \{\ket{0,0,0}, \ket{0,0,1}, \ket{0,1,0}, \ket{0,1,1}, \ket{1,0,0}, \ket{1,0,1}, \ket{1,1,0}, \ket{1,1,1}\}.$

- Tensor product and inner product.

  By definition: $(\bra{v_1} \otimes \bra{v_2})(\ket{u_1} \otimes \ket{u_2}) = \braket{v_1|u_1} \cdot \braket{v_2|u_2}.$

  $$\braket{0,1,0|1,1,0} = \underbrace{\braket{0|1}}_{=0}\underbrace{\braket{1|1}}_{=1}\underbrace{\braket{0|0}}_{=1}$$

- **Example:** for basis vectors,
  $$\braket{0,1,0|1,0,1} = \underbrace{\braket{0|1}}_{=0} \cdot \underbrace{\braket{1|0}}_{=0} \cdot \underbrace{\braket{0|1}}_{=0} = 0.$$

  In general: for basis vectors $\ket{\vec{x}}, \ket{\vec{y}}$, $\vec{x} = (x_1, x_2, \ldots, x_n) \in \{0,1\}^n$
  $$\vec{y} = (y_1, y_2, \ldots, y_n) \in \{0,1\}^n$$

  $$\braket{\vec{x}|\vec{y}} = \delta_{\vec{x},\vec{y}} = \delta_{x_1,y_1}\,\delta_{x_2,y_2}\cdots \delta_{x_n,y_n}$$

- Probabilities: For a state of $n$ qubits given by

  $$\ket{\psi} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}} \to \text{Normalization condition is } \sum_{\vec{x} \in \{0,1\}^n} |c_{\vec{x}}|^2 = 1.$$

  Probabilities are: $\Pr[\vec{x}] = |c_{\vec{x}}|^2 = \braket{\vec{x}|\psi}$

## ③ Matrices: Linear Transformations of Vectors

(✱) Matrices will be used to define and describe states inside the Bloch sphere (i.e., mixed states) and the gates we can apply to qubits on a quantum computer.

## Page 8

⊛ We also call matrices <u>linear operators / transformations</u>.

– <u>2×2 matrices</u>:  $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $a,b,c,d \in \mathbb{C}$.

- Multiplying a matrix with a vector: $\ket{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$

$$M\ket{v} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} av_1 + bv_2 \\ cv_1 + dv_2 \end{pmatrix}$$

- Matrices act linearly as follows:  $M(\alpha \ket{v_1} + \beta \ket{v_2}) = \underline{\alpha M \ket{v_1} + \beta M \ket{v_2}}$

$$= \begin{pmatrix} \alpha a & \alpha b \\ \alpha c & \alpha d \end{pmatrix}$$

- Matrix multiplication: $M_1 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix}$, $M_2 = \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix}$

$$M_1 \cdot M_2 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix} \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} = \begin{pmatrix} a_1 a_2 + b_1 c_2 & a_1 b_2 + b_1 d_2 \\ c_1 a_2 + d_1 c_2 & c_1 b_2 + d_1 d_2 \end{pmatrix}$$

- Abstract notation from vectors extends to matrices!

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} + d\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

⊛ <u>Recall</u>:  $\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ → $\bra{0} = (1\ 0)$, $\bra{1} = (0\ 1)$

⊛ <u>Observe</u>: $\ket{0}\bra{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}(1\ 0) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $\ket{0}\bra{1} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}(0\ 1) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$

$\underbrace{\phantom{xx}}_{2\times 1}\underbrace{\phantom{xx}}_{1\times 2}$

## Page 9

$$\ket{1}\bra{0} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad \ket{1}\bra{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

Then $\;M = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}\quad$ $\begin{aligned} a &= \braket{0|M|0}, & c &= \braket{1|M|0} \\ b &= \braket{0|M|1}, & d &= \braket{1|M|1} \end{aligned}$

This makes multiplication easier! (No need to remember matrix multiplication rules).

$$M\ket{v} = \big(a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}\big)\big(v_1\ket{0} + v_2\ket{1}\big)$$

$$= av_1\underbrace{\ket{0}\braket{0|0}}_{1} + av_2\ket{0}\underbrace{\braket{0|1}}_{0} + bv_1\ket{0}\underbrace{\braket{1|0}}_{0} + bv_2\underbrace{\ket{0}\braket{1|1}}_{1}$$

$$\quad + cv_1\underbrace{\ket{1}\braket{0|0}}_{1} + cv_2\ket{1}\underbrace{\braket{0|1}}_{0} + dv_1\ket{1}\underbrace{\braket{1|0}}_{0} + dv_2\underbrace{\ket{1}\braket{1|1}}_{1}$$

$$= (av_1 + bv_2)\ket{0} + (cv_1 + dv_2)\ket{1}$$

$$= \begin{pmatrix} av_1 + bv_2 \\ cv_1 + dv_2 \end{pmatrix} \checkmark \quad (\text{just as before!})$$

- **Arbitrary $d \times d$ matrices:**

$$M = \sum_{i,j=0}^{d-1} M_{i,j}\,\ket{i}\bra{j}$$

$\uparrow$ entry in the $i^{\text{th}}$ row and $j^{\text{th}}$ column. (complex number)

$$\braket{k|M|\ell} = \bra{k}\left(\sum_{i,j=0}^{d-1} M_{i,j}\,\ket{i}\bra{j}\right)\ket{\ell}$$

$$= \sum_{i,j=0}^{d-1} M_{i,j}\,\underbrace{\braket{k|i}}_{\delta_{k,i}}\underbrace{\braket{j|\ell}}_{\delta_{j,\ell}} = M_{k,\ell}$$

$$M_1 = \sum_{i,j=0}^{d-1} M^{(1)}_{i,j}\,\ket{i}\bra{j} \qquad M_2 = \sum_{i,j=0}^{d-1} M^{(2)}_{i,j}\,\ket{i}\bra{j}$$

$$M_1 \cdot M_2 = \left(\sum_{i_1,j_1=0}^{d-1} M^{(1)}_{i_1,j_1}\,\ket{i_1}\bra{j_1}\right)\left(\sum_{i_2,j_2=0}^{d-1} M^{(2)}_{i_2,j_2}\,\ket{i_2}\bra{j_2}\right)$$

$$= \sum_{i_1,j_1=0}^{d-1}\sum_{i_2,j_2=0}^{d-1} M^{(1)}_{i_1,j_1} M^{(2)}_{i_2,j_2}\,\ket{i_1}\underbrace{\braket{j_1|i_2}}_{\delta_{j_1,i_2}}\bra{j_2} = \sum_{i_1,j_2=0}^{d-1}\left(\sum_{j_1=0}^{d-1} M^{(1)}_{i_1,j_1} M^{(2)}_{j_1,j_2}\right)\ket{i_1}\bra{j_2}$$
