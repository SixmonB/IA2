import os

class Orders:
    def __init__(self,number):
        self.content = list()
        self.number = number
        self.individual = 0
        self.read_file()

    def read_file(self):
        'Lee el archivo y rellena una lista que contiene los productos de la orden corrspondiente'
        #current_dir = os.getcwd()
        #print(current_dir)
        #root = current_dir+'/orders.txt'
        self.f = open('C:/Users/merem/Documents/MATERIAS/5to/IA2/Repos/IA2/TP1/Ejercicio_4/orders.txt','r')
        #self.f = open(root,"r")
        file = self.f.readlines()
        flag = 0
        for i in file:
            i=i.rstrip('\n')
            if("Order" in i and flag==1):break
            if(("Order "+str(self.number)) in i):flag = 1
            if(flag == 1):
                if not(i=='' or i=="Order "+str(self.number)):
                    self.content.append(int(i[1:]))
        self.f.close()
    


    
            
                   
                


        