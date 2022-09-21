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
i = (2 > 3) and (5/0 > 7) #False
# error - division by zero:  j = (5/0 > 7 ) and (2 > 3)
print(i)
