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
                        self.mostrar_tareas()
                    elif opc=='2':
                        self.añadir_tareas()
                    elif opc=='3':
                        print('opcion 3')    
                    elif opc=='4':
                        print('opcion 4') 
                    elif opc=='5':
                        self.cerrar_programa()
                        break
                except Exception as e:
                    print(f'Error: {e}')
           
                
   
            
    def añadir_tareas(self):
        nombre=input('Nombre Tarea:')
        prioridad=input('Prioridad:')       
        self.manejador.añadir_tarea(nombre, prioridad)

    def mostrar_tareas(self):
        tareas_guadadas= self.manejador.tareas_a_diccionario()
        for tarea in tareas_guadadas:
            print(tarea)
    
    def cerrar_programa(self):
        tareas= self.manejador.tareas_a_diccionario()
        
        self.manejador_archivo.guardar_archivo_json(tareas)
        self.manejador_archivo.guardar_archivo_csv(tareas)
        print('Adios') 
        