import pandas as pd
from pandas.core.accessor import DirNamesMixin

class CSP(object):

    def __init__(self, machines,tasks) -> None:
                
        info_mach = self.info_machines(machines)
        self.shifts = pd.DataFrame( columns = ['Tarea', 'Maquina', 'Tipo', 'Turno', 'Duracion'], dtype = object)
        df = pd.DataFrame( columns =['Tarea', 'Maquina', 'Tipo', 'Turno'], dtype=object)

        for tarea in tasks:
            indx = 0
            for mac in machines:
                
                # si la maquina y la tarea son del mismo tipo 
                if mac.typ == tarea.tipo:
                    df_temp = pd.DataFrame(tarea.domain, columns =[ 'Tipo' , 'Turno'])
                    
                    
                    df_temp['Maquina'] = mac.ide
                    df_temp['Tarea'] = tarea.ide

                    
                    df = df.append(df_temp, ignore_index= True)



            # for i in range( info_mach[ tarea.tipo ] ):
                
            #     indx = machines.index(tarea.tipo,  0 if indx == 0 else indx + 1)
                

            #     df_temp = pd.DataFrame(tarea.domain, columns =[ 'Tipo Tarea', 'Turno'])
            #     df_temp['Maquina'] = indx
            #     df_temp['Tarea'] = tarea.ide
            #     # df_temp.drop('Tipo', inplace=True, axis=1)
                
                
            #     df = df.append(df_temp, ignore_index= True)
        
        self.dominio_actual = df.copy()
        # self.dominio_actual.to_csv('domio.csv', index=False , sep =';')
        del(df_temp)
        del(df)

        print(self.dominio_actual)
        self.backup = list()
        self.backup.append(self.dominio_actual)

 
    def podar_arbol(self, task):
        'Restringe el dominio local de la tarea que se esta apunto de asignar'
        
        self.dominio_tarea = self.dominio_actual.query(f'Tarea == "{task.ide}"').copy()#.reset_index()
        borrar = list(  self.dominio_tarea[ self.dominio_tarea['Tipo'] != task.tipo ].index)
        
        self.dominio_tarea.drop(borrar, inplace = True) 
        self.dominio_tarea.sort_values('Turno', inplace= True)


    def Propagar_restricciones(self, task):
        'Propaga las restricciones de la asignacion anterior al resto del dominio'
        
        eleccion = self.shifts.iloc[-1] # ultima asignacion

        # elimina toos los registros de tarea del dominio
        borrar = list(  self.dominio_actual[ self.dominio_actual['Tarea'] == task.ide ].index)
        self.dominio_actual.drop( borrar , inplace = True) 
        # Borrar maquina del dominio de todas las tareas en momento donde esta ocupada         
        borrar = list( self.dominio_actual.query( f'Maquina == "{eleccion.Maquina}" & Turno >= {eleccion.Turno}  & Turno <= {eleccion.Turno + task.duration}').index)
        self.dominio_actual.drop(borrar, axis = 0, inplace=  True)
        # guardamos el estado del dominio para mantener un registro para el backtracking
        # guardamos la ultima eleccion para eliminarla del dominio luego del backtracking
        self.backup.append(self.dominio_actual)
        self.last_election = eleccion
        del(borrar)
        del(eleccion)


    def Asignar_turno(self,task):
        self.shifts = self.shifts.append(self.dominio_tarea.iloc[0])
        row_labels = self.shifts.index.values
        self.shifts.at[row_labels[-1], 'Duracion'] = task.duration
        self.Propagar_restricciones(task)
        

    def backtracking(self):
        # tomamos el backup de dominios del sistema, eliminamos el ultimo caso, y volvemos al caso anterior
        # tambien eliminamos del dominio a la ultima eleccion para no volver a caer en el mismo error
        self.backup.pop()
        self.dominio_actual = self.backup[-1]
        self.dominio_actual.drop(self.last_election, inplace =True)
        self.shifts = self.shifts.drop(self.shifts.tail(1).index, inplace = True)
        

        
    def info_machines(self,machines):
        dic  = dict()
        for mac in machines:
            if mac not in dic:
                dic[mac] = 1
            else: 
                dic[mac] += 1

        return dic

    # def restrain(self):


    