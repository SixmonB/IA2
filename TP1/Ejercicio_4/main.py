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
from Ejercicio_3.cache import *
from Ejercicio_4.Genetic_algorithm import *
from random import randint
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    #Hiperparámetros
    indiv_quant = 20 #Cantidad de individuos a generar
    historal_orders = 100 #Cantidad de ordenes historicas a considerar
    it = 30 #Cantidad de iteraciones

    #Lectura de las ordenes del archivo .txt y las almacenamos en la lista all_orders
    all_orders = list()
    results = dict()
    for i in range(1,historal_orders+1):
        all_orders.append(Orders(i))

    #Instanciación de 10 individuos de tamaño 100  
    prod_quant = 100
    indiv_size = 100
    all_individuals = list()
    for i in range(indiv_quant):
        all_individuals.append(Individual(indiv_size,i))
        all_individuals[i].generate(prod_quant)
    
    #Generamos el layout del almacén
    cols = 19
    rows = 21
    store = Layout(rows,cols)
    shelves = store.shelves #Lista que contiene las estanterías del almacén
    costos = []
    n_iteracion = list()
    
    memoria = Cache()
    n_it = 0
    costos_two_gens = []
    indivs_two_gens = []
    best_20_indivs = []
    for k in range(0,it):
        print("Iteracion numero: ",k)
        #Asignamos a cada producto dentro del modelo del individuo un lugar fijo en las estanerías
        for i in all_individuals:
            i.assign_products_to_shelves(shelves[0:101])

        #Ejecutamos temple simulado para cada orden, para cada indviduo. Calculamos costo promedio para las ordenes de cada
        #individuo
        for i in all_individuals:
            i.assign_shelves_to_orders(all_orders,shelves[0:101])
            i.optimize_orders(store,memoria)
            i.calculate_average_cost()
            n_it+=1
            n_iteracion.append(n_it)
            costos.append(i.avrg)
            costos_two_gens.append(i.avrg)
            indivs_two_gens.append(i)
            results[i.avrg] = i.model
        
        #Crossover 
        #1-Creamos puntos de cruce
        while(True):
            crossing_point1 = randint(1,indiv_size-1) 
            crossing_point2 = randint(1,indiv_size-1)
            if(crossing_point1 < crossing_point2):break
                
        #2-Ejecutamos crossover 
        genetic = Genetic_algorithm(crossing_point1,crossing_point2)
        new_individuals = list()
        for i in range(0,len(all_individuals),2):
            ind1 = all_individuals[i].model
            ind2 = all_individuals[i+1].model
            aux_1 = genetic.order_crossing(ind1,ind2)
            aux_2 = genetic.order_crossing(ind2,ind1)
            new_individuals.append(Individual(indiv_size,i))
            new_individuals[i].model = aux_1
            new_individuals.append(Individual(indiv_size,i+1))
            new_individuals[i+1].model = aux_2
            aux_1 = aux_2 = []
        
        #Seleccion de los mejores individuos de la generacion anterior y la actual
        all_individuals = []
        all_individuals = new_individuals
        
    
    costs = sorted(costos)
    print("Costos totales promedio: ",costs)
    print("Costo promedio de mejor individuo: ",costs[0])
    print("Mejor individuo: ",results[costs[0]])

    graficos_evolucion = []
    calidad = np.array(costos)
    n_iteracion_np = np.array(n_iteracion)
    graficos_evolucion.append((n_iteracion,calidad))
    graf  = plt.plot(n_iteracion,calidad)
    plt.show()

    


        
        

            
    

