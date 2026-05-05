- For a linear operator $M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B})$, the (full) trace is:

$$\text{Tr}[M_{AB}] = \sum_{k=0}^{d_A-1} \sum_{\ell=0}^{d_B-1} \braket{k,\ell|_{AB} M_{AB} | k,\ell}_{AB}. \quad \text{\color{red}(sum of the diagonal elements).}$$

<span style="color:red">(Recall that $\{\ket{k,\ell} : k \in \{0,1,\ldots,d_A-1\}, \ell \in \{0,1,\ldots,d_B-1\}\}$ is a basis.)</span>

<span style="color:blue">$\text{Tr}[M] = \sum_{k=0}^{d-1} \braket{k|M|k}$</span>

$$\text{Tr}[M_{AB}] = \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \big(\bra{k}_A \otimes \bra{\ell}_B\big) M_{AB} \big(\ket{k}_A \otimes \ket{\ell}_B\big).$$

- <u>Partial trace over B</u>: $\text{Tr}_B[M_{AB}] = \cancel{\sum_{k=0}^{d_A-1}}\sum_{\ell=0}^{d_B-1} \big(\cancel{\bra{k}_A}^{\;\mathbb{1}_A} \otimes \bra{\ell}_B\big) M_{AB} \big(\cancel{\ket{k}_A}^{\;\mathbb{1}_A} \otimes \ket{\ell}_B\big).$

  $$\downarrow$$
  $$= \sum_{\ell=0}^{d_B-1} \big(\mathbb{1}_A \otimes \bra{\ell}_B\big) M_{AB} \big(\mathbb{1}_A \otimes \ket{\ell}_B\big).$$

  ⊛ <u>Note</u>: the outcome is an operator! Not a scalar, like the full trace.

- <u>Partial trace over A</u>: $\text{Tr}_A[M_{AB}] = \sum_{k=0}^{d_A-1}\cancel{\sum_{\ell=0}^{d_B-1}} \big(\bra{k}_A \otimes \cancel{\bra{\ell}_B}^{\;\mathbb{1}_B}\big) M_{AB} \big(\ket{k}_A \otimes \cancel{\ket{\ell}_B}^{\;\mathbb{1}_B}\big).$

  $$\downarrow$$
  $$= \sum_{k=0}^{d_A-1} \big(\bra{k}_A \otimes \mathbb{1}_B\big) M_{AB} \big(\ket{k}_A \otimes \mathbb{1}_B\big).$$

  ⊛ <u>Note</u>: the outcome is an operator! Not a scalar, like the full trace.

- Some Properties:

(1) $\text{Tr}_A[M_A \otimes N_B] = \sum_{k=0}^{d_A-1} \big(\bra{k}_A \otimes \mathbb{1}_B\big)\big(M_A \otimes N_B\big)\big(\ket{k}_A \otimes \mathbb{1}_B\big).$

<span style="color:blue">$= \big(\bra{k}_A M_A \otimes \mathbb{1}_B \cdot N_B\big) = \bra{k}_A M_A \otimes N_B.$</span>

$$\downarrow$$
$$= \sum_{k=0}^{d_A-1} \braket{k|_A M_A | k}_A \, N_B$$
$$= \text{Tr}[M_A]\, N_B.$$

$$\left(\begin{array}{l} \circledast \text{ Property of tensor product:} \\ (M_1 \otimes M_2)(N_1 \otimes N_2) = M_1 N_1 \otimes M_2 N_2 \end{array}\right)$$

(2) $\text{Tr}_B[M_A \otimes N_B] = \text{Tr}[N_B]\, M_A.$

<span style="color:blue">$\big(\bra{k}_A M_A \otimes N_B\big)\big(\ket{k}_A \otimes \mathbb{1}_B\big) = \braket{k|M_A|k} \cdot N_B.$</span>
