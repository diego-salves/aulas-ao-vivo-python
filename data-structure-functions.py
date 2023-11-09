# Funções globais

# len
x = [4, 5, 6]
print(len(x))

# tuple
tup = ("maçã", "banana", "morango", "banana")

# print(tup.index("banana"))
# print(tup.count("banana"))

# Como alterar uma tupla
lista_tup = list(tup)
lista_tup.append("laranja")
tup = tuple(lista_tup)

print(tup)

tupla1 = (1, 2, 3, 4)
tupla2 = (5, 6, 7, 8)

tupla1 += tupla2
print(tupla1)

# set
#possui count e index como a tupla

# listas
lista1 = ["maçã", "banana", "morango", "banana"]

#printar último elemento
print(lista1[- 1])
print(lista1[- 2])

print(lista1[1: 4])
print(lista1[1:])
print(lista1[: 2])

if "morango" in lista1:
    print("Morango está na lista")

#print(lista1.index("morango"))

#sort, ordena os números
lista2= [6,7,523,253,346,453,345,453,345,453]
lista2.sort()
print(lista2)

lista3 = ["maçã", "banana", "morango"]
print(lista3)
lista3.append("laranja")
print(lista3)

lista3.insert(0, "pessego")
print(lista3)

lista3.extend(lista1)

print(lista3)
#remove o item especificado retornando o valor
lista3.pop(1)

#remove o item especificado não retornando o valor

del lista3[0]

#remove o ultimo item
lista3.pop()
print(lista3)

lista3.clear()

print(lista3)

#dicionário

dicionario1 = {"nome": "diego", "idade": 27}

# dicionario1.pop("nome") - remove o item especificado
# dicionario1.popitem() - remove o último item
# dicionario1.clear() - exclui todos os dados do dicionário

print(dicionario1)

reference = "https://www.w3schools.com/python/python_dictionaries_methods.asp"

dicionario1.update({"profissão": "desenvolvedor"})

print(dicionario1)

dicionario1.update({"numeros": [1,2,3,4], "sexo": "masculino"})

print(dicionario1)
