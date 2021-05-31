import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from Ejercicio_2.ej_02 import * 
from Ejercicio_3.cache import *

class Punto():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def Distancia_Minima(self, otro, almacen, memo):
        "Obtiene el valor de COSTO del camino mas corto hacia otro punto a traves de A*"
        if memo.Existe_Relacion(self, otro):
            return memo.Get_Distancia(self, otro)
        else:
            short = Short_Way([self.x,self.y],[otro.x,otro.y],almacen)
            memo.Add_Distancia(self,otro,short.way_distance)
            return short.way_distance 
        '''found = memo.Read_db(str([self.x,self.y]),str([otro.x,otro.y]))
        if found == 0:
            short = Short_Way([self.x,self.y],[otro.x,otro.y],almacen)
            memo.Write_db(str([self.x,self.y]),str([otro.x,otro.y]),short.way_distance)
            return short.way_distance 
        else:
            cost = memo.cost
            return cost'''
        
    def __str__(self) -> str:
        return f'({self.x},{self.y})'

