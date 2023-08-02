#Estrutura automatizada para pedir nota do aluno
soma = 0
for i in range(1, 4):
    nota = float(input(f"informe a sua nota {i}:")) #Colocando uma variavel dentro da string, antes das aspas colocar "f" e colocar a variavel dentro das chaves

    soma = soma + nota

print("Média: ", soma/3)