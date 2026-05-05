- $p_1 = 1, p_2 = p_3 = p_4 = 0 \implies \rho_{AB} = \Phi^+_{AB} \implies$ entangled!

- $p_1 = 0, p_2 = 1, p_3 = p_4 = 0 \implies \rho_{AB} = \Phi^-_{AB} \implies$ entangled!

- $p_1 = p_2 = 0, p_3 = 1, p_4 = 0 \implies \rho_{AB} = \Psi^+_{AB} \implies$ entangled!

- $p_1 = p_2 = p_3 = 0, p_4 = 1 \implies \rho_{AB} = \Psi^-_{AB} \implies$ entangled!

- <u>But</u>: $p_1 = p_2 = p_3 = p_4 = \frac{1}{4} \implies \rho_{AB} = \frac{1}{4}\Phi^+_{AB} + \frac{1}{4}\Phi^-_{AB} + \frac{1}{4}\Psi^+_{AB} + \frac{1}{4}\Psi^-_{AB} = \frac{1}{4}\mathbb{1}_A \otimes \mathbb{1}_B$

  $\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ B/c Bell states form ONB.

  $\implies$ <u>not</u> entangled!

- General criterion: <u>Positive Partial Transpose (PPT) criterion</u>

<u>Recall</u>: Transpose of a matrix (flip rows and columns).

$\quad$ In Bra-ket notation: $\quad M = \sum_{i,j=0}^{d-1} m_{i,j} \ket{i}\bra{j}$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad M^T = \sum_{i,j=0}^{d-1} m_{i,j} \ket{j}\bra{i} \quad \rightsquigarrow (M^T)^T = M.$

$\quad$ For $M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B})$: $\quad M_{AB} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i}\bra{i'}_A \otimes \ket{j}\bra{j'}_B.$

$\quad$ <u>Partial transpose on A</u>: $\quad M_{AB}^{T_A} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i'}\bra{i}_A \otimes \ket{j}\bra{j'}_B.$

$\quad$ <u>Partial transpose on B</u>: $\quad M_{AB}^{T_B} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i}\bra{i'}_A \otimes \ket{j'}\bra{j}_B.$

$\quad$ <u>Full transpose</u>: $M_{AB}^T = M_{AB}^{T_A T_B} \implies M_{AB}^{T_A} = (M_{AB}^{T_B})^T$

$\quad\quad (M_{AB}^{T_A})^{T_A} = M_{AB} \quad\quad (M_{AB}^{T_B})^T = (M_{AB}^{T_B})^{T_A T_B} = M_{AB}^{T_A}$
