def resta(matrizA, matrizB):
    if len(matrizA) == len(matrizB) and len(matrizA[0]) == len(matrizB[0]):
        print("PRODUCTO RESTA")
        for r in range(len(matrizA)):
            print("[", end="")
            for c in range(len(matrizA[0])):
                resultado = matrizA[r][c] - matrizB[r][c]
                print("{:8.2f}".format(resultado), end=" ")
            print("]")
        print()
    else:
        print("No se puede realizar la resta: dimensiones incompatibles.\n")