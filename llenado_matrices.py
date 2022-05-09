print("Escibre el tamaño de la matriz")

filas = int(input("Filas:  "))
columnas = int(input("Columnas:  "))

M1 = []


for i in range(filas):
    M1.append([0])
    for h in range(columnas):
        entrada = float(input("Fila {}, Columna {} :  ",format(i + 1, h + 1)))
        M1[i].append(entrada)
    

#To print the matrix
print(M1)


matrix_length = len(M1)
for i in range(matrix_length):
    print(M1[i][-1])