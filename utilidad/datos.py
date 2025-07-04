from collections import OrderedDict
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


# Guardar tareas en archivo json
    def guardar_archivo_json(self, tareas):
        print('Tareas al cerrar el programa\n:',tareas)

        if not os.path.exists(self.ruta):
            os.makedirs(self.ruta)
        with open(self.ruta_completa+'.json', 'w') as file:
            json.dump(tareas, file, indent=4)
            print(f'datos guardados {self.ruta_completa}.json')
            
# Guardar tareas en CSV

    def guardar_archivo_csv(self, tareas:list):
        encabezados= tareas[0].keys() if tareas else ['id','nombre', 'prioridad','completada','nota']
        encabezados2= OrderedDict(tareas[0])
        print('Encabezados para guardar csv\n', encabezados)
        if not os.path.exists(self.ruta):
            os.makedirs(self.ruta)
        with open(self.ruta_completa+'.csv',mode='w', newline="") as archivo_csv:
            escritor_csv=csv.DictWriter(archivo_csv, fieldnames=encabezados2)
            escritor_csv.writeheader()
            escritor_csv.writerow(tareas)
            
            