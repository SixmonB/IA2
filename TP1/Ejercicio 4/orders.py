import numpy as np

class Orders:
    def __init__(self,size,quant):
        self.quant = quant
        self.size = size
        self.orders = np.zeros((size,quant))

    def read_file(self):
        self.f = open('orders.txt')
        f_content = self.f.read()
        j=0
        for j in range(1,self.quant,1):
            for i in f_content:
                print(i)
                #if(i=="Order "+str(j)):
                #    self.orders[j][i]=i
            
ord = Orders(26,100)
ord.read_file()
                   
                


        