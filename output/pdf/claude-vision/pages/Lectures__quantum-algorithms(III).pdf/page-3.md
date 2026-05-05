$$\Pr[i] = \text{Tr}\left[\ket{v_i}\bra{v_i}\rho\right] \quad \text{(Born rule)} \quad = \bra{v_i}\rho\ket{v_i}$$

The <u>expected value</u> of the observable is:

$$\langle M \rangle_\rho = \sum_{i=1}^{\hat{n}} \lambda_i \Pr[i] = \sum_{i=1}^{\hat{n}} \lambda_i \text{Tr}\left[\ket{v_i}\bra{v_i}\rho\right] = \text{Tr}\left[\underbrace{\left(\sum_{i=1}^{\hat{n}} \lambda_i \ket{v_i}\bra{v_i}\right)}_{M}\rho\right] = \text{Tr}[M\rho].$$

[Red annotation pointing to the "=" sign: "Definition of expectation value!"]

- If we don't know the eigenvectors (b/c they are hard to get for large matrices!), but we know that $M$ can be written as

$$M = \sum_{j=1}^{k} c_j \underbrace{U_j}_{\text{unitaries}}, \quad \text{then} \quad \langle M \rangle_\gamma = \text{Tr}(M\ket{\gamma}\bra{\gamma})$$

$$= \sum_{j=1}^{k} c_j \text{Tr}(U_j \ket{\gamma}\bra{\gamma})$$

$$= \sum_{j=1}^{k} c_j \underbrace{\bra{\gamma}U_j\ket{\gamma}}_{\text{Estimate using Hadamard test!}}$$

So we estimate each term individually using the Hadamard test and then add to get an overall estimate of the expectation value.
