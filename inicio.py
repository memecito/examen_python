from lib.task import Tarea
from lib.manejador_tareas import ManejadorTarea
from utilidad.menu import Menu
from utilidad.datos import Manejador_archivos
import os


def limpiar_consola():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

def main():
    limpiar_consola()
    archivos= Manejador_archivos('to-do')
    tareas= archivos.abrir_json()
    
    manejador= ManejadorTarea(tareas)
    
    menu= Menu(manejador, archivos)
    menu.inicio()
if __name__=="__main__":
    main()