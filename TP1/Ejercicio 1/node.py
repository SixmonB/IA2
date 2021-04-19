class New_node(object):
    def __init__(self, name, position, begining, finish):
        self.name = name
        self.position = position
        self.value = 0
        self.begining = begining
        self.finish = finish
        distance_origin = 0
        distance_end = 0
        for i in range(6):
            distance_origin += pow(self.position[i] - self.begining[i], 2)
            distance_end += pow(self.position[i] - self.finish[i], 2)
            
        self.distance = pow(distance_origin, 0.5) + pow(distance_end, 0.5) 
