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