import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from Ejercicio_2 import ej_02
class Punto():
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def Distancia_Minima(self, otro):
        "Obtiene el valor de COSTO del camino mas corto hacia otro punto a traves de A*"
        cols = 17
        rows = 16
        layout = Layout(rows,cols)           
        short = Short_Way([self.x,self.y],[otro.x,otro.y],layout)
        return short.way_distance

if __name__ == '__main__':
    print('hoola')