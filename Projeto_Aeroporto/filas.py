class fila_aterragem:
    
    def __init__(self):
        self._ri = []
        
    def entra(self,elemento):
        self._ri.insert(len(self._ri),elemento)

    def elimina(self, elemento):
        self._ri.remove(elemento)
        
    def vaziaQ(self):
        return self._ri == []

    def sai(self):
        if self.vaziaQ():
            print('operacao sai aplicada a fila vazia')
        else:
            del(self._ri[0])
            
    def primeiro(self):   
        if self.vaziaQ():
            print('operacao PRIMEIRO aplicada a fila vazia')
        else:
            return self._ri[0]
        
    def comp(self):
        return len(self._ri)

class fila_descolagem:

    def __init__(self):
        self._ri = []
        
    def entra(self,elemento):
        self._ri.insert(len(self._ri),elemento)

    def elimina(self, elemento):
        self._ri.remove(elemento)
        
    def vaziaQ(self):
        return self._ri == []
    
    def sai(self):
        if self.vaziaQ():
            print('operacao sai aplicada a fila vazia')
        else:
            del(self._ri[0])
            
    def primeiro(self):   
        if self.vaziaQ():
            print('operacao PRIMEIRO aplicada a fila vazia')
        else:
            return self._ri[0]
        
    def comp(self):
        return len(self._ri)