#https://leetcode.com/problems/search-insert-position/description/

#matriz ordenada

# inteiros distintos
# valor alvo
# retornar o índice ao encontrá-lo
# caso não exista retornar o índice onde ele estaria na ordem

# Dada uma matriz ordenada de inteiros distintos e um valor alvo,
# retorne o índice se o alvo for encontrado. Caso contrário, retorne o índice onde estaria se fosse inserido na ordem.
# Você deve escrever um algoritmo com O(log n)complexidade de tempo de execução.


"""
Exemplo 1:

Entrada: nums = [1,3,5,6], alvo = 5
 Saída: 2
Exemplo 2:

Entrada: nums = [1,3,5,6], alvo = 2
 Saída: 1
Exemplo 3:

Entrada: nums = [1,3,5,6], alvo = 7
 Saída: 4
"""
contador = 0

nums = [1, 3, 5, 6]
alvo = 2
indice = 10001
tamanho = len(nums) - 1

if nums[tamanho] < alvo:
    indice = tamanho + 1
    print(f"O índice do número é {indice}")
    exit()

for i, v in enumerate(nums):
    # print(f"O número {v} está na posição {i} do array")
    if v == alvo:
        print('if')
        indice = i
        break
    elif v > alvo:
        print('elif')
        indice = i
        break

print(f"O índice do número é {indice}")


"""OBS: Garantir ordenação dos números (sort, etc)
Garantir que não há números duplicados
Tentar colocar tudo numa função, que recebe o array como parâmetro
Aplicar restrições:

Restrições:

1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums contém valores distintos classificados em ordem crescente .
-10**4 <= target <= 10**4
"""