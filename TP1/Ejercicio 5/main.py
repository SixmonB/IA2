import machine
import task
import random

if __name__ == "__main__":
    m_type = 5      # cantidad de tipos de maquina
    max_duration = 10
    task_quantity = 20
    tasks = []
    machines = []
    schedule = []
    domain = []
    for i in range(1, m_type+1):
        for j in range(1, task_quantity+1):
            domain.append((i, j))


    for i in range(1, m_type+1):
        my_machine = machine.Machine("idm_"+str(i),random.randrange(1, m_type, 1))
        machines.append(my_machine)

    for i in range(1, task_quantity+1):
        my_task = task.Task("idt_"+str(i),random.randrange(1, max_duration, 1),random.randrange(1, m_type, 1), domain)
        tasks.append(my_task)
        # print(tasks[i].ide)

    # Diseño de restricciones --------------

    # Las restricciones son entre 2 tareas que requieren la misma maquina,
    # por lo que hay que definir el orden de funcionamiento.
    # Empezamos eliminando del dominio de cada tarea, todas las combinaciones 
    # que impliquen una maquina distinta de la requerida.


    print(tasks[0].domain)
    print(tasks[0].type)
    for i in range(len(tasks)):
        print("identificador de tarea", tasks[i].ide)
        for j in range(len(tasks[i].domain)):
            if j<len(tasks[i].domain):
                print(tasks[i].domain[j])
                if (tasks[i].domain[j][0] != tasks[i].type):
                    #print("i y j", i, j)
                    print(tasks[i].domain[j][0])
                    print("****", tasks[i].type)
                    tasks[i].domain.remove(tasks[i].domain[j])
    print(tasks[0].domain)
                    
# ver que la subrutina empieza eliminando bien los valores que no corresponden,
# pero luego deja de borrar tuplas hasta q se queda sin tareas. 
# if j<len(tasks[i].domain): ese if tiene como objetivo verificar que no se 
# produzca un index error por superar los limites de la lista.