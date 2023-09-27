#Operadores de atribuição são utilizados para atribuir valor a uma variável

x = 10
# soma
#x = x + 2
x += 2

print(x)

#subtração

#x = x - 3
x -= 3
print(x)

#multiplicação

#x = x * 2
x *= 2
print(x)

#divisão
#x = x / 3
x /= 3
print(int(x))

a = 5
b = 10

a+=b
a-=b
c=a
b=c+10
a = c - b
print(a)
#qual o valor de a?

nome = 'Diego'
sobrenome = 'Santos'

nome_completo = nome + ' ' + sobrenome

print(nome_completo)