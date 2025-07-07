# antonio.gutierrez-python-examen

# Programa TO-DO list
Este programa consiste en la creacion de una lista de tareas por realizar, esta diseñada para trabajar con la consola a traves del teclado numerico

# Requisitos tecnicos
Para el correcto funcionamiento de este programa se ha de tener instalado Python >=3.8 y la libreria Colorama


# Manejo y funcionamiento

Al iniciar la ejecucion del software, este comprueba si existe el fichero 'lista.json' en cuyo caso carga la informacion contenida

Una vez realizado ese paso nos muestra el menu principal

Gestion de Tareas ¿qué deseas hacer hoy?
Menú
1-Ver tareas
2-Añadir tarea
3-Editar tarea
4-Eliminar tarea
5-Salir

Desde aqui podremos navegar hacia las distintas opciones
1-Ver tareas: 
    Muestra todas la tareas existentes
2-Añadir tarea:
    Podremos añadir tareas, el programa nos pedira el nombre de la tarea, el nivel de prioridad y si deseamos añadir alguna nota
3-Editar tarea
    nos aparece un sub menu que nos da la opcion de completar una tarea, cambiarle el nombre o modificar la nota
4-Eliminar tarea
    Podemos eliminar una tarea, previamente nos muestra las tareas con su identificador seleccionaremos una y el programa nos avisara si estamos seguros de eliminarlas
5-Salir
    Por ultimo tendremos la opcion de salir, en cuyo caso el programa guardara los datos en dos archivos uno json y otro csv.

NOTA: Al realizar una modificacion sobre las tareas, añadir, cambiar estado o nombre automaticamente se guarda en el archivo json.


# Uso

Ver tareas:

Menu principal:

Selecccionar opcion 1 pulsar intro

Añadir tarea nueva:

Menu principal:

Seleccionar opcion 2 pulsar intro
introducir nombre de la tarea
Elegir la prioridad de la tarea en valor numero
si se desa añadir alguna nota, opcional

Edicion de las tareas (completar, cambiar nombre, añadir notas)

Completar tarea
Menu principal:
seleccionar opcion 3 pulsar intro

Completar tarea, se muestran las tareas no terminadas
introducir el id de la tarea y pulsar intro
si desa completar otra tarea pulsar S en caso contrario pulsar N

Modificar NOmbre tarea

Menu principal seleccionar opcion 3, pulsar intro
seleccionar opcion 2 modificar tarea
selecionar el id de la tarea a modificar
Introducir el nuevo nombre de la tarea


Eliminar Tarea
Menu principal seleccionar opcion 4
introducir el numero de la tarea
El sistema pide una confirmacion para eliminar la tarea, en caso de no querer eliminarla simplemene pulsar n e intro
si estamos seguros que queremos eliminar esa tarea pulsar S e intro



