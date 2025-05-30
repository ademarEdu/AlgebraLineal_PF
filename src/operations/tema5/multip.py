def multiplicacion(mA, mB):
    if len(mA[0]) == len(mB):
        print("COMBINACIONES")
        m3 = []
        for r in range(len(mA)):
            fila = []
            for c in range(len(mB[0])):
                total = 0
                for p in range(len(mA[0])):
                    print((r, c), (r, p), (c, p), (p, c))
                    total += mA[r][p] * mB[p][c]
                fila.append(total)
            m3.append(fila)

        print()
        print("MULTIPLICACIÓN DE DOS MATRICES")
        for r in m3:
            print("[", end="")
            for elemento in r:
                print("{:8.2f}".format(elemento), end=" ")
            print("]")
        print()
    else:
        print("No se puede realizar la multiplicación\n")

