print()
def transpuesta(m):
    print("MATRIZ TRANSPUESTA")
    for r in range(len(m[0])):
        print("[", end="")
        for c in range(len(m)):
            print("{:8.2f}".format(m[c][r]), end=" ")
        print("]")
    print()