# 8. Calculadora de Bônus
# a. Descrição: Um rei deseja distribuir bônus aos seus cavaleiros com base em suas conquistas. Se um cavaleiro completou mais de 10 missões, ele recebe um bônus de 100 moedas de ouro. Se completou entre 5 e 10 missões, recebe 50 moedas de ouro. Se completou menos de 5, recebe 10 moedas de ouro. Crie um programa que receba o número de missões completadas e informe o valor do bônus.
# b. Conceito: Desvio condicional aninhado, operadores relacionais.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Bom cavaleiro, desejo premiá-lo pelo seu trabalho!')

    qtd_missoes = int(input('Digite a quantidade de missões completadas: '))

    if qtd_missoes > 10:
        print(f'Honrado Cavaleiro, você receberá {qtd_missoes * 100} moedas pelo seu grande esforço!')
    elif qtd_missoes >= 5 and qtd_missoes <= 10:
        print(f'Cavaleiro, você receberá {qtd_missoes * 50} moedas pelo seu trabalho!')
    else:
        print(f'Mas que blasfêmia! Apenas {qtd_missoes} missões completadas!? Tome estas {qtd_missoes * 10} moedas e suma da minha frente!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")