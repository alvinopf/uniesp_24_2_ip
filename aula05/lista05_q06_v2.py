# 6. Campeonato de Corrida de Dragões
# a. Descrição: Em um campeonato de corrida de dragões, cada dragão corre uma determinada distância em um certo tempo. Crie um programa que receba a distância e o tempo de dois dragões diferentes e determine qual dragão é mais rápido, ou se ambos têm a mesma velocidade.
# b. Conceito: Operadores aritméticos, operadores relacionais, desvio condicional composto.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento(DISTANCIA, nome_dragao_1, vel_dragao_1, nome_dragao_2, vel_dragao_2):

    # Agora considerando a distância constante para os dois dragões, como em uma corrida comum.
 
    if vel_dragao_1 > vel_dragao_2:
        print(f'{nome_dragao_1} é mais veloz que {nome_dragao_2}!')
    elif vel_dragao_2 > vel_dragao_1:
        print(f'{nome_dragao_2} é mais veloz que {nome_dragao_1}!')
    else:
        print('Os dragões possuem a mesma velocidade!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    print('Você gostaria de saber qual dos dois dragões é mais veloz?')

    DISTANCIA = 1000

    nome_dragao_1 = input('Digite o nome do primeiro dragão: ')
    tempo_dragao_1 = float(input(f'Digite em quanto tempo {nome_dragao_1} percorreu essa distância (em horas): '))

    nome_dragao_2 = input('Digite o nome do segundo dragão: ')
    tempo_dragao_2 = float(input(f'Digite em quanto tempo {nome_dragao_2} percorreu essa distância (em horas): '))

    vel_dragao_1 = DISTANCIA/tempo_dragao_1
    vel_dragao_2 = DISTANCIA/tempo_dragao_2

    funcao_processamento(DISTANCIA, nome_dragao_1, vel_dragao_1, nome_dragao_2, vel_dragao_2)

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")