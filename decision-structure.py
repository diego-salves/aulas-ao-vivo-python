# estruturas condicionais

# if...else

"""
Condições lógicas aceitas:

a == b
a != b
a > b
a <= b
"""

"""
if condition:
    if True = Faça isso
else:
    if False = Faça isso        
"""

a = 100
b = 200
c = 300

if b > a:
    print("B é maior que a")
else:
    print("A é maior que B")

if b > a and c > b:
    print("Ambas as condições são verdadeiras")
else:
    print("Uma das condições é falsa")

if a < b < c:
    print("C é maior que todos e B é maior que A")
else:
    print("Erro")

luz = 'desligada'

if luz == 'ligada':
    print("A luz está ligada")
elif luz == 'desligada':
    print(luz)
    luz = 'ligada'
    print('ligamos a luz')
    print(luz)
else:
    print("Não pôde ser realizada nenhuma ação")

#short hand if

if b > a: print('a é maior que b')

a = 20
b = 10

#operação ternária

print("A") if a > b else print("B")

a = 20
b = 20

print("A") if a > b else print("=") if a == b else print("B")

#OR

if b > a or b == a:
    print("Uma das condições é verdadeira")
else:
    print("Ambas as condições são falsas")

#NOT

if not a != b:
    print("a NÃO é diferente de b")

#Ifs aninhados

luiz = 12

xuxa = 3 #categoria para assistir o filme
"""
0 - 4 = Criança                1
5 - 12 = Criança grande        2
13 - 17 = Adolescente          3 
18 - ~ = Adulto                4
"""
if luiz <= 4:
    categoria = 1
    if xuxa > categoria:
        print("Não pode assistir o filme")
    else:
        print("Pode assistir!")
if luiz <= 12:
    categoria = 2
    if xuxa > categoria:
        print("Não pode assistir o filme")
    else:
        print("Pode assistir!")
if luiz <= 17:
    categoria = 3
    if xuxa > categoria:
        print("Não pode assistir o filme")
    else:
        print("Pode assistir!")
if luiz >= 18:
    categoria = 4
    print("Pode assistir qualquer filme")

#match/case

senha = 1234

match senha:

    case 123:
        print("senha correta")
    case 111:
        print("senha incorreta")
    case 122:
        print("senha incorreta")
    case _:
        print("Nenhuma das opções estava correta")

# Estudarem a função pass/break
