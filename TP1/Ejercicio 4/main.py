from orders import Orders
from Individual import Individual

if __name__ == "__main__":
    #Lectura de las ordenes del archivo .txt
    historal_orders = 100
    all_orders = list()
    for i in range(1,historal_orders+1):
        all_orders.append(Orders(i))

    #Creacion de 10 individuos de tamaño 100  
    indiv_quant = 10
    prod_quant = 100
    indiv_size = 100
    individuals = list()
    for i in range(indiv_quant):
        individuals.append(Individual(indiv_size,prod_quant))

    
    

