import machine
import task
import random

if __name__ == "__main__":
    m_type = 5      # cantidad de tipos de maquina
    max_duration = 10   # tiempo maximo de duracion de tarea
    task_quantity = 40  # cantidad de tareas a realizar
    my_machines = [1,1,1,2,2,3,4,4,5]
    n1 = 3
    n2 = 2
    n3 = 1
    n4 = 2
    n5 = 1
    tasks = []
    machines = []
    domain = []
    duration = []
    total_time = 0

    for i in range(task_quantity):
        duration.append(random.randrange(1, max_duration, 1))
        total_time += duration[i]

    # sumando el tiempo total de duracion de las tareas, definimos el dominio formando tuplas 
    # con los tipos de maquinas disponibles y turnos de trabajo, segun el tiempo total de trabajo.

    for i in range(1, m_type+1):
        for j in range(1, total_time+1):
            domain.append((i, j))

    for i in range(1, m_type+1):
        my_machine = machine.Machine("idm_"+str(i),random.randrange(1, m_type, 1))
        machines.append(my_machine)

    for i in range(1, task_quantity+1):
        my_task = task.Task("idt_"+str(i),duration[i-1],random.randrange(1, m_type, 1), domain)
        tasks.append(my_task)
        # print(tasks[i].ide)

    # Diseño de restricciones --------------

    # Las restricciones son entre 2 tareas que requieren la misma maquina,
    # por lo que hay que definir el orden de funcionamiento.
    # Empezamos eliminando del dominio de cada tarea, todas las combinaciones 
    # que impliquen una maquina distinta de la requerida.


    print(tasks[0].domain)
    print(tasks[0].type)
    
    for tarea in tasks:
        delete = list()
        print("identificador de tarea", tarea.ide)
        for j in range(len(tarea.domain)):
            
            if j<len(tarea.domain):
            
                print(tarea.domain[j])            
                if (tarea.domain[j][0] != tarea.type):
                    #print("i y j", i, j)
                    print(tarea.domain[j][0])
                    print("****", tarea.type)
                    delete.append(tarea.domain[j])
                    # tarea.domain.remove(tarea.domain[j])

        for x in delete: tarea.domain.remove(x)
    # print(tasks[0].domain)


    input('ENTER para ver dominio de cada tarea')

    for tas in tasks:
        print(f'\n\nDominio tarea task {tas.ide} de tipo {tas.type}\n')
        print(f'Tamaño del dominio: {len(tas.domain)}')
        print( tas.domain)
