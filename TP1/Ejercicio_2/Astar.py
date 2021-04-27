import numpy as np
import math

class Astar:
    def __init__(self,init,goal,shelves):
        self.init = init #Coordenadas del punto de inicio
        self.goal = goal #Coordenadas del punto meta 
        self.current = self.init #Coordenadas del punto actual
        self.shelves = shelves #Contiene coordenadas [x,y] de los puntos que son estantería
        self.way = [] #Guarda al final, todos los puntos por los cuales paso el codigo (todos los puntos que tienen un "1")
        self.ch = True
        self.count_gn = 0 #Tiene en cuenta el costo del camino. Suma 1 en cada iteracion
        self.distance_fn = [] #f = gn + hn
        self.distance_hn = [] #Considera la distancia entre cada vecino del nodo actual y el punto meta
        self.distance_gn = [] #Guarda el costo del camino de cada vecino del nodo actual (es decir, guarda count_gn para cada vecino)
        self.shortest_way = []
        self.way_distance = int() 
    def gn(self,neighboors): #Costo del camino, suma 1 a la funcion distance_gn en cada iteración
        for i in range(len(neighboors)):
            self.distance_gn.append(self.count_gn)
        self.count_gn+=1

    def hn(self,neighboors): #Distancia euclideana al punto de fin
        for i in neighboors:
            r1 = pow((i[0] - self.goal[0]),2)
            r2 = pow((i[1] - self.goal[1]),2)
            self.distance_hn.append(math.sqrt(r1+r2)*2)
        
    def fn(self,neighboors): #f = gn + hn
        for i in range(len(neighboors)):
            self.distance_fn.append(self.distance_gn[i] + self.distance_hn[i])

    def select_minimum(self,current_node,nodes):
        cond = True
        while cond:
            min_point = min(self.distance_fn)
            index_min = self.distance_fn.index(min_point)
            if(nodes[index_min].visited == 0):
                nodes[index_min].visited = 1
                self.way.append(nodes[index_min])
                cond = False
            elif(nodes[index_min].visited == 1):
                nodes.remove(nodes[index_min]) #Si el pto ya fue visitado, entonces debemos removerlo de nodes, para que ya no busque en el y no ramifique sus vecinos nuevamente.
                self.distance_fn.remove(min_point)
            if(nodes[index_min].value == self.goal): #Condición para cuando se llegue a la meta.
                self.ch = False
                self.check
        self.distance_gn = []
        self.distance_hn = []
        return nodes[index_min]

    def clean_way(self,mapm):
        n = len(self.way) - 1 
        cond = True
        new_way = []
        new_node = self.way[n]
        while cond:
            node = new_node
            par = node.parent
            new_way.append(node.value)
            mapm[node.value[0],node.value[1]]=1
            if(par.parent == None):
                cond = False
            new_node = par
        # print(mapm)
        # print(new_way)
        self.shortest_way = new_way.copy()
        self.way_distance = len(self.shortest_way)
        # print(len(new_way))

    def check(self):
        return self.ch




