(\*) $F_{AB}\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right) = \ket{\chi_2}_A \otimes \ket{\chi_1}_B.$

<u>Proof</u>: $F_{AB}\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right) = \left(\sum_{i,j=0}^{d-1} \ket{j}\bra{i}_A \otimes \ket{i}\bra{j}_B\right)\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right)$

$$= \sum_{i,j=0}^{d-1} \ket{j}\braket{i|\chi_1} \otimes \ket{i}\braket{j|\chi_2}$$

$$= \sum_{i,j=0}^{d-1} \ket{j}\braket{j|\chi_2} \otimes \ket{i}\braket{i|\chi_1}$$

$$= \underbrace{\left(\sum_{j=0}^{d-1} \ket{j}\bra{j}_A\right)}_{=\mathbb{1}_A}\ket{\chi_2}_A \otimes \underbrace{\left(\sum_{i=0}^{d-1} \ket{i}\bra{i}_B\right)}_{=\mathbb{1}_B}\ket{\chi_1}_B$$

$$= \ket{\chi_2}_A \otimes \ket{\chi_1}_B.$$

$p_1 = 1-p$
$p_2 = p_3 = p_4 = \frac{p}{3}.$

– <u>Isotropic state</u>: $\rho_{AB}^{(p)} = (1-p)\,\Phi_{AB}^+ + \frac{p}{3}\left(\Phi_{AB}^- + \Psi_{AB}^+ + \Psi_{AB}^-\right),\quad p \in [0,1].$

$$\rho_{AB}^{(p)} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{array}{cccc} 00 & 01 & 10 & 11 \end{array} \\ \left(\begin{array}{cccc} \frac{1-p}{2}+\frac{p}{6} & 0 & 0 & \frac{1-p}{2}-\frac{p}{6} \\ 0 & \frac{p}{3} & 0 & 0 \\ 0 & 0 & \frac{p}{3} & 0 \\ \frac{1-p}{2}-\frac{p}{6} & 0 & 0 & \frac{1-p}{2}+\frac{p}{6} \end{array}\right)$$

[Purple ovals/arrows indicate swapping the (00,11) anti-diagonal block with the (01,10) block under partial transpose]

$$\left(\rho_{AB}^{(p)}\right)^{T_B} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{array}{cccc} 00 & 01 & 10 & 11 \end{array} \\ \left(\begin{array}{cccc} \frac{1-p}{2}+\frac{p}{6} & 0 & 0 & 0 \\ 0 & \frac{p}{3} & \frac{1-p}{2}-\frac{p}{6} & 0 \\ 0 & \frac{1-p}{2}-\frac{p}{6} & \frac{p}{3} & 0 \\ 0 & 0 & 0 & \frac{1-p}{2}+\frac{p}{6} \end{array}\right)$$
