# 14. O Julgamento do Sábio
# a. Descrição: Um sábio está julgando um duelo entre dois guerreiros. Ele quer saber qual guerreiro deve ser considerado vencedor, com base em suas habilidades de ataque e defesa. Crie um programa que receba os valores de ataque e defesa dos dois guerreiros e determine o vencedor (aquele com maior soma de ataque e defesa). Se houver empate, o programa deve considerar a defesa como critério de desempate.
# b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Quem será o vencedor do duelo entre os dois guerreiros? Vamos descobrir baseado em seus atributos?')

    atk_warr1 = float(input('Digite o poder de ataque do primeiro guerreiro (entre 0 e 10): '))
    def_warr1 = float(input('Digite o nível de defesa do primeiro guerreiro (entre 0 e 10): '))
    atk_warr2 = float(input('Digite o poder de ataque do segundo guerreiro (entre 0 e 10): '))
    def_warr2 = float(input('Digite o nível de defesa do segundo guerreiro (entre 0 e 10): '))

    soma_warr1 = atk_warr1 + def_warr1
    soma_warr2 = atk_warr2 + def_warr2

    if soma_warr1 == soma_warr2:
        if def_warr1 > def_warr2:
            print('O duelo foi acirradíssimo, mas a defesa do primeiro guerreiro o fez vencedor!')
        elif def_warr2 > def_warr1:
            print('O duelo foi acirradíssimo, mas a defesa do segundo guerreiro o fez vencedor!')
        else:
            print('O duelo foi acirradíssimo e nenhum vencedor foi declarado!')
    elif soma_warr1 > soma_warr2:
        print('O primeiro guerreiro é o vencedor deste duelo!')
    elif soma_warr2 > soma_warr1:
        print('O segundo guerreiro é o vencedor deste duelo!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")