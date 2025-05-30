def readI(n):
    matriz = []
    for i in range(n):
        matriz.append([0] * n)
    for i in range(n):
        for j in range(n):
            print(f"Elemento [{i}][{j}]=")
            matriz[i][j] = float(input())
    return matriz

def printI(M):
    for fila in M:
        print(" ".join(f"{x:.4f}" for x in fila))
    print()

def gauss_jordan_inversa(A):
    n = len(A)
    aug = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]
    

    for i in range(n):
        if aug[i][i] == 0:
            for j in range(i + 1, n):
                if aug[j][i] != 0:
                    aug[i], aug[j] = aug[j], aug[i] 
                    break
            else:
                raise ValueError("La matriz no es invertible.")

        pivote = aug[i][i]
        for j in range(2 * n):
            aug[i][j] /= pivote

        for k in range(n):
            if k != i:
                factor = aug[k][i]
                for j in range(2 * n):
                    aug[k][j] -= factor * aug[i][j]

    inversa = [row[n:] for row in aug]
    return inversa