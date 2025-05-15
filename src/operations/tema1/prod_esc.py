# Función para realizar el producto escalar de un vector

def dot_product(vectors):
    """
    Función para calcular el producto punto de dos vectores.

    Parameters:
        vectors(list): Lista de dos vectores.

    Returns:
        float: Escalar obtenido de la operación.

    Example:
        >>> dot_product([[1, -2, 3, 4], [2, 3, -2, 1]])
        -6.0
    """
    v1 = vectors[0]
    v2 = vectors[1]

    # Calcular el producto punto
    dot = 0

    for i in range(len(v1)):
        dot += v1[i]*v2[i]

    return dot