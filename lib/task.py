from datetime import datetime


# Definicion de clase para la entidad tarea
class Tarea:

    nombre: str = ""
    inicio: datetime
    fin_tarea: datetime
    clas_prioridad = {"0": "Normal", "1": "Baja", "2": "Urgente", "3": "Ayer"}
    prioridad: int
    nota: str = ""

    def __init__(self, nombre: str, fin_tarea: datetime, prioridad: int, nota: str):
        self.nombre = nombre
        self.inicio = datetime.now()
        self.fin_tarea = fin_tarea
        self.prioridad = prioridad
        self.nota = nota
