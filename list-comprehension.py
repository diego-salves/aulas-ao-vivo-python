import random
from random import randint, randrange

# Compreensão de listas - uma syntax curta para criar uma nova lista baseada nos valores de uma lista, ou listas, existentes

carros = ["civic", "celta", "nissan", "palio", "onix"]
novalista = []

for x in carros:
    if "celta" in x:
        novalista.append(x)

print(novalista)

novalista2 = [x for x in carros if "celta" in x]

print(novalista2)

# newlist = [expressão for item in iterável if condicao == true]

# retorna uma nova lista mantendo a antiga da mesma forma, muito parecido com um filtro

numeros = []

for c in range(1, 101):
    numeros.append(c)

print(numeros)

pares = []

for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        continue

print(pares)

lambdapares = [c for c in numeros if c % 2 == 0]

print(lambdapares)

randomNumbers = []

for c in range(1, 201):
    random = randrange(200)
    randomNumbers.append(random)

print(randomNumbers)

# encontrar os numeros maiores que 187 e criar uma lista

maiorque187 = []

for c in randomNumbers:
    if c > 187:
        maiorque187.append(c)

print(maiorque187)

lambdaMaiorque17 = [x for x in randomNumbers if x > 187]

print(lambdaMaiorque17)

randomNumbers2 = sorted(randomNumbers)

print(randomNumbers2)

tamanho = len(randomNumbers)

print(tamanho)

print(randomNumbers2[100])
print(randomNumbers2[150])
print(randomNumbers2[175])
print(randomNumbers2[185])
