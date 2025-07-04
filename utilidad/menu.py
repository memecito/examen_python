import os
from lib.task import Tarea


class Menu:
    
    def __init__(self):
        self.inicio()
        pass

    def limpiar(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def inicio(self):
            self.limpiar()
            print(
                "Gestion de Tareas ¿qué deseas hacer hoy?\nMenú\n1-Ver tareas\n2-Añadir tarea\n3-Editar tarea\n4-Eliminar tarea\n5-Salir"
            )
            opcion = input()
            while not opcion.isnumeric():
                print('Opcion no validad')
                print('Vuelva a intentarlo')
                opcion= input()
                
    def opciones(opc:int):
        if opc=='1':
            print('opcion 1')    
        elif opc=='2':
            print('opcion 2')    
        elif opc=='3':
            print('opcion 3')    
        elif opc=='4':
            print('opcion 4') 
        elif opc=='5':
            print('opcion 5 adios')   
