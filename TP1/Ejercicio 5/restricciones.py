import pandas as pd

class CSP(object):

    def __init__(self, machines,tasks) -> None:
                
        info_mach = self.info_machines(machines)
        self.shifts = pd.DataFrame( columns = ['Tarea', 'Maquina', 'Tipo', 'Turno'], dtype = object)
        self.backup_tarea = []
        self.backup_maquinas = []
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
        self.bookkeeping = list(   )

 
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
        borrar_tarea = list(  self.dominio_actual[ self.dominio_actual['Tarea'] == task.ide ].index)
        self.dominio_actual.drop( borrar_tarea , inplace = True) 
        self.backup_tarea.append(borrar_tarea)
        # Borrar maquina del dominio de todas las tareas en momento donde esta ocupada         
        borrar_maquina = list( self.dominio_actual.query( f'Maquina == "{eleccion.Maquina}" & Turno >= {eleccion.Turno}  & Turno <= {eleccion.Turno + task.duration}').index)
        self.dominio_actual.drop(borrar_maquina, axis = 0, inplace=  True)
        self.backup_maquinas.append(borrar_maquina)
        del(borrar_maquina)
        del(borrar_tarea)
        del(eleccion)


    def Asignar_turno(self,task):
        self.shifts = self.shifts.append(self.dominio_tarea.iloc[0])
        self.Propagar_restricciones(task)
        

    def backtracking(self, index):
        self.dominio_actual = self.dominio_actual.concat(self.backup_maquinas[index])
        self.dominio_actual = self.dominio_actual.concat(self.backup_tarea[index])
        # Agregar rutina de cambio de eleccion de variable
        # Verificar subfuncion if, la idea es q se produzca la recursividad hasta que haya dominio suficiente
        # como para cambiar de eleccion.
        if self.dominio_actual ==  1:
            return self.backtracking(self, index-1)
        return index # retornamos el indice para indicarle a la funcion principal desde donde continuar
        # la recursividad.
        

        
    def info_machines(self,machines):
        dic  = dict()
        for mac in machines:
            if mac not in dic:
                dic[mac] = 1
            else: 
                dic[mac] += 1

        return dic

    # def restrain(self):


    