class evento:
    
    def __init__(self, x, y, z):
        self._i = x # where i is the instant of the event
        self._c = y # where c is the category of the event
        self._p = z # where p is the priority of the event
    def inst(self):
        return self._i # return the instant of the event
    def cat(self):
        return self._c # return the category of the event
    def prio(self):
        return self._p # return the priority of the event