class Cache():
    'Guara la distancia entre ubicaciones apra acelerar el codigo'
    def __init__(self) -> None:
        self.MEMO = dict()
        

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