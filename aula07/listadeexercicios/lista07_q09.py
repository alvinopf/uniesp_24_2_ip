# Desenho de Padrões com Caracteres:
# Contexto: Crie um programa que desenhe padrões simples com caracteres, como triângulos, quadrados ou losangos. Utilize loops aninhados para controlar a quantidade de linhas e colunas e a exibição dos caracteres.

def funcao_principal():
    tamanho = int(input('Digite o número de linhas e colunas para formar o seu quadrado: '))
    
    print(f"\nEste é o seu quadrado com {tamanho} linhas e colunas:\n")
    
    for i in range(tamanho):
        for j in range(tamanho):
            print('+', end=' ')
        print()

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Desenhando quadrados com +!\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")