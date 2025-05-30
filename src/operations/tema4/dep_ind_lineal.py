def gauss_dependencia(A):
    n = len(A)        # filas
    m = len(A[0])     # columnas

    # Matriz aumentada con columna 0s (sistema homogéneo)
    for i in range(n):
        A[i].append(0)

    rango = 0
    for i in range(min(n, m)):
        # Pivote
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]

        if abs(A[i][i]) < 1e-10:
            continue  # Sin pivote válido

        rango += 1

        # Eliminación
        for k in range(i+1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, m+1):
                A[k][j] -= factor * A[i][j]

    # Si rango < número de vectores → hay solución no trivial
    return rango == m

def verificar_dependencia():
    print("\n--- DEPENDENCIA O INDEPENDENCIA LINEAL ---\n")

    dimension = int(input("¿Cuál es la dimensión de los vectores? "))
    num_vectores = int(input("¿Cuántos vectores deseas ingresar? "))
    print()

    columnas = []
    for i in range(num_vectores):
        print(f"Vector {i+1}:")
        vector = []
        for j in range(dimension):
            val = float(input(f"  Componente {j+1}: "))
            vector.append(val)
        columnas.append(vector)
        print()

    # Reorganizar como matriz de filas (por dimensión)
    A = [[col[i] for col in columnas] for i in range(dimension)]

    A_copia = [fila[:] for fila in A]
    independiente = gauss_dependencia(A_copia)

    print()
    if independiente:
        print("Los vectores son linealmente INDEPENDIENTES.")
    else:
        print("Los vectores son linealmente DEPENDIENTES.")