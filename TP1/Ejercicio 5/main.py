import machine
import task
import random
from restricciones import CSP



if __name__ == "__main__":
    m_type = 5      # cantidad de tipos de maquina
    max_duration = 10   # tiempo maximo de duracion de tarea
    task_quantity = 40  # cantidad de tareas a realizar
    my_machines = [1,1,1,2,2,3,4,4,5]
    tasks = []
    machines = []
    
    duration = []
    total_time = 0

    for i in range(task_quantity):
        duration.append(random.randrange(1, max_duration, 1))
        total_time += duration[i]

    # sumando el tiempo total de duracion de las tareas, definimos el dominio formando tuplas 
    # con los tipos de maquinas disponibles y turnos de trabajo, segun el tiempo total de trabajo.

    for i in range(1,len(my_machines)+1):
        machines.append(machine.Machine( "idm_" + str(i), my_machines[i-1] ))

    for i in range(1, task_quantity+1):
        tasks.append(task.Task("idt_"+str(i),duration[i-1],random.randrange(1, m_type, 1)))
        # print(tasks[i].ide)

    

    # Diseño de restricciones --------------

    # Las restricciones son entre 2 tareas que requieren la misma maquina,
    # por lo que hay que definir el orden de funcionamiento.
    # Empezamos eliminando del dominio de cada tarea, todas las combinaciones 
    # # que impliquen una maquina distinta de la requerida.

    # for tarea in tasks:
    #     delete = list()
        
    #     for j in range(len(tarea.domain)):
            
    #         if j<len(tarea.domain):
            
                      
    #             if (tarea.domain[j][0] != tarea.tipo):
    #                 #print("i y j", i, j)
    #                 delete.append(tarea.domain[j])
    #                 # tarea.domain.remove(tarea.domain[j])

    #     for x in delete: tarea.domain.remove(x)
    # print(tasks[0].domain)



    # input('ENTER para ver dominio de cada tarea')

    # for tas in tasks:
    #     print(f'\n\nDominio tarea task {tas.ide} de tipo {tas.tipo}\n')
    #     print(f'Tamaño del dominio: {len(tas.domain)}')
    #     print( tas.domain)}   
    
    index = 0
    csp =  CSP(machines, tasks, total_time)

    def my_recursive(index):
        csp.podar_arbol(tasks[index])
        
        if len(csp.dominio_tarea) != 0:
            csp.Asignar_turno(tasks[index])
            if index < len(tasks)-1:
                return my_recursive(index+1)
            else : return True
        elif len(csp.dominio_tarea) == 0:
            csp.backtracking()
            return my_recursive(index-1)
        

    
    my_recursive(index)
    print("Los turnos son\n", csp.shifts) 
