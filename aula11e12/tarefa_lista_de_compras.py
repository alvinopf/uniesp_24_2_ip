# No mundo moderno, a organização é fundamental, e uma lista de compras inteligente pode facilitar muito a vida. O objetivo deste projeto é criar um programa em Python que utilize um vetor para armazenar uma lista de compras. Mas não para por aí! O programa deve permitir ao usuário adicionar itens à lista, remover itens, exibir a lista atualizada.

# Inicializar um vetor vazio para armazenar os itens da lista de compras.
# Criar um menu de opções para o usuário, com as seguintes funcionalidades:

    # Adicionar item: Ler o nome do item e a categoria e adicionar ao vetor.
    # Remover item: Ler o nome do item a ser removido e removê-lo do vetor.
    # Exibir lista: Exibir a lista de compras atualizada na tela.
    # Sair: Encerrar o programa.

# Criar um loop que exiba o menu repetidamente até que o usuário escolha a opção "Sair".


# criação de uma lista vazia, onde serão adicionados os itens
lista_de_compras = [] 

# definição de uma variável com um valor inicial "inválido" para que o programa fique rodando com a estrutura de repetição abaixo até que a condição de parar (no caso, a digitação de 0 pelo usuário) seja alcançada:
op = -1

while (op != 0):

    print('Escolha uma das opções:')
    print('1 - Adicionar um item à lista')
    print('2 - Remover item da lista')
    print('3 - Exibir lista')
    print('0 - Encerrar o programa')
    op = int(input('Digite a opção desejada: '))

    # para adicionar um item
    if (op == 1):
        
        print('\n')
        print('== Adição de item ==')
        aitem = input('Digite um novo item: ')
        lista_de_compras.append(aitem)
        print(f'O item {aitem} foi adicionado à lista de compras.')

    # para remover um item
    elif (op == 2):
        
        print('\n')
        print('== Remoção de item ==')
        ritem = input('Digite qual item você deseja remover da lista: ')
        lista_de_compras.remove(ritem)
        print(f'O item {ritem} foi removido da lista de compras.')

    # para exibir a lista
    elif (op == 3):
        print('\n')
        print('== Lista de Compras ==')

        for i in range(len(lista_de_compras)):
            print(f'{i+1} | {lista_de_compras[i]}') 
            # o i+1 é pq o usuário precisa ver a lista iniciando em 1, ao invés de 0, como nós programadores vemos.
        
        print('== Fim ==')

    # para sair do programa
    elif (op == 0):
        print('Programa Encerrado!')

    # para caso o usuário digite algo diferente
    else:
        print('Opção inválida!')