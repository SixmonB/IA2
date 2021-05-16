
from os import write

def create_file(rows,cols):
    name = "memoria_cache_"+str(rows)+"_"+str(cols)+".txt"
    file = open(name,"r+")
    return file

def write_file(file,x1,y1,x2,y2,cost):
    p1 = str([x1,y1])
    p2 = str([x2,y2])
    file.write(p1+","+p2+"="+str(cost))
    file.close()



