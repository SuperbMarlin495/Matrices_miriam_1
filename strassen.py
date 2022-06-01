def dividir_matrix(A):
    mid = len(A)//2
    m_11 = [M[:mid] for M in A[:mid]]
    m_12 = [M[mid:] for M in A[:mid]]
    m_21 = [M[:mid] for M in A[mid:]]
    m_22 = [M[mid:] for M in A[mid:]]

    return (m_11, m_12, m_21, m_22)
def mezclar_matrix(matrix_11, matrix_12, matrix_21, matrix_22):
    matrix_total = []
    rows1 = len(matrix_11)
    rows2 = len(matrix_21)
    for i in range(rows1):
        matrix_total.append(matrix_11[i] + matrix_12[i])
    for j in range(rows2):
        matrix_total.append(matrix_21[j] + matrix_22[j])
    return matrix_total

def sum_matrix(X, Y):
    n = len(X)
    if n == 1:
        return [[X[0][0] + Y[0][0]]]
    S = []
    for i in range(n):
        S.append([])
        for j in range(n):
            S[i].append(X[i][j] + Y[i][j])
    return S

def rest_matrix(X, Y):
    n = len(X)
    if n == 1:
        return [[X[0][0] - Y[0][0]]]
    S = []
    for i in range(n):
        S.append([])
        for j in range(n):
            S[i].append(X[i][j] - Y[i][j])
    return S

def strassen(X, Y):
    if len(X) == 1:
        return [[X[0][0] * Y[0][0] ]]
    else:
        A, B, C, D = dividir_matrix(X)
        E, F, G, H = dividir_matrix(Y)

        P1 = strassen(A, rest_matrix(F, H))
        P2 = strassen(sum_matrix(A, B), H)
        P3 = strassen(sum_matrix(C, D), E)
        P4 = strassen(D, rest_matrix(G, E))
        P5 = strassen(sum_matrix(A, D), sum_matrix(E, H))
        P6 = strassen(rest_matrix(B, D), sum_matrix(G, H))
        P7 = strassen(rest_matrix(A, C), sum_matrix(E, F))

        Z11 = sum_matrix(rest_matrix(sum_matrix(P5, P4), P2), P6)
        Z12 = sum_matrix(P1, P2)
        Z21 = sum_matrix(P3, P4)
        Z22 = rest_matrix(rest_matrix(sum_matrix(P5, P1), P3), P7)

        return mezclar_matrix(Z11, Z12, Z21, Z22)


# A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# B = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,0]]

A = [ [3,5,4,2], [6,8,1,2], [9,8,2,3], [4,3,1,3] ]
B = [ [9,2,3,5], [1, 4,3,4], [2, 6,6,3], [5, 8,9,8] ]

print("Strassen")
print(*strassen(A,B), sep='\n')
