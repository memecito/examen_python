from lib.task import Tarea


class ManejadorTarea:
    

    
    def __init__ (self, tareas=[]):
        # inicializamos una lista de tareas
        # creamos una tarea para cada item de la lista pasada
        self.tareas = [ Tarea.desde_diccionario(t) for t in tareas]
        
    def añadir_tarea(self, nombre,  prioridad):
        # si dejaramos como identificador la longitud puede darse el caso de tener identificadores repetidos
        if len(self.tareas)==0:
            id=0
        else:
            print(self.tareas[len(self.tareas)-1].id)
            id=self.tareas[len(self.tareas)-1].id
        id+=1
        nueva_tarea=Tarea(id,nombre, prioridad)
        self.tareas.append(nueva_tarea)
        
    def eliminar_tarea(self, tarea_id):
        self.tareas= [tarea for tarea in self.tareas if tarea.id!=tarea_id]
        
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