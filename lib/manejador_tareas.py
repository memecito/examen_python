from lib.task import Tarea
from colorama import init, Fore, Back, Style


class ManejadorTarea:
    

    
    def __init__ (self, tareas=[]):
        init(autoreset=True)

        # inicializamos una lista de tareas
        # creamos una tarea para cada item de la lista pasada
        self.tareas = [ Tarea.desde_diccionario(t) for t in tareas]
        
    def añadir_tarea(self, nombre,  prioridad, nota):
        # si dejaramos como identificador la longitud puede darse el caso de tener identificadores repetidos
        if len(self.tareas)==0:
            id=0
        else:
            id=self.tareas[len(self.tareas)-1].id
        id+=1
        nueva_tarea=Tarea(id,nombre, prioridad, nota)
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
        
        self.tareas = [tarea for tarea in self.tareas if tarea.id != int(tarea_id)]


        if len(self.tareas) < contador:
            return True  # Sí eliminó una tarea
        else:
            return False  # No se encontró ninguna tarea con ese ID

        
    def ver_tareas(self):
        return self.tareas
    
    def tareas_sin_completar(self):
        return [tarea for tarea in self.tareas if not tarea.completada]
    
 
            
    
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

    def añadir_nota(self, id_tarea:int, nota:str):
        tareas_notas=[]
        for tarea in self.tareas:
            if tarea.id==id_tarea:
                tarea.nota+=nota+'\n'
            tareas_notas.append(tarea)

    def nota_nueva(self, id_tarea:int, nota:str):
        tareas_notas=[]
        for tarea in self.tareas:
            if tarea.id==id_tarea:
                tarea.nota=nota+'\n'
            tareas_notas.append(tarea)
    
        
    def tareas_a_diccionario(self):
        return [tarea.a_diccionario() for tarea in self.tareas]        