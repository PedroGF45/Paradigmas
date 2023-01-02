from eventos import evento
class cap:
    def __init__(self):
        self._ri = []

    def acr(self, e):    
        if isinstance(e, evento):
            i = 0
            w = self._ri
            while i < len(w) and w[i].inst() <= e.inst():
                i += 1
            self._ri.insert(i, e) 
        else:
            raise ValueError ('o argumento não é um evento')

    def vaziaQ(self):
        return self._ri == []

    def comp(self):
        return len(self._ri)
    
    def getIndexPri(self, elemento):
        for i in range(len(self._ri)):
            if elemento == self._ri[i].pri():
                return i
    
    def getIndexCat(self, elemento):
        for i in range(len(self._ri)):
            if elemento == self._ri[i].cat():
                return i
    
    def moveToFirst(self, i):
        self._ri.insert(0, self._ri[i])

    def retira(self):
        if self.vaziaQ():
            raise ValueError('operação sai aplicada a fila vazia')
        else:
            del(self._ri[0])

    def proximo(self):
        if self.vaziaQ():
            raise ValueError('operação primeiro aplicada a fila vazia')
        else:
            return self._ri[0]

    def mostra(self):
        for i in range(len(self._ri)):
            print(dict(inst = self._ri[i].inst(), cat = self._ri[i].cat(), prio = self._ri[i].pri()))

    def primeiro(self):
        print('primeiro -> ', dict(inst = self._ri[00].inst(), cat = self._ri[0].cat(), prio = self._ri[0].pri()))
