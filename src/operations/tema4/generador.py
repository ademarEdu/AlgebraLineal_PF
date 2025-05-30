def gauss_jordan_simbolico(matriz):
    n = len(matriz)
    m = len(matriz[0])
    nombres = ["x", "y", "z", "w", "u", "v", "t", "s", "r", "q"][:m]
    sol = ["" for _ in range(m)]

    # Paso 1: Gauss-Jordan
    fila = 0
    for col in range(m):
        if fila >= n:
            break
        # Buscar fila con pivote
        max_fila = fila
        for k in range(fila + 1, n):
            if abs(matriz[k][col]) > abs(matriz[max_fila][col]):
                max_fila = k
        if abs(matriz[max_fila][col]) < 1e-10:
            continue

        matriz[fila], matriz[max_fila] = matriz[max_fila], matriz[fila]
        pivote = matriz[fila][col]
        matriz[fila] = [v / pivote for v in matriz[fila]]

        for i in range(n):
            if i != fila:
                factor = matriz[i][col]
                matriz[i] = [a - factor * b for a, b in zip(matriz[i], matriz[fila])]

        fila += 1

    # Paso 2: Extraer ecuaciones simbólicas
    leading = [-1] * n
    for i in range(n):
        for j in range(m):
            if abs(matriz[i][j]) > 1e-10:
                leading[i] = j
                break

    pivots = set(leading) - {-1}
    libres = [i for i in range(m) if i not in pivots]

    for i in reversed(range(n)):
        j = leading[i]
        if j == -1:
            continue
        ecuacion = f"{nombres[j]} = "
        terms = []
        for k in libres:
            coef = -matriz[i][k]
            if abs(coef) > 1e-10:
                coef_str = f"{coef:+.2f}" if abs(coef) != 1 else ("+" if coef > 0 else "-")
                terms.append(f"{coef_str}{nombres[k]}")
        sol[j] = ecuacion + (" ".join(terms) if terms else "0")

    for k in libres:
        sol[k] = f"{nombres[k]} = {nombres[k]} (libre)"

    print("\n📐 Sistema simbólico del conjunto generador:")
    for eq in sol:
        print(eq)

def generar_ecuacion_conj_generador():
    print("\n--- ECUACIÓN DEL CONJUNTO GENERADOR (GAUSS-JORDAN SIMBÓLICO) ---\n")

    dimension = int(input("¿Cuál es la dimensión de los vectores? "))
    num_vectores = int(input("¿Cuántos vectores deseas ingresar? "))
    print()

    vectores = []
    for i in range(num_vectores):
        print(f"Vector {i+1}:")
        vector = []
        for j in range(dimension):
            val = float(input(f"  Componente {j+1}: "))
            vector.append(val)
        vectores.append(vector)
        print()

    # Matriz con columnas = vectores ⇒ convertimos a filas para resolver sistema homogéneo
    matriz = []
    for i in range(dimension):
        fila = []
        for v in vectores:
            fila.append(v[i])
        matriz.append(fila)

    print("\nResolviendo sistema homogéneo: x₁·v₁ + x₂·v₂ + ... + xₙ·vₙ = 0")
    gauss_jordan_simbolico(matriz)