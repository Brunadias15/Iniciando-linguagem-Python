# > DICIONÁRIO - Associa um nome (chave)  unico para o elemento na lista

#Criando dicionaários
dicionario = {} #vazia

#com elementos- primeiro a chave depois o elemento
dicionario = {'nome': 'bruna', 'idade': 26, 'altura': 1.67}

print(dicionario)
print(dicionario['nome']) #pegando so o nome

#adicionando elementos em dicionário
dicionario['programadora'] = "Sim"
print(dicionario)

#iterando sobre um dicionário
#por padrão percorre a chave do dicionário
for i in dicionario:
    print(i, dicionario[i])

#testando a existencia de uma chave
print('peso' in dicionario)
print('altura' in dicionario)