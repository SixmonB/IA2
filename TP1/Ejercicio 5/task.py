class Task(object):
    def __init__(self,ide,duration,tipo, domain):
        self.ide = ide
        self.tipo = tipo
        self.duration = duration
        self.domain = domain.copy()