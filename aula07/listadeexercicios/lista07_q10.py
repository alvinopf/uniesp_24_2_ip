# Simulador de Lançamento de Dados:
# Contexto: Implemente um programa que simule o lançamento de um dado de 6 faces várias vezes, conforme especificado pelo usuário. Utilize um loop para realizar os lançamentos e exibir os resultados.

import random

def funcao_principal():

    lancamentos = int(input('Digite quantas vezes o dado deve ser lançado: '))
        
    print(f'\nOs resultados dos {lancamentos} lançamentos são:\n')

    for i in range(lancamentos):
        dado = random.randint(1, 6)
        print(dado)

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Lançamentos de dado de 6 faces!\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")