# Funciones de apoyo, como validación de entradas, añadir formato, etc.

def validate_input(prompt, valid_options):
    """
    Función para validar la entrada del usuario.
    :param prompt: Mensaje que se mostrará al usuario.
    :param valid_options: Opciones válidas para la entrada.
    :return: Entrada válida del usuario.
    """
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            print(f"Entrada no válida. Por favor, elige entre {valid_options}.")