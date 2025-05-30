matriz = []

def mat(n):
    temp = []
    for i in range(n):
        temp.append([])
        for j in range(n):
            temp[i].append(0)
    return temp

def llenar(n):
    global matriz
    matriz = mat(n)
    for x in range(n):
        for y in range(n):
            matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str(y) + ']= '))

def gauss(n):
    for z in range(n - 1):
        # Pivoteo parcial
        if matriz[z][z] == 0:
            for i in range(z + 1, n):
                if matriz[i][z] != 0:
                    matriz[z], matriz[i] = matriz[i], matriz[z]
                    break

        for x in range(1, n - z):
            if matriz[z][z] != 0:
                p = matriz[x + z][z] / matriz[z][z]
                for y in range(n):
                    matriz[x + z][y] -= p * matriz[z][y]

def det(n):
    global matriz
    deter = 1
    for x in range(n):
        deter *= matriz[x][x]
    print("El determinante es: ", deter)