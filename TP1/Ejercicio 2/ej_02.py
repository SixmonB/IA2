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
    init = [2,14]
    goal = [3,4]
    node_init = Node(init,None)
    node_goal = Node(goal,None)
    astar = Astar(init,goal,shelves)
    current_node = node_init
    all_nodes = []
    all_nodes_values = []
    while astar.check():
        current_node.find_neighboors(shelves,goal,all_nodes) #Se buscan los vecinos del nodo actual y se los agrega a la lista neighboors
        for i in current_node.neighboors:
            if (i not in all_nodes_values):
                all_nodes.append(Node(i,current_node))
            else:
                for j in all_nodes:
                    if(j.value == i):
                        all_nodes.append(j)
                        break
        current_node.visited = 1
        astar.gn(current_node.neighboors)
        astar.hn(current_node.neighboors)
        astar.fn(current_node.neighboors)
        current_node = astar.select_minimum(current_node,all_nodes)
        all_nodes_values = []
        for i in all_nodes:
            all_nodes_values.append(i.value)
    
    shortest_way,map = astar.clean_way(mapxy)
    print("Camino mas corto: ",shortest_way)
    print("Costo del camino: ",len(shortest_way))
    print("Layout de puntos recorridos: ")
    print(map)
  
    









