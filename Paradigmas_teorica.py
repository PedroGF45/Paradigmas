#Hello World

#Iniciacao dos operadores e regra de operadores no Python
a = 5 + 10/5 * (2+2)
print(a)

#Iniciacao das expressoes condicionais
b = 5 if 3 > 5 else (7 if 8 > 9 else 99)
print(b)

#Operacoes com numeros - Divisao, Quociente da Divisao e Resto da divisao
c = 7 / 2
d = 7 // 2
e = 7 % 2
print (c, d, e)

#Outras operacoes com numeros
f = round(3.6)
g = int(3.6)
h = float(3.6)
print(f, g, h)

#Introducao aos valores booleanos and, or, not
#i = (2 > 3) and (5/0 > 7) False
#j = (5/0 > 7 ) and (2 > 3) error - division by zero:  

#Outras operacoes de igualdade
k = 1 if 3 == 2 else "3 nao e igual a 2"
l = "3 e diferente de 2" if 3 != 2 else 1
print (k, l)

a1 = 10 + 5 # Atribuicao de um nome e uma expressao
a1 + 5.5 # Nao ha atribuicao a variavel a1
print("a1=", a1)
a1 = a1 + 5.5
print("a1 vale agora ", a1)
b1 = a1 
print("b1=", b1)
a1 = 12
print("a1=", a1, "b1=", b1)
# c1 + 5 # Erro - c is not defined

#Atribuicoes multiplas
d1 = 7
e1 = 15
d1, e1, = e1, d1 # Troca de variaveis
print("d1=", d1, "e1=", e1)

#Cuidado com estas atribuicoes 
f1 = 7
g1 = 15
f1 = g1 #15
g1 = f1 #15
print("f1=", f1, "g1", g1)

#Para fazer o de cima precisamos de uma outra variavel
h1 = 7
i1 = 15
j1 = h1 #7
h1 = i1 #15
i1 = j1 #7
print("h1=", h1, "i1=", i1, "j1=", j1)

# Definicao de tuplos/tuples
k1 = (5 + 10, True, 4.0 - 2.5)
print("k1=", k1)

l1 = len(()) # Como nao ha elementos, a length e zero
print("l1=", l1)

m1 = (5,9,) # Ignora o espaco vazio
print("m1=", m1)

n1 = (5)
o1 = (5,)
print("n1=", n1, "o1=", o1)
print("classe do n1 e", type(n1), "classe do o1 e", type(o1)) # Em python as classes sao os tipos de dados. Para ser tuple tem de ter virgula

p1 = (5, True, (5, 8, 0)) # 3 argumentos
print("length e ", len(p1))