# Conversão de tipos

idade = '27'

#Conferindo o tipo de variavel da idade, nesse caso é str
print (idade, type(idade))

#Convertando a srt idade para int
idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

"""
int() - converte para Int
str() - converte para String
float() - converte para float
bool() - converte para boolean
"""

#Em Python tudo que é digitado no input é lido como String, porém quando se ter certeza do tipo de variável que o usuário irá digitar faz-se a conversação
altura = float(input("Informe sua altura: "))

print(altura, type(altura))