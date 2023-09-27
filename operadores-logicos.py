#Operadores Lógicos

#AND

numero1 = 10
numero2 = 20

a = numero1 > 0

#print(type(a))

print(numero1 > 0 and numero2 > 0)

#exemplo prático

#Pra uma pessoa dirigir, ela precisa ter mais de 18 anos E ser habilitada

# idade = int(input("Qual sua idade?"))
# habilitada = input("Você é habilitado? s ou n").lower()
#
# aprovacao = idade >= 18 and habilitada == 's'
#
# if aprovacao:   #if aprovacao == True
#     print("Você pode dirigir")
# else:
#     print("Você não pode dirigir")

#Operadores de comparação
"""
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""

#OR

numero1 = 10
numero2 = 30


resultado = numero1 < 0 or numero2 >= 20
print(resultado)

#NOT
negacao = not resultado

print(negacao)

# 0 = False 1 = True
a = 0
print(not a)

a = 3
b = 2

c = a + 3
a = 2

print('Operador de Identidade')
print(a is b)
