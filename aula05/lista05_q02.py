# 2. Guerreiro da Idade Média
# a. Descrição: Um guerreiro precisa de uma armadura especial para a batalha. Para forjar a armadura, ele precisa de uma liga metálica que combina ferro e ouro. O ferreiro diz que a liga precisa ter no mínimo 70% de ferro. Crie um programa que receba a quantidade de ferro e ouro em kg e verifique se a porcentagem de ferro na liga é suficiente.
# b. Conceito: Operadores aritméticos, operadores lógicos, desvio condicional simples.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    qtd_ferro = float(input('Digite a quantidade de ferro: '))
    qtd_ouro = float(input('Digite a quantidade de ouro: '))

    total_liga_metalica = qtd_ferro + qtd_ouro

    if (qtd_ferro/total_liga_metalica) >= 0.7:
        print('A sua armadura será massa!')
    else:
        print('A sua armadura vai quebrar!')
    
if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")