lista_numeros = []

for c in range(0,50):
    lista_numeros.append(c)

print(lista_numeros)

pares = []

for numero in lista_numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

pares_comprehension = [numero for numero in lista_numeros if numero % 2 == 0]

print(pares_comprehension)