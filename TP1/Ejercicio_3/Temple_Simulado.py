import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from Ejercicio_3.Punto import Punto  

from random import randint
from math import exp

class Temple_Simulado():
    def __init__(self) -> None:
        self.costo_total = int()
        
        self.punto_inicio = Punto(0,0)
        self.punto_fin = Punto(0,0)

        self.estado_actual = list() # lista de puntos de una orden
        self.estado_siguiente = list()
        
        self.TEMPERATURA = int() # o float()
        self.it = int() # o float()
        self.ENERGIA = float()
        self.probabilidad = float()

    def Calcular_Costo(self, estado):
        "Calcula el costo de una orden incluytendo punto de partida "
        costo =  int()
        
        for i,point in enumerate(estado):
            
            if i == 0:
                costo += point.Distancia_Minima(estado[i+1]) + self.punto_inicio.Distancia_Minima(point)
            
            elif i== len(estado)-1: costo += point.Distancia_Minima(self.punto_fin)
            
            else: costo += point.Distancia_Minima(estado[i+1])
        return costo
    
    def Generar_Vecino(self):
        "A partir del estado actual genera el estado siguiente permutando dos de sus valores"
        
        #generar indices de permutacion}        
        per_1 = randint(0,len(self.estado_actual)-1)
        per_2 = randint(0,len(self.estado_actual)-1)
       
        self.estado_siguiente = self.estado_actual.copy()
       
        self.estado_siguiente[per_1] = self.estado_actual[per_2]
        self.estado_siguiente[per_2] = self.estado_actual[per_1]

    def Funcion_Decrecimiento(self , modo =1):
        "Almacena las distintas formas de bajar la TEMPERATURA en funcion de it"

        #lineal
        if modo == 1:
            pass
        elif modo == 2:
            pass
        
    def Calcular_probabilidad(self):
        "Calcula la probabilidad y luego de manera aleatoria decide si fue positiva o negativa"

        #n°e elevado a energiasobre Temperatura

        umbral_probabilidad = int(exp(self.ENERGIA/self.TEMPERATURA) *1000)
        azar = randint(0,1000)
        
        if azar <= umbral_probabilidad: return True
        else: return False


    def Calcular_Energia(self):
        costo_actual = self.Calcular_Costo(self.estado_actual)

        costo_siguiente = self.Calcular_Costo(self.estado_siguiente)
        self.ENERGIA = costo_siguiente - costo_actual

        


    def Iniciar_Busqueda_Local(self):
        "Procedimiento del temple simulado en si"
        terminado = False

        while not terminado:

            self.Funcion_Decrecimiento()
            if self.TEMPERATURA == 0 : terminado = True
           
            self.Generar_Vecino()
            self.Calcular_Energia()
            
            if self.ENERGIA > 0: self.estado_actual = self.estado_siguiente.copy()
            
            else:
                if self.Calcular_probabilidad(): self.estado_actual = self.estado_siguiente.copy()

if __name__ == '__main__':
    print('hola')