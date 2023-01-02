from eventos import evento

class cap:
    
    def __init__ (self):
        self._ri =[]
        
    def acr(self, evt):    
        if isinstance(evt, evento):
            i = 0
            w = self._ri
            while i<len(w) and w[i].inst()<=evt.inst():
                i=i+1
            self._ri.insert(i,evt) 
        else:
            print('o argumento não é um evento')
            
    def vaziaQ(self):      
        return self._ri == []
    
    def retira(self):
        if self.vaziaQ():
            print('operação sai aplicada a fila vazia')
        else:
            del(self._ri[0])
            
    def proximo(self):
        if self.vaziaQ():
            print('Operação primeiro aplicada a fila vazia')
        else:
            return self._ri[0]

    def mostra(self):
        for i in range(len(self._ri)):
            print(dict(inst = self._ri[i].inst(), cat = self._ri[i].cat(), prio = self._ri[i].pri()))
