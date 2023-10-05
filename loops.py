# Lição - Saber tipos de dados primitivos

# Aula de Loops - Laços de repetição
# For - while

# For - O for é usado para iterar sobre uma sequência

nomes = ["Diego", "Anderson", "Carlos", "Luiz"]

# print(nomes[2])

for nome in nomes:
    print(nome)

# Strings são objetos iteráveis

for letra in "Mentorama":
    print(letra)

#usando break

frutas = ["maçã", "banana", "uva", "manga"]

for fruta in frutas:
    print(fruta)
    if fruta == "uva":
        break

# continue - para a iteração e continua a partir do próximo elemento

for fruta in frutas:
    if fruta == "banana":
        continue
    print(fruta)

numeros = []
# in range tem 3 parametros, 1 obrigatório, 2 opcionais
for c in range(1, 101, 2):
    numeros.append(c)

print(numeros)

for numero in range(11):
    print(numero)
else:
    print("Loop Encerrado")

nomes2 = ["diego", "anderson", "Carlos", "luiz"]

nomesFormatados = []

for nome in nomes2:
    if nome[0].isupper():
        nomesFormatados.append(nome)
        pass
    else:
        nomesFormatados.append(nome.capitalize())

print(nomesFormatados)

# Enumerate

cursos = ["Javascript", "Python", "Java", "Ruby"]

"Lista de cursos"

for contador, curso in enumerate(cursos, 1):
    print(contador, "-" ,curso)

# While

#While é baseado em CONDIÇÃO

number = 1

while number <= 10:
    print(number)
    number += 1

# usando break

number = 1

while number < 10:
    print(number)
    if number == 5:
        break          # cuidado ao usar continue
    number += 1

number = 1

while number < 10:
    print(number)
    number += 1
else:
    print(f"Numero agora é {number}")

#While True

produtos = []

while True:
    produto = input("Insira o produto: ")
    produtos.append(produto)
    pergunta = input("Você deseja cadastrar um novo produto? S/N").upper()
    if pergunta == 'S':
        continue
    else:
        break

print("--------- Nota Fiscal -----------")

for produto in produtos:
    print(f"- {produto} - R$00,00")
