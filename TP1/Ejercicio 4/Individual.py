import random

class Individual:
    def __init__(self,size,prod_quant,number):
        self.model = list()
        self.model_by_index = list()
        self.orders_by_shelves = list()
        self.model_size = size
        self.number = number
        self.generate(prod_quant)
    
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
        for i in all_orders:
            for j in i.content: 
                ind = self.model.index(j)
                aux_list.append(shelves[ind])
            self.orders_by_shelves.append(aux_list)
            aux_list = []






