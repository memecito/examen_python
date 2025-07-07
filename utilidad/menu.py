from lib.manejador_tareas import ManejadorTarea
from utilidad.datos import Manejador_archivos
import os
from colorama import init, Fore, Back, Style



class Menu:
    
    def __init__(self, manejador:ManejadorTarea, manejador_archivo:Manejador_archivos):
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
                # self.limpiar()
                print(
                    Fore.GREEN+
                    "Gestion de Tareas ¿qué deseas hacer hoy?\nMenú\n1-Ver tareas\n2-Añadir tarea\n3-Editar tarea\n4-Eliminar tarea\n5-Salir"
                )
                try: 
                    opc = self.comprobar_entrada('',5)
                    if opc==1:
                        self.mostrar_tareas()
                    elif opc==2:
                        self.añadir_tareas()
                    elif opc==3:
                        self.actualizar_tarea()
                    elif opc==4:
                        self.eliminar_tarea()
                    elif opc==5:
                        self.cerrar_programa()
                        break
                except Exception as e:
                    print(f'Error: {e}')
           
                
   
            
  

    def mostrar_tareas(self):
        self.limpiar()
        tareas_guadadas= self.manejador.tareas_a_diccionario()
        print('Prioridad:   Nombre:      Estado:     Notas:')
        for tarea in tareas_guadadas:
            tarea_tex=self.prioridades(tarea['prioridad'])+'\t'+tarea['nombre']+'\t'+self.completada(tarea['completada'])+'\t'+Fore.WHITE+tarea['nota']            
            print(tarea_tex)            
        input('Pulse intro para continuar')

    def mostrar_una_tarea(self, tarea):
        print('Prioridad:   Nombre:      Estado:     Notas:')
        tarea_tex=self.prioridades(tarea['prioridad'])+'\t'+tarea['nombre']+'\t'+self.completada(tarea['completada'])+'\t'+tarea['nota']            
        print(tarea_tex)  

        
    def muestra_reducida_tareas(self):
        self.limpiar()
        tareas_guadadas= self.manejador.tareas_a_diccionario()
        print('id\tNombre:')
        for tarea in tareas_guadadas:
            # tarea_tex=tarea['id']+'\t'+tarea['nombre']      
            print( f'{tarea['id']} \t{tarea['nombre']}' )    

    def comprobar_entrada(self,texto:str,opciones:int)->int:
        opc_tex=input(texto)
        opc=self.comprobar_numero(opc_tex)
        if opc!=-1:
            if opc<=opciones:
                return opc
            else:
                print(Fore.RED+'Opcion no valida, intentelo de nuevo')
                self.comprobar_entrada(texto,opciones)
        return -1
    
    def comprobar_numero(self,opc:str)->int:
        if opc.isnumeric():
            return int(opc)
        else:
            print(Fore.RED+'Opcion no valida, intentelo de nuevo')
            opc=input()
            self.comprobar_numero(opc)
        return -1
    
        


    def añadir_tareas(self):
        self.limpiar()
        nombre=input('Nombre Tarea:')
        print('-1 Baja\n0 Normal\n1 Alta\n3 o mas: Para Ayer')
        prioridad=self.comprobar_entrada('Prioridad',4)  
        nota=input('Desea añadir alguna nota:\n')  
        self.manejador.añadir_tarea(nombre, prioridad, nota)

    def actualizar_tarea(self):
        print('Qué deseas hacer?\n1-Completar tarea\n2-Modificar tarea\n3-Añadir Nota\n4-Volver al menu')
        opc=self.comprobar_entrada('Opcion:',4)
        if opc==1:
            self.completar_tarea()
        elif opc==2:
            self.cambiar_nombre()
        elif opc==3:
            self.cambiar_nota()
        elif opc==4:
            pass

    def completar_tarea(self):
        self.muestra_reducida_tareas()
        opc=input('Introduce el numero de la tarea: ')
        opc=self.comprobar_numero(opc)
        self.manejador.completar_tareas(opc)
        self.mostrar_tareas()
    
    def cambiar_nombre(self):
        self.muestra_reducida_tareas()
        opc=input('Introduce el numero de la tarea: ')
        opc=self.comprobar_numero(opc)
        nuevo_nombre=input('Introduce nuevo nombre para la tarea:')
        self.manejador.cambiar_nombre(opc,nuevo_nombre)

    def cambiar_nota(self):
        self.muestra_reducida_tareas()
        opc=input('Introduce el numero de la tarea: ')
        opc=self.comprobar_numero(opc)
        print('Qué deseas hacer?\n1-Añadir a la nota\n2-Nota nueva\n3-Volver al menu')
        opc=self.comprobar_entrada('Opcion:',4)
        if opc==1:
            nota=input('Añade a la nota\n')
            self.manejador.añadir_nota(opc, nota)
        elif opc==2:
            nota=input('Introduce nota nueva:\n')
            self.manejador.nota_nueva(opc,nota)
        elif opc==3:
            pass


        
        
    def eliminar_tarea(self):
        self.muestra_reducida_tareas()
        opc=input('Introduce el numero de la tarea: ')
        tarea_id=self.comprobar_numero(opc)
        print(Fore.RED+'Atencion va a eliminar una tarea:')
       
        opc=input(Fore.RED+'Esta seguro S/N:')
        if opc.lower()=='s':
                   self.manejador.eliminar_tarea(tarea_id)
        elif opc.lower()=='n':
            print('No se elimina la tarea')
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
            result= 'Baja'
        elif num==0:
            result='Normal'
        elif num==1:
            result=Fore.BLUE+'Alta'
        elif num>=3:
            result=Fore.RED+'Para ayer'
        else:
            result='Vaya, no tienes prisas...'
        return result
    
    def completada(otro,estado:bool)->str:
        if estado==True:
            return Fore.GREEN+'Completada'
        else:
            return Fore.RED+'Sin Completar'
