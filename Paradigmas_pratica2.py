# Formatacao de cadeias de caracteres (formatacao por %, str.format() e f-strings)

# Ex 3

nome = "Petra"
print(f"Ola! O meu nome e {nome}")

tempo = 65433998
print(f"{tempo} segundos correspondem a, aproximadamente, {(tempo / 3600 / 24):.2f}")

nota_Marcelo = 52.83
nota_Gabriel = 74.94
nota_Amanda = 87.75
nota_media = (nota_Marcelo + nota_Gabriel + nota_Amanda) / 3
print(f"O Marcelo obteve {nota_Marcelo} % na frequencia. \n O Gabriel obteve {nota_Gabriel} % na frequencia. \n A Amanda obteve {nota_Amanda} % na frequencia. \n A media da turma na frequencia foi de {nota_media:.0f} %, arredondada as unidades.")
