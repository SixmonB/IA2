import numpy as np
from Layout import *
from Astar import *

if __name__ == "__main__":
    cols = 13
    rows = 16
    layout = Layout(rows,cols)
    mapxy = layout.create_map()
    print(mapxy)
    halls = layout.create_halls()
    shelves = layout.create_shelves()
    init = 1
    goal = 27
    astar = Astar(init,goal,mapxy,shelves,halls)
    while astar.check():
        astar.find_neighboors()
        astar.gn()
        astar.hn()
        astar.fn()
        astar.select_minimum()
    









