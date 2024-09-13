# 7. Classificação de Plantas Mágicas
# a. Descrição: Um botânico está classificando plantas mágicas em uma floresta. Ele quer saber se uma planta é pequena (menos de 1 metro), média (entre 1 e 3 metros), ou grande (mais de 3 metros). Crie um programa que receba a altura da planta e informe a sua classificação.
# b. Conceito: Operadores relacionais, desvio condicional aninhado.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Você gostaria de saber se a planta mágia em questão pode ser considerada pequena, média ou grande?')

    alt_planta_magica = float(input('Digite a altura da planta encontrada (em metros): '))

    if alt_planta_magica < 1:
        print('A planta mágica encontrada é pequena!')
    elif alt_planta_magica >= 1 and alt_planta_magica <= 3:
        print('A planta mágica encontrada tem tamanho médio!')
    else:
        print('A planta mágica encontrada é grande!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")