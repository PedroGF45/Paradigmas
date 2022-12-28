class fila:
    
    def __init__(self):
        self._ri = []
        
    def entra(self,elemento):
        self._ri.insert(len(self._ri),elemento)
        # ou self._ri.append(elemento)
        
    def vaziaQ(self):
        return self._ri == []
    
    def sai(self):
        if self.vaziaQ():
            print('operação sai aplicada a fila vazia')
        else:
            del(self._ri[0])
            
    def primeiro(self):   
        if self.vaziaQ():
            print('operação PRIMEIRO aplicada a fila vazia')
        else:
            return self._ri[0]
        
    def comp(self):
        return len(self._ri)