# Jogo de Adivinhação:
# Contexto: Implemente um jogo onde o computador escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar. Utilize um loop para permitir que o usuário faça várias tentativas, fornecendo dicas (maior ou menor) a cada tentativa.

def funcao_principal():

    import random

    numero_maximo = 100
    numero_secreto = random.randint(0, numero_maximo)
    chute = 101
    tentativas = 1

    while chute != numero_secreto:
        chute = int(input(f'Tente adivinhar um número inteiro que vai de 0 a {numero_maximo}: '))

        if chute == numero_secreto:
            break
        elif chute > numero_secreto:
            print(f'O número secreto é menor que {chute} :(')
        else:
            print(f'O número secreto é maior que {chute} :(')
        tentativas += 1

    palavra_tentativa = 'tentativas' if tentativas > 1 else 'tentativa'

    print(f'Isso aí! Você descobriu o número Secreto ({numero_secreto}) com {tentativas} {palavra_tentativa}!')

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Seja bem-vindo ao jogo do número secreto!\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")