# Función para realizar el producto vectorial de un vector

def cross_product(vectors):
    """
    Función para calcular el producto vectorial de un vector.

    Parameters:
        vectors(list): Lista de 2 vectores del mismo tamaño.

    Returns:
        list: Vector después de ser multiplicado.

    Example:
        >>> cross_product([[1, 0, 0], [0, 1, 0]])
        [0, -0, 1]
    """
    v1 = vectors[0]
    v2 = vectors[1]

    vec = [1, 1, 1]

    # Calcular el producto punto
    vec[0] *= (v1[1]*v2[2]) - (v1[2]*v2[1])
    vec[1] *= -( v1[0]*v2[2] - v1[2]*v2[0] )
    vec[2] *= v1[0]*v2[1] - v1[1]*v2[0]    

    return vec
