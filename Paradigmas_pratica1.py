#Aulas praticas de Paradigmas da Programacao
#Que esperar das expressoes e o tipo de dado

a = (3 + 4 * 5 - 2) / 7 
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

h = 9 // 4 == 7 % 5
htype = type(h)
print("h", h, htype)

i = 8 // 2 == 8 / 2.0
itype = type(i)
print("i", i, itype)

j = 3 > 2.0 and 7 > 8.5
jtype = type(j)
print("j", j, jtype)

k = 3.0 != 2 or 7.5 > 8
ktype = type(k)
print("k", k, ktype)

l = not(17 % 2 == 0 and 3 / 0 > 5)
ltype = type(l)
print("l", l, ltype)

# m = true and False #erro
# mtype = type(m)
# print("m", m, mtype)

