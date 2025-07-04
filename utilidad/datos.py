import json
import csv
import os
# Definicion de clase para el trabajo con archivos
class Manejador_archivos:

    def __init__(self, nombre:str, ruta:str='./datos/'):
        self.ruta=ruta
        self.nombre=nombre
        self.ruta_completa=ruta+nombre       


# Abrir archivo json
    def abrir_json(self)->dict:
        if os.path.exists(self.ruta_completa+'.json'):
            with open(self.ruta_completa+'.json', 'r') as archivo_json:
                datos=json.load(archivo_json)   
                return datos               
        return []



# Crear archivo vacio 
    def crear_vacio(self):
        with open(self.ruta_completa+'.json', 'w') as archivo_json:
            json.dump('', archivo_json, indent=4)
        print('Archivo vacio creado')

    
    

# Actualizar archivo


# Guardar archivo
    def guardar_archivo_json(self, tareas):
        if not os.path.exists(self.ruta):
            os.makedirs(self.ruta)
        with open(self.ruta_completa+'.json', 'w') as file:
            json.dump(tareas, file, indent=4)
            print(f'datos guardados {self.ruta_completa}.json')