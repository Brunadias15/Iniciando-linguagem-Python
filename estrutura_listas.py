#Estrutura de Listas
#Listas []
notas = [7.9, 9.7, 8.2]

#criando listas
#lista vazia
lista = []

#vazia com função
lista = list()

#listas aceitam todos todos os tipos de variáveis de uma vez só
lista = [10, 'Bruna', 3.4541, True]

#acessando alementos
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[-1])
#acessando com negativos, começando do -1, acessa o ultimo elemento, -2 o penultimo e assim por diante

#Slides - pegar um pedaço
lista = [10, 50, 30, 40, 25, 60, 5]

#começa no indice 0 [10] e vai até menor que 3 [50, 30]
print(lista[0:3])
#Sem definir onde parar ele mostra até o final
print(lista[2:])
#Colocando o terceiro elemento ele pula da quantidade que for solicitado no ultimo elemento
print(lista[2:6:2])

# > Iterações com FOR
# 1 usando os proprios elementos da lista
for elemento in lista:
    print(elemento)

# 2 utilizando os indices
#len - traz a quandidade de elementos que existem na lista
print("comprimento da lista: ", len(lista))

#percorrendo pelos indices 
for i in range(len(lista)):
    print(lista[i])

# > MÉTODOS DE LISTAS
print("\n ---- Metodos de listas ----")

#append - adiciona um elemento na lista

lista2 = [1, 3, 12, 8, 20]
print('antes do append', lista2)

lista2.append(7)
print('depois do append', lista2)

#insert - adiciona elemento e você escolhe em qual indice adicionar
#primeiro elemento é o indice e segundo é numero que você quer adicionar
lista2.insert(2,10)
print('depois do insert', lista2)

#extend - juntar duas listas
lista.extend(lista2)
print('depois do extend', lista)

#pop - remover elemento
#se nenhum valor for passado ele elimina o ultimmo indice, passando o indice ele elimina o mesmo.
lista2.pop(2)
print('depois do pop', lista2)

#remove - diz qual o elemento que quer remover - Caso tenha elementos iguais, ele remove apenas o primeiro
lista2.remove(12)
print('depois do remove', lista2)

#count - quer contar quantas vezes o elemento passa na lista
print('quantidade de 8 na lista: ', lista2.count(8))

#index - mostra qual o indice do elemento que você passar
print('qual indice do elemento 20: ', lista2.index(20))

#sort - ordenar sua lista
lista2.sort() #crescente
print(lista2)

lista2.sort(reverse=True) #decrescente
print(lista2)

#FUNÇÕES PARA LISTAS
print("\n----FUNÇÕES PARA LISTAS----")
#len - quantos elementos tem na lista
print(len(lista2))

#sum - soma todos os elementos da lista
print(sum(lista2))

#max - retorna o maior valor da lista
print(max(lista2))

#min - retorna o menor valor da lista
print(min(lista2))
