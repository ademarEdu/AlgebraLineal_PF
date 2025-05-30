# Funcion para resolver un sitema de ecuaciones de la forma ax + by + ... = c
import numpy as np

def gauss_jordan_solve(mat):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Jordan.
    El argumento matrix debe ser una matriz numpy de tamaño (n, n+1).

    Parameters:
        mat(np.array): Matriz de numpy que representa los coeficientes (float) del sistema de ecuaciones y sus igualdades.

    Returns:
        numpy.ndarray: Solución del sistema de ecuaciones.

    Example:
        >>> gauss_jordan_solve([[4, 4, -8], [-3, 4, 11]])
        array([-19/7, 5/7])
    """
    n = mat.shape[0]

    for i in range(n):
        # Hacer el pivote igual a 1
        if mat[i, i] == 0:
            # Buscar una fila para intercambiar
            for k in range(i+1, n):
                if mat[k, i] != 0:
                    mat[[i, k]] = mat[[k, i]]
                    break
            else:
                raise ValueError("El sistema no tiene solución única.")
        mat[i] = mat[i] / mat[i, i]
        # Hacer ceros en la columna actual para otras filas
        for j in range(n):
            if j != i:
                mat[j] = mat[j] - mat[j, i] * mat[i]
    # Las soluciones están en la última columna
    return mat[:, -1].tolist()