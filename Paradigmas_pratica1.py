#Aulas praticas de Paradigmas da Programacao
#Que esperar das expressoes e o tipo de dado

a = (3 + 4 * 5 - 2) / 7 # 3.0 - Float
atype = type(a)
print("a=", a, atype)

b = 3 + 4 * 5.0 - 2 / 7
btype = type(b)
print("b=", b, btype)

c = int(5.78)
ctype = type(c)
print("c=", c, ctype)

d = float(2)
dtype = type(d)
print("d", d, dtype)

e = 4 ** 2
etype = type(e)
print("e", e, etype)

f = abs(-4.75)
ftype = type(e)
print("f=", f, ftype)

g = 4.25e-1 + 8e-2
gtype = type(g)
print("g", g, gtype)