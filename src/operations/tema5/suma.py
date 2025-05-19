def suma(mA, mB):
    if len(mA) == len(mB) and len(mA[0]) == len(mB[0]):
    
        m3 = []
        for r in range(len(mA)):
            m3.append([])
            for c in range(len(mA[0])):
                m3[r].append(mA[r][c] + mB[r][c])
        return m3
    else:   
        return None
matrizS = suma(matrizA, matrizB)    
if matrizS == None:
    print("No se puede realizar la suma")
    print()

else:
    print("PRODUCTO SUMA")
    for r in matrizS:
        print("[", end="")
        for elemento in r:
            print("{:8.2f}" .format(elemento), end=" ")
        print("]")
        print