# Escreva um algoritmo que permita a leitura das notas de uma turma de 5 alunos. Depois responda:
# a. Qual a média da turma?
# b. Quantos alunos obtiveram nota acima da média da turma?
# c. Imprimir a média da turma e o resultado da contagem.

lista_de_notas = [8, 10, 5.6, 7, 4.8]
# defino a lista de notas (poderia usar input, por ex, se fosse pra perguntar ao usuário)

soma = 0
# defino a variável soma, com valor zerado

for i in range(len(lista_de_notas)):
# acumulo valores na variável soma através da estrutura de repetição for
    soma += lista_de_notas[i]

media = soma / len(lista_de_notas)
# respondo qual é a média da turma

contador = 0
# para definir a quantidade dos alunos acima da média, começo definindo um contador e defino o valor inicial como zero

for i in range(len(lista_de_notas)):
# acumulo a quantidade no contador, se for encontrado acima da média
    if lista_de_notas[i] > media:
        contador += 1

print(f'A média da turma é: {media:.2f}')
print(f'Existem {contador} alunos acima da média.')
# imprimo os valores