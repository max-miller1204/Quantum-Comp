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
