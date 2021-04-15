import numpy as np

class Layout:
    def __init__(self,rows,cols):
        self.layout = np.zeros((rows,cols))
        self.halls = []
        self.shelves = []
        self.cols = cols
        self.rows = rows
        self.x = [0,5,10,15]
        self.y = [0,3,6,9,12]

    def create_map(self):
        self.layout = np.zeros((self.rows,self.cols))
        count = 0
        for i in range(self.cols):
            for j in range(self.rows):
                self.layout[j,i]=count
               count = count + 1
        return self.layout
    
    def create_halls(self):
        halls_x = []
        halls_y = []
        for i in self.x:
            for j in range(self.cols):
                halls_x.append(self.layout[i,j])
        for j in self.y:
            for i in range(self.rows):
                halls_y.append(self.layout[i,j])
        self.halls = halls_x + halls_y
        return self.halls
    
    def create_shelves(self):
        for i in range(self.cols):
            for j in range(self.rows):
                if((self.layout[j,i] in self.halls)==False):
                    self.shelves.append(self.layout[j,i])
        return self.shelves

