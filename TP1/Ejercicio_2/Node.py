
class Node:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.visited = 0
        self.neighboors = []
        self.fn = 0

    def find_neighboors(self,shelves,goal,all_nodes):
        'Encuentra todos los vecinos del punto actual' 
        ri = self.value[0] #Coordenada x del punto actual
        ci = self.value[1] #Coordenada y
        self.neighboors = [[ri,ci+1],[ri,ci-1],[ri+1,ci],[ri-1,ci]] #Son todos los vecinos del punto, incluyendo estanterias
        print(self.neighboors)
        self.remove_neighboors_shelves(shelves,goal)
    
    def remove_neighboors_shelves(self,shelves,goal):
        'Elimina los vecinos que son estanterias o que son de coordenadas negativas'
        to_remove = []
        for i in self.neighboors:
            if (i[0]<0) or (i[1]<0): #Guarada en un vector aquellos vecinos que tienen coordenadas [x,y] negativas (es decir, que no pertenecen a la matriz)
                to_remove.append(i)
            elif(i in shelves)and(i != goal): #Guarda en un vector los vecinos que son estanterías, para luego elminarlos. Así en el vector neighboors solo nos quedan vecinos por los cuales se puede circular (pasillos).
                to_remove.append(i)
        for i in range(len(to_remove)): #Elimina los valores que en el for anterior guardamos en el vector "to_remove"
            self.neighboors.remove(to_remove[i])
    

