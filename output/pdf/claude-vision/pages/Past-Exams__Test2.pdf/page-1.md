1. (a) Determine whether the following $2 \times 2$ matrices are unitary matrices.

   i. $M = \begin{pmatrix} \frac{3}{5} & \frac{4i}{5} \\ \frac{4i}{5} & \frac{3}{5} \end{pmatrix}$  $\quad C_1 = \begin{pmatrix} 3/5 \\ \frac{4i}{5} \end{pmatrix}$  $\quad C_2 = \begin{pmatrix} \frac{4i}{5} \\ 3/5 \end{pmatrix}$
   
   [marked: $\boxed{-2}$]
   
   $\rightarrow U^T U = I$
   
   $\rightarrow \begin{pmatrix} 3/5 & -\frac{4i}{5} \end{pmatrix} \begin{pmatrix} \frac{4i}{5} \\ 3/5 \end{pmatrix} = \frac{12i}{25} + \text{[...]}$

   ii. $M = \begin{pmatrix} \frac{2+i}{3} & \frac{2i}{3} \\ \frac{2i}{3} & \frac{2-i}{3} \end{pmatrix}$  $\quad C_1 = \begin{pmatrix} \frac{2+i}{3} \\ \frac{2i}{3} \end{pmatrix}$  $\quad C_2 = \begin{pmatrix} \frac{2i}{3} \\ \frac{2-i}{3} \end{pmatrix}$
   
   [marked: $\boxed{-2}$]
   
   $\rightarrow \begin{pmatrix} \frac{2-i}{3} & -\frac{2i}{3} \end{pmatrix} \begin{pmatrix} \frac{2i}{3} \\ \frac{2-i}{3} \end{pmatrix} = \begin{pmatrix} \frac{2-i}{3} \end{pmatrix}\begin{pmatrix} \frac{2i}{3} \end{pmatrix}$

   (b) Calculate the partial trace $\mathrm{Tr}_B[M_{AB}]$ of the following two-qubit matrices.

$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$

   i. $M_{AB} = \begin{pmatrix} \frac{1}{2}-\frac{1}{3}i & \frac{2}{3}+\frac{3}{4}i & -\frac{5}{7} & \frac{1}{2}i \\ -\frac{4}{3} & \frac{7}{5}-\frac{2}{5}i & \frac{1}{9}+\frac{2}{3}i & 0 \\ \frac{1}{8} & \frac{4}{5}i & -\frac{2}{11} & \frac{6}{7}+\frac{3}{8}i \\ \frac{2}{9}i & \frac{1}{6} & -\frac{1}{7}i & \frac{3}{2}-\frac{1}{6}i \end{pmatrix}$
   
   [marked: $\boxed{-2}$]
   
   $\mathrm{Tr}_B(M_{AB}) = \begin{pmatrix} a+d & 0 \\ 0 & a+d \end{pmatrix}$

   ii. $M_{AB} = \begin{pmatrix} \frac{3}{5} & \frac{1}{2}-\frac{1}{4}i & 0 & \frac{1}{3}i \\ \frac{1}{2}+\frac{1}{4}i & \frac{2}{3} & \frac{4}{7}i & 0 \\ 0 & -\frac{4}{7}i & 1 & -\frac{2}{9}+\frac{1}{2}i \\ -\frac{1}{3}i & 0 & -\frac{2}{9}-\frac{1}{2}i & \frac{4}{9} \end{pmatrix}$
   
   [marked: $\boxed{-1}$]
   
   $\mathrm{Tr}_B(M_{a3}) = \begin{pmatrix} \frac{12}{10} & -\frac{8}{15}i \\ & \\ & 0 \end{pmatrix}$

$\mathrm{Tr}_B[M_{AB}] = \begin{pmatrix} \frac{16}{5} & 0 \\ 0 & \frac{13}{9} \end{pmatrix}$

TOTAL: $\boxed{1-7}$

2
