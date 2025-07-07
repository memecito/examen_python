from lib.task import Tarea
from colorama import init, Fore, Back, Style


class ManejadorTarea:
    

    
    def __init__ (self, tareas=[]):
        init(autoreset=True)

        # inicializamos una lista de tareas
        # creamos una tarea para cada item de la lista pasada
        self.tareas = [ Tarea.desde_diccionario(t) for t in tareas]
        
    def añadir_tarea(self, nombre,  prioridad):
        # si dejaramos como identificador la longitud puede darse el caso de tener identificadores repetidos
        if len(self.tareas)==0:
            id=0
        else:
            id=self.tareas[len(self.tareas)-1].id
        id+=1
        nueva_tarea=Tarea(id,nombre, prioridad)
        self.tareas.append(nueva_tarea)
        
    # def eliminar_tarea(self, tarea_id):
    #     self.tareas= [tarea for tarea in self.tareas if tarea.id!=tarea_id]
    #     #         self.tasks = [task for task in self.tasks if task.id != task_id]
    #     print('tareas ya eliminadas')
    #     for n in self.tareas:
    #         print(list(n))
    #     return self.tareas
    
    def eliminar_tarea(self, tarea_id:int):
        contador = len(self.tareas)  # Guardamos el número de tareas antes
        print(Fore.RED+'Atencion va a eliminar una tarea:')
        posicion=self.tareas.index(Tarea.id==tarea_id)
        print(Fore.BLUE+self.tareas)
        opc=input(Fore.RED+'Esta seguro S/N:')
        if opc.lower()=='s':
            self.tareas = [tarea for tarea in self.tareas if tarea.id != int(tarea_id)]
           
        elif opc.lower()=='n':
            print('No se elimina la tarea')

        if len(self.tareas) < contador:
            return True  # Sí eliminó una tarea
        else:
            return False  # No se encontró ninguna tarea con ese ID

        
    def ver_tareas(self):
        return self.tareas
    
    def completar_tareas(self, id_tarea):
        tareas_completadas=[]
        for tarea in self.tareas:
            if tarea.id==id_tarea:
                tarea.completada=True
            tareas_completadas.append(tarea)

    def cambiar_nombre(self, id_tarea:int, nombre):
        tareas_completadas=[]
        for tarea in self.tareas:
            if tarea.id==id_tarea:
                tarea.nombre=nombre
            tareas_completadas.append(tarea)
        
    def tareas_a_diccionario(self):
        return [tarea.a_diccionario() for tarea in self.tareas]        