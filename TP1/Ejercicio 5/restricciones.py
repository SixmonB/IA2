import pandas as pd

class CSP(object):

    def __init__(self, machines,tasks) -> None:
                
        info_mach = self.info_machines(machines)
        
        
        df = pd.DataFrame( columns =['Tarea', 'Maquina', 'Turno'], dtype=object)

        for tarea in tasks:
            
            indx = 0
            for i in range( info_mach[ tarea.tipo ] ):
                
                indx = machines.index(tarea.tipo,  0 if indx == 0 else indx + 1)
                

                df_temp = pd.DataFrame(tarea.domain, columns =[ 'Tipo', 'Turno'])
                df_temp['Maquina'] = indx
                df_temp['Tarea'] = tarea.ide
                df_temp.drop('Tipo', inplace=True, axis=1)
                
                
                df = df.append(df_temp, ignore_index= True)
        
        self.dominio_actual = df.copy()
        self.dominio_actual.to_csv('domio.csv', index=False , sep =';')
        del(df_temp)
        del(df)

        print(self.dominio_actual)
        self.bookkeeping = list(   )

    def Asignar(self, task):
        'para una tarea elige la menor  numero '
        df_task = self.dominio_actual.query(f'Tarea == "{task.ide}"')
        
        pass

    def podar_arbol(self):
        'Cada vez que realiza una asignacioneleimina del dominio actual aquellos registros (asignaciones) inconsistentes'
        pass


    def info_machines(self,machines):
        dic  = dict()
        for mac in machines:
            if mac not in dic:
                dic[mac] = 1
            else: 
                dic[mac] += 1

        return dic

    