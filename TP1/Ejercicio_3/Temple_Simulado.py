
import math
import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

#from Ejercicio_4.orders import Orders
from Ejercicio_2.Layout import *
from Ejercicio_3.Temple_Simulado import *
from Ejercicio_3.Punto import *
from Ejercicio_3.cache import *
from Ejercicio_4.Genetic_algorithm import *
from random import randint
import matplotlib.pyplot as plt

import numpy as np
from Ejercicio_3.Punto import Punto  
from Ejercicio_3.cache import *
from Ejercicio_2.Layout import *


from random import randint
from math import exp

class Temple_Simulado():
    def __init__(self, orden, mapa,t_inicial, mult_energia = 1) -> None:
        self.costo_total = int()
        self.almacen = mapa
        self.punto_inicio = Punto(4,4)
        self.punto_fin = Punto(4,4)

        self.estado_actual = orden.copy() # lista de puntos de una orden
        self.estado_siguiente = list()
        
        self.T_INICIAL = t_inicial
        self.it_max = t_inicial
        self.TEMPERATURA = int() # o float()

        self.it = int() # o float()
        
        self.ENERGIA = float()
        self.umbral_probabilidad = float()
        
        self.causa = str()

        #para graficar
        self.eje_x = list()#np.array([])
        self.evolucion_costo = list()#np.array([])#list()
        self.mult_energia = mult_energia

    def Calcular_Costo(self, estado):
        "Calcula el costo de una orden incluytendo punto de partida "
        global memoria
        costo =  int()
        
        for i,point in enumerate(estado):
            
            if i == 0:
                
                costo += point.Distancia_Minima(estado[i+1],self.almacen,memoria) + self.punto_inicio.Distancia_Minima(point,self.almacen,memoria)
            
            elif i == len(estado)-1: costo += point.Distancia_Minima(self.punto_fin,self.almacen,memoria)
            
            else: costo += point.Distancia_Minima(estado[i+1],self.almacen,memoria)
        return costo
    
    def Generar_Vecino(self):
        "A partir del estado actual genera el estado siguiente permutando dos de sus valores"
        
        #generar indices de permutacion}        
        per_1 = randint(0,len(self.estado_actual)-1)
        per_2 = randint(0,len(self.estado_actual)-1)
       
        self.estado_siguiente = self.estado_actual.copy()
       
        self.estado_siguiente[per_1] = self.estado_actual[per_2]
        self.estado_siguiente[per_2] = self.estado_actual[per_1]

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

        self.umbral_probabilidad = int(exp(self.ENERGIA* self.mult_energia/self.TEMPERATURA) *1000)
        self.azar = randint(1,1000)
        
        if self.azar <= self.umbral_probabilidad: return True
        else: return False


    def Calcular_Energia(self):
        '''La energia es negativa cuando el siguiente es peor que el actual.
            pero en nuetro caso el mejor es el mas corto. por tanto multiplicamos por (-1) para indicar Energia negativa      
         '''
        self.costo_actual = self.Calcular_Costo(self.estado_actual)

        self.costo_siguiente = self.Calcular_Costo(self.estado_siguiente)
        self.ENERGIA = -(self.costo_siguiente - self.costo_actual)

        


    def Iniciar_Busqueda_Local(self):
        "Procedimiento del temple simulado en si"
        # self.it_max = 30
        
        terminado = False
        convergencia = False
        it_converg = 0
        it_converg_max = 100
        while not terminado and not convergencia and self.it < self.it_max:
            # print(self.TEMPERATURA)
            devolucion = str()
            self.Funcion_Decrecimiento()
            
            # print(self.TEMPERATURA)
            if self.TEMPERATURA <= 0   :
                self.causa = f'Tmperatura 0'
                break
           
            self.Generar_Vecino()
            

            self.Calcular_Energia()
            if self.ENERGIA >= 0: 
                
                if self.ENERGIA ==0:
                    it_converg += 1
                else: 
                    it_converg = 0
                # devolucion += f'COSTO ACTUAL: {self.Calcular_Costo(self.estado_actual)} ,COSTO SIGUIENTE: {self.Calcular_Costo(self.estado_siguiente)}, ENERGIA: {self.ENERGIA}, SIN PROBABILIDAD' #,ESTADO ACTUAL: {self.estado_actual},                                            
                self.estado_actual = self.estado_siguiente.copy()
                self.costo_actual = self.costo_siguiente
            
            else:
                # devolucion += f'COSTO ACTUAL: {self.Calcular_Costo(self.estado_actual)} ,COSTO SIGUIENTE: {self.Calcular_Costo(self.estado_siguiente)}, ENERGIA: {self.ENERGIA}, PROBABILIDAD: {self.umbral_probabilidad}'#ESTADO ACTUAL: {self.estado_actual},                                            
                if self.Calcular_probabilidad(): 
                    self.estado_actual = self.estado_siguiente.copy()
                    self.costo_actual = self.costo_siguiente
                
                # devolucion += f'COSTO: {self.Calcular_Costo(self.estado_actual)} , ENERGIA: {self.ENERGIA}, PROBABILIDAD: {self.umbral_probabilidad}'#ESTADO ACTUAL: {self.estado_actual},                                            

            
            # self.evolucion_costo.append([self.Calcular_Costo(self.estado_actual),f'ENERGIA: {self.ENERGIA}', f'PROBABILIDAD: {self.umbral_probabilidad}'])
            
            self.eje_x.append(self.it) 
            self.evolucion_costo.append(self.Calcular_Costo(self.estado_actual))

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
        array = 1 - array


    return array

