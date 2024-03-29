import os 
from random import choice, randint, uniform

import numpy as np
import pandas as pd
from random import randint
from math import exp
import matplotlib.pyplot as plt
from machine_learning import train, inicializar_pesos, generar_datos_clasificacion
class Estado():
    def __init__(self) -> None:

        # HIPERPARAMETROS  ---> definen un estado
        
        self.hiperparametros = [ 'learning_rate', 'neuronas_capa_oculta'  ] # , 'funcion_activacion' --- saque la fncion de activacion por que siempre dio relu

        self.LEARNING_RATE = int()         # RANGO DE VALORES
        self.NEURONAS_CAPA_OCULTA = int()  # RANGO DE VALORES
        self.FUNCION_ACTIVACION = 'ReLU' #str()    # ReLU SIGMOIDE

        

        # Valores para los limites de aleeatoriedad
        self.MIN_learning_rate = 0.7
        self.MAX_learning_rate = 1.1
        self.posibles_learning_rates =  list( np.arange(self.MIN_learning_rate, self.MAX_learning_rate, 0.05))
        
        self.MIN_neuronas_capa_oculta = 60
        self.MAX_neuronas_capa_oculta = 120
        self.posibles_neuronas_ocultas =  list( np.arange(self.MIN_neuronas_capa_oculta, self.MAX_neuronas_capa_oculta, 5))
        

        self.funciones_activacion = [ 'ReLU', 'SIGMOIDE' ]

        #   -------------     #

        # parametros de entrada de train
    
        self.K_FOLDS = 5 # Canidad e veces que se hace el calculo de la presicion para un mismo estado
        self.N_EPOCHS = 2000
        self.q_ejemplos = 300
        self.q_clases = 3
        self.tolerancia = 3
        
        self.DATOS_ENTRADA = np.array([])
        self.T_ENTRADA =  np.array([])


    
    def leer_datos_entrada(self):
        'Obtiene del archivo csv los datos de entrada, si no existe, lo crea por unica vez'
        
        if  os.path.isfile('datos_entrada.csv'):
            df = pd.read_csv('datos_entrada.csv', sep= ';')
            self.DATOS_ENTRADA = df.loc[:, ["x", "y"]].values
            self.T_ENTRADA = df.loc[:, ["t"]].values.reshape((300, ))
            # print(self.T_ENTRADA.shape)
            # print(self.T_ENTRADA)
            

        else:
            Generar_Ejemplos_Temple()
            self.leer_datos_entrada()


    def Calcular_precision(self):
        '''Calcula el PROMEDIO LA PRESCISION de k veces correr la RED NEURONAL 
        para N_EPOCHS para conjunto de validacion, distintos del de entrenamiento '''
        
        sum_precision = 0
        
        for k in range(self.K_FOLDS):
            #variar 
            self.separar_train_validation()
            pesos = inicializar_pesos(n_entrada = 2,  n_capa_2 = self.NEURONAS_CAPA_OCULTA,  n_capa_3 = self.q_clases )
            sum_precision += train( self.x_train, self.t_train, pesos, self.LEARNING_RATE, self.N_EPOCHS, self.x_validation, self.t_validation, 1000, self.tolerancia, self.FUNCION_ACTIVACION )
        
        prom_precision = sum_precision / self.K_FOLDS
        
        return prom_precision


    def Generar_estado_primogenito(self):
        'Genera el primer estado aleatorio'
        
        self.LEARNING_RATE =   choice( self.posibles_learning_rates)                        #uniform(self.MIN_learning_rate, self.MIN_learning_rate)
        self.NEURONAS_CAPA_OCULTA = choice( self.posibles_neuronas_ocultas)                #randint( self.MIN_neuronas_capa_oculta, self.MAX_neuronas_capa_oculta)
        # self.FUNCION_ACTIVACION = choice( self.funciones_activacion )
        
     
    def Get_hiperparametros(self):
         
        return self.LEARNING_RATE, self.NEURONAS_CAPA_OCULTA, self.FUNCION_ACTIVACION
        

    def Set_hiperparametros(self, hiperparametros):

        self.LEARNING_RATE = hiperparametros[0]
        self.NEURONAS_CAPA_OCULTA = hiperparametros[1]
        self.FUNCION_ACTIVACION = hiperparametros[2]
        

    def Generar_Vecino(self):
        'Genera un vecino a partr de sus valores actuales elegiendo uno de los hiperparametros aleatoriamente'
        
        
        vecino =  Estado()
        vecino.Set_hiperparametros( self.Get_hiperparametros() )
        vecino.DATOS_ENTRADA = self.DATOS_ENTRADA.copy()
        vecino.T_ENTRADA =  self.T_ENTRADA.copy()

        hiper = choice(self.hiperparametros)
        
        if  hiper == 'learning_rate': 
            # vecino.LEARNING_RATE =  uniform( self.MIN_learning_rate, self.MAX_learning_rate)
            act = self.posibles_learning_rates.copy()
            act.remove(self.LEARNING_RATE)
            vecino.LEARNING_RATE = choice( act )
            
        
        elif hiper == 'neuronas_capa_oculta': 
            # vecino.NEURONAS_CAPA_OCULTA =  randint( self.MIN_neuronas_capa_oculta, self.MAX_neuronas_capa_oculta)
            act = self.posibles_neuronas_ocultas.copy()
            act.remove(self.NEURONAS_CAPA_OCULTA)
            vecino.NEURONAS_CAPA_OCULTA = choice( act )

        elif hiper == 'funcion_activacion': 
            act = self.funciones_activacion.copy()
            act.remove(self.FUNCION_ACTIVACION)
            vecino.FUNCION_ACTIVACION = choice( act )

        return vecino
        
    def __str__(self) -> str:
        res  =  f'LEARNING RATE: {self.LEARNING_RATE}\nNEURONAS OCULTAS: {self.NEURONAS_CAPA_OCULTA}\nFUNCION ACTIVACION: {self.FUNCION_ACTIVACION}'
        return res
        
        

        
        

    def separar_train_validation(self):
        'Separa la aprte de validacion y la parte de entranamientodcvc'
        
        #prepara los indices finales
        train_idx = list( range(  len( self.DATOS_ENTRADA ) ) )
        validation_idx = list()
        
        size_valid = int( len(train_idx) * 0.25 )
        
        for i in range( size_valid):
            
            ele = choice(train_idx)
            validation_idx.append(ele)
            train_idx.remove(ele)
            
            
        self.x_train = self.DATOS_ENTRADA[train_idx].copy()
        self.t_train = self.T_ENTRADA[train_idx].copy()
        
        self.x_validation = self.DATOS_ENTRADA[validation_idx].copy()
        self.t_validation = self.T_ENTRADA[validation_idx].copy()
        
    


