
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
        j=0
        for i in range(inf_limit,len(aux_new_ind1)):
            cond = True
            while(cond):
                if(aux_ind1[j] in aux_new_ind1):
                    j+=1
                    aux_new_ind1[i]=aux_ind1[j]
                    break
                else:
                    aux_new_ind1[i]=aux_ind1[j]
                    break
        #print(aux_ind1)
        #print(aux_new_ind1)
        new_ind1 = []
        sec1 = aux_new_ind1[(self.p2-self.p1):(self.p2-self.p1+len(part2))]
        sec2 = aux_new_ind1[:(self.p2-self.p1)]
        sec3 = aux_new_ind1[self.p2-self.p1+len(part2):]
        new_ind = sec3+sec2+sec1
        return new_ind

ind1 = [[1,2],[3,4],[5,6],[6,7],[2,2],[2,4],[2,6],[8,2],[1,8],[8,9]]
ind2 = [[5,2],[4,5],[3,6],[2,7],[8,2],[1,4],[3,6],[2,3],[4,4],[9,9]]
genetic = Genetic_algorithm(4,7)
new_ind1 = genetic.order_crossing(ind1,ind2)
new_ind2 = genetic.order_crossing(ind2,ind1)
print(new_ind1)
print(new_ind2)



            

            
        
        


