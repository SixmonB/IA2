from machine import Machine
from task import Task

if __name__ == "__main__":
    m_type = [1,1,2,3,4]            # tipos de maquina
    req_machine = [1,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1]       # requerimientos de maquina (tipo)
    duration =    [2,4,5,6,7,2,4,5,6,8,1,3,1,5,8,7,1,5,4,5]     # duracion de la tarea (discretizada en turnos)
    tasks = []
    machines = []
    schedule = []
    for i in range(len(m_type)):
        machine = Machine("idm_"+str(i),m_type[i])
        machines.append(machine)

    for i in range(len(req_machine)):
        task = Task("idt_"+str(i),duration[i],req_machine[i])
        tasks.append(task)
        print(tasks[i].ide)

# diseño de restricciones
# cada restriccion involucra el periodo de inicializacion de 2 tareas y las maquinas utilizadas 

