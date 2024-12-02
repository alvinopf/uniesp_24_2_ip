# criação de uma matriz:
lista_de_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# impressão da matriz:
print(lista_de_numeros)

# impressão apenas da segunda linha:
print(lista_de_numeros[1])

# impressão apenas de um item da segunda linha:
print(lista_de_numeros[1][1])

# impressão da qtdd de numeros na lista de números:
print(f'Tamanho da lista: {(len(lista_de_numeros))}')

# captura de um valor dentro de uma faixa de valores (len calcula o tamanho de um objeto, range tem o valor final não inclusivo) (o for externo está iterndo sobre a matrz, ele assume o índice de cada  uma das listas da matriz. O  for interno itera sobre a lista selecionada da vez):
for linha in range(len(lista_de_numeros)):
    for coluna in range(len(lista_de_numeros[linha])):
        print(f'Linha: {linha} - Coluna: {coluna} -> {lista_de_numeros[linha][coluna]}')