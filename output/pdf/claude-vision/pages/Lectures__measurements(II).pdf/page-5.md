For $n$ qubits: $\ket{\psi}_{A_1 A_2 \cdots A_n} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}}_{A_1 A_2 \cdots A_n}$

$$\hookrightarrow \equiv \ket{x_1, x_2, \ldots, x_n}_{A_1 A_2 \cdots A_n}$$
$$\equiv \ket{x_1}_{A_1} \otimes \ket{x_2}_{A_2} \otimes \cdots \otimes \ket{x_n}_{A_n}$$

- We do the same for linear operators (including density operators)

$M \in L(\mathbb{C}^d) \quad M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}) \to (d_A \cdot d_B) \times (d_A \cdot d_B)$ matrix

System $A$ has dimension $d_A$; $B$ has dimension $d_B$.

$$M_{AB} = \sum_{i,j=0}^{d_A - 1} \sum_{k,\ell=0}^{d_B - 1} M_{i,k;j,\ell} \, \ket{i,k}\bra{j,\ell}_{AB}$$

$$\hookrightarrow \equiv \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B \to \text{These form a basis for } L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}).$$

$$M_{A_1 A_2 \cdots A_n} \in L(\mathbb{C}^{d_{A_1}} \otimes \mathbb{C}^{d_{A_2}} \otimes \cdots \otimes \mathbb{C}^{d_{A_n}}) \to (d_{A_1} \cdot d_{A_2} \cdots d_{A_n}) \times (d_{A_1} \cdot d_{A_2} \cdots d_{A_n}) \text{ matrix.}$$

— Suppose we have a two-qubit density operator $\rho_{AB}$, and we measure the qubit $A$ in the computational basis.

Measurement operators are $\ket{0}\bra{0}$ and $\ket{1}\bra{1}$.

Probabilities are: 
$$\Pr[0] = \mathrm{Tr}\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B)\, \rho_{AB}\right]$$

$$\Pr[1] = \mathrm{Tr}\left[\underbrace{(\ket{1}\bra{1}_A \otimes \mathbb{1}_B)}_{\uparrow}\, \rho_{AB}\right]$$

We measure qubit $A$ only, so we apply the measurement operator only on $A$; we apply identity ("do nothing") on $B$.
