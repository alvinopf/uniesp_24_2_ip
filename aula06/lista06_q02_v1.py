# Faça um programa que calcule as tabuadas dos números de 1 a 10 e armazene o resultado em um arquivo de texto.

def funcao_principal():

    numero = 1
    while numero <= 10:
        arquivo = open("aula06/tabuada1a10.txt", "a")
        arquivo.write(f'Tabuada de {numero}\n{numero} * 1 = {numero*1}\n{numero} * 2 = {numero*2}\n{numero} * 3 = {numero*3}\n{numero} * 4 = {numero*4}\n{numero} * 5 = {numero*5}\n{numero} * 6 = {numero*6}\n{numero} * 7 = {numero*7}\n{numero} * 8 = {numero*8}\n{numero} * 9 = {numero*9}\n{numero} * 10 = {numero*10}\n\n')
        numero += 1
        arquivo.close()

if  __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n") # Mensagem de início do programa
    funcao_principal() # Processamento realizado pelo programa
    print("\n--- --- Fim do programa! --- ---\n") # Mensagem de fim do programa