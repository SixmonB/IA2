class New_node(object):
    def __init__(self, name, position, begining, finish):
        self.name = name
        self.position = position
        self.value = 0
        self.begining = begining
        self.finish = finish
        distance = 0
        for i in range(6):
            distance += pow(pow(self.position[i] - self.begining[i], 2),0.5) + pow(pow(self.position[i] - self.finish[i], 2),0.5)
        self.distance = distance 
