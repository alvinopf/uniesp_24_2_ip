# Sequência de Fibonacci:
# Contexto: Desenvolva um programa que gere os primeiros N números da sequência de Fibonacci, onde N é fornecido pelo usuário. Utilize um loop para calcular e exibir os termos da sequência.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def funcao_principal():

    nfibonacci = int(input('Digite quantos números da Sequência de Fibonacci você gostaria de ver: '))
    
    print(f'\nOs primeiros {nfibonacci} números da Sequência de Fibonacci são:\n')
    
    for i in range(nfibonacci):
        print(fibonacci(i))

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Sequência de Fibonacci!\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")