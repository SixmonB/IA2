from machine import Machine

class Task(Machine):
    def __init__(self,ide,duration,typ):
        Machine.__init__(self,ide,typ)
        self.duration = duration