import numpy as np

A = [ [3,5], [6,8] ]
B = [ [9,2], [1, 4] ]

n = len(A)

C = np.empty((n, n), int)

for i in range(n):
    for j in range(n):
        C[i][j] = 0
        for k in range(n):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

print(C)
