# Funcionalidad del CLI para el tema 5

# Importar las funciones necesarias
from src.interface.utils import validate_input
from src.operations.tema5.suma import suma
from src.operations.tema5.resta import resta
from src.operations.tema5.prod_esc import readM, printM, scalar_multiplication
from src.operations.tema5.multip import multiplicacion
from src.operations.tema5.inversa import readI, printI, gauss_jordan_inversa
from src.operations.tema5.transpuesta import transpuesta

# Operaciones disponibles
operaciones = ["Suma de matrices",
    "Resta de matrices",
    "Producto de matriz por escalar",
    "Multiplicación de matrices",
    "Inversa de matrices",
    "Transposición de matrices",
    "Regresar"
    ]

def tema_5():
    print("\nHas escogido el tema 5\n")

    # Mostrar las operaciones disponibles
    for i in range(len(operaciones)):
        print(f"{i+1}. {operaciones[i]}")

    prompt = "\nEscribe el número de la operación que deseas calcular (del 1 al 7): "
    valid_options = [str(i) for i in range(1, len(operaciones) + 1)]
    # Preguntar al usuario por la operación
    choice = validate_input(prompt, valid_options)
    choice = int(choice) - 1  # Convertir a índice de lista

    if choice == 0:
    # Llamar a la función para la suma de matrices
        R1 = int (input("Ingrese el número de filas de la matriz A: "))
        C1 = int (input("Ingrese el número de columnas de la matriz A: "))
        print()
        R2 = int (input("Ingrese el número de filas de la matriz B: "))
        C2 = int (input("Ingrese el número de columnas de la matriz B: "))
        print()

        matrizA = []
        matrizB = []

        print ("Ingrese los elementos de la matriz A:")
        for r in range(R1):
            matrizA.append([])
            for c in range(C1):
                valor = float(input("Renglon {}, Columna {} : " .format(r+1, c+1)))
                matrizA[r].append(valor)

        print("Ingrese los elementos de la matriz B:")
        for r in range(R2):
            matrizB.append([])
            for c in range(C2):
                valor = float(input("Renglon {}, Columna {} : " .format(r+1, c+1)))
                matrizB[r].append(valor)
        print()
        print("La matriz A es:")
        for R in matrizA:
            print("[", end="")
            for elemento in R:
                print("{:8.2f}" .format(elemento), end=" ")
            print("]")
        print()

        print("La matriz B es:")
        for R in matrizB:
            print("[", end="")
            for elemento in R:
                print("{:8.2f}" .format(elemento), end=" ")
            print("]")
        print()

        suma(matrizA, matrizB)

                
    elif choice == 1:
        # Llamar a la función para el producto de matriz por escalar
        R1 = int (input("Ingrese el número de filas de la matriz A: "))
        C1 = int (input("Ingrese el número de columnas de la matriz A: "))
        print()
        R2 = int (input("Ingrese el número de filas de la matriz B: "))
        C2 = int (input("Ingrese el número de columnas de la matriz B: "))
        print()

        matrizA = []
        matrizB = []

        print ("Ingrese los elementos de la matriz A:")
        for r in range(R1):
            matrizA.append([])
            for c in range(C1):
                valor = float(input("Renglon {}, Columna {} : " .format(r+1, c+1)))
                matrizA[r].append(valor)

        print("Ingrese los elementos de la matriz B:")
        for r in range(R2):
            matrizB.append([])
            for c in range(C2):
                valor = float(input("Renglon {}, Columna {} : " .format(r+1, c+1)))
                matrizB[r].append(valor)
        print()
        print("La matriz A es:")
        for R in matrizA:
            print("[", end="")
            for elemento in R:
                print("{:8.2f}" .format(elemento), end=" ")
            print("]")
        print()

        print("La matriz B es:")
        for R in matrizB:
            print("[", end="")
            for elemento in R:
                print("{:8.2f}" .format(elemento), end=" ")
            print("]")
        print()
        
        resta(matrizA, matrizB)


    elif choice == 2:
        # Llamar a la función para la multiplicación de matrices
        filas = int(input("Ingrese el número de filas: "))
        while filas <= 0:
            filas = int(input("Ingrese un número de filas mayor a 0: "))

        columnas = int(input("Ingrese el número de columnas: "))
        while columnas <= 0:
            columnas = int(input("Ingrese un número de columnas mayor a 0: "))

        # Leer la matriz
        A = readM(filas, columnas)
        print("\nMatriz original:")
        printM(A)

        # Leer el escalar
        k = float(input("Ingrese el valor del escalar: "))

        # Multiplicar la matriz por el escalar
        resultado = scalar_multiplication(k, A)
        print(f"\nPRODUCTO DE LA MATRIZ POR EL ESCALAR {k}:")
        printM(resultado)

        
    elif choice == 3:
        # Multiplicación de matrices
        R1 = int (input("Ingrese el número de filas de la matriz A: "))
        C1 = int (input("Ingrese el número de columnas de la matriz A: "))
        print()
        R2 = int (input("Ingrese el número de filas de la matriz B: "))
        C2 = int (input("Ingrese el número de columnas de la matriz B: "))
        print()

        matrizA = []
        matrizB = []

        print ("Ingrese los elementos de la matriz A:")
        for r in range(R1):
            matrizA.append([])
            for c in range(C1):
                valor = float(input("Renglon {}, Columna {} : " .format(r+1, c+1)))
                matrizA[r].append(valor)

        print("Ingrese los elementos de la matriz B:")
        for r in range(R2):
            matrizB.append([])
            for c in range(C2):
                valor = float(input("Renglon {}, Columna {} : " .format(r+1, c+1)))
                matrizB[r].append(valor)
        print()
        print("La matriz A es:")
        for R in matrizA:
            print("[", end="")
            for elemento in R:
                print("{:8.2f}" .format(elemento), end=" ")
            print("]")
        print()

        print("La matriz B es:")
        for R in matrizB:
            print("[", end="")
            for elemento in R:
                print("{:8.2f}" .format(elemento), end=" ")
            print("]")
        print()

        multiplicacion(matrizA, matrizB)

        

    elif choice == 4:
        # Llamar a la función para la inversa de matrices

        n = int(input("Ingrese el tamaño de la matriz: "))
        while n <= 0:
            n = int(input("Ingrese una dimension mayor a 0: "))
            print()

        A = readI(n)
        print("\nMatriz original:")
        printI(A)

        try:
            invM = gauss_jordan_inversa(A)
            print("MATRIZ INVERSA:")
            printI(invM)

        except ValueError as e:
            print(f"Error: {str(e)}")

        

    elif choice == 5:
        # Llamar a la función para la transposición de matrices

        R= int (input("Ingrese el número de filas de la matriz A: "))
        C= int (input("Ingrese el número de columnas de la matriz A: "))

        matriz=[]

        print ("Ingrese los elementos de la matriz A:")
        for r in range(R):
            matriz.append([])
            for c in range(C):
                valor = float(input("Renglon {}, Columna {} : " .format(r+1, c+1)))
                matriz[r].append(valor)

        print()
        print("La matriz A es:")
        for R in matriz:
            print("[", end="")
            for elemento in R:
                print("{:8.2f}" .format(elemento), end=" ")
            print("]")
            print()

        transpuesta(matriz)


    elif choice == 6:
        # Regresar al menú principal
        return True

    if validate_input("Quieres calcular más operaciones? (y/n): ", ["y", "n"]) == "y":
        return True

    return False
