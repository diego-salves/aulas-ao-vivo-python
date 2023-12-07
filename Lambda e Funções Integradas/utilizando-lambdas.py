# lambda

# Uma função lambda é uma pequena função anônima.
# Uma função lambda pode receber qualquer número de argumentos, mas só pode ter uma expressão.

# syntax: lambda arguments : expression

# Exemplo 1:

x = lambda a: a + 10

print(x(5))

# Exemplo 2:

x = lambda a, b: a * b
print(x(5, 6))

soma3 = lambda a, b, c: a + b + c
print(soma3(1, 2, 3))


def somaTres(a, b, c):
    return print(a + b + c)


somaTres(1, 2, 3)


# Porque usar lambda?
# Uma função anônima dentro de outra função

def dobra(n):
    return lambda x: x * n


multiplicapor2 = dobra(2)
print(multiplicapor2)
print(multiplicapor2(10))
multiplicarpor3 = dobra(3)
print(multiplicarpor3(10))

# Use funções lambdas quando umma função é necessária por um período curto de tempo
