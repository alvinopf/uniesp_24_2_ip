# 5. Jornada no Deserto
# a. Descrição: Um explorador está cruzando um deserto. Ele precisa saber se a quantidade de água que tem é suficiente para chegar ao próximo oásis. Ele calcula que precisa de 2 litros de água para cada quilômetro. Crie um programa que receba a quantidade de água disponível e a distância até o oásis, e informe se a água é suficiente.
# b. Conceito: Operadores aritméticos, desvio condicional simples.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Você gostaria de saber se a quantidade de água que tem é suficiente para chegar ao próximo oásis?')

    qtd_agua = float(input('Digite a quantidade (em litros) de água que você tem: '))
    dist_ate_oasis = float(input('Digite a distância (em quilômetros) até o próximo oasis: '))

    if dist_ate_oasis * 2 <= qtd_agua:
        print('Você tem água suficiente para chegar ao próximo oásis!')
    else:
        print('Você passará sede antes de chegar ao próximo oásis!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")