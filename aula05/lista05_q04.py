# 4. Contagem de Moedas
# a. Descrição: Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de 25 centavos. Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o valor total que o colecionador tem.
# b. Conceito: Operadores aritméticos, tipos de dados (float).

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Você gostaria de saber qual o valor que você tem na sua coleção de moedas?')

    qtd_25cent = int(input('Digite a quantidade de moedas de 25 centavos que você tem: '))
    qtd_50cent = int(input('Digite a quantidade de moedas de 50 centavos que você tem: '))
    qtd_1real = int(input('Digite a quantidade de moedas de 1 real que você tem: '))

    valor_em_reais = float(qtd_25cent*0.25 + qtd_50cent*0.50 + qtd_1real*1)

    print(f'Você tem R${f"{valor_em_reais:.2f}".replace(".", ",")} reais em moedas!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")