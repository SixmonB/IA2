
def calcular_pertenencia(value,fuzzy_set,type):
    keys = []
    u = []
    j=0
    for key,val in fuzzy_set.items():
        if value<val[1] and value>val[0]:
            keys.append(key)
    
    print(keys)
    centers = encontrar_centros(keys,fuzzy_set)
    
    m_t=0.055 #Las pendientes de las rectas no cambian, son las mismas , solo cambia sus signo
    m_v=1.25

    if type == 'theta':
        m=m_t
    else:
        m=m_v

    #Finalmente, calculamos las pertenencias
    for i in centers:
        aux_u = m*(value-i)+1
        if aux_u>1:
            m = -m
            aux_u = abs(m*(value-i)+1)
        u.append(aux_u)
        j+=1
    print(u)


def encontrar_centros(keys,fuzzy_set):
    centers = []
    for i in keys:
        aux = fuzzy_set[i]
        if i != 'PG' or i != 'NG':
            center = (aux[0]+aux[1])/2
        if i=='NG':
            center = aux[1]*2
        if i=='PG':
            center = aux[0]*2 
        centers.append(center)
    return centers