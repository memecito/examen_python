import os
from colorama import init, Fore, Back, Style
#from lib.task import Tarea


class Menu:
    
    def __init__(self, manejador, manejador_archivo):
        init(autoreset=True)
        self.manejador=manejador
        self.manejador_archivo=manejador_archivo
        

    def limpiar(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def inicio(self):
            while True:
                self.limpiar()
                print(
                    "Gestion de Tareas ¿qué deseas hacer hoy?\nMenú\n1-Ver tareas\n2-Añadir tarea\n3-Editar tarea\n4-Eliminar tarea\n5-Salir"
                )
                try: 
                    opc = input()
                    if opc=='1':
                        self.mostrar_tareas()
                    elif opc=='2':
                        self.añadir_tareas()
                    elif opc=='3':
                        pass
                    elif opc=='4':
                        self.eliminar_tarea()                    
                    elif opc=='5':
                        self.cerrar_programa()
                        break
                except Exception as e:
                    print(f'Error: {e}')
           
                
   
            
    def añadir_tareas(self):
        self.limpiar()
        nombre=input('Nombre Tarea:')
        print('-1 Baja\n0 Normal\n1 Alta\n3 o mas: Para Ayer')
        prioridad=input('Prioridad:')       
        self.manejador.añadir_tarea(nombre, prioridad)

    def mostrar_tareas(self):
        self.limpiar()
        tareas_guadadas= self.manejador.tareas_a_diccionario()
        print('Prioridad:   Nombre:      Estado:     Notas:')
        for tarea in tareas_guadadas:
            tarea_tex=self.prioridades(tarea['prioridad'])+'\t'+tarea['nombre']+'\t'+self.completada(tarea['completada'])+'\t'+tarea['nota']            
            print(tarea_tex)            
        input('Pulse intro para continuar')
        
    def muestra_reducida_tareas(self):
        # self.limpiar()
        tareas_guadadas= self.manejador.tareas_a_diccionario()
        print('id\tNombre:')
        for tarea in tareas_guadadas:
            tarea_tex=tarea['id']+'\t'+tarea['nombre']      
            print(tarea_tex)            
        
        
    def eliminar_tarea(self):
        self.muestra_reducida_tareas()
        opc=input('Introduce el numero de la tarea: ')
        self.manejador.eliminar_tarea(opc)
        input('Presione intro para continuar')
        
    
    def cerrar_programa(self):
        tareas= self.manejador.tareas_a_diccionario()
        
        self.manejador_archivo.guardar_archivo_json(tareas)
        self.manejador_archivo.guardar_archivo_csv(tareas)
        print('Adios') 
        
        
    def prioridades(otro,num)->str:
        num=int(num)
        result=''
        if num==-1:
            result='Baja'
        elif num==0:
            result='Normal'
        elif num==1:
            result='Alta'
        elif num>=2:
            result='Para ayer'
        else:
            result='Vaya, no tienes prisas...'
        return result
    
    def completada(otro,estado:bool)->str:
        if estado==True:
            return 'Completada'
        else:
            return 'Sin Completar'