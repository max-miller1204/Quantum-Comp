- We write the basis vectors as $\ket{e_k}$

$$\rightarrow \ket{v} = \sum_{k=1}^{d} a_k \ket{e_k} \quad \rightarrow \quad \bra{v} = \sum_{k=1}^{d} \bar{a}_k \bra{e_k} \quad \rightarrow \quad \braket{v|v} = \sum_{k=1}^{d} \bar{a}_k \cdot a_k = \sum_{k=1}^{d} |a_k|^2 = \| \ket{v} \|^2$$

$$\left( \sum_{k=1}^{d} \bar{a}_k \bra{e_k} \right) \left( \sum_{k'=1}^{d} a_{k'} \ket{e_{k'}} \right) = \sum_{k,k'=1}^{d} \bar{a}_k a_{k'} \braket{e_k | e_{k'}}$$

⊛ With this abstract notation, we do not have to explicitly write column vectors! (Helpful for large vectors — for $n$ qubits the size of the vectors is $2^n$!)
