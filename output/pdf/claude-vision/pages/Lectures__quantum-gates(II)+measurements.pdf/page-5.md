- **Tracking the State of qubits through a circuit**

$$\ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$$

$$\ket{+}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{0}$$

[Circuit: top qubit $\ket{0}$ through $H$, then control of CNOT; bottom qubit $\ket{0}$ is target. Red arrows mark stages ① and ②.]

$$\ket{0}\ket{0} \xmapsto{\;①\;} H\ket{0}\ket{0} = \ket{+}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{0})$$

$$\xmapsto{\;②\;} \tfrac{1}{\sqrt{2}}\big(\underbrace{\text{CNOT}\ket{0}\ket{0}}_{\ket{0}\ket{0}} + \underbrace{\text{CNOT}\ket{1}\ket{0}}_{\ket{1}\ket{1}}\big)$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{1})$$

$$\ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0}-\ket{1})$$

[Circuit: top qubit $\ket{1}$ through $H$, then control of CNOT; bottom qubit $\ket{0}$ target. Stages ① and ②.]

$$\ket{1}\ket{0} \xmapsto{\;①\;} H\ket{1}\ket{0} = \ket{-}\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{0})$$

$$\xmapsto{\;②\;} \tfrac{1}{\sqrt{2}}\big(\text{CNOT}\ket{0}\ket{0} - \text{CNOT}\ket{1}\ket{0}\big)$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{1})$$

---

[Three-qubit circuit: qubit 1 $\ket{0}$ — $H$ — • — — — $H$; qubit 2 $\ket{0}$ — $H$ — — • — $H$; qubit 3 $\ket{0}$ — — ⊕ — ⊕ — . Red arrows mark stages ①, ②, ③, ④.]

$$\ket{0}\ket{0}\ket{0} \xmapsto{\;①\;} \ket{+}\ket{+}\ket{0}$$

$$= \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\,\tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{0}$$

$$= \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{0} + \ket{1}\ket{0}\ket{0} + \ket{1}\ket{1}\ket{0}\big)$$

$$\xmapsto{\;②\;} \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{0} + \ket{1}\ket{0}\ket{1} + \ket{1}\ket{1}\ket{1}\big)$$

$$\xmapsto{\;③\;} \tfrac{1}{2}\big(\ket{0}\ket{0}\ket{0} + \ket{0}\ket{1}\ket{1} + \ket{1}\ket{0}\ket{1} + \ket{1}\ket{1}\ket{0}\big)$$

$$\xmapsto{\;④\;} \tfrac{1}{2}\big(\ket{+}\ket{+}\ket{0} + \ket{+}\ket{-}\ket{1} + \ket{-}\ket{+}\ket{1} + \ket{-}\ket{-}\ket{0}\big)$$

$$= \tfrac{1}{2}\Big(\underbrace{(\ket{+}\ket{+}+\ket{-}\ket{-})}_{(a)}\ket{0} + \underbrace{(\ket{+}\ket{-}+\ket{-}\ket{+})}_{(b)}\ket{1}\Big)$$

$$= \tfrac{1}{\sqrt{2}}\Big(\tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}+\ket{1}\ket{1})\ket{0} + \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0}-\ket{1}\ket{1})\ket{1}\Big)$$

(a) $\tfrac{1}{2}\big(\ket{0}\ket{0}+\ket{0}\ket{1}+\ket{1}\ket{0}+\ket{1}\ket{1}$
$\quad\quad +\ket{0}\ket{0}-\ket{0}\ket{1}-\ket{1}\ket{0}+\ket{1}\ket{1}\big)$
$= \ket{0}\ket{0} + \ket{1}\ket{1}$

(b) $\tfrac{1}{2}\big(\ket{0}\ket{0}-\ket{0}\ket{1}+\ket{1}\ket{0}-\ket{1}\ket{1}$
$\quad\quad +\ket{0}\ket{0}+\ket{0}\ket{1}-\ket{1}\ket{0}-\ket{1}\ket{1}\big)$
$= \ket{0}\ket{0} - \ket{1}\ket{1}$
