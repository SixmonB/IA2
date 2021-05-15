import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from Ejercicio_3.Punto import Punto  
from Ejercicio_2.Layout import *

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
        
        self.T_INICIAL = 600
        self.TEMPERATURA = int() # o float()

        self.it = int() # o float()
        self.ENERGIA = float()
        self.umbral_probabilidad = float()
        self.evolucion_costo = list()
        self.causa = str()

    def Calcular_Costo(self, estado):
        "Calcula el costo de una orden incluytendo punto de partida "
        costo =  int()

        for i,point in enumerate(estado):
            
            if i == 0:
                costo += point.Distancia_Minima(estado[i+1],self.almacen) + self.punto_inicio.Distancia_Minima(point,self.almacen)
            
            elif i== len(estado)-1: 
                costo += point.Distancia_Minima(self.punto_fin,self.almacen)
            
            else:
                costo += point.Distancia_Minima(estado[i+1],self.almacen)
        return costo
    
    def Generar_Vecino(self):
        "A partir del estado actual genera el estado siguiente permutando dos de sus valores"
        
        #generar indices de permutacion        
        per_1 = randint(0,len(self.estado_actual)-1)
        per_2 = randint(0,len(self.estado_actual)-1)
       
        self.estado_siguiente = self.estado_actual.copy()
       
        self.estado_siguiente[per_1] = self.estado_actual[per_2]
        self.estado_siguiente[per_2] = self.estado_actual[per_1]

    def Funcion_Decrecimiento(self , modo =2):
        "Almacena las distintas formas de bajar la TEMPERATURA en funcion de it"

        #lineal
        if modo == 1:
            self.TEMPERATURA = self.T_INICIAL - self.it
            
        #cuadratico
        elif modo == 2:
            self.TEMPERATURA = int(self.T_INICIAL*exp(-self.it))
        print(self.TEMPERATURA)
        
    def Calcular_probabilidad(self):
        "Calcula la probabilidad y luego de manera aleatoria decide si fue positiva o negativa"

        #n°e elevado a energiasobre Temperatura

        self.umbral_probabilidad = int(exp(self.ENERGIA/self.TEMPERATURA) *1000)
        azar = randint(0,1000)
        
        if azar <= self.umbral_probabilidad: return True
        else: return False


    def Calcular_Energia(self):
        '''La energia es negativa cuando el siguiente es peor que el actual.
            pero en nuetro caso el mejor es el mas corto. por tanto multiplicamos por (-1) para indicar Energia negativa      
         '''
        costo_actual = self.Calcular_Costo(self.estado_actual)
        print("Costo actual")

        costo_siguiente = self.Calcular_Costo(self.estado_siguiente)
        self.ENERGIA = -(costo_siguiente - costo_actual)

        


    def Iniciar_Busqueda_Local(self):
        "Procedimiento del temple simulado en si"
        terminado = False
        convergencia = False
        it_converg = 0
        it_max = 20
        while not terminado and not convergencia :
            # print(self.TEMPERATURA)
            devolucion = str()
            self.Funcion_Decrecimiento()
            # print(self.TEMPERATURA)
            if self.TEMPERATURA == 0 :
                self.causa = 'cantidad de iteraciones agotadas'
                break
           
            self.Generar_Vecino()
            
            self.Calcular_Energia()
            if self.ENERGIA >= 0: 
                
                if self.ENERGIA ==0:
                    it_converg += 1
                else: 
                    it_converg = 0
                devolucion += f'COSTO ACTUAL: {self.Calcular_Costo(self.estado_actual)} ,COSTO SIGUIENTE: {self.Calcular_Costo(self.estado_siguiente)}, ENERGIA: {self.ENERGIA}, SIN PROBABILIDAD' #,ESTADO ACTUAL: {self.estado_actual},                                            
                self.estado_actual = self.estado_siguiente.copy()
            
            else:
                devolucion += f'COSTO ACTUAL: {self.Calcular_Costo(self.estado_actual)} ,COSTO SIGUIENTE: {self.Calcular_Costo(self.estado_siguiente)}, ENERGIA: {self.ENERGIA}, PROBABILIDAD: {self.umbral_probabilidad}'#ESTADO ACTUAL: {self.estado_actual},                                            
                if self.Calcular_probabilidad(): self.estado_actual = self.estado_siguiente.copy()
                
                # devolucion += f'COSTO: {self.Calcular_Costo(self.estado_actual)} , ENERGIA: {self.ENERGIA}, PROBABILIDAD: {self.umbral_probabilidad}'#ESTADO ACTUAL: {self.estado_actual},                                            

            
            # self.evolucion_costo.append([self.Calcular_Costo(self.estado_actual),f'ENERGIA: {self.ENERGIA}', f'PROBABILIDAD: {self.umbral_probabilidad}'])
            self.evolucion_costo.append(devolucion)
            self.it += 1
            if it_converg == it_max: 
                self.causa ='Convergencia del codigo'
                for i in self.estado_actual:
                    print(i)
                break 
            
            
            # it_converg += 1
            # print(self.it)
        
        

def Ejecutar_temple(almacen,q_picks,orden):
    '''almacen = Layout(rows,cols)
    print(almacen.halls)
    orden = list()
    for i in range(q_picks):
        n = randint(0, len(almacen.halls)-1)
        a = almacen.halls[n]
        orden.append(Punto(almacen.halls[n][0],almacen.halls[n][1]))
    
    orden = [Punto(3,0),Punto(7,6),Punto(1,0),Punto(0,3)]
    '''
    for i,pic in enumerate(orden) :
        if i == len(orden)-1:
            print(pic)
        else:
            print(pic,end=',')
    temple = Temple_Simulado(orden,almacen)
    temple.Iniciar_Busqueda_Local()
    #for i in temple.evolucion_costo:
    #    print(i)
    print(temple.causa)
    for i in temple.estado_actual:
        print("X:"+str(i.x)+" Y:"+str(i.y))
    
    return temple.estado_actual,temple.costo_total

if __name__ == '__main__':
    cols = 19
    rows = 19
    almacen = Layout(rows,cols) 
    q_picks = 8
    orden = list()
    for i in range(q_picks):
        n = randint(0, len(almacen.halls)-1)
        a = almacen.halls[n]
        orden.append(Punto(almacen.halls[n][0],almacen.halls[n][1]))
    
    orden = [Punto(9,7),Punto(4,7),Punto(8,4),Punto(9,16),Punto(1,13),Punto(10,8),Punto(6,17),Punto(7,14),Punto(3,1),Punto(1,11),Punto(7,17),Punto(2,14),Punto(3,2),Punto(3,16),Punto(10,1),Punto(2,17),Punto(2,4),Punto(8,11)]
    for i,pic in enumerate(orden) :
        if i == len(orden)-1:
            print(pic)
        else:
            print(pic,end=',')
    temple = Temple_Simulado(orden,almacen)
    temple.Iniciar_Busqueda_Local()
    for i in temple.evolucion_costo:
        print(i)
    print(temple.causa)
    for i in temple.estado_actual:
        print("X:"+str(i.x)+" Y:"+str(i.y))