#Estruturas de Dados

#Tipos de dados
"""
Tipos primitivos:

Numerico:
Inteiro - int -> Numeros inteiros( -2,-1,1,2,3,4....)
Real, Ponto flutuante - float -> Numeros com casas decimais(2.56)
Complexo - complex -> ver exemplo abaixo

Texto:
String - str -> textos alfanumericos("a melancia custou 12.50")

Booleano - bool -> verdadeiro ou falso (true, false)

Outros tipos:

Sequenciais: list, tuple, range
Mapping: dict
Set: set
None: None
"""

# como ver o tipo

nome = "Diego"
print(type(nome))

#tipo complex, muito incomum
x = 3 + 4j
print(type(x))

#setar o tipo de dado específico

floatNumber = float(20)

print(floatNumber)

# 4 estruturas de dados principais = Tupla, Lista, Set, Dicionário
# tuple (), list [], set {}, dict {}

# tuple
# a tupla é uma coleção ordenada, imutável e permite valores duplicados.
# ordenada, significa que tem uma ordem definida, e que a ordem não vai mudar
#imutável quer dizer que não podemos mudar, adicionar, ou remover items após a criação

tupla1 = ("maçã", "banana", "morango", ("maracujá", "pera", "pessego"), "maçã")
#print(tupla1)
#print(tupla1[3][1][2])

tupla2 = (1, 2, 3)
print(tupla2)

# exemplo de tentativa de mudança
# tupla2[1] = 0
# print(tupla2)

contaOcorrencias = tupla1.count("maçã")
print(contaOcorrencias)

# Lista (array, vetor)
# a lista é ordenada(indexáveis), mutável e permite valores duplicados.

lista1 = ["maçã", "maçã", "banana", "morango", (1, 2, 3), True]
print(lista1)
print(lista1[4][1])

tamanho = len(lista1)
print(tamanho)

# mudança de valor
lista1[2] = "uva"
lista1.append("Mentorama")
print(lista1)

#Set
# a lista é desordenada(desindexado), imutável e não permite valores duplicados.

set1 = {"maçã", "maçã", "banana", "morango", "1", 1}
print(set1)

# o Set é imutável, mas permite remoção e adição de itens

set1.add("Mentorama")
set1.remove(1)

print(set1)

#curiosidade
set2 = {False, 0, 1, True}
print(set2)

# Dicionário / Dict
# o dicionário é ordenado(a partir do python 3.7), mutável e não permite valores duplicados.

thisdict = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964,
    "blindado": False,
    "cores": ["branco", "preto", "azul"]
    #chave: valor
}

print(f'{thisdict["marca"]} {thisdict["modelo"]} {thisdict["ano"]} - Carro disponível nas seguintes cores: {thisdict["cores"]}')

thisdict2 = dict(nome="Diego", idade=27)

print(thisdict2)
