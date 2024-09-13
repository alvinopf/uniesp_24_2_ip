# 11. Decisão da Coroa Real
# a. Descrição: O conselho real precisa tomar uma decisão crítica: selecionar o próximo governante entre três candidatos, baseado na sua pontuação em uma série de provas. Crie um programa que receba as notas dos três candidatos e determine qual deles teve a maior média. Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando que há um empate.
# b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    # Encuquei e resolvi refazer a questão colocando todas as combinações possíveis, considerando também sugestão de novas eleições para desempates, por exemplo...

    print('Aqui não tem conversa de eleição por voto popular! Só entra quem realmente for o mais inteligente para o cargo! As provas não foram feitas à toa!')

    nota_gov_1 = float(input('Digite a média de notas do Governante Um: '))
    nota_gov_2 = float(input('Digite a média de notas do Governante Dois: '))
    nota_gov_3 = float(input('Digite a média de notas do Governante Três: '))

    if nota_gov_1 == nota_gov_2 == nota_gov_3:
        print('As médias dos governantes são iguais e um novo formato de seleção precisa ser realizado entre eles!')
    elif nota_gov_1 == nota_gov_2 or nota_gov_2 == nota_gov_3 or nota_gov_1 == nota_gov_3:
        if nota_gov_1 == nota_gov_2 and nota_gov_1 == max(nota_gov_1, nota_gov_2, nota_gov_3):
            print(f'Temos médias iguais entre os Governantes Um e Dois, a qual é maior ({nota_gov_1}), e um novo formato de seleção precisa ser realizado entre os dois!')
        elif nota_gov_1 == nota_gov_2 and nota_gov_3 == max(nota_gov_1, nota_gov_2, nota_gov_3):
            print(f'Temos médias iguais entre os Governantes Um e Dois, mas a maior é a do Três ({nota_gov_3}), que será o próximo Governante!')
        elif nota_gov_2 == nota_gov_3 and nota_gov_2 == max(nota_gov_1, nota_gov_2, nota_gov_3):
            print(f'Temos médias iguais entre os Governantes Dois e Três, a qual é maior ({nota_gov_2}), e um novo formato de seleção precisa ser realizado entre os dois!')
        elif nota_gov_2 == nota_gov_3 and nota_gov_1 == max(nota_gov_1, nota_gov_2, nota_gov_3):
            print(f'Temos médias iguais entre os Governantes Dois e Três, mas a maior é a do Um ({nota_gov_1}), que será o próximo Governante!')
        elif nota_gov_1 == nota_gov_3 and nota_gov_1 == max(nota_gov_1, nota_gov_2, nota_gov_3):
            print(f'Temos médias iguais entre os Governantes Um e Três, a qual é maior ({nota_gov_1}), e um novo formato de seleção precisa ser realizado entre os dois!')
        elif nota_gov_1 == nota_gov_3 and nota_gov_2 == max(nota_gov_1, nota_gov_2, nota_gov_3):
            print(f'Temos médias iguais entre os Governantes Um e Três, mas a maior é a do Dois ({nota_gov_2}), que será o próximo Governante!')
    else:
        if max(nota_gov_1, nota_gov_2, nota_gov_3) == nota_gov_1:
            print(f'A maior média é a do Governante Um ({nota_gov_1}), que será o próximo Governante!')
        elif max(nota_gov_1, nota_gov_2, nota_gov_3) == nota_gov_2:
            print(f'A maior média é a do Governante Dois ({nota_gov_2}), que será o próximo Governante!')
        elif max(nota_gov_1, nota_gov_2, nota_gov_3) == nota_gov_3:
            print(f'A maior média é a do Governante Três ({nota_gov_3}), que será o próximo Governante!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")