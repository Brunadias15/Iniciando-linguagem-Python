# Laços de Repetição (loop) "For" - Para
#Para (for) uma determinada variável (i) dentro de uma faixa (in range), nesse caso 0 a 9
for i in range(10):
    print(i)

#Se eu quisesse do 5 até 10 - Lembrando que sempre começa do zero
for i in range(5, 11):
    print(i)

#Com 3 parametros, o ultimo faz a contagem de quantos vai pular
for i in range(1, 12, 2):
    print(i)

#Estrutura automatizada para pedir nota do aluno
soma = 0
for i in range(1, 4):
    nota = float(input(f"informe a sua nota {i}:")) #Colocando uma variavel dentro da string, antes das aspas colocar "f" e colocar a variavel dentro das chaves

    soma = soma + nota

print("Média: ", soma/3)