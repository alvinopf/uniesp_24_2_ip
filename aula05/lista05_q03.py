# 3. Adivinhação de Animais
# a. Descrição: Imagine que você é um mago que pode adivinhar o animal favorito das pessoas. Crie um programa que pergunte à pessoa se seu animal favorito é mamífero ou réptil. Se for mamífero, o programa deve sugerir que é um cachorro; se for réptil, o programa deve sugerir que é uma tartaruga.
# b. Conceito: Desvio condicional composto, variáveis.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('Digite o seu tipo de animal favorito: ')
    print('1 - Mamífero \n2 - Réptil')
    opcao = int(input('Qual sua opção: '))

    if opcao == 1:
        print('Ah! Certeza que é um doguinho!')
    else:
        print('Caramba! Você curte tartarugas!')

if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")