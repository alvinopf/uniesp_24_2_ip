# Calculadora de Média de Notas:
# Contexto: Crie um programa que peça ao usuário para inserir várias notas de um aluno e calcule a média. Utilize um loop para continuar pedindo notas até que o usuário digite um valor específico para encerrar a entrada (por exemplo, -1).

def funcao_principal():

    soma_notas = 0
    contador = 0
    
    nota = float(input("Digite uma nota válida entre 0 e 10 (digite -1 quando não tiver mais notas e use ponto para decimais): "))
    
    while nota != -1:
        soma_notas += nota
        contador += 1
        nota = float(input("Digite uma nota válida entre 0 e 10 (digite -1 quando não tiver mais notas e use ponto para decimais): "))

    if contador > 0:
        media = soma_notas / contador
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Nenhuma nota válida foi inserida.")

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")