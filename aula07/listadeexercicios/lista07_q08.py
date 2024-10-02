# Conversor de Decimal para Binário:
# Contexto: Desenvolva um programa que converta um número decimal fornecido pelo usuário para sua representação binária. Utilize um loop para realizar as divisões sucessivas por 2 e armazenar os restos.

def funcao_principal():

    ndecimal = int(input('Digite um número decimal para ser transformado em binário: '))
    # Perguntei ao usuário que número ele quer transformar e armazenei na variável ndecimal.
    resultado = ''
    # Aqui eu criei uma variável chamada resultado que por enquanto tem uma string vazia. Também poderia ter criado a variável apenas com None escrito.

    while ndecimal > 0:
    # Aqui começo um loop para enquanto o número decimal for maior que 0, o programa fazer as divisões, pois essa é a lógica da conversão de decimal para binário.
        resto = ndecimal % 2  # Aqui é dividido o ndecimal perguntado ao usuário por dois e o seu resto é armazenado na variável resto
        resultado = str(resto) + resultado  # Aqui eu pego a variável resultado criada vazia anteriormente e começo a adicionar o resto à esquerda, convertendo para string, no loop. Então, a cada divisão, o resto vai sendo adicionado à esquerda do resultado anterior.
        ndecimal = ndecimal // 2  # Aqui é feita a divisão inteira por 2.

    print(f'A representação binária é: {resultado}') # Aqui vai ser impresso o  resultado final, quando acabar o loop por o ndecimal deixar de ser maior que zero.

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Transformação de número decimal em binário!\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")