# 10. A Caverna dos Desafios
# a. Descrição: Um aventureiro encontrou uma caverna cheia de portas, cada uma com um número de 1 a 5. Atrás de cada porta há um desafio. Crie um programa que receba o número da porta escolhido pelo aventureiro e use match-case para mostrar qual desafio ele enfrentará.
# b. Conceito: Match-case, operadores relacionais.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Você está diante das cinco portas da Caverna dos Desafios! Em cada porta você encontrará um teste físico e/ou mental diferente!')
    print('1 - Desafio do Um Anel \n2 - Desafio Toca dos Hobbits \n3 - Desafio dos Rangers \n4 - Desafio Élfico \n5 - Desafio dos Anões')
    opcao = int(input('Escolha uma das cinco portas (1, 2, 3, 4 ou 5): '))

    match opcao:
        case 1:
            print('Você entrou na primeira porta e agora terá que resistir à tentação de usar o Um Anel por um ano inteiro!')
        case 2:
            print('Você entrou na segunda porta e agora terá que suportar cheirar os pés cabeludos e fedorentos da vizinha do Sam diariamente por um ano inteiro!')
        case 3:
            print('Você entrou na terceira porta e agora terá que suportar servir de parceiro de treino de Aragorn, apenas sofrendo seus golpes de espada vestindo uma armadura de metal por um ano inteiro!')
        case 4:
            print('Você entrou na terceira porta e agora terá que passar um ano inteiro na Floresta Negra fugindo das aranhas sem qualquer arma e apenas com lembas suficiente para não morrer de fome!')
        case 5:
            print('Você entrou na quinta porta e agora terá que passar um ano inteiro sozinho abrindo um túnel na Montanha Solitária! Cuidado com o Balrog que dizem ainda viver nas suas profundezas!')
        case _:
            print('Por que você está tentando cavar uma nova porta, ô, filhote de orc com goblin!? Escolha uma das que já existem!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")