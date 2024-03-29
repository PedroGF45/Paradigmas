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

# Indice de tuplos

q1 = (50, 10, 9, 14)
print("o terceiro elemento ou o elemento de indice 2 e o", q1[2]) # Indices comecam da esquerda para a direito no 0. Se for no sentido contrario comecamos no -1

r1 = (7, 8, 0, 53, 999)
print(r1[5-4]) # Podemos usar calculos para descobrir o indice
# print(r1[25]) # Erro porque nao ha nenhum elemento com indice 25
# print(r1[len(r1)]) # Erro porque nao ha nehum elemento com indice 5
print(r1[-1]) # Quando usamos numeros negativos vemos da direita pa esquerda
print(r1[-3])

s1 = ((5, 7), (8, 9, 0), ("a", 3, "b")) # Tuple de 3 elementos
print("tamanho e de", len(s1))
print(s1[1][0]) # Aceder ao segundo elemento e dentro desse aceder ao primeiro elemento
print(s1[-1][2]) # Aceder ao terceiro elemento e dentro desse aceder ao terceiro elemento

# Operacoes com tuplos
t1 = (4, 6)
u1 = (1, 3, 0)
print(t1 + u1) # (4, 6, 1, 3, 0)
v1 = u1 + t1
print (v1) # (1, 3, 0, 4, 6)
print(t1 * 3) # (4, 6, 4, 6, 4, 6)

print(tuple("a8k")) # ('a', '8', 'k')

x1 = ((9, 8), (6,), (), 7)
print(7 in x1) # True
print(() in x1) # True
print(9 in x1) # False
print(9 in x1[0]) # True

y1 = (5, 12, 14, 9, 0, 0)
print(y1[1:4]) # (12, 14, 9)

z1 = (5, 15, 25, 35)
print(z1[1:3]) # (15,25)
print(z1[2:2]) # ()
print(z1[:2] + (0,) + z1[3:]) # Construct a subtuple from z1 without '25' and with '0' -> (5, 15, 0, 35)