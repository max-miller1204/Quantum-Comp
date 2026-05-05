## ③ Quantum Fourier Transform

(a) <u>Recap</u>: discrete Fourier transform (DFT).

- Used in a lot of places!
    - Signal processing — identifying frequency components of a signal. (audio and video processing)
    - Machine learning — feature extraction
    - Scientific Computing — solving differential equations numerically.

- <u>Definition</u>: for a signal $\{x_k\}_{k=0}^{N-1}$, its DFT is

$$y_k = \frac{1}{\sqrt{N}} \sum_{k'=0}^{N-1} x_{k'}\, e^{\frac{2\pi i k' k}{N}} \qquad \left( e^{2\pi i x} = \cos(2\pi x) + i\sin(2\pi x) \right)$$

- <u>Example</u>: consider a signal of two sine waves put together:

$$x(t) = \sin(2\pi f_1 t) + \tfrac{1}{2}\sin(2\pi f_2 t)$$

with $f_1, f_2$ marked as <span style="color:purple">frequencies</span>.

- $f_1 = 5$ Hz
- $f_2 = 15$ Hz
- Sampling rate: $f_s = 100$ Hz $\Rightarrow$ 100 samples total (in 1 sec.)

[Three plots side by side:
1. "Time-Domain Signal" — continuous oscillating waveform, amplitude between -1 and 1, time 0 to 1 s.
2. "Time-Domain Signal (sampled)" — same waveform shown as discrete sample points connected by lines.
3. "Frequency-Domain Spectrum ($|y_k|$)" — magnitude vs frequency [Hz], with a tall spike of magnitude 1.0 at 5 Hz and a smaller spike of magnitude 0.5 at 15 Hz.]
