import random

class Individual:
    def __init__(self,size,prod_quant):
        self.model = []
        self.model_size = size
        self.generate(prod_quant)
    
    def generate(self,prod_quant):
        for i in range(1,self.model_size):
            cond = True
            while(cond):
                ran = random.randint(1,prod_quant)
                if(ran not in self.model):cond=False
            self.model.append(ran)
        print(self.model)
        pass

ind = Individual(100,100)