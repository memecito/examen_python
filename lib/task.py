
# Definicion de clase para la entidad tarea
class Tarea:

    nombre: str = ""
    class_prioridad = {"0": "Normal", "1": "Baja", "2": "Urgente", "3": "Ayer"}
    prioridad: int
    nota: str = ""

    def __init__(self,id, nombre: str, prioridad:int=0, nota:str='', completada=False):
        # Inicializacion de teareas
        self.id=id,
        self.nombre = nombre
        self.prioridad = prioridad
        self.nota = nota
        self.completada=completada

    def a_diccionario(self):
        # con esta funcion devolvemos un diccionario con el valor de la tarea
        return {
            'nombre': self.nombre,
            'prioridad':self.prioridad,
            'completada':self.completada,
            'nota':self.nota
        }
    def actualizar_tarea(data):
        # for key, valor in data:
        #     Tarea.[]
        pass
        
    @staticmethod
    def desde_diccionario(data):
        # con estsa funcion devolvemos una tarea a partir de los datos pasados
        return Tarea(
            nombre=data['nombre'],
            prioridad=data['prioridad'],
            complretada=data['completada'],
            nota=data['nota']
            
        )