from datetime import datetime
import os
from colorama import init, Fore, Back, Style
#from lib.task import Tarea


class Menu:
    
    def __init__(self, manejador, manejador_archivo):
        init(autoreset=True)
        self.manejador=manejador
        self.manejador_archivo=manejador_archivo
        

    def limpiar(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def inicio(self):
            self.limpiar()
            while True:
                print(
                    "Gestion de Tareas ¿qué deseas hacer hoy?\nMenú\n1-Ver tareas\n2-Añadir tarea\n3-Editar tarea\n4-Eliminar tarea\n5-Salir"
                )
                try: 
                    opc = input()
                    if opc=='1':
                        print('opcion 1')    
                    elif opc=='2':
                        self.añadir_tareas()
                    elif opc=='3':
                        print('opcion 3')    
                    elif opc=='4':
                        print('opcion 4') 
                    elif opc=='5':
                        print('opcion 5 adios') 
                except Exception as e:
                    print(f'Error: {e}')
           
                
   
            
    def añadir_tareas(self):
        nombre=input('Nombre Tarea:')
        prioridad=input('Prioridad:')
        fecha=input('Fecha de finalizacion:')
        fecha=datetime.fromisoformat(fecha)
        self.manejador.añadir_tarea(nombre, prioridad)
