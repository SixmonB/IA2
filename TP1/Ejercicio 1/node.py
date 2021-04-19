class New_node(object):
    def __init__(self, name, position, begining, finish):
        self.name = name
        self.position = position
        self.value = 0
        self.begining = begining
        self.finish = finish
        distance_origin = 0
        distance_end = 0
        max_dist = 0
        g_n = 0
        for i in range(6):
            distance_origin = pow(pow(self.position[i] - self.begining[i], 2),0.5)            
            if distance_origin>max_dist : max_dist= distance_origin 
            distance_end += pow(pow(self.position[i] - self.finish[i], 2),0.5)

        
            
        self.distance = max_dist + distance_end 
        # print(self.distance)
