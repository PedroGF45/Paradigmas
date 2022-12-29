from eventos import evento
class cap:
    def __init__(self):
        self._ri = []

    def acr(self, e):
        if isinstance(e, evento):
            i = 0
            w = self._ri
            while i < len(w) and w[i].inst() <= e.inst():
                i = i+1
                self._ri.insert(i, e)
        else:
            raise ValueError('o argumento não é um evento')

    def vaziaQ(self):
        return self._ri == []

    def retira(self):
        if self.vaziaQ():
            raise ValueError('operação sai aplicada a fila vazia')
        else:
            del (self._ri[0])

    def proximo(self):
        if self.vaziaQ():
            raise ValueError('operação primeiro aplicada a fila vazia')
        else:
            return self._ri[0]
