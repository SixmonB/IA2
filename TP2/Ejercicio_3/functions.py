import collections
import math
from numpy.core import shape_base

def crear_grupos_difusos(max_limit,sets,typ):
    'Crea los grupos difusos con sus limites y sus centros'
    set_length = (max_limit*2/5)
    limits = list()
    #Cantidad de decimales a considerar en los limites dependiendo si estoy con theta,v, o f
    if typ=='theta': 
        decimals = 10
    else:
        decimals=1
    aux = round((-max_limit-set_length/2),decimals)

    for i in range(5): #El 5 es porque tengo 5 conjuntos difusos, NG,NP,Z,PP,PG
        aux += set_length
        limits.append(round(aux,decimals))
    limits = [-max_limit]+limits+[max_limit]
    fuzzy_set = dict()
    j=0
    for i in sets:
        a=j
        b=j+2
        fuzzy_set[i]=[limits[a],limits[b],limits[b]-set_length]
        j+=1

    return fuzzy_set #Devuelvo el conjunto difuso creado como un diccionario, por ejemplo para theta {'NG':[-2,-0.8,-1.6],'NP':[...]}

def fusificar(value,fuzzy_set,max_val_theta,max_val_v,typ):
    'Devuelve a que conjuntos difusos pertenece el valor que estoy analizando (que puede ser de theta o v)'
    #value = valor actual ABSTRACTO (por ejemplo pi/3 radianes)que estoy analizando
    #fuzzy_set = contiene el diccionario (creado en la funcion anterior) que contiene todos los conjuntos difusos para una variabable theta o v
    #typ = contiene el tipo de variable que estoy analizando (theta o v)
    
    keys = []
    for key,val in fuzzy_set.items():
        if value<val[1] and value>val[0]:
            keys.append(key)
        elif typ == 'theta' and value>=max_val_theta: keys=['PG']
        elif typ == 'theta' and value<=-max_val_theta: keys=['NG']
        elif typ == 'v' and value>=max_val_v: keys=['PG']
        elif typ == 'v' and value<=-max_val_v: keys=['NG']
    #keys = conjuntos difusos a los que pertenece el valor que estoy analizando (por ej. pi/5rad pertenece a PP Y PG, por ende keys = [PP,PG])
    return keys

def calcular_pertenencia(value,keys,fuzzy_set,type):
    'Calulamos la pertenencia de cada valor abstracto a cada conjunto difuso que corresponda'
    #value = valor actual ABSTRACTO de la variable que estoy analizando
    #fuzzy_set = diccionario que contiene los conjuntos difusos para una determinada variable
    #keys = conjuntos difusos a los que pertenece el valor abstracto que estoy analizando

    centers = encontrar_centros(keys,fuzzy_set) #Obtenemos los centros de cada conjunto difuso (serían los centros de los triangulos)
    m_t=3.18 #Pendiende de rectas de conjuntos difusos de theta
    m_v=1.25 #Pendiende de rectas de conjuntos difusos de velocidad

    if type == 'theta': #Elegimos con qué pendiente vamos a trabajar si estamos analizando theta o v
        m=m_t
    else:
        m=m_v
    j=0
    u = dict()

    #Calculamos las pertenencias
    if len(keys)==1:
        u[keys[0]]=1
    else:
        for i in centers:
            aux_u = m*(value-i)+1 #Ecuación de una recta => m*(x-x0)+y0
            if aux_u>1: #La pertenencia no puede dar mayor a 1 , si lo da es porque la pendiente en esa parte es negativa:
                m = -m
                aux_u = abs(m*(value-i)+1)
            u[keys[j]]=aux_u
            j+=1

    return u


def encontrar_centros(keys,fuzzy_set):
    'Encontramos los centros de cada triángulo (los centros se encuentran en la tercer componente de la lista que contiene los límites del triangulo [pmax,pmin,centro])'
    centers = []
    for i in keys:
        aux = fuzzy_set[i]
        centers.append(aux[2])
    #centers = contiene los centros pero analizanso solo los valores dentro de keys
    return centers

def formar_reglas(sets_theta,sets_v,fam,sets):
    rules = []
    #'Creamos' las reglas como una lista, por ejemplo PP Y PG -> NP la representamos como [PP,PG,NP]
    for i in sets_theta:
        aux = []
        index_set_theta = sets.index(i)
        for j in sets_v:
            index_set_v = sets.index(j)
            force = fam[index_set_theta][index_set_v]
            aux = [i,j,force]
            rules.append(aux)
    return rules

def procesamiento(rules,u_theta,u_v):
    'Procesamos las reglas creadas y obtenemos los valores de pertenencias de la fuerza'
    #Tomamos las reglas creadas y verificamos cuales tienen el mismo consecuente haciendo un preproceso.
    u_preproc,repeated_rules = preprocesamiento(rules,u_theta,u_v)
    mins_values = list()
    for i in range(len(rules)):
        if i not in repeated_rules:
            k=rules[i]
            a1 = u_theta[k[0]]
            a2 = u_v[k[1]]
            mins_values.append([min(a1,a2),k[2]])
    total_values=mins_values+u_preproc
    return total_values

def preprocesamiento(rules,u_theta,u_v):
    'Preprocesamiento para reglas que tienen los mismos consecuentes'
    
    #Guardamos los consecuentes de cada regla
    consequents = list()
    for i in rules:
        consequents.append(i[2])

    #Obtenemos cuales son los consecuentes que se repiten
    repeated = [x for x, y in collections.Counter(consequents).items() if y > 1]

    #Si los hay, guardamos en una lista que reglas tienen los mismos consecuentes 
    same_consecuent = dict()
    aux = list()
    repeated_rules = list()
    count = 0
    if repeated != []:
        for i in consequents:
            for k in repeated:
                if i==k:
                    aux.append(rules[count])
                    repeated_rules.append(count)
                count+=1
            same_consecuent[k]=aux
        count = 0
        
    #Aplicamos la regla de max(min(a1,a2),min(b1,b2),...) (osea aplicar la conjuncion y disyuncion)
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

def desfusificar(rules,fuzzy_set_force):
    'Devuelve el valor abstracto de fuerza que deberé aplicar (que aplicará finalmente el controlador)'
    #Multiplicamos el valor de pertenencia obtenido por su centro, luego sumamos y dividmos por la suma de las pertenencias:
    product=list()
    sum_us = 0
    #print(rules)
    for i in rules:
        center_value = fuzzy_set_force[i[1]][2]
        sum_us += i[0]
        product.append(center_value*i[0])
    abstract_force = sum(product)/sum_us
    return abstract_force

#crear_grupos_difusos(2,['NG','NP','Z','PP','PG'],'v')