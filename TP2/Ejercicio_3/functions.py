import collections
import math
from numpy.core import shape_base

'''def crear_grupos_difusos(max_limit,sets):
    length = (max_limit*2/5)
    limits = list()
    aux = 0
    for i in range(5):
        aux += (-max_limit)+length*2
        limits.append(aux)
    print(limits)'''

def obtener_conjuntos_difusos(value,fuzzy_set,typ):
    keys = []
    for key,val in fuzzy_set.items():
        if value<val[1] and value>val[0]:
            keys.append(key)
        elif typ == 'theta' and value>=45*math.pi/180: keys=['PG']
        elif typ == 'theta' and value<=-45*math.pi/180: keys=['NG']
        elif typ == 'v' and value>=2: keys=['PG']
        elif typ == 'v' and value<=-2: keys=['NG']
    return keys

def calcular_pertenencia(value,keys,fuzzy_set,type):
    centers = encontrar_centros(keys,fuzzy_set)
    m_t=3.18 #Las pendientes de las rectas no cambian, son las mismas , solo cambia sus signo
    m_v=1.25

    if type == 'theta':
        m=m_t
    else:
        m=m_v
    j=0
    u = dict()

    #Calculamos las pertenencias
    print(keys)
    if len(keys)==1:
        u[keys[0]]=1
    else:
        for i in centers:
            aux_u = m*(value-i)+1
            if aux_u>1: #La partenencia no puede dar mayor a 1 , si lo da es porque la pendiente en esa parte es negativa:
                m = -m
                aux_u = abs(m*(value-i)+1)
            u[keys[j]]=aux_u
            j+=1
    #print("Pertenencias:{}".format(u))
    return u


def encontrar_centros(keys,fuzzy_set):
    centers = []
    for i in keys:
        aux = fuzzy_set[i]
        centers.append(aux[2])
    #print("Centros: ",centers)
    return centers

def formar_reglas(sets_theta,sets_v,fam,sets,u_theta,u_v):
    rules = []
    for i in sets_theta:
        aux = []
        index_set_theta = sets.index(i)
        for j in sets_v:
            index_set_v = sets.index(j)
            force = fam[index_set_theta][index_set_v]
            aux = [i,j,force]
            rules.append(aux)
    #print(rules)

    #Tomamos las primeras 2 reglas y vemos si tienen o no el mismo consecuente
    u_preproc,repeated_rules = preprocesamiento(rules,u_theta,u_v)
    mins_values = list()
    for i in range(len(rules)):
        if i not in repeated_rules:
            k=rules[i]
            a1 = u_theta[k[0]]
            a2 = u_v[k[1]]
            mins_values.append([min(a1,a2),k[2]])
    total_values=mins_values+u_preproc
    #print(total_values)
    return total_values

def preprocesamiento(rules,u_theta,u_v):
    #Guardamos los consecuentes de cada regla
    consecuents = list()
    for i in rules:
        consecuents.append(i[2])

    #Analizamos si hay consecuentes iguales
    repeated = [x for x, y in collections.Counter(consecuents).items() if y > 1]

    #Si los hay, guardamos en una lista que reglas son estas
    same_consecuent = dict()
    aux = list()
    repeated_rules = list()
    count = 0
    if repeated != []:
        for i in consecuents:
            for k in repeated:
                if i==k:
                    aux.append(rules[count])
                    repeated_rules.append(count)
                count+=1
            same_consecuent[k]=aux
        count = 0
        
    #Aplicamos la regla de max(min(a1,a2),min(b1,b2),...)
    a = list()
    mins_values = list()
    max_value = list()
    for key,i in same_consecuent.items():
        mins_values = []
        for k in i:
            a1 = u_theta[k[0]]
            a2 = u_v[k[1]]
            a.append([a1,a2])
            mins_values.append(min(a1,a2))
        max_value.append([max(mins_values),key])
    #retornamos el valor maximo obtenido al aplicar la regla y cuales son las reglas que tenian el mismo consecuente
    return max_value,repeated_rules

def desborrosificar(rules,fuzzy_set_force):
    #Multiplicamos el valor de pertenencia obtenido por su centro:
    product=list()
    sum_us = 0
    #print(rules)
    for i in rules:
        center_value = fuzzy_set_force[i[1]][2]
        sum_us += i[0]
        product.append(center_value*i[0])
    abstract_force = sum(product)/sum_us
    return abstract_force

crear_grupos_difusos(45,['NG','NP','Z','PP','PG'])