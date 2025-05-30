def readM(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)
    for i in range(filas):
        for j in range(columnas):
            print(f"Elemento [{i}][{j}]=")
            matriz[i][j] = float(input())
    return matriz

def printM(M):
    for fila in M:
        print(" ".join(f"{x:.4f}" for x in fila))
    print()

def scalar_multiplication(k, M):
    # Crear una nueva matriz para almacenar el resultado
    R = [[k * M[i][j] for j in range(len(M[i]))] for i in range(len(M))]
    return R