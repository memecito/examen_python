import json
import csv
import os
# Definicion de clase para el trabajo con archivos
class Manejador_archivos:
    ruta:str=''
    nombre:str=''
    def __init__(self, ruta:str='./', nombre:str='to-do'):
        self.ruta=ruta
        self.nombre=nombre
        
        


    
        
        


# Abrir archivo json
    def abrir_json(self)->dict:
        try:
            with open(self.ruta+self.nombre+'.json', 'r') as archivo_json:
                datos=json.load(archivo_json)                
        except FileNotFoundError:
            print(f'el archivo {self.nombre} no existe')
            print('Se creara uno con ese nombre')        
        return datos



# Crear archivo vacio 
    def crear_vacio(self):
        with open(self.ruta+self.nombre, 'w') as archivo_json:
            json.dump('', archivo_json, indent=4)
        print('Archivo vacio creado')

    
    

# Actualizar archivo


# Guardar archivo
    def guardar_archivo(self, tareas):
        with open(self.ruta+self.nombre+'.json', 'w') as file:
            json.dump(tareas, file, indent=4)