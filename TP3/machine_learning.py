import numpy as np
import matplotlib.pyplot as plt
import collections
from random import randint, uniform

from numpy.core.defchararray import array

# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)
def generar_datos_clasificacion(cantidad_ejemplos, cantidad_clases, modo):
    FACTOR_ANGULO = 0.79
    AMPLITUD_ALEATORIEDAD = 0.1

    # Calculamos la cantidad de puntos por cada clase, asumiendo la misma cantidad para cada 
    # una (clases balanceadas)
    n = int(cantidad_ejemplos / cantidad_clases)

    # Entradas: 2 columnas (x1 y x2)
    x = np.zeros((cantidad_ejemplos, 2))
    # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
    # t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")

    randomgen = np.random.default_rng() 

    # Por cada clase (que va de 0 a cantidad_clases)...
    for clase in range(cantidad_clases):
       
        if modo == "REGRESION":
            indices = range(cantidad_ejemplos)
            t = np.zeros((cantidad_ejemplos,),dtype= np.float64)

            x1 = np.linspace(0, 1, n)
            x2 = np.linspace(0, 1, n)
            x[indices] = np.c_[x1, x2]
            
            t[indices] = (x1 + x2) #.reshape(cantidad_ejemplos,0)
        
        else:
            t = np.zeros(cantidad_ejemplos, dtype="uint8")
            # Tomando la ecuacion parametrica del circulo (x = r * cos(t), y = r * sin(t)), generamos 
            # radios distribuidos uniformemente entre 0 y 1 para la clase actual, y agregamos un poco de
            # aleatoriedad
            radios = np.linspace(0, 1, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)

            # ... y angulos distribuidos tambien uniformemente, con un desfasaje por cada clase
            angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n)

            # Generamos un rango con los subindices de cada punto de esta clase. Este rango se va
            # desplazando para cada clase: para la primera clase los indices estan en [0, n-1], para
            # la segunda clase estan en [n, (2 * n) - 1], etc.
            indices = range(clase * n, (clase + 1) * n)

            # Generamos las "entradas", los valores de las variables independientes. Las variables:
            # radios, angulos e indices tienen n elementos cada una, por lo que le estamos agregando
            # tambien n elementos a la variable x (que incorpora ambas entradas, x1 y x2)
            x1 = radios * np.sin(angulos)
            x2 = radios * np.cos(angulos)
            x[indices] = np.c_[x1, x2]

            # Guardamos el valor de la clase que le vamos a asociar a las entradas x1 y x2 que acabamos
            # de generar. Para regresión, aplicamos  una función.
            t[indices] = clase

    return x, t

def generar_datos_clasificacion_alternativo(cantidad_ejemplos, cantidad_clases): # by mere
    #Inicializamos arrays
    n = int(cantidad_ejemplos / cantidad_clases) #Cantidad de ejemplos
    x = np.zeros((cantidad_ejemplos, 2))
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")

    #Inicializamos arrays vacios
    centros_x = np.array([])
    centros_y = np.array([])
    angulos = np.array([])

    #Se inicializan valores. Su usan estos limites para que los puntos no tengan valores muy mayores a 1.
    paso = 120*np.pi/180
    angulo = np.pi/2
    radio_ppal = uniform(0.2,0.4)

    #Generamos los centros de las circunferencias
    for i in range(1,cantidad_clases+1,1):
        angulos = np.append(angulos,angulo)
        centros_x = np.append(centros_x,radio_ppal*np.cos(angulo)+0.5)
        centros_y = np.append(centros_y,radio_ppal*np.sin(angulo)+0.5)
        angulo = angulo + paso
    
    #Generamos todos los puntos pertenecientes a cada clase
    for clase in range(cantidad_clases):
        x1 = np.array([])
        x2 = np.array([]) 
        centro_x = abs(centros_x[clase])
        centro_y = abs(centros_y[clase])
        radio = uniform(0.2,0.4)
        for i in range(n):
            ran_value = uniform(0,radio)
            x1 = np.append(x1,centro_x+(radio-ran_value)*np.cos(i*(2*np.pi/100)))
            x2 = np.append(x2,centro_y+(radio-ran_value)*np.sin(i*(2*np.pi/100)))
        indices = range(clase * n, (clase + 1) * n)
        x[indices]=np.c_[x1,x2]
        t[indices]=clase
    return x, t

