class New_node(object):
    def __init__(self, name, position, begining, finish, level):
        # name = numero que indica el numero de nodo generado 
        # position = vector de variables articulares
        # value = indica si el nodo ya fue abierto o no
        # begining y finish se usan para calcular la funcion heuristica
        # level = nivel de profundidad en el arbol de datos
        self.name = name
        self.position = position
        self.value = 0
        self.begining = begining
        self.finish = finish
        self.level = level
        distance_origin = 0
        distance_end = 0
        max_dist = 0
        for i in range(6):
            # tomamos la maxima diferencia entre la posicion actual y el origen 
            # para tener una referencia de la cantidad de iteraciones que hubo entre
            # ambas posiciones. La idea es evitar casos en los que se rote una sola articulacion, 
            # y preferenciar aquellos casos en los que muevo todas las articulaciones al mismo tiempo#
            distance_origin = pow(pow(self.position[i] - self.begining[i], 2),0.5)            
            if distance_origin>max_dist : max_dist= distance_origin 
            distance_end += pow(pow(self.position[i] - self.finish[i], 2),0.5)

        
            
        self.distance = max_dist + distance_end 
        # print(self.distance)
