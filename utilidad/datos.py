from collections import OrderedDict
from datetime import datetime
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

# Crear un archivo de log para tener los fallos
    def logs(self, error):
        carpeta_log='./reg'
        ruta_log=os.path.join(carpeta_log,'error.log')
        if not os.path.exists(carpeta_log):
            os.mkdirs(carpeta_log)
        with open(ruta_log,'a', encoding='utf-8') as file_log:
            marca_tiempo=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file_log.write(f"[{marca_tiempo}] {error}\n")

    
    

# Actualizar archivo


# Guardar tareas en archivo json
    def guardar_archivo_json(self, tareas):

        if not os.path.exists(self.ruta):
            os.makedirs(self.ruta)
        with open(self.ruta_completa+'.json', 'w') as file:
            json.dump(tareas, file, indent=4)
            print(f'datos guardados {self.ruta_completa}.json')
            
# Guardar tareas en CSV

    def guardar_archivo_csv(self, tareas:list):
        encabezados= tareas[0].keys() if tareas else ['id','nombre', 'prioridad','completada','nota']
        
        if not os.path.exists(self.ruta):
            os.makedirs(self.ruta)
        try:
            with open(self.ruta_completa+'.csv',mode='w', newline="") as archivo_csv:
                escritor_csv=csv.DictWriter(archivo_csv, fieldnames=encabezados)
                escritor_csv.writerows(tareas)
                print(f'datos guardados {self.ruta_completa}.csv')

        except Exception as error:
            print('Error al guardad el csv:\n',error)
            
        
        
            