class Temple_Simulado():
    def __init__(self, estado_inicial,t_inicial) -> None:

        
        self.costo_total = int()
                
        self.estado_actual =  estado_inicial   #orden.copy() # lista de puntos de una orden
        self.estado_siguiente = Estado()
        
        self.T_INICIAL = t_inicial
        self.it_max = t_inicial
        self.TEMPERATURA = int() # o float()

        self.it = int() # o float()
        
        self.ENERGIA = float()
        self.umbral_probabilidad =  float()
        
        self.causa = str()

        #para graficar
        self.eje_x = list()#np.array([])
        self.evolucion_costo = list()#np.array([])#list()
        

    def Calcular_Costo(self, estado):
        "Calcula el costo de una orden incluytendo punto de partida "
        global memoria
        
        costo  =  estado.Calcular_precision()
        
        return costo
    

    def Funcion_Decrecimiento(self , modo = 2):
        "Almacena las distintas formas de bajar la TEMPERATURA en funcion de it"

        #lineal
        if modo == 1:
            self.TEMPERATURA = self.T_INICIAL - self.it
            
       
        #Decreciemiento exponencial por 2
        elif modo == 2:
            if self.it == 0: self.TEMPERATURA = self.T_INICIAL
            self.TEMPERATURA = self.TEMPERATURA/2
        
        # decreciemiento exponencial por 4
        elif modo == 3:
            if self.it == 0: self.TEMPERATURA = self.T_INICIAL
            self.TEMPERATURA = self.TEMPERATURA/4
        
    def Calcular_probabilidad(self):
        "Calcula la probabilidad y luego de manera aleatoria decide si fue positiva o negativa"

        #n°e elevado a energiasobre Temperatura

        self.umbral_probabilidad = int(exp(self.ENERGIA*1/self.TEMPERATURA) *1000)
        self.azar = randint(1,1000)
        # print('PROBABILIDAD DE ACEPTAR: ' , self.umbral_probabilidad/1000)
        if self.azar <= self.umbral_probabilidad: return True
        else: return False


    def Calcular_Energia(self):
        '''La energia es negativa cuando el siguiente es peor que el actual.
            En nuestro caso e costo es la precision, y es mejor que el siguiente sea mas alta
         '''
        if self.it == 0:
            self.costo_actual = self.Calcular_Costo(self.estado_actual)

        self.costo_siguiente = self.Calcular_Costo(self.estado_siguiente)
        # print('COSTO ACTUAL: ', self.costo_actual)
        # print('COSTO SIGUIENTE: ', self.costo_siguiente)
        self.ENERGIA = (self.costo_siguiente - self.costo_actual)
        # print('ENERGIA: ', self.ENERGIA)

    
    def Generar_Vecino(self):
        "genera vecino a traves de metodos de Estado, segun el problema"
           
        self.estado_siguiente = self.estado_actual.Generar_Vecino()        

    def Iniciar_Busqueda_Local(self):
        "Procedimiento del temple simulado en si"
        # self.it_max = 30
        
        #Flags 
        #



        terminado = False
        convergencia = False
        it_converg = 0
        it_converg_max = 100


        while not terminado and not convergencia and self.it < self.it_max:
           
            # print(self.TEMPERATURA)
            
            self.Funcion_Decrecimiento()
            
            # print(self.TEMPERATURA)
            if self.TEMPERATURA <= 0 :
                self.causa = f'Temperatura 0'
                break
           
            self.Generar_Vecino()
            

            self.Calcular_Energia()
            if self.ENERGIA >= 0: 
                
                if self.ENERGIA == 0:
                    it_converg += 1
                else: 
                    it_converg = 0
                # devolucion += f'COSTO ACTUAL: {self.Calcular_Costo(self.estado_actual)} ,COSTO SIGUIENTE: {self.Calcular_Costo(self.estado_siguiente)}, ENERGIA: {self.ENERGIA}, SIN PROBABILIDAD' #,ESTADO ACTUAL: {self.estado_actual},                                            
                self.estado_actual = self.estado_siguiente
                self.costo_actual = self.costo_siguiente
            
            else:
                # devolucion += f'COSTO ACTUAL: {self.Calcular_Costo(self.estado_actual)} ,COSTO SIGUIENTE: {self.Calcular_Costo(self.estado_siguiente)}, ENERGIA: {self.ENERGIA}, PROBABILIDAD: {self.umbral_probabilidad}'#ESTADO ACTUAL: {self.estado_actual},                                            
                if self.Calcular_probabilidad(): 
                    self.estado_actual = self.estado_siguiente
                    self.costo_actual = self.costo_siguiente
                
                # devolucion += f'COSTO: {self.Calcular_Costo(self.estado_actual)} , ENERGIA: {self.ENERGIA}, PROBABILIDAD: {self.umbral_probabilidad}'#ESTADO ACTUAL: {self.estado_actual},                                            

            
            # self.evolucion_costo.append([self.Calcular_Costo(self.estado_actual),f'ENERGIA: {self.ENERGIA}', f'PROBABILIDAD: {self.umbral_probabilidad}'])
            
            self.eje_x.append(self.it) 
            self.evolucion_costo.append(self.costo_actual)

            self.it += 1
            
            
            if it_converg == it_converg_max: 
                self.causa ='Convergencia del codigo'
                break 

            if self.it == self.it_max   :
                self.causa = f'Iteraciones agotadas {self.it}'
                break
            # it_converg += 1
            # print(self.it)
        

