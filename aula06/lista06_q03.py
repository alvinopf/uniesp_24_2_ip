# Faça um programa que receba um número e que calcule a tabuada desse número, e armazene o resultado em um arquivo de texto.

def funcao_principal():

    numero = int(input('Digite um número para calcularmos sua tabuada: '))

    arquivo = open("aula06/tabuadanumerosolicitado.txt", "a")
    arquivo.write(f'Tabuada de {numero}\n\n')
        
    # Loop para automatizar as multiplicações de 1 a 10
    for i in range(1, 11, 1):
        arquivo.write(f'{numero} * {i} = {numero * i}\n')
 
    arquivo.close()

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")