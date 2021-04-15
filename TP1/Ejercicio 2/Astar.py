import numpy as np
class Astar:
    def __init__(self,init,goal,mapm,shelves,halls):
        self.init = init
        self.goal = goal
        self.current = self.init
        self.mapm = mapm
        self.shelves = shelves
        self.halls = halls
        self.trip = []
        self.init_index = np.where(self.mapm == self.init)
        self.goal_index = np.where(self.mapm == self.goal)
        self.rinit = int(self.init_index[0]) ##Indice en filas del punto inicial
        self.cinit = int(self.init_index[1]) ##Indice en columnas del punto incial

    
    def find_neighboors(self):
        self.current_index = np.where(self.mapm == self.current)
        self.rcurrent = int(self.current_index[0])
        self.ccurrent = int(self.current_index[1])
        self.neighboors = []
        ri = self.rcurrent
        ci = self.ccurrent
        self.neighboors = [[ri,ci+1],[ri,ci-1],[ri+1,ci],[ri-1,ci],[ri+1,ci+1],[ri-1,ci-1],[ri+1,ci-1],[ri-1,ci+1]]
        to_remove = []
        for i in self.neighboors:
            i_content = self.mapm[i[0],i[1]]
            if (i[0]<0) or (i[1]<0):
                to_remove.append(i)
            elif(i_content in self.shelves):
                to_remove.append(i)
        
        for i in range(len(to_remove)):
            self.neighboors.remove(to_remove[i])
    
    def gn(self):
        self.distance_gn = []
        for i in self.neighboors:
            self.distance_gn.append(abs(i[1] - self.cinit)+abs(i[0] - self.rinit)) #Diferencia entre el punto inicial y su vecino en columnas
    
    def hn(self):
        self.distance_hn = []
        for i in self.neighboors:
            self.distance_hn.append(abs(i[0] - self.goal_index[0])+abs(i[1] - self.goal_index[1])) #Diferencia entre el punto inicial y su vecino en columnas
    
    def fn(self):
        self.distance_fn = []
        for i in range(len(self.neighboors)):
            self.distance_fn.append(int(self.distance_gn[i]) + int(self.distance_hn[i]))
        
        print(self.distance_fn)
    
    def select_minimum(self):
        self.trip.append(self.current)
        min_point = np.amin(self.distance_fn)
        index_min = self.distance_fn.index(min_point)
        new_index = self.neighboors[index_min]
        self.current = self.mapm[new_index[0],new_index[1]]
        print(self.current)
    
    def check(self):
        if(self.current == self.goal):
            print(self.trip)
            return False
        else:
            return True




