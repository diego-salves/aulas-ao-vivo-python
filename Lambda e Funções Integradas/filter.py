# filter

# Filtre uma lista de numeros e retorne apenas os maiores ou iguais que 18

idades = [5, 12, 17, 18, 24, 32, 40, 15, 27, 33, 32, 80]

idade_maior_que_18 = []

for idade in idades:
    if idade >= 18:
        idade_maior_que_18.append(idade)

print(idade_maior_que_18)


def filtraMaiores(x):
    if x >= 18:
        return True
    else:
        return False


adultos = filter(filtraMaiores, idades)
print(adultos)
print(tuple(adultos))
