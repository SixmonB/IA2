import random
import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from Ejercicio_2.Layout import *
from Ejercicio_3.Temple_Simulado import *
from Ejercicio_3.Punto import *

class Individual:
    def __init__(self,size,number):
        self.model = list()
        self.model_by_index = list()
        self.orders_by_shelves = list()
        self.optimized_orders = list(list())
        self.costs = list()
        self.model_size = size
        self.number = number
        self.avrg = 0
        
    def generate(self,prod_quant):
        'Genera el genoma o modelo del individuo'
        for i in range(0,self.model_size+1,1):
            cond = True
            while(cond):
                ran = random.randint(0,prod_quant)
                if(ran not in self.model):cond = False
            self.model.append(ran)

    def assign_products_to_shelves(self,shelves):
        'Asocia a cada producto dentro de self.model un lugar en las estanterías'
        j=0
        for i in self.model:
            self.model_by_index.append(shelves[j])
            j+=1
    
    def assign_shelves_to_orders(self,all_orders,shelves):
        aux_list = []
        for i in all_orders: #i es un objeto de la clase orden
            for j in i.content: #i.content es una lista justamente, atributo del objeto i. por ejemplo (P10,P11,P5,P8,etc)
                ind = self.model.index(j) #Analizo dentro de mi individuo, donde se encuetra el producto j
                aux_list.append(shelves[ind]) #Ese producto, esta asociado a un lugar dentro de las estanterias. Como yo quiero obtener una lista de ordenes parcial en forma de puntos dentro del
                #almacén y no de productos (para ejecutar el temple simulado), genero esta lista.
            self.orders_by_shelves.append(aux_list) 
            aux_list = []
    
    def optimize_orders(self,store,memoria):
        'Optimiza todas las ordenes - Para ello ejecutamos el temple simulado'
        order_to_optimize = list()
        aux = list()
        k=0
        for i in self.orders_by_shelves:
            for j in i:
                order_to_optimize.append(Punto(j[0],j[1]))
            [order,total_cost]=Ejecutar_temple(store,order_to_optimize,memoria)
            self.costs.append(total_cost)
            aux.append(order)
            self.optimized_orders.append(aux)
            order_to_optimize = []
            k+=1
        print("Fin individuo numero: ",self.number)
        
    def calculate_average_cost(self):
        aux1 = sum(self.costs)
        aux2 = len(self.costs)
        self.avrg = aux1/aux2
        print("Promedio de costos individuo numero "+str(self.number)+": "+str(self.avrg))
    
        







