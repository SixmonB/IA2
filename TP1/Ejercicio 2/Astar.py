import numpy as np
class Astar:
    def __init__(self,init,goal,mapm,shelves,halls):
        self.init = init
        self.goal = goal
        self.mapm = mapm
        self.shelves = shelves
        self.halls = halls
    
    def find_neighboors(self):
        init_index = np.where(self.mapm == self.init)
        self.neighboors = []
        ri = int(init_index[0])
        ci = int(init_index[1])
        self.ri = ri
        self.ci = ci
        self.neighboors = [[ri,ci+1],[ri,ci-1],[ri+1,ci],[ri-1,ci],[ri+1,ci+1],[ri-1,ci-1],[ri+1,ci-1],[ri-1,ci+1]]
        to_remove = []
        for i in self.neighboors:
            print(i)
            if (i[0]<0) or (i[1]<0):
                to_remove.append(i)
            elif(i[0] in self.shelves) or (i[1] in self.shelves):
                to_remove.append(i)
        
        for i in range(len(to_remove)):
            self.neighboors.remove(to_remove[i])

        print(self.neighboors)
    
    def gn(self):
        for i in self.neighboors:
            distance_c = i[1] - self.ci
            distance_r = i[0] - self.ri
        
        print(distance_c,distance_r) 

