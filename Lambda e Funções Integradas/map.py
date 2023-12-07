# map

# Exemplo 1
# Calcular o tamanho de cada palavra em uma tupla

tupla = ("Isabel", "Anderson", "Rainold")

for nome in tupla:
    print(f'O nome {nome} tem {len(nome)} letras.')


def conta(n):
    return len(n)


x = map(conta, tupla)

print(x)
print(list(x))
