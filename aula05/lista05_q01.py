#  1. O Tesouro Escondido
#  a. Descrição: Um mapa do tesouro tem duas partes, A e B. A primeira parte está escondida no X número de passos para o norte, e a segunda no Y número de passos para o leste. Crie um programa que receba os valores de X e Y e calcule a distância total que o pirata precisa percorrer para chegar ao tesouro (soma de X e Y). 
# # b. Conceito: Operadores aritméticos, variáveis.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    # Valores aleatórios abaixo
    x = 10 # poderia ser: int(input('Digite os passos ate X: '))
    y = 15 # poderia ser: int(input('Digite os passos ate Y: '))

    # Soma da quantidade de passos
    qtd_passos = x + y

    # Apresentação do resultado
    print(f'A quantidade de passos para o pirata será de {qtd_passos}.')

# Inicialização do programa main
if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")