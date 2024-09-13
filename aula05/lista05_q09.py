# 9. Escolha de Feitiços
# a. Descrição: Um mago tem três feitiços: fogo, água e terra. Crie um programa que receba a escolha do usuário (1 para fogo, 2 para água, 3 para terra) e use o comando match-case para exibir o feitiço escolhido.
# b. Conceito: Match-case, variáveis.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('O poderoso Mago tem três tipos de feitiço para derrotar seus adversários!')
    print('1 - Fogo \n2 - Água \n3 - Terra')
    opcao = int(input('Escolha o tipo de feitiço a ser usado por ele (1, 2 ou 3): '))

    match opcao:
        case 1:
            print('Você escolheu incinerar seus adversários!')
        case 2:
            print('Você escolheu afogar seus inimigos em um grande dilúvio!')
        case 3:
            print('Você escolheu enterrar seus oponentes à sete palmos!')
        case _:
            print('Este feitiço não existe! Escolha uma das opções indicadas, seu espada-de-plástico!')
if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")