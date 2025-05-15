# Funciones de apoyo, como validación de entradas, añadir formato, etc.

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


def graph3D_vectors(vectors, title="Gráfica 3D de Vectores"):
    """
    Función para graficar vectores en 3D.

    Parameters:
        vectors(list): Lista de vectores a graficar. Los vectores deben ser listas, tuplas o numpy array de longitud 3.
        title(str): Título de la gráfica.

    Returns: 
        None

    Example:
        >>> graph3D_vectors([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        Ventana emergente con la gráfica 3D de los vectores.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for vector in vectors:
        ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], arrow_length_ratio=0.1)

    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_zlim([0, 10])
    ax.set_title(title)
    plt.show()

def graph2D_vectors(vectors, title="Gráfica 2D de Vectores"):
    """
    Función para graficar vectores en 2D.

    Parameters:
        vectors(list): Lista de vectores a graficar. Los vectores deben ser listas, tuplas o numpy array de longitud 2.
    
    Returns: 
        None

    Example:
        >>> graph2D_vectors([[1, 2], [3, 4], [5, 6]])
        Ventana emergente con la gráfica 2D de los vectores.
    """
    fig, ax = plt.subplots()

    for vector in vectors:
        ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1)

    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_title(title)
    plt.show()

def graph_functions(functions, title="Gráfica de Funciones"):
    """
    Función para graficar múltiples funciones matemáticas.

    Parameters:
        functions(list): Lista de funciones a graficar. Cada función debe aceptar un solo argumento.
        title(str): Título de la gráfica.

    Returns: 
        None

    Example:
        >>> graph_functions([lambda x: x**2, lambda x: x**3], title="Funciones Cuadrática y Cúbica")
        Ventana emergente con la gráfica de las funciones cuadrática y cúbica.
    """
    x = np.linspace(-10, 10, 100)

    for func in functions:
        y = func(x)
        plt.plot(x, y)

    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend([func.__name__ for func in functions])
    plt.show()