class evento:
    def __init__(self, x, y):
        self._i = x # x is the instant when the category occurs
        self._c = y # c is the category
    def cat(self):
        return self._c
    def inst(self):
        return self._i