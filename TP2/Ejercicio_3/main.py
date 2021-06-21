from functions import *

if __name__ == "__main__":
    #Definición de fam, limites de trabajo y conjuntos difusos
    theta_lims = (-45,45)
    v_lims = (-2,2)
    force_lims = (-2,2)

    fam = [['PP','PG','PG','PP','Z'],
    ['PG','PG','PP','Z','NP'],
    ['PG','PP','Z','NP','NG'],
    ['PP','Z','NP','NG','NG'],
    ['Z','NP','NG','NG','NG']]

    #Definimos conjuntos borrosos, cada lista tiene [pmin,pmax]
    fuzzy_sets_theta = {'NG':[-45,-18],'NP':[-36,0],'Z':[-18,18],'PP':[0,36],'PG':[18,45]}
    fuzzy_sets_v = {'NG':[-2,-0.8],'NP':[-1.6,0],'Z':[-0.8,0.8],'PP':[0,1.6],'PG':[0.8,2]}  

    calcular_pertenencia(30,fuzzy_sets_theta,'theta')
    calcular_pertenencia(1.5,fuzzy_sets_v,'v')




