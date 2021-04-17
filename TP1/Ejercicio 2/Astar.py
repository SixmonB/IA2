import numpy as np
import math

class Astar:
    def __init__(self,init,goal,mapm,shelves,halls):
        self.init = init
        self.goal = goal
        self.current = self.init
        self.mapm = mapm
        self.shelves = shelves
        self.halls = halls
        self.way = []
        self.ch = True
        self.count_gn = 0
        self.distance_fn = []
        self.distance_hn = []
        self.distance_gn = []
        self.nodes = []

    def find_neighboors(self):
        self.neighboors = []
        ri = self.current[0]
        ci = self.current[1]
        self.neighboors = [[ri,ci+1],[ri,ci-1],[ri+1,ci],[ri-1,ci]]
        to_remove = []
        for i in self.neighboors:
            if (i[0]<0) or (i[1]<0):
                to_remove.append(i)
            elif(i in self.shelves)and(i != self.goal):
                to_remove.append(i)
        
        for i in range(len(to_remove)):
                self.neighboors.remove(to_remove[i])

        for i in range(len(self.neighboors)):
            self.nodes.append(self.neighboors[i])
            
    
    def gn(self):
        for i in range(len(self.neighboors)):
            self.distance_gn.append(self.count_gn)
        self.count_gn+=1

    def hn(self):
        for i in self.neighboors:
            r1 = pow((i[0] - self.goal[0]),2)
            r2 = pow((i[1] - self.goal[1]),2)
            self.distance_hn.append(math.sqrt(r1+r2)*2)
        
    def fn(self):
        for i in range(len(self.neighboors)):
            self.distance_fn.append(self.distance_gn[i] + self.distance_hn[i])
    
    def select_minimum(self):
        cond = True
        while cond:
            min_point = min(self.distance_fn)
            index_min = self.distance_fn.index(min_point)
            new_current_index = self.nodes[index_min]
            if(self.mapm[new_current_index[0],new_current_index[1]] == 0):
                self.current = new_current_index
                self.mapm[new_current_index[0],new_current_index[1]]=1
                self.way.append(self.current)
                cond = False
            elif(self.mapm[new_current_index[0],new_current_index[1]] == 1):
                self.nodes.remove(new_current_index)
                self.distance_fn.remove(min_point)
            if(new_current_index == self.goal):
                self.ch = False
                self.check
        self.distance_gn = []
        self.distance_hn = []
    
    def check(self):
        return self.ch




