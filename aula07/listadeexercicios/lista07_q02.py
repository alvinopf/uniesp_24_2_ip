# Tabuada Personalizada:
# Contexto: Desenvolva um programa que peça ao usuário um número e gere a tabuada completa desse número (de 1 a 10). Utilize um loop para realizar as multiplicações e exibir os resultados de forma organizada.

def funcao_principal():

    while True:

        numero = input("Digite um número para calcularmos a sua tabuada ou \"sair\" para parar (use apenas ponto para decimais): ")

        if numero.lower() == "sair":
            break
        
        try:
            numero_float = float(numero)
            print(f"\nTabuada de {float(numero)}\n\n{numero} * 1 = {float(numero)*1:.2f}\n{numero} * 2 = {float(numero)*2:.2f}\n{numero} * 3 = {float(numero)*3:.2f}\n{numero} * 4 = {float(numero)*4:.2f}\n{numero} * 5 = {float(numero)*5:.2f}\n{numero} * 6 = {float(numero)*6:.2f}\n{numero} * 7 = {float(numero)*7:.2f}\n{numero} * 8 = {float(numero)*8:.2f}\n{numero} * 9 = {float(numero)*9:.2f}\n{numero} * 10 = {float(numero)*10:.2f}")
            break            
        except:
            print("Você não digitou um número válido.")

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Vamos descobrir a tabuada de um número?\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")