def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):
    randomgen = np.random.default_rng()

    w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))
    if n_capa_3 == 0:
        w2 = 0.1 * randomgen.standard_normal((n_capa_2,)) #.reshape(n_capa_2,)   
        b2 = 0.1 * randomgen.standard_normal((1,))
    else: 
        w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
        b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}

def sigmoide(x):
    return 1 / ( 1 + np.exp(-x) )



def ejecutar_adelante(x, pesos, f_activacion = 'ReLU' ):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]

    # Funcion de activacion SIGMOIDE para la capa oculta (h -> "hidden")
    if f_activacion == 'SIGMOIDE':  h = sigmoide(z)    #1 / ( 1 + np.exp(-z) )
        
    # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
    else:  h = np.maximum(0, z)        
        

    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = (h.dot(pesos["w2"]) + pesos["b2"])  #.reshape(300,)
    
    
    return {"z": z, "h": h, "y": y}


def clasificar(x, pesos):
    # Corremos la red "hacia adelante"
    resultados_feed_forward = ejecutar_adelante(x, pesos)
    
    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
    # (es decir, por filas)
    max_scores = np.argmax(resultados_feed_forward["y"], axis=1)

    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return max_scores[:, 0]

# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x, t, pesos, learning_rate, epochs, x_validation, t_validation, N_EPOCHS, TOLERANCIA, MODO, f_activ = 'ReLU'): # quite  x_test, t_test para usr en temple
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0)
    check_validation = list()
    

    for i in range(epochs):
        
        
        # Ejecucion de la red hacia adelante
        resultados_feed_forward = ejecutar_adelante(x, pesos, f_activ)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]
        
        # LOSS ---------------------------

        # Clasificacion: Softmax
        if MODO == 'CLASIFICACION':
            # a. Exponencial de todos los scores
            exp_scores = np.exp(y)

            # b. Suma de todos los exponenciales de los scores, fila por fila (ejemplo por ejemplo).
            #    Mantenemos las dimensiones (indicamos a NumPy que mantenga la segunda dimension del
            #    arreglo, aunque sea una sola columna, para permitir el broadcast correcto en operaciones
            #    subsiguientes)
            sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)

            # c. "Probabilidades": normalizacion de las exponenciales del score de cada clase (dividiendo por 
            #    la suma de exponenciales de todos los scores), fila por fila
            p = exp_scores / sum_exp_scores

        # d. Calculo de la funcion de perdida global. Solo se usa la probabilidad de la clase correcta, 
        #    que tomamos del array t ("target")
        if MODO == 'REGRESION':
            # # a. Cuadrado del error ( Li(W) = (ti - yi)^2 )
            try :
                a = (t-y)
                square_error = np.power( (y-t),2)
            except: print(i)
            loss = np.sum(square_error)/m
        else:
            loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))
        
        # Regresion: Mean Squared Error (MSE)

        
        
        # accuracy = precision(y, t)
        # Mostramos solo cada 1000 epochs
  

        # Extraemos los pesos a variables locales
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation

        if MODO == "CLASIFICACION":
            dL_dy = p                # Para todas las salidas, L' = p (la probabilidad)...
            dL_dy[range(m), t] -= 1  # ... excepto para la clase correcta
            dL_dy /= m

            dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
            dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2

            dL_dh = dL_dy.dot(w2.T)

        # Ajustamos los pesos: MSE

        else:
            
            dL_dy = 2*(y-t)/m
            dL_dw2 = h.T.dot(dL_dy)
            
            # dL_db2 = dL_dy 
            dL_db2 = np.sum(  ( dL_dy ) , keepdims=True)
          
            dL_dh = dL_dy.reshape(m,1).dot(w2.reshape(1,pesos['w1'].shape[1]))


        if f_activ == 'SIGMOIDE':
            dh_dz  = sigmoide(z) * (1- sigmoide(z)) 
            dL_dz = dL_dh * dh_dz
        else:
            dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
            dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)
        
     
        


        dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1


        # Aplicamos el ajuste a los pesos
        w1 += -learning_rate * dL_dw1
        b1 += -learning_rate * dL_db1
        w2 += -learning_rate * dL_dw2
        b2 += -learning_rate * dL_db2

        # Actualizamos la estructura de pesos
        # Extraemos los pesos a variables locales
        pesos["w1"] = w1
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2

       
        # calculos de 
        # resultados_test = ejecutar_adelante(x_test, pesos, f_activ)
        # y_test = resultados_test["y"]
        # accuracy_test = precision(y_test, t_test)

        # calculos para validation
        resultados_validation = ejecutar_adelante(x_validation, pesos, f_activ)
        y_validation = resultados_validation["y"]
        accuracy_validation = precision(y_validation, t_validation, MODO)
        check_validation.append(accuracy_validation)

        # if i %1000 == 0:
            # print("Loss epoch", i, ":", loss)
            # print("Precision epoch", i, ":", accuracy_test)
            # check_validation.append(loss)
            # if not validation(TOLERANCIA, check_validation):
            #     break
            # print('')        

        if i % N_EPOCHS == 0:
             print("Loss epoch", i, "with validation :", loss)
             print("Precision Test epoch", i, ":", accuracy_validation)  # --- > lo quite para pdoer llamar a la funcion desde temple
        #     # check_validation.apppend(loss)
        #     if i > 2:
        #         if not validation(TOLERANCIA,check_validation):
        #             break

    
    resultados_validation = ejecutar_adelante(x_validation, pesos, f_activ)
    y_validation = resultados_validation["y"]
    accuracy_validation = precision(y_validation, t_validation, MODO)
    check_validation.append(accuracy_validation)
    return accuracy_validation
            


