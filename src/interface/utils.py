# Funciones de apoyo, como validación de entradas, añadir formato, etc.

def vector_input(dim):
    """
    Función para que el usuario ingrese un vector.

    Parameters:
        dim (int): El número de dimensiones del vector.

    Returns:
        list: Vector con el formato de una lista en python. 
    """
    # Crear un vector unitario de n dimensiones
    vec = [1 for i in range(dim)]

    # Obtener los valores del vector
    for i in range(dim):
        vec[i] *= validate_float_input(f"\nEscribe el valor del {i+1} componente de vector: ")
    return vec

def validate_input(prompt, valid_options):
    """
    Función para validar la entrada del usuario.

    Parameters:
        prompt (str): Mensaje que se mostrará al usuario.
        valid_options (list): Opciones válidas para la entrada.

    Returns:  
        str: Entrada válida del usuario.
    """
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            print(f"Entrada no válida. Por favor, elige entre {valid_options}.")

def validate_float_input(prompt):
    """
    Función para validar la entrada del usuario a solo números.

    Parameters:
        prompt (str): Mensaje que se mostrará al usuario.

    Returns:  
        float: Entrada válida del usuario.
    """
    while True:
        user_input = input(prompt)
        try:
            user_input = float(user_input)
            return user_input
        except:
            print("Entrada no válida. Por favor, ingresa un número.")

def validate_int_input(prompt):
    """
    Función para validar la entrada del usuario a solo números.

    Parameters:
        prompt (str): Mensaje que se mostrará al usuario.

    Returns:  
        float: Entrada válida del usuario.
    """
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except:
            print("Entrada no válida. Por favor, ingresa un número.")