from pathlib import Path
import pandas as pd
import os

class Cache():
    'Guara la distancia entre ubicaciones apra acelerar el codigo'
    def __init__(self) -> None:
        p = Path(os.getcwd())
        self.path = p/'IA2'/'TP1'/'Ejercicio_3/'

        

        self.MEMO = self.Cargar_Memoria()# dict()
        

    def Existe_Relacion(self,px, py):
        keys = self.Armar_Keys(px,py)
        return keys[0] in self.MEMO or keys[1] in self.MEMO

    def Get_Distancia(self,px,py):
        key =  self.Armar_Keys(px,py)[0]
        dist = self.MEMO[key]
        return dist

    def Add_Distancia(self,px,py,costo):
        
        if not self.Existe_Relacion(px,py):
            keys = self.Armar_Keys(px,py)
            
            self.MEMO[keys[0]] = costo
            self.MEMO[keys[1]] = costo


    def Armar_Keys(self, px, py):
        'arma las dos key para guaradar en el dic'
        key_1 = str(px)+str(py)
        key_2 = str(py)+str(px)
        
        return  key_1, key_2

    def Guardar_Memoria(self):
        
        df = pd.DataFrame(list(self.MEMO.items()),columns = ['Orden','Costo']) 
        print(df)
        # df.drop
        df.to_csv(self.path/'memo.csv', sep = ';', index = False)

        pass

    def Cargar_Memoria(self):
        if os.path.isfile(self.path/'memo.csv'):
            df = pd.read_csv(self.path/'memo.csv', sep = ';').set_index('Orden').to_dict()
            return df
            
            
        else: 
            print('No existe memoria')
            return dict()



if __name__ == '__main__':
    memo = Cache()
    pass