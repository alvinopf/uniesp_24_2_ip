# Escreva um algoritmo que permita a leitura dos nomes de 5 clubes de futebol e armazene os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 5 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

lista_de_clubes = [] 
# criação de uma lista vazia, onde serão adicionados os 5 clubes

for i in range(5):
# estrutura de repetição onde será perguntado ao usuário um novo club para ser adicionado à lista
    
    clube = input('Digite um novo clube: ')

    lista_de_clubes.append(clube)
    # adição do clube digitado pelo usuário à lista criada anteriormente, na sequência

clube_pesquisado = input('Digite o clube que você gostaria de pesquisar: ')
# pergunta ao usuário sobre um item específico a ser procurando na lista

encontrou = False
# começo setando a variável encontrou como um booleano falso como controle de fluxo (se eu não tivesse criado ou tivesse começado como true, o programa iria ficar acusando falso o tempo todo atéee q fosse verdadeiro)

# for time in lista_de_clubes:
# defino a variável time para ser buscada com a estrutura de repetição na lista de clubes - essa parte ficou comentada pq o prof disse que não era assim que se usava vetores, mas sim o formato que faço logo abaixo.

    # if time.upper() == clube_pesquisado.upper():
    # faço uma comparação do nome pesquisado da variável time com as variáveis em clube pesquisado (com o upper para variar entre maiúscula e minúscula) para procurar

        # encontrou = True
        # se o time for encontrado, vai passar a ser True a variável encontrou

for i in range(len(lista_de_clubes)):
# neste formato, realmente usando vetores, a busca é feita em cada posição da lista gerada

    if lista_de_clubes[i].upper() == clube_pesquisado.upper():
        encontrou = True

if encontrou:
# se for encontrado, vai imprimir Achei
    print('Achei!')
else:
# se não for encontrado, vai imprimir Não achei
    print('Não achei!')