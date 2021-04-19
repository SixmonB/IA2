import numpy as np
import math

class Astar:
    def __init__(self,init,goal,mapm,shelves,halls):
        self.init = init #Coordenadas del punto de inicio
        self.goal = goal #Coordenadas del punto meta 
        self.current = self.init #Coordenadas del punto actual
        self.mapm = mapm #Matriz del almacén
        self.shelves = shelves #Contiene coordenadas [x,y] de los puntos que son estantería
        self.halls = halls #Contiene coordenadas [x,y] de los puntos que son pasillo
        self.way = [] #Guarda al final, todos los puntos por los cuales paso el codigo (todos los puntos que tienen un "1")
        self.ch = True
        self.count_gn = 0 #Tiene en cuenta el costo del camino. Suma 1 en cada iteracion
        self.distance_fn = [] #f = gn + hn
        self.distance_hn = [] #Considera la distancia entre cada vecino del nodo actual y el punto meta
        self.distance_gn = [] #Guarda el costo del camino de cada vecino del nodo actual (es decir, guarda count_gn para cada vecino)
        self.nodes = [] #Contiene todos los nodos por los que pasa 

    def find_neighboors(self):
        self.neighboors = []
        ri = self.current[0] #Coordenada x del punto actual
        ci = self.current[1] #Coordenada y
        self.neighboors = [[ri,ci+1],[ri,ci-1],[ri+1,ci],[ri-1,ci]]
        to_remove = []
        for i in self.neighboors:
            if (i[0]<0) or (i[1]<0): #Guarada en un vector aquellos vecinos que tienen coordenadas [x,y] negativas (es decir, que no pertenecen a la matriz)
                to_remove.append(i)
            elif(i in self.shelves)and(i != self.goal): #Guarda en un vector los vecinos que son estanterías, para luego elminarlos. Así en el vector neighboors solo nos quedan vecinos por los cuales se puede circular (pasillos).
                to_remove.append(i)
        
        for i in range(len(to_remove)): #Elimina los valores que en el for anterior guardamos en el vector "to_remove"
                self.neighboors.remove(to_remove[i])

        for i in range(len(self.neighboors)):
            self.nodes.append(self.neighboors[i])
            
    
    def gn(self): #Costo del camino, suma 1 a la funcion distance_gn en cada iteración
        for i in range(len(self.neighboors)):
            self.distance_gn.append(self.count_gn)
        self.count_gn+=1

    def hn(self): #Distancia euclideana al punto de fin
        for i in self.neighboors:
            r1 = pow((i[0] - self.goal[0]),2)
            r2 = pow((i[1] - self.goal[1]),2)
            self.distance_hn.append(math.sqrt(r1+r2)*2)
        
    def fn(self): #f = gn + hn
        for i in range(len(self.neighboors)):
            self.distance_fn.append(self.distance_gn[i] + self.distance_hn[i])
    
    def select_minimum(self):
        cond = True
        while cond:
            min_point = min(self.distance_fn) #Busca el menor valor dentro de distance_fn
            index_min = self.distance_fn.index(min_point) #Obtiene el valor dentro de el índice encontrado anteriormente.
            new_current_index = self.nodes[index_min] #Como distance_fn y nodes se rellenan y vacian al mismo tiempo, el indice anterior tambien corresponde al indice dentro de nodes.
            if(self.mapm[new_current_index[0],new_current_index[1]] == 0): #Si se cumple condicion, quiere decir que es un pto nunca visitado.
                self.current = new_current_index 
                self.mapm[new_current_index[0],new_current_index[1]]=1 #Le asigna el valor 1 al punto, para que ya no lo visite.
                self.way.append(self.current) #Agrega el punto al camino
                cond = False
            elif(self.mapm[new_current_index[0],new_current_index[1]] == 1): #Si ingresa, es un pto ya visitado.
                self.nodes.remove(new_current_index) #Si el pto ya fue visitado, entonces debemos removerlo de nodes, para que ya no busque en el y no ramifique sus vecinos nuevamente.
                self.distance_fn.remove(min_point)
            if(new_current_index == self.goal): #Condición para cuando se llegue a la meta.
                self.ch = False
                self.check
        self.distance_gn = [] #Se declaran 0 al final de cada iteración, ya que contendrán solo valores parciales, no de todo el recorrido como fn.
        self.distance_hn = []
    
    def check(self):
        return self.ch




