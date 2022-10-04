# Tuple and Arrays edits
# Ficha 2

# Ex 1

a = (4, (2, 0, 7), (8, 9), 1, (5, ), (2, 1))
print(a + (2,0))
print(len(a))
print(a[1]) # second term of a (2, 0, 7)
print(a[2][0]) # third term of a (8, 9) and first term of it (8)
# print(a[len(a)]) # out of range because len(a) is 7 and last index on a is 6
print(9 in a) # 9 isn't on a but (8, 9) is, so false
print((1, 2) not in a) # (1, 2) isn't on a so it's true
# a[1] = 'xpto' # we cannot change tuples

# Ex 2

b = ((5, 2, 8, 3, 9, 1, 10))
c = b[4:] # Create a tuple from the indice 4 onwards
d = b[4:7] # Create a tuple from the indice 4 till indice 7-1=6
e = (b[4],) + (b[5],) + (b[6],) # Create a tuple concatenating the elements with indices 4, 5 and 6
f = b[-3:] # Create a tuple from the indice -3 onwards - better choice
print(c) # (9, 1, 10)
print(d) # (9, 1, 10)
print(e) # (9, 1, 10)
print(f) # (9, 1, 10)

# Ex 3

g = ((5, 2, 8), (9, 1), (7, ), (4, 2, 9, 8))
g_firstE_lastE = g[0][2]
print(g_firstE_lastE) # 8
g_fourthE_ThirdE = g[3][2]
print(g_fourthE_ThirdE) # 9
h = (g[1],) + (g[-2],) * 3
print(h) # ((9, 1), (7,), (7,), (7,))

i = ()
for x in range(0, len(g)): # for x getting the values from 0 to length in g tuple(4)
    i = i + (len(g[x]),) 
    print(i) 
    # (3,)
    # (3, 2)
    # (3, 2, 1)
    # (3, 2, 1, 4)

j = tuple(len(y) for y in g) # I want the length of y for each y in tuple g
print(j) # (3, 2, 1, 4)

# Ex 4

k = tuple(x for x in range(1, 26, 2)) # if range(1, 25, 2) it won't output 25
print(k) # (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25)

# Ex 5

print('4 / 2 * 3') # '4 / 2 * 3' because it's a string
print('xpto'[2:]) # 'to'
print('xpto'[1:-1]) # 'pt' elments from index 1 and -1-1=-2
print(len('abc xpto')) # 8
print('xpto' * 2) # 'xptoxpto' concatenates 'xpto' to 'xpto'
l = tuple(x * 2 for x in (4, (0,), (8, 9), 1)) # multiplicates the integers and concatenates the tuples
print(l) # (8, (0, 0), (8, 9, 8, 9), 2)
m = tuple(x[0] for x in ('xpto', 'abc')) # gets the first element of each element
print(m) # ('x', 'a')
n = tuple(str(x) for x in range (2, 20, 3)) # x gets the virtual sequence 2 5 8 11 14 17 and then puts in a string
print(n) # ('2', '5', '8', '11', '14', '17')

# Ex 6

o = [2, 9, 1, 1, 2, 3, 4, 5, 6]
print(o[2:5]) # [1, 1, 2]
print(o[:4]) # [2, 9, 1, 1]
print(o[-3:-1]) # [4, 5]
print(o[-15:-3]) # [2, 9, 1, 1, 2, 3] python accepts -15 as the last number
print(o[:]) # [2, 9, 1, 1, 2, 3, 4, 5, 6]
p = o
p[1] = 3 # Changes the the second element (9) to 3
print(p) # [2, 3, 1, 1, 2, 3, 4, 5, 6]
print(o) # [2, 3, 1, 1, 2, 3, 4, 5, 6] Because it is the same object!
print(o[:len(o)-1]) # [2, 3, 1, 1, 2, 3, 4, 5] Everything unless the last element

# Ex 7

q = [4, 5, 1, 2, 3, 9]
del(q[3]) # deleted element in position 3 (2)
print(q) # [4, 5, 1, 3, 9]
q.append(0) # insert 0 in the last position of q
print(q) # [4, 5, 1, 3, 9, 0]
q.insert(2, 8) # insert in position 2, the integer 8
print(q) # [4, 5, 8, 1, 3, 9, 0]
q[1] = 7 # Change the element in position 1(5), to the integer 7
print(q) # [4, 7, 8, 1, 3, 9, 0]
r = q + [2,(5,6,7),[5],(9,)] # Concatenates 2 arrays with tuples, integers and arrays in it
print(r) # [4, 7, 8, 1, 3, 9, 0, 2, (5, 6, 7), [5], (9,)]

# Ex 8

s = [[x*x for x in range(1,26)],[y for y in range(100, 201, 2)]] # square x when x is in virtual sequence from 1-25 and y when y is in virtual sequence from 100-200 with increment of 2
print(s) # [[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625], [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]]