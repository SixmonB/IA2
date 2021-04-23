import numpy as np
from Layout import *
from Astar import *
from Node import *

if __name__ == "__main__":
    cols = 16
    rows = 16
    layout = Layout(rows,cols)
    mapxy = layout.create_map()
    halls = layout.create_halls()
    shelves = layout.create_shelves()
    init = [0,0]
    goal = [15,15]
    node_init = Node(init,None)
    node_goal = Node(goal,None)
    astar = Astar(init,goal,shelves)
    current_node = node_init
    all_nodes = []
    first_it = False
    while astar.check():
        current_node.find_neighboors(shelves,goal,all_nodes)
        for i in range(len(current_node.neighboors)):
            if current_node.neighboors[i] not in all_nodes:
                all_nodes.append(Node(current_node.neighboors[i],current_node))
            else:
                for j in all_nodes:
                    if(j.value == current_node.neighboors[i]):
                        indice = all_nodes.index(j)
                all_nodes.append(j)
        current_node.visited = 1
        astar.gn(current_node.neighboors)
        astar.hn(current_node.neighboors)
        astar.fn(current_node.neighboors)
        current_node = astar.select_minimum(current_node,all_nodes)
    astar.clean_way(mapxy)
    print(astar.count_gn)
    
    

    #astar.clean_way(rows,cols)
  
    









