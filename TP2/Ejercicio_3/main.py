from functions import *
import math

def run(theta,velocity):
    #Definición de fam, limites de trabajo y conjuntos difuso
    fuzzy_sets = ['NG','NP','Z','PP','PG']
    fam = [['PG','PG','PG','PP','Z'],
            ['PG','PG','PP','Z','NP'],
            ['PG','PP','Z','NP','NG'],
            ['PP','Z','NP','NG','NG'],
            ['Z','NP','NG','NG','NG']]
    rad = math.pi/180
    max_values_variables = [45*rad,2,50]
    #Definimos conjuntos borrosos, cada lista tiene [pmin,pmax,centro]
    
    fuzzy_sets_theta = {'NG':[-45*rad,-18*rad,-36*rad],'NP':[-36*rad,0*rad,-18*rad],'Z':[-18*rad,18*rad,0],'PP':[0*rad,36*rad,18*rad],'PG':[18*rad,36*rad,45*rad]}
    fuzzy_sets_v = {'NG':[-2,-0.8,-1.6],'NP':[-1.6,0,-0.8],'Z':[-0.8,0.8,0],'PP':[0,1.6,0.8],'PG':[0.8,2,1.6]}
    fuzzy_sets_force = {'NG':[-50,-20,-40],'NP':[-40,0,-20],'Z':[-20,20,0],'PP':[0,40,20],'PG':[20,50,40]}  

    #Calculamos a que conjunto difuso pertenecen las variables de entrada ( ) de entrada tita y tita' (o v )
    sets_theta = obtener_conjuntos_difusos(theta,fuzzy_sets_theta,'theta')
    sets_v = obtener_conjuntos_difusos(velocity,fuzzy_sets_v,'v')

    #Calcular pertenencias
    u_theta = calcular_pertenencia(theta,sets_theta,fuzzy_sets_theta,'theta')
    u_v = calcular_pertenencia(velocity,sets_v,fuzzy_sets_v,'v')

    #Formamos las reglas, por ejemplo PG Y PG -> NG , como [PG,PG,NG] y vemos si hay consecuentes repetidos. Devolvemos las reglas definitivas
    rules = formar_reglas(sets_theta,sets_v,fam,fuzzy_sets,u_theta,u_v)

    abstract_force = desborrosificar(rules,fuzzy_sets_force)
    print("Fuerza: ",abstract_force)
    return (abstract_force)

absf = run(45*math.pi/180,2)

    





