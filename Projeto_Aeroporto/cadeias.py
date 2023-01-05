from eventos import evento
class cap:
    def __init__(self):
        self._ri = []

    # adds the event in ascending order by its instant
    def acr(self, e):    
        if isinstance(e, evento):
            i = 0
            w = self._ri
            while i < len(w) and w[i].inst() <= e.inst():
                i += 1
            self._ri.insert(i, e) 
        else:
            raise ValueError ('The argument is not an event')

    # True if chain of events is empty
    def vaziaQ(self):
        return self._ri == []

    # returns the length of the chain
    def comp(self):
        return len(self._ri)
    
    # gets the index of the first element in the chain of events which is priority is equal to element
    def getfirstIndexPri(self, element):
        for i in range(len(self._ri)):
            if element == self._ri[i].pri():
                return i
            else:
                return 0
    
    # gets the index of the first element in the chain of events which its category is equal to element
    def getFirstIndexCat(self, element):
        for i in range(len(self._ri)):
            if element == self._ri[i].cat():
                return i
    
    # gets the index of the second element in the chain of events which its category is equal to element
    def getSecondIndexCat(self, element):
        indices = []
        for i in range(len(self._ri)):
            if element == self._ri[i].cat():
                indices.append(i)
        if len(indices) > 1:
            return indices[1]
        else:
            return float
            
    # moves the element with index i to second in the chain of events
    def moveToSecond(self, i):
        self._ri.insert(1, self._ri.pop(i))

    # deletes the element with index i   
    def retira(self, i):
        if self.vaziaQ():
            raise ValueError('operação sai aplicada a fila vazia')
        else:
            del(self._ri[i])

    def proximo(self):
        if self.vaziaQ():
            raise ValueError('operação primeiro aplicada a fila vazia')
        else:
            return self._ri[0]

    # returns the event given the index
    def mostraE(self, i):
        return self._ri[i]

#   Benching functions
#    def mostra(self):
#        for i in range(len(self._ri)):
#            print(dict(inst = self._ri[i].inst(), cat = self._ri[i].cat(), prio = self._ri[i].pri()))
#
#    def primeiro(self):
#        print('primeiro -> ', dict(inst = self._ri[00].inst(), cat = self._ri[0].cat(), prio = self._ri[0].pri()))