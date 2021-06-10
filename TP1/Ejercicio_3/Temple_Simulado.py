import math
import sys  
from pathlib import Path

from numpy.core.records import array  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))


import matplotlib.pyplot as plt
import numpy as np
from Ejercicio_3.Punto import Punto  
from Ejercicio_3.cache import *
from Ejercicio_2.Layout import *
from Ejercicio_4.orders import *


from random import randint
from math import exp

class Temple_Simulado():
    def __init__(self, orden, mapa) -> None:
        self.costo_total = int()
        self.almacen = mapa
        self.punto_inicio = Punto(0,0)
        self.punto_fin = Punto(0,0)

        self.estado_actual = orden.copy() # lista de puntos de una orden
        self.estado_siguiente = list()
        
        self.T_INICIAL = 30
        self.TEMPERATURA = int() # o float()

        self.it = int() # o float()
        
        self.ENERGIA = float()
        self.umbral_probabilidad = float()
        
        self.causa = str()

        #para graficar
        self.eje_x = list()#np.array([])
        self.evolucion_costo = list()#np.array([])#list()

    def Calcular_Costo(self, estado):
        "Calcula el costo de una orden incluytendo punto de partida "
        #global memoria
        costo =  int()
        self.costo_estado_actual = 0
        
        for i,point in enumerate(estado):
            
            if i == 0:
                
                costo += point.Distancia_Minima(estado[i+1],self.almacen,memoria) + self.punto_inicio.Distancia_Minima(point,self.almacen,memoria)
            
            elif i == len(estado)-1: costo += point.Distancia_Minima(self.punto_fin,self.almacen,memoria)
            
            else: costo += point.Distancia_Minima(estado[i+1],self.almacen,memoria)
        
        self.costo_estado_actual = costo
        return costo
    
    def Generar_Vecino(self):
        "A partir del estado actual genera el estado siguiente permutando dos de sus valores"
        
        #generar indices de permutacion}        
        per_1 = randint(0,len(self.estado_actual)-1)
        per_2 = randint(0,len(self.estado_actual)-1)
       
        self.estado_siguiente = self.estado_actual.copy()
       
        self.estado_siguiente[per_1] = self.estado_actual[per_2]
        self.estado_siguiente[per_2] = self.estado_actual[per_1]

    def Funcion_Decrecimiento(self , modo =4):
        "Almacena las distintas formas de bajar la TEMPERATURA en funcion de it"

        #lineal
        if modo == 1:
            self.TEMPERATURA = self.T_INICIAL - self.it
            
        #cuadratico
        elif modo == 2:
            self.TEMPERATURA = self.T_INICIAL - self.it*2
        
        #Decreciemiento exponencial por 2
        elif modo == 3:
            if self.it == 0: self.TEMPERATURA = self.T_INICIAL
            self.TEMPERATURA = self.TEMPERATURA/2
        
        # decreciemiento exponencial por 4
        elif modo == 4:
            if self.it == 0: self.TEMPERATURA = self.T_INICIAL
            self.TEMPERATURA = self.TEMPERATURA/4
        
    def Calcular_probabilidad(self):
        "Calcula la probabilidad y luego de manera aleatoria decide si fue positiva o negativa"

        #n°e elevado a energiasobre Temperatura

        self.umbral_probabilidad = int(exp(self.ENERGIA*1000/self.TEMPERATURA) *1000)
        azar = randint(0,1000)
        
        if azar <= self.umbral_probabilidad: return True
        else: return False


    def Calcular_Energia(self):
        '''La energia es negativa cuando el siguiente es peor que el actual.
            pero en nuetro caso el mejor es el mas corto. por tanto multiplicamos por (-1) para indicar Energia negativa      
         '''
        costo_actual = self.Calcular_Costo(self.estado_actual)

        costo_siguiente = self.Calcular_Costo(self.estado_siguiente)
        #self.costo_total = self.costo_total + costo_actual + costo_siguiente
        self.ENERGIA = -(costo_siguiente - costo_actual)


    def Iniciar_Busqueda_Local(self):
        "Procedimiento del temple simulado en si"
        it_max = 1000
        
        terminado = False
        convergencia = False
        it_converg = 0
        it_converg_max = 200
        while not terminado and not convergencia and self.it < it_max:
            # print(self.TEMPERATURA)
            devolucion = str()
            self.Funcion_Decrecimiento()
            # print(self.TEMPERATURA)
            if self.TEMPERATURA <= 0   :
                self.causa = f'Iteraciones agotadas {self.it}'
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
            
            else:
                # devolucion += f'COSTO ACTUAL: {self.Calcular_Costo(self.estado_actual)} ,COSTO SIGUIENTE: {self.Calcular_Costo(self.estado_siguiente)}, ENERGIA: {self.ENERGIA}, PROBABILIDAD: {self.umbral_probabilidad}'#ESTADO ACTUAL: {self.estado_actual},                                            
                if self.Calcular_probabilidad(): self.estado_actual = self.estado_siguiente.copy()
                
                # devolucion += f'COSTO: {self.Calcular_Costo(self.estado_actual)} , ENERGIA: {self.ENERGIA}, PROBABILIDAD: {self.umbral_probabilidad}'#ESTADO ACTUAL: {self.estado_actual},                                            

            
            # self.evolucion_costo.append([self.Calcular_Costo(self.estado_actual),f'ENERGIA: {self.ENERGIA}', f'PROBABILIDAD: {self.umbral_probabilidad}'])
            
            self.eje_x.append(self.it) 
            self.evolucion_costo.append(self.Calcular_Costo(self.estado_actual))

            self.it += 1
            if it_converg == it_converg_max: 
                self.causa ='Convergencia del codigo'
                break 
            if self.it == it_max :
                self.causa = f'Iteraciones agotadas {self.it}'
                break
        
def normalizar(array):
    array = array/abs(array).max()   
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

if __name__ == '__main__':
    cols = 19
    rows = 21
    almacen = Layout(rows,cols) 
    q_picks = 25
    q_ordenes = 30
    global memoria
    memoria = Cache()
    #memoria.Conect_db()
    graficos_evolucion = list()
    print(len(almacen.halls))
    for j in range(q_ordenes):
       
        #generar orden 
        orden = list()
        for i in range(q_picks):
            n = randint(0, len(almacen.shelves)-1)
            a = almacen.shelves[n]
            orden.append(Punto(almacen.shelves[n][0],almacen.shelves[n][1]))
        
        for i,pic in enumerate(orden):
            if i == len(orden)-1:
                print(pic)
            else:
                print(pic,end=',')
        temple = Temple_Simulado(orden,almacen)
        temple.Iniciar_Busqueda_Local()
        n_iteracion = normalizar ( np.array(temple.eje_x) )
        

        calidad = normalizar( np.array(temple.evolucion_costo) )
        graficos_evolucion.append((n_iteracion,calidad))
        graf  = plt.plot(n_iteracion,calidad)
        print(temple.causa)
    
    #memoria.Disconect_db()
    plt.show()
