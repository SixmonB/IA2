import sys  
from pathlib import Path  
file = Path(__file__). resolve()  

package_root_directory = file.parents [1]  

sys.path.append(str(package_root_directory))
import numpy as np
from Ejercicio_2.Layout import *
from Ejercicio_2.Astar import *
from Ejercicio_2.Node import *

def Short_Way( init, goal, layout):
    node_init = Node(init,None)
    node_goal = Node(goal,None)
    astar = Astar(init,goal,layout.shelves)
    current_node = node_init
    all_nodes = []
    first_it = False

    while astar.check():
        current_node.find_neighboors(layout.shelves,goal,all_nodes)
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
    astar.clean_way(layout.layout)
    return astar



if __name__ == "__main__":
    cols = 13
    rows = 14
    layout = Layout(rows,cols)    
    print(layout.shelves)   
    print(layout.layout)   
    init = [4,12]
    goal = [0,0]
    short = Short_Way(init,goal,layout)
    
    print(short.way_distance)
    
    
    

    #astar.clean_way(rows,cols)
  
    









