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
        return self.layout
    
    def create_halls(self):
        halls_x = []
        halls_y = []
        for i in self.x:
            for j in range(self.cols):
                halls_x.append([i,j])
        for j in self.y:
            for i in range(self.rows):
                halls_y.append([i,j])
        self.halls = halls_x + halls_y
        return self.halls
    
    def create_shelves(self):
        for i in range(self.cols):
            for j in range(self.rows):
                if(([j,i] in self.halls)==False):
                    self.shelves.append([j,i])
        return self.shelves