def validation(tol, check_validation):
    
    if (check_validation[-1] - check_validation[-2]) < -tol:
        print("Error Validation")
        return False
    return True


def precision(y, target, modo):
    
    # recibe el valro de y 
    if modo == 'CLASIFICACION':
        maximos = y.argmax(axis = 1)
        c = np.equal(maximos,target)
        counter = collections.Counter(c)
        precision = counter[1]/len(target)*100
    
    else: 
        
        dif = np.abs((target - y))
        tol =  np.exp(-8)
        aciertos = dif < tol
        counter = collections.Counter(aciertos)
        precision = counter[1]/len(target)*100
    

    return precision
  

def iniciar(numero_clases, numero_ejemplos, graficar_datos, FUNCION_ACTIVACION = 'SIGMOIDE', MODO = 'CLASIFICACION'):

    # Generamos datos
    x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases, MODO)
    print(t.shape)
    x_test, t_test = generar_datos_clasificacion(int(numero_ejemplos*0.1), numero_clases,MODO)
    x_validation, t_validation = generar_datos_clasificacion(int(numero_ejemplos*0.2), numero_clases,MODO)
    N_EPOCHS = 700
    TOLERANCIA = 3
    # Graficamos los datos si es necesario
    if graficar_datos:
        # Parametro: "c": color (un color distinto para cada clase en t)
        if MODO == 'CLASSIFICACION':
            plt.scatter(x[:, 0], x[:, 1], c=t)
            plt.show()
        # else:
        #     ax = plt.axes(projection='3d')
        #     zline = t
        #     xline = x[:,0]
        #     yline = x[:,1]
        #     ax.plot3D(xline, yline, zline, 'gray')

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 70
    NEURONAS_ENTRADA = 2
    
    if MODO == 'REGRESION':
        pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3= 0)
    
    else:
        pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)
    
    # Entrena
    LEARNING_RATE= 0.85
    EPOCHS=10000
    train(x, t, pesos, LEARNING_RATE, EPOCHS, x_validation, t_validation, N_EPOCHS, TOLERANCIA, MODO,f_activ = FUNCION_ACTIVACION) # # quite  x_test, t_test para usr en temple

    # test

    # validation
    # ejecutar_adelante(x_validation, pasos_validation)
if __name__ == '__main__':
    iniciar(numero_clases=3, numero_ejemplos=300, graficar_datos=False,FUNCION_ACTIVACION= 'ReLU', MODO='CLASIFICACION')