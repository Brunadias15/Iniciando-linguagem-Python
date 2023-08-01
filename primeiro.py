#1 Saida de dados em Python (Imprime na tela)
print('1 - Hello World!')

#2 Entrada de dados
#O que o usuário digitar no input será atribuido a variável que recebe, que nesse caso é a variável "linguagem".
#'n' com barra invertida "\n" pula uma linha.
linguagem = input('\n2 - Qual á a linguagem de programação que você esta estudando?')
print('A linguagem que você esta estudando é:', linguagem )

#Os dados são guardados em varavéis, que cada mais é um pedacinho da memória que armazena esses dados.
#Toda variável tem um nome único

# > Variáveis 
# 3 Primeiro vem o nome da variável recebe (=) o que ela vai receber.

idade = 26 #Variável tipo Int 
nome = 'Bruna' #Variável tipo String
altura = 1.65 #variável tipo float
estudante = True #variável tipo bool

#parametro sep= usado para definir o caractere de separação
print("\n 3 - Imprimindo as variáveis:", idade, nome, altura, estudante, sep='-')

""" Tipos primitivos de variáveis
int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000;
float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14;
str: cadeias de caracteres, ou seja, dados textuais. (string)
bool: valores lógicos (booleanos): true ou false. (escrever com letra maiúscula - case sensitive)
"""
#4 imprimindo o tipo das variáveis
print ("\n 4 - imprimindo o tipo das variáveis:")
print( type(idade))
print( type(nome))
print( type(altura))
print( type(estudante))
