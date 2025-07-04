from datetime import datetime
from datetime import timedelta


# Definicion de clase para la entidad tarea
class Tarea:

    nombre: str = ""
    inicio: datetime
    fin_tarea: datetime
    class_prioridad = {"0": "Normal", "1": "Baja", "2": "Urgente", "3": "Ayer"}
    prioridad: int
    nota: str = ""

    def __init__(self,id, nombre: str, fin_tarea:datetime=datetime.now()+timedelta(days=14), prioridad:int=0, nota:str='', completada=False):
        # Inicializacion de teareas
        self.id=id,
        self.nombre = nombre
        self.inicio = datetime.now()
        self.fin_tarea = fin_tarea
        self.prioridad = prioridad
        self.nota = nota
        self.completada=completada

    def ver_tarea(self):
        # con esta funcion devolvemos un diccionario con el valor de la tarea
        return {
            'nombre': self.nombre,
            'inicio': self.inicio,
            'fin':self.fin_tarea,
            'prioridad':self.prioridad,
            'completada':self.completada,
            'nota':self.nota
        }
    def actualizar_tarea(data):
        # for key, valor in data:
        #     Tarea.[]
        pass
        
    @staticmethod
    def para_tarea(data):
        # con estsa funcion devolvemos una tarea a partir de los datos pasados
        return Tarea(
            nombre=data['nombre'],
            inicio=data['inicio'],
            fin_tarea=data['fin'],
            prioridad=data['prioridad'],
            complretada=data['completada'],
            nota=data['nota']
            
        )