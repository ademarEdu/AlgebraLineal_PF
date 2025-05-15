# Código para la interfaz de línea de comandos

# Importar las funciones necesarias
from src.interface.utils import validate_input
from src.interface.cli_tema1 import tema_1
from src.interface.cli_tema2 import tema_2
from src.interface.cli_tema3 import tema_3
from src.interface.cli_tema4 import tema_4
from src.interface.cli_tema5 import tema_5
from src.interface.cli_tema6 import tema_6

# Temas disponibles
temas = ["Producto escalar, vectorial, triple producto escalar y triple producto punto.",
    "Gráfica de funciones.",
    "Sistemas de ecuaciones lineales.",
    "Conjunto generador, dependencia e independencia lineal entre vectores.",
    "Operaciones básicas de álgebra lineal (suma, resta, producto escalar, multiplicación, inversa y transpuesta de matrices) y transformaciones lineales.",
    "Determinante de matrices.",
    "Cerrar el programa"
    ]

# Función principal (iniciar la interfaz de línea de comandos)
def start_cli():
    # La variable flag permitirá regresar al menú principal
    # Cuando el usuario elija regresar, flag seguirá siendo True y el bucle continuará
    flag = True
    while flag:
        print("\nTemas disponibles:")
        # Mostrar los temas disponibles
        for i in range(len(temas)):
            print(f"{i+1}. {temas[i]}")

        prompt = "\nEscribe el tema que contiene la operación que deseas calcular (del 1 al 7): "
        valid_options = [str(i) for i in range(1, len(temas) + 1)]
        # Preguntar al usuario por el tema
        choice = validate_input(prompt, valid_options)
        choice = int(choice) - 1  # Convertir a índice de lista

        if choice == 0:
            flag = tema_1()
        elif choice == 1:
            flag = tema_2()
        elif choice == 2:
            flag = tema_3()
        elif choice == 3:
            flag = tema_4()
        elif choice == 4:
            flag = tema_5()
        elif choice == 5:
            flag = tema_6()
        elif choice == 6:
            exit()