def gauss_pivot(A, b):
    n = len(A)      # número de ecuaciones (filas)
    m = len(A[0])   # número de incógnitas (columnas)

    # Aumentar la matriz A con la columna b
    for i in range(n):
        A[i].append(b[i])

    for i in range(min(n, m)):
        # Pivoteo parcial
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]

        if abs(A[i][i]) < 1e-10:
            continue  # Saltar fila si el pivote es 0

        # Eliminación hacia abajo
        for k in range(i+1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, m + 1):
                A[k][j] -= factor * A[i][j]

    # Verificación de compatibilidad (últimas filas: 0 ... 0 | b ≠ 0 → no hay solución)
    for i in range(n):
        izquierda = all(abs(A[i][j]) < 1e-10 for j in range(m))
        derecha = abs(A[i][m]) > 1e-10
        if izquierda and derecha:
            return False  # sistema inconsistente

    return True


def combinacion_lineal_check():
    print("\n--- COMBINACIÓN LINEAL: ¿ES O NO? ---\n")

    dimension = int(input("¿Cuál es la dimensión de los vectores? "))
    num_vectores = int(input("¿Cuántos vectores base deseas ingresar? "))
    print()

    columnas = []
    for i in range(num_vectores):
        print(f"Vector base {i+1}:")
        vector = []
        for j in range(dimension):
            val = float(input(f"  Componente {j+1}: "))
            vector.append(val)
        columnas.append(vector)
        print()

    # Transponer para tener A como matriz de filas por columnas
    A = [[col[i] for col in columnas] for i in range(dimension)]

    print("Vector objetivo:")
    b = []
    for i in range(dimension):
        val = float(input(f"  Componente {i+1}: "))
        b.append(val)

    A_copia = [fila[:] for fila in A]

    posible = gauss_pivot(A_copia, b)

    print()
    if posible:
        print("El vector objetivo SÍ es combinación lineal de los vectores base.")
    else:
        print("El vector objetivo NO es combinación lineal de los vectores base.")

