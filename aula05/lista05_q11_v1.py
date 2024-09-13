# 11. Decisão da Coroa Real
# a. Descrição: O conselho real precisa tomar uma decisão crítica: selecionar o próximo governante entre três candidatos, baseado na sua pontuação em uma série de provas. Crie um programa que receba as notas dos três candidatos e determine qual deles teve a maior média. Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando que há um empate.
# b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Aqui não tem conversa de eleição por voto popular! Só entra quem realmente for o mais inteligente para o cargo! As provas não foram feitas à toa!')

    nota_gov_1 = float(input('Digite a média de notas do governante um: '))
    nota_gov_2 = float(input('Digite a média de notas do governante dois: '))
    nota_gov_3 = float(input('Digite a média de notas do governante três: '))

    if nota_gov_1 == nota_gov_2 and nota_gov_2 == nota_gov_3:
        print('As médias dos governantes são iguais!')
    elif nota_gov_1 == nota_gov_2 or nota_gov_2 == nota_gov_3 or nota_gov_1 == nota_gov_3:
        print(f'Temos duas médias iguais entre os governantes e a maior é {max(nota_gov_1, nota_gov_2, nota_gov_3)}!')
    elif nota_gov_1 != nota_gov_2 and nota_gov_2 != nota_gov_3 and nota_gov_1 != nota_gov_3:
        print(f'A maior média é {max(nota_gov_1, nota_gov_2, nota_gov_3)}!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")