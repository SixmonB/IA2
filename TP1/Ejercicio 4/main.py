import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from orders import Orders
from Individual import Individual
from Ejercicio_2.Layout import *
from Ejercicio_3.Temple_Simulado import *
from Ejercicio_3.Punto import *


if __name__ == "__main__":
    #Lectura de las ordenes del archivo .txt
    indiv_quant = 10
    historal_orders = 100
    all_orders = list()
    for i in range(1,historal_orders+1):
        all_orders.append(Orders(i))

    #Instanciación de 10 individuos de tamaño 100  
    prod_quant = 107
    indiv_size = 107
    all_individuals = list()
    for i in range(indiv_quant):
        all_individuals.append(Individual(indiv_size,prod_quant,i))
    
    #Generamos el layout del almacén
    cols = 19
    rows = 21
    store = Layout(rows,cols)
    shelves = store.shelves #Lista que contiene las estanterías del almacén
    #Asignamos a cada producto dentro del modelo del individuo un lugar fijo en las estanerías
    for i in all_individuals:
        i.assign_products_to_shelves(shelves)

    all_individuals[0].assign_shelves_to_orders(all_orders,shelves)
    
    #Creamos objetos tipo Punto para enviar a procesar por el temple simulado:
    all_individuals[0].optimize_orders(store)

        
        

            
    

