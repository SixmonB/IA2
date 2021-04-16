import random
import numpy as np

def generate(array, d, o):
# Generacion de valores articulares al azar. Discretizacion cada 2°. 0<Rango articular<180 
    for x in range(d):
        for y in range(o):
            array[x][y] = random.randrange(0, 180, 2)
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
origin = np.zeros((d,1))
origin = generate(origin, d, 1)
end = np.zeros((d,1))
end = generate(end, d, 1)
obstacles = np.zeros((d,o))
obstacles = generate(obstacles, d, o)
position = origin
# Generacion de nodos
#while True:
#    nodes = nodes(position, v)

print("Origen en:\n", origin)
print("Meta en:\n", end)
node = np.array([[[[[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]]]]])
print(node)
print(node.shape)




# discretizacion cada 2°


