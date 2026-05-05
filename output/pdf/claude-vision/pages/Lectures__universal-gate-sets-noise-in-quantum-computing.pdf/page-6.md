$$(1-\alpha)\rho + \alpha X\rho X = \underbrace{(1-\alpha)\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)}_{\rho} + \alpha \underbrace{X\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z)X}_{\rho}$$

$$\underline{XY = -YX}$$
$$\underline{XZ = -ZX}$$

$$= \tfrac{1}{2}(X\mathbb{1}X + r_x \underbrace{XXX}_{=X^2 \cdot X = X} + r_y \underbrace{XYX}_{=-X^2 Y = -Y} + r_z \underbrace{XZX}_{=-X^2 Z = -Z})$$
$$\underbrace{= X^2}_{=\mathbb{1}}$$

$$= (1-\alpha)\tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z) + \alpha\tfrac{1}{2}(\mathbb{1} + r_x X - r_y Y - r_z Z)$$

$$= \tfrac{1}{2}\Big((1-\alpha+\alpha)\mathbb{1} + ((1-\alpha)r_x + \alpha r_x)X$$
$$\qquad + ((1-\alpha)r_y - \alpha r_y)Y$$
$$\qquad + ((1-\alpha)r_z - \alpha r_z)Z\Big)$$

$$= \tfrac{1}{2}(\mathbb{1} + \underbrace{r_x}_{r'_x = r_x} X + \underbrace{(1-2\alpha)r_y}_{r'_y} Y + \underbrace{(1-2\alpha)r_z}_{r'_z} Z).$$

<u>Check</u>: If $\rho = \ket{0}\bra{0}$, then $r_x = 0$, $r_y = 0$, $r_z = 1 \xrightarrow{\alpha=1} r'_x = 0,\; r'_y = 0,\; r'_z = -1$ ✓

- <u>Example</u>: Phase-flip / dephasing channel

$$\rho \mapsto \underbrace{(1-\alpha)\rho}_{\text{Do nothing with probability } 1-\alpha} + \underbrace{\alpha Z\rho Z}_{\text{Apply Pauli-}Z\text{ with probability }\alpha}.$$

(✱) Now how do the coordinates transform?

$$\rho = \tfrac{1}{2}(\mathbb{1} + r_x X + r_y Y + r_z Z) \longmapsto \rho' = \tfrac{1}{2}(\mathbb{1} + r'_x X + r'_y Y + r'_z Z)$$

$$r'_x = (1-2\alpha) r_x,\quad r'_y = (1-2\alpha) r_y,\quad r'_z = r_z.$$
