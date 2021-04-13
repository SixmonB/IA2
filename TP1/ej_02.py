import numpy as np
from Layout import *
from Astar import *

if __name__ == "__main__":
    cols = 13
    rows = 15
    layout = Layout(rows,cols)
    mapxy = layout.create_map()
    halls = layout.create_halls()
    shelves = layout.create_shelves()
    init = 7
    goal = 26
    astar = Astar(init,goal,mapxy,shelves,halls)
    astar.find_neighboors()
    astar.gn()









