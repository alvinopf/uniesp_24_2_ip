# 13. Sistema de Defesa de Castelos
# a. Descrição: O sistema de defesa de um castelo mágico precisa estar sempre ativo quando o exército do rei está fora. Crie um programa que receba a posição do exército (dentro ou fora do castelo) e use match-case para ativar ou desativar o sistema de defesa automaticamente.
# b. Conceito: Match-case, operadores lógicos, desvio condicional.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Como está o sistema de defesa do Castelo Mágio?')

    posicao_exercito = input('Digite onde o exército do rei se encontra em relação ao castelo (dentro ou fora): ')

    match posicao_exercito:
        case 'fora':
            print('O sistema de defesa deste Castelo Mágico será ativado!')
        case 'dentro':
            print('O sistema de defesa deste Castelo Mágico será desativado!')
        case _:
            print('Essa opção não existe, ô da guarita! Escolha uma das duas indicadas!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")