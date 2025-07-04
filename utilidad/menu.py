import os


class Menu:

    def __init__(self):
        pass

    def limpiar(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def inicio():
        limpiar()
        print(
            "Gestion de Tareas ¿qué deseas hacer hoy?\nMenú\n1-Ver tareas\n2-Añadir tarea\n3-Editar tarea\n4-Eliminar tarea\n5-Salir"
        )
        opcion = int(input())
