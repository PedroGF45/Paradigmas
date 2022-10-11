# Tuple, Arrays and Dictonary edits
# Ficha 3

# Ex 1

alunosNotas = {'Joao': 10, 'Maria': 14, 'Jose': 8}
notas = tuple(alunosNotas[x] for x in alunosNotas) # tuple with each grade
print(notas) #(10, 14, 8)

x = input('Escreva o seu nome: ',)
if x not in alunosNotas: 
    print('Erro: esse nome nao consta do registo')
elif (x in alunosNotas) & (alunosNotas[x] >= 10):
    print(alunosNotas[x])
else:
    print('Rep')

# Ex 2

notas = {'Joao': (10,12),'Maria': (9,14),'Jose': (12,8),'Rafael': (6,7)}
mediaAlunos = {x: (notas[x][0] + notas[x][1])/2 for x in notas}
print(mediaAlunos) # {'Joao': 11.0, 'Maria': 11.5, 'Jose': 10.0, 'Rafael': 6.5}

notaMaxima = max([notas[x][0] for x in notas]) # gets the maximum value on the array
print(notaMaxima) # 12

# Ex 3

listaInteiros = [0, 1, 2, 3, 4, 5]
listaInversa = [listaInteiros[x] for x in range(-1,-len(listaInteiros)-1,-1)] # range starts at -1 and goes to -6 with increments of -1
print(listaInversa) # [5, 4, 3, 2, 1, 0]
# or
listaInversa1 = [listaInteiros[-1-x] for x in range(len(listaInteiros))] # range starts at 0 and goes till 6-1=5
print(listaInversa1) # [5, 4, 3, 2, 1, 0]
# or
listInversa2 = listaInteiros[::-1] # inverts the list
print(listInversa2) # [5, 4, 3, 2, 1, 0]