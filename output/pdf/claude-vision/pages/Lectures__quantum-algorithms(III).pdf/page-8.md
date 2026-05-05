Consider $n=3$: $\mathcal{Q}\ket{j_1, j_2, j_3} = \left(\frac{1}{\sqrt{2}}\sum_{k_1 \in \{0,1\}} e^{2\pi i k_1 \frac{j}{2}}\ket{k_1}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_2 \in \{0,1\}} e^{2\pi i k_2 \frac{j}{2^2}}\ket{k_2}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_3 \in \{0,1\}} e^{2\pi i k_3 \frac{j}{2^3}}\ket{k_3}\right)$

$$j = 4j_1 + 2j_2 + j_3 \implies \frac{j}{2} = 2j_1 + j_2 + \frac{j_3}{2}$$

$$\frac{j}{2^2} = \frac{j}{4} = j_1 + \frac{j_2}{2} + \frac{j_3}{4}$$

$$\frac{j}{2^3} = \frac{j}{8} = \frac{j_1}{2} + \frac{j_2}{4} + \frac{j_3}{8}$$

$$\implies e^{2\pi i k_1 \frac{j}{2}} = \underbrace{e^{2\pi i k_1 (2j_1)}}_{=1} \underbrace{e^{2\pi i k_1 j_2}}_{=1} e^{2\pi i k_1 \frac{j_3}{2}} = e^{\pi i k_1 j_3} = (-1)^{k_1 j_3}$$

$$e^{2\pi i k_2 \frac{j}{4}} = \underbrace{e^{2\pi i k_2 j_1}}_{=1} \underbrace{e^{2\pi i k_2 (\frac{j_2}{2})}}_{=(-1)^{k_2 j_2}} \underbrace{e^{2\pi i k_2 (\frac{j_3}{4})}}_{= e^{\frac{2\pi i}{4} k_2 j_3}}$$

$$e^{2\pi i k_3 \frac{j}{8}} = \underbrace{e^{\frac{2\pi i}{2} k_3 j_1}}_{(-1)^{k_3 j_1}} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3}$$

Therefore: $\mathcal{Q}\ket{j_1, j_2, j_3} = \left(\frac{1}{\sqrt{2}}\sum_{k_1 \in \{0,1\}} (-1)^{k_1 j_3} \ket{k_1}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_2 \in \{0,1\}} (-1)^{k_2 j_2} e^{\frac{2\pi i}{4} k_2 j_3} \ket{k_2}\right)$

$$\left(\frac{1}{\sqrt{2}}\sum_{k_3 \in \{0,1\}} (-1)^{k_3 j_1} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3} \ket{k_3}\right)$$

$$= \frac{1}{\sqrt{2^3}} \sum_{k_1, k_2, k_3 \in \{0,1\}} (-1)^{k_1 j_3} (-1)^{k_2 j_2} (-1)^{k_3 j_1} e^{\frac{2\pi i}{4} k_2 j_3} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3} \ket{k_1, k_2, k_3}$$

$$= \widetilde{\mathcal{Q}} \ket{j_3, j_2, j_1}$$

$R_z(\theta) = e^{i\frac{\theta}{2} Z} = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}$ [illegible: factor]

✱ Define the rotation gate $R_k = \begin{pmatrix} 1 & 0 \\ 0 & e^{\frac{2\pi i}{2^k}} \end{pmatrix}$ $\quad R_2 = \begin{pmatrix} 1 & 0 \\ 0 & e^{\frac{2\pi i}{4}} \end{pmatrix}$

[Quantum circuit diagram enclosed in dashed purple box, labeled $\widetilde{\mathcal{Q}}$ below:
- Top wire $\ket{j_3}$: passes through control, then $R_3$ gate, then $R_2$ gate, then $H$
- Middle wire $\ket{j_2}$: $R_2$ gate, then control, then $H$, then control
- Bottom wire $\ket{j_1}$: $H$, then control, then control
]

$\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$

$e^{\frac{\pi i}{2}} = i$