def str_orden(orden):
    ord = str()
    for i,pic in enumerate(orden) :
        if i == len(orden)-1:
            ord += str(pic)
        else:
            ord += str(pic)+','
    return(ord)

def Ejecutar_temple(almacen,orden,memo):
    global memoria 
    memoria = memo
    #memoria.Conect_db()

    temple = Temple_Simulado(orden,almacen)
    temple.Iniciar_Busqueda_Local()

    #memoria.Disconect_db()
    costo_estado_actual = temple.Calcular_Costo(temple.estado_actual)
    return temple.estado_actual,costo_estado_actual

if __name__ == '__main__':
    
    
    cols = 13
    rows = 13
    almacen = Layout(rows,cols) 
    pick_max = len(almacen.shelves)
    ord_max = 100
    
    temperatura_inicial = 500
    memoria = Cache()
    graficos_evolucion = list()

    q_experiment = 10

    for ex in range(q_experiment):

        q_picks = randint(30,45 )  # cantidad de pedidos por orden
        
        q_ordenes =  randint(50,ord_max ) #Cantidad de oprdenes por experimento       20
        print('\n\n')
        print ('='.center(40, "=")) 
        print(f'EXPERIMENTO: {ex} ')
        print(f'Cantidad de ordenes: {q_ordenes}')
        print(f'Pedidos por orden: {q_picks}')
        print(f'Pedidos por orden: {temperatura_inicial}')
        print ('='.center(40, "=")) 
        print('\n\n')
        for j in range(q_ordenes):
            
            

            #generar orden 
            orden = list()
            for i in range(q_picks):
                n = randint(0, len(almacen.shelves)-1)
                a = almacen.shelves[n]
                orden.append(Punto(almacen.shelves[n][0],almacen.shelves[n][1]))
            


            
            
                    
            temple = Temple_Simulado(orden,almacen,temperatura_inicial)
            temple.Iniciar_Busqueda_Local()
            
            n_iteracion = normalizar ( np.array(temple.eje_x) )
            

            calidad = normalizar( np.array(temple.evolucion_costo),2 )
            # graficos_evolucion.append((n_iteracion,calidad))
            graf  = plt.plot(n_iteracion,calidad)
            
            
            print(temple.causa)
      
        memoria.Guardar_Memoria()
        plt.show()

    # for i in temple.evolucion_costo:
    #     print(i)
    
