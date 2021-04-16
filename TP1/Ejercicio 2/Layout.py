import numpy as np

class Layout:
    def __init__(self,rows,cols):
        self.layout = np.zeros((rows,cols))
        self.halls = []
        self.shelves = []
        self.cols = cols
        self.rows = rows
        self.x = []
        self.y = []
        countx = 0
        county = 0
        for i in range(int(rows/4)):
            self.x.append(countx)
            countx+=5

        for i in range(int((cols-1)/3 + 1)):
            self.y.append(county)
            county+=3
        print(self.x,self.y)

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

