class Obstacles(object):
    def __init__(self, center):
        self.center = center
        self.obstacle = []
        n = 3
        # siendo n la cantidad de elementos que quiero generar en sentido positivo y negativo
        # 2*n + 2 : limite superior del for
        # 2*n: limite inferior del for
        for a in range(center[0] -(2*n), center[0] +(2*n+2), 2):
            for b in range(center[1] -(2*n), center[1] +(2*n+2), 2):
                for c in range(center[2] -(2*n), center[2] +(2*n+2), 2):
                    for d in range(center[3] -(2*n), center[3] +(2*n+2), 2):
                        for e in range(center[4] -(2*n), center[4] +(2*n+2), 2):
                            for f in range(center[5] -(2*n), center[5] +(2*n+2) , 2):
                                self.obstacle.append([a,b,c,d,e,f])
