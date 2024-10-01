def funcao_principal():

    numero = 1
    while numero <= 10:
        arquivo = open("aula06/tabuada1a10-.txt", "a")
        arquivo.write(f'Tabuada de {numero}\n')
        
        # Loop para automatizar as multiplicações de 1 a 10
        for i in range(1, 11):
            arquivo.write(f'{numero} * {i} = {numero * i}\n')
        
        arquivo.write('\n')  # Adiciona uma linha em branco entre as tabuadas
        
        numero += 1  # Incrementa o número para evitar loop infinito
        arquivo.close()

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")