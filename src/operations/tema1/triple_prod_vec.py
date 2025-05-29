# Función para realizar el triple producto vectorial

from src.operations.tema1.prod_esc import dot_product
from src.operations.tema1.prod_vec import cross_product

def triple_cross_product(vectors):
    """
    Función para calcular el triple producto vectorial.
    La forma del triple producto vectorial es:

    vector_1 . ( vector_2 x vector_3 )

    Parameters:
        vectors(list): Lista de vectores (listas)

    Returns:
        float: Valor resultante del triple producto escalar
    """

    triple_cross = cross_product([vectors[0], cross_product([vectors[1], vectors[2]])])

    return triple_cross