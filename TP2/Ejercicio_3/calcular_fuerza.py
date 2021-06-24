from functions import *
import math

def calcular_fuerza(theta,velocity):
    #Definición de fam, limites de trabajo y conjuntos difuso
    fuzzy_sets = ['NG','NP','Z','PP','PG']
    fam = [['PG','PG','PG','PP','Z'],
            ['PG','PG','PP','Z','NP'],
            ['PG','PP','Z','NP','NG'],
            ['PP','Z','NP','NG','NG'],
            ['Z','NP','NG','NG','NG']]

    #Valores máximos constantes a considerar
    theta_max = 45*math.pi/180
    v_max = 2
    force_max = 50

    #Creamos los conjuntos borrosos, con sus limites en valores abstractos y sus centros 
    fuzzy_sets_theta = crear_grupos_difusos(theta_max,fuzzy_sets,'theta')
    fuzzy_sets_v = crear_grupos_difusos(v_max,fuzzy_sets,'v')
    fuzzy_sets_force = crear_grupos_difusos(force_max,fuzzy_sets,'f')

    #Calculamos a que conjunto deifuso (NP,NG,etc) pertenecen las variables de entrada theta y v
    current_sets_theta = fusificar(theta,fuzzy_sets_theta,theta_max,v_max,'theta') #devuelve a que conjuntos difusos a los que pertenece el theta ingresado, por ejemplo ['PP','PG']
    current_sets_v = fusificar(velocity,fuzzy_sets_v,theta_max,v_max,'v')#devuelve a que conjuntos difusos a los que pertenece la v ingresada , por ejemplo ['PP','PG']

    #Calculamos el "porcentaje" de pertenencia de cada valor de entrada a cada uno de los conjuntos difusos a los que ya vimos que pertenece
    u_theta = calcular_pertenencia(theta,current_sets_theta,fuzzy_sets_theta,'theta')
    u_v = calcular_pertenencia(velocity,current_sets_v,fuzzy_sets_v,'v')

    #Formamos las reglas, por ejemplo PG Y PP -> NG , como [PG,PP,NG] y vemos si hay consecuentes repetidos.
    rules = formar_reglas(current_sets_theta,current_sets_v,fam,fuzzy_sets)

    #Procesamiento de las reglas creadas
    u_force = procesamiento(rules,u_theta,u_v)

    #Desfusificamos: A partir de las pertenencias y reglas anteriores, podemos obtener un valor abstracto de fuerza para que la aplique el control
    abstract_force = desfusificar(u_force,fuzzy_sets_force) 
    print("Fuerza: ",abstract_force)
    abstract_force = round(abstract_force,1)

    return (abstract_force)

if __name__ == "__main__":
    absf = calcular_fuerza(30*math.pi/180,2)

    





