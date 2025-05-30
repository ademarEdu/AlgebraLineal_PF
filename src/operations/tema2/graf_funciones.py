# Función para graficar funciones de la forma lambda x: f(x)
import numpy as np
import matplotlib.pyplot as plt

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