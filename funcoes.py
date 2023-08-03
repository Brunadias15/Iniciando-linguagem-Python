#Funções
def saudacao():
    print("Seja bem vinda")

saudacao()

#Funções com parâmetros
nome = input("Digite seu nome: ")
def saudacao(nome):
    print(f"Seja bem vinda, {nome}")

saudacao(nome)

#função com parametros default
def saudacao(nome, curso='Python'):
    print(f"Seja bem vinda, {nome}, você esta fazendo curso de {curso}")

saudacao('bruna')

#função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)

print("A soma dos numeros é: ", resultado)

#exemplo de colculadora usando várias coisas que aprendemos
num1 = float(input("Qual o primeiro numero: "))
operacao = input("Qual a operação: ")
num2 = float(input("Qual o segundo numero: "))
def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    
resultado = calculadora(num1, num2, operacao)

print(resultado)