import random
import numpy as np

def generate(array, d):
# Generacion de valores articulares al azar. Discretizacion cada 2°. 0<Rango articular<180 
    for x in range(d):
        array[x] = random.randrange(0, 180, 2)
    return array
#def nodes(position, v):
#    node = [[[[[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]]]]]
#   for a in range(v):
#      for b in range(v):
#         for c in range(v):
#            for d in range(v):
#  
#                for e in range(v):
#                  for f in range(v):
#                     node.append(position+2) 

# Robot de 6 gdl -> 6 dimensiones en el espacio articular
# Generacion de las posiciones articulares inicial y final en grados
d = 6 # dimensiones
o = 20 # posiciones obstaculo
v = 3 # cantidad de variaciones posibles (posicion +- 1 y la posicion actual)
origin = np.ones((1,1,1,1,1,1)) # lo llenamos con un 1 para indicar que ya visitamos esa posicion
origin = generate(origin, len(origin.shape))
end = np.zeros((1,1,1,1,1,1))   #lo llenamos con 0 para indicar que todavia no visitamos esa posicion
end = generate(end, len(end.shape))
obstacles = np.zeros((1,1,1,1,1,1))
obstacles = generate(obstacles, len(obstacles.shape))
position = origin
# Generacion de nodos
#while True:
#    nodes = nodes(position, v)



#node = np.array([[[[[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]]]]])
#print(node)
# print(node.shape)

print("Origen en:\n", origin)
print("Meta en:\n", end)
# discretizacion cada 2°


