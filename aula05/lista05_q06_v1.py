# 6. Campeonato de Corrida de Dragões
# a. Descrição: Em um campeonato de corrida de dragões, cada dragão corre uma determinada distância em um certo tempo. Crie um programa que receba a distância e o tempo de dois dragões diferentes e determine qual dragão é mais rápido, ou se ambos têm a mesma velocidade.
# b. Conceito: Operadores aritméticos, operadores relacionais, desvio condicional composto.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    # Apesar de ser uma corrida, onde geralmente os participantes correm a mesma distância lado a lado, a questão pode estar querendo distâncias diferentes para cada dragão, então resolvi seguir pelo caminho abaixo:
    
    print('Você gostaria de saber qual dos dois dragões é mais veloz?')

    nome_dragao_1 = input('Digite o nome do primeiro dragão: ')
    dist_dragao_1 = float(input(f'Digite a distância que {nome_dragao_1} percorreu (em quilômetros): '))
    tempo_dragao_1 = float(input(f'Digite em quanto tempo {nome_dragao_1} percorreu essa distância (em horas): '))

    nome_dragao_2 = input('Digite o nome do segundo dragão: ')
    dist_dragao_2 = float(input(f'Digite a distância que {nome_dragao_2} percorreu (em quilômetros): '))
    tempo_dragao_2 = float(input(f'Digite em quanto tempo {nome_dragao_2} percorreu essa distância (em horas): '))

    vel_dragao_1 = dist_dragao_1/tempo_dragao_1
    vel_dragao_2 = dist_dragao_2/tempo_dragao_2

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
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")