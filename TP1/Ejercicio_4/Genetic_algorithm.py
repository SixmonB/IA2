
from random import randint


class Genetic_algorithm:
    def __init__(self,p1,p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def Execute_genetic(self,all_costs):
        self.calculate_fitness(all_costs)

    def calculate_fitness(self,all_costs):
        aux =  sum(all_costs)
        probs = list()
        for j in all_costs:
            probs.append(j/aux)
        
    def order_crossing(self,ind1,ind2):
        new_ind1 = []
        new_ind2 = []
        for i in range(len(ind1)):
            new_ind1.append(list())
            new_ind2.append(list())
        #Declaramos 3 partes del nuevo individuo y reordenamos para luego hacer el crossover
        part1 = ind1[:self.p1]
        new_ind1[self.p1:self.p2]=ind2[self.p1:self.p2]
        part2 = ind1[self.p2:]
        aux_ind1 = part2+part1+ind1[self.p1:self.p2]
        aux_new_ind1= []
        for i in range(len(aux_ind1)):
            aux_new_ind1.append(list())
        aux_new_ind1[:(self.p2-self.p1)]= ind2[self.p1:self.p2]
        inf_limit = self.p2-self.p1
        cond =  True
        for i in range(inf_limit,len(aux_new_ind1)):
            j=0
            while(cond):
                if(aux_ind1[j] in aux_new_ind1):
                        j+=1
                else:
                    aux_new_ind1[i]=aux_ind1[j]
                    break
        new_ind = []
        sec1 = aux_new_ind1[(self.p2-self.p1):(self.p2-self.p1+len(part2))]
        sec2 = aux_new_ind1[:(self.p2-self.p1)]
        sec3 = aux_new_ind1[self.p2-self.p1+len(part2):]
        new_ind = sec3+sec2+sec1
        return new_ind

if __name__ == "__main__":
    ind1 = list()
    ind2 = list()
    n=20
    for i in range(0,n,1):
            cond = True
            while(cond):
                ran = randint(0,20)
                if(ran not in ind1):cond = False
            ind1.append(ran)

    for i in range(0,n,1):
            cond = True
            while(cond):
                ran = randint(0,20)
                if(ran not in ind2):cond = False
            ind2.append(ran)

    print(ind1)
    print(ind2)
    genetic = Genetic_algorithm(4,7)
    new_ind1 = genetic.order_crossing(ind1,ind2)
    new_ind2 = genetic.order_crossing(ind2,ind1)
    print(new_ind1)
    print(new_ind2)
    

            

            
        
        


