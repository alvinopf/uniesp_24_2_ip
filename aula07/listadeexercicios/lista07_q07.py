# Calculadora de Fatorial:
# Contexto: Implemente um programa que calcule o fatorial de um número fornecido pelo usuário. Utilize um loop para realizar as multiplicações necessárias.

def funcao_principal():

    numero = int(input('Digite um número para calcularmos o seu fatorial: '))

    if numero < 0:
        print(f'Não existe fatorial para números negativos!')
        return
    elif numero == 0:
        print(f'O fatorial de 0 é 1!')
        return
    elif numero == 1:
        print(f'O fatorial de 1 é 1!')
        return
    
    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i

    print(f'O fatorial deste número ({numero}) é: {fatorial}!')

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Cálculo de Fatorial!\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")