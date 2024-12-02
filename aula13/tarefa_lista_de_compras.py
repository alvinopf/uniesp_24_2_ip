# Programa: Lista de Compras
lista_de_compras = [] # variável global
op = -1

# Opção 01 - Adicionar um item a lista
def adicionar_item(lista_compras:list) -> list:
    print('\n')
    print('== Adição de item ==')
    item = input('Digite um novo item: ')
    
    lista_compras = lista_compras + [item]

    print(f'O item {item} foi adicionado à lista de compras.')

    return lista_compras


# Opção 02 - Remover da lista
def remover_da_lista(lista_compras:list):
    item = int(input('Digite o código do item a ser removido: '))
    item_deletado = lista_compras[item-1]
 
    del lista_compras[item-1]
 
    print(f'O item {item_deletado} foi removido da lista de compras.')
    print('== Fim ==')

    return lista_compras


# Opção 03 - Exibir a lista
def exibir_lista(lista_compras:list):
    print('\n')
    print('== Lista de Compras ==')

    for i in range(len(lista_compras)):
        print(f'{i+1} | {lista_compras[i]}') 
        
    print('== Fim ==')


while (op != 0):

    print('Escolha uma das opções:')
    print('1 - Adicionar um item à lista')
    print('2 - Remover item da lista')
    print('3 - Exibir lista')
    print('0 - Encerrar o programa')
    op = int(input('Digite a opção desejada: '))

    # para adicionar um item
    if (op == 1):
        adicionar_item(lista_compras=lista_de_compras)

    # para remover um item
    elif (op == 2):
        exibir_lista(lista_compras=lista_de_compras)
        lista_de_compras = remover_da_lista(lista_compras=lista_de_compras)
        
    # para exibir a lista
    elif (op == 3):
        exibir_lista(lista_compras=lista_de_compras)
        
    # para sair do programa
    elif (op == 0):
        print('Programa Encerrado!')

    # para caso o usuário digite algo diferente
    else:
        print('Opção inválida!')