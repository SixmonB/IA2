import random
import numpy as np
import node
import obstacles


def generate(d):
# Generacion de valores articulares al azar. Discretizacion cada 2°. 0<Rango articular<180 
    array = []
    for x in range(d):
        array.append(random.randrange(0, 180, 2))
    return array

# generacion de nodos hijo 
# open_node(lista de posiciones articulares del nodo padre, lista donde agregar los nodos, contador)
def open_node(father, nodes, cnt):
    for a in range(father[0] -2, father[0] +4, 2):
        for b in range(father[1] -2, father[1] +4, 2):
            for c in range(father[2] -2, father[2] +4, 2):
                for d in range(father[3] -2, father[3] +4, 2):
                    for e in range(father[4] -2, father[4] +4, 2):
                        for f in range(father[5] -2, father[5] +4, 2):
                            if not Check_Obstacles([a,b,c,d,e,f]):
                                if not Check_Generado([a,b,c,d,e,f]):
                                    Agregar_Espacio_Nodos([a,b,c,d,e,f])
                                    nodes.append(node.New_node(cnt, [a,b,c,d,e,f], origin, end))
                                    cnt+=1
    return nodes, cnt 

NODOS_GENERADOS = list()
def Agregar_Espacio_Nodos(position):
    'agrega un nodo al espacio de nodos'
    position_str = list(map(str,position))
    nodo_str = ','.join(position_str)
    if nodo_str not in NODOS_GENERADOS:
        NODOS_GENERADOS.append(nodo_str)
        
def Check_Generado(position):
    'Checkea si un nodo ya ha sido generado'
    position_str = list(map(str,position))
    nodo_str = ','.join(position_str)
    if nodo_str in NODOS_GENERADOS: return True
    else: return False
    
def Check_Obstacles(position):
    for i in range(len(obstacle1.obstacle)):
        if position == obstacle1.obstacle[i] or position == obstacle2.obstacle[i] or position == obstacle3.obstacle[i]:
            return True
    return False



# Robot de 6 gdl -> 6 dimensiones en el espacio articular
# Generacion de las posiciones articulares inicial y final en grados
d = 6 # dimensiones
o = 20 # posiciones obstaculo
v = 3 # cantidad de variaciones posibles (posicion +- 1 y la posicion actual)
origin = generate(d) #[100, 100, 100, 100, 100, 100]#  generate(d)
end =generate(d)# [50, 128, 70, 116, 160, 104] # generate(d)

# generamos 3 obstaculos de 20 elementos en cada dimension
center1 = generate(d)
center2 = generate(d)
center3 = generate(d)

obstacle1 = obstacles.Obstacles(center1)
obstacle2 = obstacles.Obstacles(center2)
obstacle3 = obstacles.Obstacles(center3)
print("Origen en:\n", origin)
print("Final en:\n", end)


nodes = []
cnt = 0
# generacion de los primeros 729 nodos a partir del origen. 3^6 = 729. 3 posiciones en 6 dimensiones
nodes, cnt = open_node(origin, nodes, cnt)

while True:
    # ordenamos la lista de nodos segun la distancia heuristica  
    nodes.sort(key=lambda x:x.distance)
    aux = 0
    while True:
        # verificamos que el nodo no haya sido abierto
        if nodes[aux].value == 0:
            # si el nodo no ha sido abierto, generamos sus hijos y 
            # ponemos value = 1 para indicar q ya fue abierto #
            nodes, cnt = open_node(nodes[aux].position, nodes, cnt)
            
            
            nodes[aux].value = 1
            # los prints son para visualizar resultados
            print("Abriendo nodo numero: \n", nodes[aux].name)
            print("Nodo abierto en posicion: \n", nodes[aux].position)
            print("Funcion euristica del nodo abierto: \n", nodes[aux].distance)

            break
        
        else:
            # si el nodo ya fue abierto, analizamos el nodo siguiente en la lista
            aux += 1  
   
    # verificamos la satisfaccion de la condicion
    if nodes[aux].position == end:
        print("Final encontrado\n")
        print(nodes[aux].position)
        break
    #print(cnt)




