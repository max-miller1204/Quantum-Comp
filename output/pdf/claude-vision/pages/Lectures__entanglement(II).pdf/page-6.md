$$= \ket{\Phi_d^+}$$

$$= \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k,k}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{k=1}^{d} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \braket{j | e_k} \braket{\ell | \bar{e}_k} \qquad \overline{\braket{e_k|\ell}} = \braket{e_k|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{k=1}^{d} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \braket{j|e_k}\braket{e_k|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \bra{j} \underbrace{\left( \sum_{k=1}^{d} \ket{e_k}\bra{e_k} \right)}_{= \mathbb{1}_d \text{ b/c } \{\ket{e_k}\} \text{ is ONB!}} \ket{\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j,\ell=0}^{d-1} \ket{j,\ell} \braket{j|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j=0}^{d-1} \ket{j,j}$$

$$\downarrow$$
$$= \ket{\Phi_d^+}. \qquad \underline{\underline{\quad}}$$

---

$$\frac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1})$$

$$\frac{1}{\sqrt{2}}(\underbrace{\ket{0}}_{\ket{e_1}}\underbrace{\ket{1}}_{\ket{f_1}} + \underbrace{\ket{1}}_{\ket{e_2}}\underbrace{\ket{0}}_{\ket{f_2}})$$

---

**(f) Vectorized unitaries are maximally entangled**

$$\ket{\gamma}_{AB} = (\mathbb{1} \otimes U)\ket{\Phi_d^+} = \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \underbrace{\ket{k}}_{\equiv \ket{e_k}} \otimes \underbrace{U\ket{k}}_{\equiv \ket{f_k}}$$

(↑ unitary)

Also, 
$$\mathrm{Tr}_A\!\left[\ket{\gamma}\bra{\gamma}_{AB}\right] = \mathrm{Tr}_A\!\left[(\mathbb{1}_A \otimes U_B) \overbrace{\Phi^+_{AB}}^{\ket{\Phi_d^+}\bra{\Phi_d^+}_{AB}} (\mathbb{1}_A \otimes U_B^\dagger)\right]$$

$$\downarrow$$
$$= U\, \mathrm{Tr}_A\!\left[\Phi^+_{AB}\right] U^\dagger \quad (*)$$
$$\qquad \searrow = \frac{\mathbb{1}_B}{d}$$

$$\downarrow$$
$$= \frac{1}{d} U U^\dagger$$

$$\downarrow$$
$$= \frac{1}{d} \mathbb{1}_B \qquad \left(\text{Similar for } \mathrm{Tr}_A[\ket{\gamma}\bra{\gamma}_{AB}]\right).$$

$(M \otimes \mathbb{1})(\mathbb{1} \otimes N)$
$\quad = (\mathbb{1} \otimes N)(M \otimes \mathbb{1})$

$(*):$
$$= \sum_{k=0}^{d-1} (\bra{k}_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes U_B)\Phi^+(\mathbb{1}_A \otimes U_B^\dagger)(\ket{k}_A \otimes \mathbb{1})$$

$$= \sum_{k=0}^{d-1} U_B \bra{k}_A \Phi^+_{AB} \ket{k}_A U_B^\dagger = U_B\, \mathrm{Tr}_A[\Phi^+_{AB}]\, U_B^\dagger$$
