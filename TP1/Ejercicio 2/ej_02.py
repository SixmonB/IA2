import numpy as np
from Layout import *
from Astar import *
from Node import *

if __name__ == "__main__":
    cols = 17
    rows = 16
    layout = Layout(rows,cols)
    mapxy = layout.create_map()
    halls = layout.create_halls()
    shelves = layout.create_shelves()
    init = [0,1] #Punto de incio
    goal = [15,15] #Punto meta
    node_init = Node(init,None) #Instanciamos el nodo inicio
    node_goal = Node(goal,None) #Instanciamos el nodo meta
    astar = Astar(init,goal,shelves)
    current_node = node_init
    all_nodes = []
    while astar.check():
        current_node.find_neighboors(shelves,goal,all_nodes) #Se buscan los vecinos del nodo actual y se los agrega a la lista neighboors
        for i in range(len(current_node.neighboors)):
            #if current_node.neighboors[i] not in all_nodes: #Creamos los OBJETOS de tipo nodo, de cada vecino del nodo actual y los agregamos a la lista all_nodes
            all_nodes.append(Node(current_node.neighboors[i],current_node))
            #else:
            #    for j in all_nodes:
            #        if(j.value == current_node.neighboors[i]):
            #            indice = all_nodes.index(j)
            #    all_nodes.append(j) 
        current_node.visited = 1
        astar.gn(current_node.neighboors)
        astar.hn(current_node.neighboors)
        astar.fn(current_node.neighboors)
        current_node = astar.select_minimum(current_node,all_nodes)
    
    shortest_way,mapxy = astar.clean_way(mapxy)
    print("Camino mas corto: \n",shortest_way)
    print("Layout de puntos recorridos: \n",mapxy)

  
    