def normalizar(array, modo = 1):
    #Normalizacion para las ietreaciones
    if modo == 1:
        # array = (abs(array).max()-array)/(abs(array).max()  - abs(array).min())
        # array = abs(array).max() - array
        array = (array - abs(array).min())/(abs(array).max()  - abs(array).min())
        # array = 1 - array

        # array = 1 - array
    # Normalizacion para la calidad
    if modo == 2:
        array = (array - abs(array).min())/(abs(array).max()  - abs(array).min())
        # array = 1 - array


    return array



def Ejecutar_temple(almacen,orden,memo):
    global memoria 
    memoria = memo
    #memoria.Conect_db()

    temple = Temple_Simulado(orden,almacen)
    temple.Iniciar_Busqueda_Local()

    #memoria.Disconect_db()
    costo_estado_actual = temple.Calcular_Costo(temple.estado_actual)
    return temple.estado_actual,costo_estado_actual


def Generar_Ejemplos_Temple():
    'Usa funcion de generar ejemplo de profesor y guarda en csv los datos para ser usado en temple'
    x, t = generar_datos_clasificacion( 300 , 3 )    

    df = pd.DataFrame({ 'x':x[:,0],'y':x[:,1], 't':t})
    df.to_csv('datos_entrada.csv', sep =';', index= False)





if __name__ == '__main__':
    
    
    



    temperatura_inicial = 200
    # # memoria = Cache()
    graficos_evolucion = list()

    q_experiment = 30



    for ex in range(q_experiment):

        estado_inicial = Estado()
        estado_inicial.Generar_estado_primogenito()
        estado_inicial.leer_datos_entrada()
                    
        temple = Temple_Simulado(estado_inicial,temperatura_inicial)
        temple.Iniciar_Busqueda_Local()
            
        n_iteracion = normalizar ( np.array(temple.eje_x) )
            
        print(len(temple.evolucion_costo))
        calidad = normalizar( np.array(temple.evolucion_costo),2 )
        # print(calidad)
        # graficos_evolucion.append((n_iteracion,calidad))
        graf  = plt.plot(n_iteracion,calidad)
        print('\n\n')
        print ('='.center(40, "=")) 
        print(f'EXPERIMENTO: {ex} ')
        # print(f'Cantidad de ordenes: {q_ordenes}')
        # print(f'Pedidos por orden: {q_picks}')
        print(f'Pedidos por orden: {temperatura_inicial}')
        
            
        print('CAUSA DE SALIDA: ',temple.causa)
        print(f'MEJOR ESTADO: ', temple.estado_actual)
        print(f'CALIDAD DE ESTADO: ', temple.costo_actual)
        print ('='.center(40, "=")) 
        print('\n\n')
      
        # memoria.Guardar_Memoria()
    plt.show()




    # for i in temple.evolucion_costo:
    #     print(i)