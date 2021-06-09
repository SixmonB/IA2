
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
    print(sorted([10, 83, 14, 15, 60, 63, 44, 32, 65, 79, 2, 61, 28, 52, 26, 57, 24, 50, 16, 17, 99, 4, 11, 3, 42, 39, 12, 78, 1, 27, 100, 8, 23, 41, 58, 21, 89, 54, 20, 72, 53, 47, 88, 48, 95, 93, 38, 40, 56, 80, 81, 77, 55, 76, 66, 73, 51, 94, 86, 22, 13, 67, 84, 70, 19, 96, 5, 30, 59, 62, 92, 74, 43, 91, 18, 97, 45, 34, 75, 69, 25, 7, 71, 82, 6, 9, 29, 85, 87, 35, 98, 64, 33, 31, 90, 36, 68, 0, 49, 37, 46]))
    

            

            
        
        


