from orders import Orders
from Individual import Individual

if __name__ == "__main__":
    historal_orders = 100
    all_orders = list()
    for i in range(1,historal_orders+1):
        all_orders.append(Orders(i))

    indiv_quant = 10
    individuals = list()
    for i in range(indiv_quant):
        individuals.append(Individual(30,100))

