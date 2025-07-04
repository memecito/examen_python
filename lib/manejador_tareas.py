from lib.task import Tarea


class ManejadorTarea:
    

    
    def __init__ (self, tareas=[]):
        # inicializamos una lista de tareas
        # creamos una tarea para cada item de la lista pasada
        self.tareas = [ Tarea.desde_diccionario(t) for t in tareas]
        
    def añadir_tarea(self, nombre,  prioridad):
        id=len(self.tareas)
        id+=1
        nueva_tarea=Tarea(id,nombre, prioridad)
        self.tareas.append(nueva_tarea)
        
    def ver_tareas(self):
        return self.tareas
    
    def completar_tareas(self, id_tarea):
        #opcion 1
        for tarea in self.tareas:
            if tarea.id==id_tarea:
                tarea.completada=True        
                
        # Opcion 2
        # pos_tarea=self.tareas.index((tarea.id==id_tarea))
        # self.tareas[pos_tarea][completada]=True
        
    def tareas_a_diccionario(self):
        return [tarea.a_diccionario() for tarea in self.tareas]        