#Multiplicacion de matrices recursivo


from ast import arg
from audioop import mul
import numpy as np

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,0]]

n = len(A)
C = np.empty((n, n))
def matrizRecursiva(A, B):

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        # print(A)
        C[0][0] = matrizRecursiva(A[0][0], B[0][0]) + matrizRecursiva(A[0][1], B[1][0])
        C[0][1] = matrizRecursiva(A[0][0], B[0][1]) + matrizRecursiva(A[0][1], B[1][1])
        C[1][0] = matrizRecursiva(A[1][0], B[0][0]) + matrizRecursiva(A[1][1], B[1][0])
        C[1][1] = matrizRecursiva(A[1][0], B[0][1]) + matrizRecursiva(A[1][1], B[1][1])

    return C

print(matrizRecursiva(A, B))
