#import this

x = 5
nome = "Diego"

#print(nome)
#isto é um comentário

"""
Isto é um comentário
de várias linhas
"""



#vendo os tipos
x = 4    #int
print(type(x))
x = "João"   #str
print(type(x))
x = 5
y = '5'
print(type(x))

#casting

x = str(5)
y = int(3)
z = float(3)

print(y)
print(z)
#soma = int(y + z)
print(int(y + z))

"""
str = string 
int = integer / inteiro
float = float / número decimal
"""

#aspas simples ou duplas
print("Roberto")
#é o mesmo que
print('Roberto')
print('Curtis "50 Cent" Jackson')

#case-sensitive = se considera ou não maiúsculas

a = 1
A = 2

print(a)
print(A)

#nomes de variáveis

"""
- Um nome de variável sempre deve começar com uma letra ou underline(_)
- O nome de uma variável nunca pode começar com um número
- Pode conter caracteres alfa-numericos e underlines(_)
- São case-sensitive
- O nome de uma variável NUNCA pode ser uma palavra-chave do Python
"""

teste_244c = "teste"

# print = "diego"
# print(print)

#Camel Case
#Cada palavra, menos a primeira, começa com uma letra maiúscula

meuNomeCompleto = "Diego Santos"

#Pascal Case
#Toda palavra começa com letra maiúscula

MeuNomeCompleto = "Diego Santos"

#Snake Case
#Cada palavra é separada por um underline

meu_nome_completo = "Diego Santos"

x, y, idade = "Diego", "Santos", 26

print(x)
print(y)
print(idade)