12. Messages relayed over a communication channel have probability $p$ of being received correctly. A message that is not received correctly is retransmitted until it is. What value should $p$ have so that the probability of more than one retransmission is less than $0.05$?

13. ★ Consider a discrete-time Markov chain consisting of four states, $a$, $b$, $c$, and $d$, whose transition probability matrix is given by
$$P = \begin{pmatrix} 0 & 0 & 0.8 & 0.2 \\ 0 & 0.4 & 0 & 0.3 \\ 1 & 0.6 & 0.2 & 0 \\ 0 & 0 & 0 & 0.5 \end{pmatrix} \tag{45}$$

   Compute the following probabilities.

   (a) $\Pr[X_4 = c, X_3 = c, X_2 = c, X_1 = c | X_0 = a]$
   (b) $\Pr[X_6 = d, X_5 = c, X_4 = b | X_3 = a]$
   (c) $\Pr[X_5 = c, X_6 = a, X_7 = c, X_8 = c | X_4 = b, X_3 = d]$.

14. ★ A Markov chain with two states, $a$ and $b$, has the following conditional probabilities: if it is in state $a$ at time step $t$, $t \in \{0, 1, 2, \dots\}$, then it stays in state $a$ with probability $\frac{1}{2}(\frac{1}{2})^t$. If it is in state $b$ at time step $t$, then it stays in state $b$ with probability $\frac{3}{4}(\frac{1}{4})^t$.

   (a) Determine the transition probability matrix of the Markov chain.
   (b) If the Markov chain begins in state $a$ at time step $t = 0$, then compute the probabilities of the following sample paths:
   $$a \to b \to a \to b \quad \text{and} \quad a \to a \to b \to b. \tag{46}$$

10
