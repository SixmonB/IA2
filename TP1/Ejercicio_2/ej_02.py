import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

import numpy as np
from Ejercicio_2.Layout import *
from Ejercicio_2.Astar import *
from Ejercicio_2.Node import *

import sys  
from pathlib import Path  
file = Path(__file__). resolve()  

package_root_directory = file.parents [1]  

sys.path.append(str(package_root_directory))
import numpy as np
from Ejercicio_2.Layout import *
from Ejercicio_2.Astar import *
from Ejercicio_2.Node import *

def Short_Way(init, goal, layout):
    node_init = Node(init,None)
    node_goal = Node(goal,None)
    astar = Astar(init,goal,layout.shelves)
    current_node = node_init
    all_nodes = []
    all_nodes_values = []
    count = 0

    while astar.check():
        count +=1
        current_node.find_neighboors(layout.shelves,goal,all_nodes)
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
    astar.clean_way(layout.layout)
    return astar

if __name__ == "__main__":
    cols = 18
    rows = 18
    layout = Layout(rows,cols)    
    init = [1,0]
    goal = [10,1]
    short = Short_Way(init,goal,layout)
    print("Camino mas corto: ",short.shortest_way)
    print("Costo del camino: ",short.way_distance)
    print("Layout: ")
    print(short.mapm)
  
    









