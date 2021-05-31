#import sqlite3

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


'''class Cache():
    'Guara la distancia entre ubicaciones apra acelerar el codigo'
    def Conect_db(self):
        self.con = sqlite3.connect("orders.db")
        self.cur = self.con.cursor()
    
    def Create_table(self):
        self.cur.execute("CREATE TABLE orders (p1 VARCHAR(50),p2 VARCHAR(50),cost INTEGER)")

    def Read_db(self,p1,p2):
        self.cost = 0
        str_p1 = str(p1)
        str_p2 = str(p2)
        entities_r = (str_p1,str_p2)
        try:
            data = self.cur.execute("SELECT cost FROM orders WHERE p1=? AND p2=?",entities_r)
            self.cost = data.fetchone()
            self.cost = self.cost[0]
            self.con.commit()
        except:
            self.cost = 0
        return self.cost
            
    def Write_db(self,p1,p2,cost):
        entities_w = (str(p1),str(p2),cost)
        self.cur.execute("INSERT INTO orders VALUES (?,?,?)", entities_w) #Insertamos datos en la db
        self.con.commit() #Confirmamos cambios para que se carguen a la db

    def Disconect_db(self):
        self.con.close()
    
memo = Cache()
memo.Conect_db()
#memo.Create_table()
found = memo.Read_db([4,2],[4,4])
if memo.cost == 0:
    print("Not found")
    memo.Write_db([4,2],[4,4],2)
else:
    cost = memo.cost
memo.Disconect_db()'''

