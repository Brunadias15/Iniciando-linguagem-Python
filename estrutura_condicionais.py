# Estruturas Condicionais (Controle de fluxo)
# Condicionais

#Exemplo de condição, se a idade for maior que 18, irá imprimir na tela "maior de idade"
idade = 10

#If palavra reservada (Se) idade maior ou igual (>=) 18 então (:) enter para identar e a condição. Do contrario (else) você não é maior
if idade >= 18:
    print('você é maior de idade.')
else:
    print('você é menor de idade.')

"""
Imagine que você queira imprimir "Aprovado(o)", caso o estudante tenha uma média 
superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""

media = float(input('Imforme a média do estudante: '))

if media >= 7:
    print('Aprovado')

#elif mesma coisa de else if, palavra reservada do python
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')

#exemplo de comparação conjunta! Nesse caso para ser aprovado o aluno precisa ter nota >= 7 e presença >= 75

nota = 10
presenca = 100

if nota >= 7 and presenca >= 75:
    print("aprovado")
else:
    print('Reprovado')
