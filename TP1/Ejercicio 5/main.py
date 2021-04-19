from machine import Machine
from task import Task

if __name__ == "__main__":
    m_type = [1,1,2,3,4]
    req_machine = [1,3,2,1,4]
    duration = [2,4,6,8,10]
    tasks = []
    machines = []
    for i in range(len(m_type)):
        machine = Machine("idm_"+str(i),m_type[i])
        machines.append(machine)

    for i in range(len(req_machine)):
        task = Task("idt_"+str(i),duration[i],req_machine[i])
        tasks.append(task)
        print(tasks[i].ide)

    