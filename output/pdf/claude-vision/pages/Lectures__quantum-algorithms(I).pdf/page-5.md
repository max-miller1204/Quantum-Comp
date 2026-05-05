$$= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{\psi} - i\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})U\ket{\psi}\right)$$

$$= \frac{1}{2}\left(\ket{0}\ket{\psi} + \ket{1}\ket{\psi} - i\ket{0}U\ket{\psi} + i\ket{1}U\ket{\psi}\right)$$

$$= \frac{1}{2}\left(\ket{0}(\ket{\psi}-iU\ket{\psi}) + \ket{1}(\ket{\psi}+iU\ket{\psi})\right) \longrightarrow (\ket{\psi}-iU\ket{\psi})^\dagger = \bra{\psi} + i\bra{\psi}U^\dagger$$

$$\Rightarrow \Pr[0] = \frac{1}{4}\left(\bra{\psi}+i\bra{\psi}U^\dagger\right)\left(\ket{\psi}-iU\ket{\psi}\right) = \frac{1}{4}\Big(\underbrace{\braket{\psi|\psi}}_{=1} - i\braket{\psi|U|\psi} + i\braket{\psi|U^\dagger|\psi}$$

$$+ \underbrace{\braket{\psi|U^\dagger U|\psi}}_{\substack{=\mathbb{1}\\=1}}\Big)$$

$$= \frac{1}{4}\Big(1 - i\underbrace{\braket{\psi|U|\psi}}_{z} + i\underbrace{\overline{\braket{\psi|U|\psi}}}_{\bar z} + 1\Big) \qquad \left(z - \bar z = x+iy - x+iy = 2iy\right)$$

$$= \frac{1}{4}\left(2 - i\underbrace{\left(\braket{\psi|U|\psi} - \overline{\braket{\psi|U|\psi}}\right)}_{= 2i\,\mathrm{Im}(\braket{\psi|U|\psi})}\right)$$

$$= \frac{1}{2}\Big(1 + \underbrace{\mathrm{Im}(\braket{\psi|U|\psi})}_{\alpha}\Big)$$

$$\Pr[1] = \frac{1}{2}\Big(1 - \underbrace{\mathrm{Im}(\braket{\psi|U|\psi})}_{\alpha}\Big)$$

$\rightarrow$ Then same procedure as above to estimate $\alpha$!
$$\Pr[0] = \tfrac{1}{2}(1+\alpha), \quad \Pr[1] = \tfrac{1}{2}(1-\alpha).$$
