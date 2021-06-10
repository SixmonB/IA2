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
def open_node(father, nodes, cnt, level):
    for a in range(father[0] -2, father[0] +4, 2):
        for b in range(father[1] -2, father[1] +4, 2):
            for c in range(father[2] -2, father[2] +4, 2):
                for d in range(father[3] -2, father[3] +4, 2):
                    for e in range(father[4] -2, father[4] +4, 2):
                        for f in range(father[5] -2, father[5] +4, 2):
                            if not Check_Obstacles([a,b,c,d,e,f]):
                                if not Check_Generado([a,b,c,d,e,f]):
                                    Agregar_Espacio_Nodos([a,b,c,d,e,f])
                                    nodes.append(node.New_node(cnt, [a,b,c,d,e,f], origin, end,level+1))
                                    cnt+=1
    return nodes, cnt

NODOS_GENERADOS = list()

# agregamos a una lista los strings de las posiciones articulares para no agregar nodos repetidos
def Agregar_Espacio_Nodos(position):
    'agrega un nodo al espacio de nodos'
    position_str = list(map(str,position))
    nodo_str = ','.join(position_str)
    if nodo_str not in NODOS_GENERADOS:
        NODOS_GENERADOS.append(nodo_str)
        
# verificacion de que un nodo a generar no haya sido generado antes
def Check_Generado(position):
    'Checkea si un nodo ya ha sido generado'
    position_str = list(map(str,position))
    nodo_str = ','.join(position_str)
    if nodo_str in NODOS_GENERADOS: return True
    else: return False

# verificacion de no generar un nodo que este bloqueado por algun obstaculo  
def Check_Obstacles(position):
    for i in range(len(obstacle1.obstacle)):
        if position == obstacle1.obstacle[i] or position == obstacle2.obstacle[i] or position == obstacle3.obstacle[i]:
            return True
    return False



# Robot de 6 gdl -> 6 dimensiones en el espacio articular
# Generacion de las posiciones articulares inicial y final en grados
d = 6 # dimensiones

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
# es importante agregar el origen al espacio de nodos para evitar el riesgo de generarlo como un 
# vecino de alguna posicion secundaria
Agregar_Espacio_Nodos(origin)
level = 1
cnt = 0
# generacion de los primeros 729 nodos a partir del origen. 3^6 = 729. 3 posiciones en 6 dimensiones
# el ultimo argumento es el nivel de profundidad del origen.
nodes, cnt = open_node(origin, nodes, cnt, 0)
path = []
while True:
    # ordenamos la lista de nodos segun la distancia heuristica  
    nodes.sort(key=lambda x:x.distance)
    aux = 0
    while True:
        # verificamos que el nodo no haya sido abierto
        if nodes[aux].value == 0:

            # verificamos si hemos encontrado el final dentro de los nodos abiertos 
            # antes de abrir un nuevo nodo. Tambien evitamos generar los nodos vecinos del objetivo
            if nodes[aux].position == end:
                    print("\nFinal encontrado: \n", nodes[aux].position)
                    path.append(nodes[aux])
                    print("Nivel: \n", nodes[aux].level)
                    break
            else:
                # si el nodo no ha sido abierto, generamos sus hijos y 
                # ponemos value = 1 para indicar q ya fue abierto
                # nodes(father, destiny, name, level)    
                nodes, cnt = open_node(nodes[aux].position, nodes, cnt, nodes[aux].level)
                level +=1          
                nodes[aux].value = 1
                path.append(nodes[aux])
                # los prints son para visualizar resultados
                print("\nAbriendo nodo numero: \n", nodes[aux].name)
                print("Nodo abierto en posicion: \n", nodes[aux].position)
                print("Funcion heuristica del nodo abierto: \n", nodes[aux].distance)
                print("Nivel: \n", nodes[aux].level)

                break
        
        else:
            # si el nodo ya fue abierto, analizamos el nodo siguiente en la lista
            aux += 1  
    if nodes[aux].position == end:
        break
    # verificamos la satisfaccion de la condicion

    #print(cnt)
shortest_path = path

# recorremos la lista desde el final comparando con el elemento anterior. 
# La idea es que el nivel de profundidad de un elemento sea mas grande
# que el elemento anterior, por lo que si no se cumple esta condicion,
# se elimina los elementos que signifiquen un desvio del camino mas corto.#
for i in range(len(shortest_path)-1, 0, -1):
    if shortest_path[i].level <= shortest_path[i-1].level:
        shortest_path.remove(nodes[i-1])

# printeo de los nodos del camino mas corto
print("Camino mas corto: \n")
for i in range(len(shortest_path)):
    print("\nPosicion: \n", shortest_path[i].position)
    print("Nivel: \n", shortest_path[i].level)





