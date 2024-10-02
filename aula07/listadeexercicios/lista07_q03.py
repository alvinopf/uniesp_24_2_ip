# Contador de Vogais e Consoantes:
# Contexto: Crie um programa que peça ao usuário uma frase e conte o número de vogais e consoantes presentes nela. Utilize um loop para percorrer cada caractere da frase e realizar a contagem.

def funcao_principal():

    nvogais = 0
    nconsoantes = 0
    noutroscaracteres = 0
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚ"

    frase = input("Digite uma frase para que possamos contar quantas vogais e quantas consoantes estão presentes: ")

    for char in frase:

        if char.isalpha():
            if char in vogais:
                nvogais += 1
            else:
                nconsoantes += 1
        else:
            noutroscaracteres += 1

    print(f"Você escreveu uma frase com {nvogais} vogais, {nconsoantes} consoantes e {noutroscaracteres} espaços ou símbolos!")

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Vamos descobrir quantas vogais e consoantes existem nas suas frases?\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")