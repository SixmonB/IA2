class Task(object):
    def __init__(self,ide,duration,tipo, domain):
        self.ide = ide
        self.tipo = tipo
        self.duration = duration
        self.domain = domain.copy()
        # incluir la cantidad de elementos en el dominio, para despues multiplicarlo por la cantidad 
        # de maquina de ese tipo disponible, y obtener el dominio real en cada momento.