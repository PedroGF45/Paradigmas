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
print(c)
print(d)
print(e)
print(f)