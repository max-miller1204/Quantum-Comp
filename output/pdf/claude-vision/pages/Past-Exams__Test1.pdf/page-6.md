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
