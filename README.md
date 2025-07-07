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

