from utilidad.menu import Menu
from lib.manejador_tareas import ManejadorTarea
from utilidad.datos import Manejador_archivos



def main():
    archivos= Manejador_archivos('lista')
    tareas= archivos.abrir_json()

    manejador= ManejadorTarea(tareas)
    
    menu= Menu(manejador, archivos)
    menu.inicio()
    
if __name__=="__main__":
    main()