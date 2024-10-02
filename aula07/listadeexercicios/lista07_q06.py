# Verificador de Número Primo:
# Contexto: Crie um programa que peça ao usuário um número inteiro e verifique se ele é primo. Utilize um loop para testar a divisibilidade do número por outros números menores.

def funcao_principal():

    numero = int(input("Digite um número para que possamos verificar se ele é primo: "))

    if numero < 2:
        print(f'O número que você digitou ({numero}) não é primo!')
        return

    for i in range(2, numero):
        if numero % i == 0:
            print(f'O número que você digitou ({numero}) não é primo!')
            return

    print(f'O número que você digitou ({numero}) é primo!')

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Números Primos!\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")