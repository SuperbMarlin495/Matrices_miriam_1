#Multiplicacion de matrices

import numpy as np

# A = [ [3,5], [6,8] ]
# B = [ [9,2], [1, 4] ]


A = [ [2,0,1], [3,0,0], [5,1,1] ]
B = [ [1,0,1], [1,2,1], [1,1,0] ]


n = len(A)

C = np.empty((n, n), int)

for i in range(n):
    for j in range(n):
        C[i][j] = 0
        for k in range(n):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

print(C)
