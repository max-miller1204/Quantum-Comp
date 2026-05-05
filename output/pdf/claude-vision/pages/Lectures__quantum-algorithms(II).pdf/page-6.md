$$\ket{\psi_{\text{init}}} = \ket{0}\ket{\psi}\ket{\phi} \xmapsto{H} \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{\psi}\ket{\phi} + \ket{1}\ket{\psi}\ket{\phi}\right)$$

$H\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$

$$\xmapsto{\text{CSWAP}} \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{\psi}\ket{\phi} + \ket{1}\ket{\phi}\ket{\psi}\right)$$

$$\xmapsto{H} \tfrac{1}{2}\left(\ket{+}\ket{\psi}\ket{\phi} + \ket{-}\ket{\phi}\ket{\psi}\right) \qquad \ket{\pm} = \tfrac{1}{\sqrt{2}}(\ket{0}\pm\ket{1})$$

$\{\ket{0}\bra{0}, \ket{1}\bra{1}\}.$

$$\ket{\psi_{\text{final}}} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\tfrac{1}{\sqrt{2}}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}) + \ket{1}\tfrac{1}{\sqrt{2}}(\ket{\psi}\ket{\phi}-\ket{\phi}\ket{\psi})\right)$$

$$= \tfrac{1}{2}\ket{0}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}) + \tfrac{1}{2}\ket{1}(\ket{\psi}\ket{\phi}-\ket{\phi}\ket{\psi})$$

Now measure — what is the probability of getting zero? (Recall partial measurements).

$\Pr[0] = \mathrm{Tr}\left[(\ket{0}\bra{0}\otimes \mathbb{1}\otimes \mathbb{1})\ket{\psi_{\text{final}}}\bra{\psi_{\text{final}}}\right].$

$\underbrace{\phantom{xxxxxxxxxx}}_{= \tfrac{1}{2}(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi})}$

$$= \tfrac{1}{4}\mathrm{Tr}\left[\underbrace{(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi})(\bra{\psi}\bra{\phi}+\bra{\phi}\bra{\psi})}_{\ket{v}}\right] \qquad \mathrm{Tr}[\ket{v}\bra{v}] = \braket{v|v}$$

$$= \tfrac{1}{4}\left(\bra{\psi}\bra{\phi}+\bra{\phi}\bra{\psi}\right)\left(\ket{\psi}\ket{\phi}+\ket{\phi}\ket{\psi}\right)$$

$$= \tfrac{1}{4}\Big(\underbrace{\braket{\psi|\psi}\braket{\phi|\phi}}_{=1} + \underbrace{\braket{\psi|\phi}\braket{\phi|\psi}}_{=|\braket{\psi|\phi}|^2} + \braket{\phi|\psi}\braket{\psi|\phi} + \underbrace{\braket{\phi|\phi}\braket{\psi|\psi}}_{=1}\Big)$$

$$\boxed{\Pr[0] = \tfrac{1}{2}\left(1 + |\braket{\psi|\phi}|^2\right)}$$

$$\Pr[1] = \tfrac{1}{2}\left(1 - |\braket{\psi|\phi}|^2\right)$$

❋ The probabilities contain the inner product!
   So how do we extract the value of the inner product?
   <u>We run the algorithm many times!</u>

- Each time we get outcome "0" → record $x_i = 1$  ⎫  ❋ This defines a <u>random</u>
- Each time we get outcome "1" → record $x_i = -1$ ⎭     <u>variable</u> $X$:
- Do this $N$ times, then take the <u>sample</u>
  <u>mean / average</u>: $\hat{x}_N = \tfrac{1}{N}\sum_{i=1}^{N} x_i$

$\Pr[X = \pm 1] = \tfrac{1}{2}\left(1 \pm |\braket{\psi|\phi}|^2\right).$
