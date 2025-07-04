import os
import csv
import json
# Definicion de clase para el trabajo con archivos
class Datos:
    ruta:str=''
    nombre:str=''
    def __init__(self, ruta:str='./', nombre:str='to-do.csv'):
        self.ruta=ruta
        self.nombre=nombre
        
        


    
        
        


# Abrir archivo json
    def abrir_json(self)->dict:
        try:
            with open(self.ruta+self.nombre, 'r') as archivo_json:
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