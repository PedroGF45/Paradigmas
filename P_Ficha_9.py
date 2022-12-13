# Exercise 1
class sequencia:
    def __init__(self):
        self._ri = [] # _ri -> representacao interna

    def acr(self, n):
        self._ri.insert(0, n)

    def vaziaQ(self):
        return self._ri == []

    def primeiro(self):
        if self.vaziaQ():
            print('sequencia vazia')
        else:
            return self._ri[0]

    def tiraPrim(self):
        if self.vaziaQ():
            print('sequencia vazia')
        else:
            del(self._ri[0])

    def comp(self):
        return len(self._ri)

    def retPares(self):
        i = self.comp() - 1
        while i >= 0:
            if self._ri[i] % 2 == 0:
                del(self._ri[i])
            i += -1

    def insereOrdenada(self, n):
        i = 0
        k = self.comp()
        while i < k and self._ri[i] <= n:
            i += 1
        self._ri.insert(i, n)

# Exercise 2

class fila:
    def __init__(self):
        self._ri = []
    
    def entra(self, x):
        self._ri.append(x)

    def vaziaQ(self):
        return self._ri == []

    def primeiro(self):
        if self.vaziaQ():
            print('Erro: sequencia vazia')
        else:
            self._ri[0]
    
    def sai(self):
        if self.vaziaQ():
            print('Erro: sequencia vazia')
        else:
            del(self._ri[0])

    def desUlt(self):
        if self.vaziaQ():
            print('Erro: sequencia vazia')
        else:
            del(self._ri[-1])