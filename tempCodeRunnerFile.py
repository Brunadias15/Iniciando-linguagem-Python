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