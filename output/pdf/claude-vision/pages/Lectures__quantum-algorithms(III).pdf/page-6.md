$$\downarrow \quad \rightarrow \delta_{j,k}$$

$$= \frac{1}{d}\sum_{k'=0}^{d-1} e^{\frac{2\pi i}{d} k'(k-j)}$$

with $\underbrace{(k-j)}_{\equiv x}$

[Sketch: sine and cosine waves over $[0, 2\pi]$ on the same axis]

① If $x = 0 \rightarrow \dfrac{1}{d}\sum_{k'=0}^{d-1}(1) = 1$

② If $x \neq 0 \rightarrow \dfrac{1}{d}\sum_{k'=0}^{d-1} \omega^{k'x} \rightarrow (\omega^x)^{k'}$

$$(\omega^x)^d = e^{\frac{2\pi i}{d}\cdot d \cdot x} = e^{2\pi i x} = \underbrace{\cos(2\pi x)}_{=1\,\forall x} + i\underbrace{\sin(2\pi x)}_{=0\,\forall x}$$

$$\omega = e^{\frac{2\pi i}{d}}, \qquad \omega^x = e^{\frac{2\pi i x}{d}}, \qquad \omega^{xd} = e^{2\pi i x} = 1$$

$$= \underbrace{\frac{1}{d}\sum_{k'=0}^{d-1}(\omega^x)^{k'}}_{\text{Finite geometric series!}} = \frac{1}{d}\left(\frac{1-(\omega^x)^d}{1-\omega}\right) = 0.$$

$$\sum_{k=0}^{d-1} r^{k'} = \frac{1-r^d}{1-r}$$

③ So $\dfrac{1}{d}\sum_{k'=0}^{d-1} \omega^{k'(k-j)} = \delta_{j-k,\,0} = \delta_{j,k}$

$$\Rightarrow \;\; QQ^\dagger = \sum_{k,j=0}^{d-1} \underbrace{\left(\frac{1}{d}\sum_{k'=0}^{d-1}\omega^{k'(k-j)}\right)}_{\delta_{k,j}} \ket{k}\bra{j} = \mathbb{1} \;\checkmark$$

Similarly, $Q^\dagger Q = \mathbb{1}$.

$$Q = \frac{1}{\sqrt{d}}\begin{pmatrix} 1 & 1 & 1 & \cdots & 1 \\ 1 & \omega & \omega^2 & \cdots & \omega^{d-1} \\ 1 & \omega^2 & \omega^4 & \cdots & \omega^{2(d-1)} \\ \vdots & \vdots & & & \vdots \\ 1 & \omega^{d-1} & \omega^{2(d-1)} & \cdots & \omega^{(d-1)^2} \end{pmatrix}$$
