import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from Ejercicio_2.ej_02 import * 
from Ejercicio_3.Cache_mem import *

class Punto():
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def Distancia_Minima(self, otro, almacen,file):
        "Obtiene el valor de COSTO del camino mas corto hacia otro punto a traves de A*"
        #print("X:"+str(self.x)+" "+"Y: "+str(self.y))
        short = Short_Way([self.x,self.y],[otro.x,otro.y],almacen)
        retorno = short.way_distance *100
        write_file(file,self.x,self.y,otro.x,otro.y,retorno)
        return retorno
    def __str__(self) -> str:
        return f'({self.x},{self.y})'

