import numpy as np
from Layout import *
from Astar import *

if __name__ == "__main__":
    cols = 16
    rows = 16
    layout = Layout(rows,cols)
    mapxy = layout.create_map()
    halls = layout.create_halls()
    shelves = layout.create_shelves()
    init = [0,0]
    goal = [14,11]
    astar = Astar(init,goal,mapxy,shelves,halls)
    while astar.check():
        astar.find_neighboors()
        astar.gn()
        astar.hn()
        astar.fn()
        astar.select_minimum()
    print(astar.mapm)
    print(astar.way)
    print(astar.count_gn)
    #astar.clean_way(rows,cols)
  
    









