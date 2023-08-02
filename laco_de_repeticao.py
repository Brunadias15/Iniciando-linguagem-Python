import random #importa biblioteca random, para gerar numero aleatório

# Laços de Repetição (loop) "While" - Enquanto
#Estrutura não controlada, repete até a condição não satisfazer
numero_sorteado = random.randint (1,5) #gerando numero aletatorio entre 1 e 5

numero_escolhido = int(input("Informe um número entre 1 e 5: "))

#Enquanto (while) o numero escolhido for diferenete (!=) do numero sorteado
while numero_escolhido != numero_sorteado:
    print('Você errou o numero, tente novamente...')

    numero_escolhido = int(input("Informe um número entre 1 e 5: "))

print('Parabéns você acertou')

#estrtura controlada (Com contador)
contador = 0

while contador < 5:
    print('O contador roudou: ', contador, ' vezes')

    contador = contador + 1