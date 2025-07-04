from datetime import datetime


# Definicion de clase para la entidad tarea
class Tarea:

    nombre: str = ""
    inicio: datetime
    fin_tarea: datetime
    clas_prioridad = {"0": "Normal", "1": "Baja", "2": "Urgente", "3": "Ayer"}
    prioridad: int
    nota: str = ""

    def __init__(self, nombre: str, fin_tarea: datetime, prioridad: int, nota: str, completada=False):
        self.nombre = nombre
        self.inicio = datetime.now()
        self.fin_tarea = fin_tarea
        self.prioridad = prioridad
        self.nota = nota
        self.completada=completada

    def ver_tarea(self):
        return {
            'nombre': self.nombre,
            'inicio': self.inicio,
            'fin':self.fin_tarea,
            'prioridad':self.prioridad,
            'completada':self.completada,
            'nota':self.nota
        }
        
    @staticmethod
    def para_tarea(data):
        return Tarea(
            nombre=data['nombre'],
            inicio=data['inicio'],
            fin_tarea=data['fin'],
            prioridad=data['prioridad']
            complretada=data['completada'],
            nota=data['nota']
            
        )