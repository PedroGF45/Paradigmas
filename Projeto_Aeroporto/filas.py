class fila_aterragem:
    
    def __init__(self):
        self._ri = []

    # the element will enter in the end of the queue   
    def entra(self,element):
        self._ri.insert(len(self._ri),element) 

    # remove element from queue
    def elimina(self, element):
        self._ri.remove(element)

    # returns true if queue is empty    
    def vaziaQ(self):
        return self._ri == []

    # deletes the first element from queue, if not empty
    def sai(self):
        if self.vaziaQ():
            print('Empty queue')
        else:
            del(self._ri[0])
            
    # returns the first element from queue, if not empty
    def primeiro(self):   
        if self.vaziaQ():
            print('Empty queue')
        else:
            return self._ri[0]
        
    # returns the length of the queue
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

class fila_media:

    def __init__(self):
        self._ri = []

    def entra(self,elemento):
        self._ri.insert(len(self._ri),elemento)
        
    def comp(self):
        return len(self._ri)