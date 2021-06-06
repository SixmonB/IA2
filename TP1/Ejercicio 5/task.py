class Task(object):
    def __init__(self,ide,duration,type, domain):
        self.ide = ide
        self.type = type
        self.duration = duration
        self.domain = domain.copy()