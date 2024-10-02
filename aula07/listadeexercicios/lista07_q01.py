# Calculadora de Média de Notas:
# Contexto: Crie um programa que peça ao usuário para inserir várias notas de um aluno e calcule a média. Utilize um loop para continuar pedindo notas até que o usuário digite um valor específico para encerrar a entrada (por exemplo, -1).

def funcao_principal():

    soma_notas = 0 
    # Defino que a soma das notas começa em 0.
    contador = 0 
    # Defino que a contagem de notas adicionadas começa em 0.
    
    while True: 
    # Crio o loop abaixo para rodar enquanto a situação for possível.
        nota = input("Digite uma nota entre 0 e 10 (digite \"sair\" quando não tiver mais notas e use ponto para decimais): ")
        # Pergunto a nota ao usuário e armazeno na variável nota.
        if nota.lower() == "sair": 
        # Completo a condição de não existir mais notas ao usuário digitar sair, quebrando o loop com o break abaixo. O lower garante que o usuário pode escrever SAIR Sair sair e etc.
            break     
        try:
        # Faço um teste para verificar se o que o usuário inseriu foi realmente um valor numérico float onde é criada a variável nota_float abaixo.
            nota_float = float(nota)
            if 0 <= nota_float <= 10:          
                soma_notas += float(nota)
                contador += 1
            # Durante a verificação, confirmo a condição de o valor estar entre 0 e 10. Se estiver, o programa somará a variável nota e armazenará mais um à contagem, como acima.
            else:
                print("Nenhuma nota válida foi inserida.")
            # Se durante a verificação o valor não estava entre 0 e 10, a mensagem acima será exibida.

        except:
            print("Nenhuma nota válida foi inserida.")
        # Se durante a verificação o valor não era numérico float (inclusive, não estava escrito com ponto), a mensagem acima será exibida.

    if contador > 0:
        media = soma_notas / contador
        print(f"A média das notas é: {media:.2f}")
    # Se após o loop as condições forem favoráveis à soma dos valores das notas, os códigos acima serão realizados. O .2f garante que o valo final seja apresentado com apenas duas casas decimais.
    else:
        print("Nenhuma nota válida foi inserida.")
    # Se durante o loop o usuário apenas digitou sair, esta condição será concluída e a mensagem acima será apresentada, também finalizando o programa.

if __name__ == '__main__':

    print("\n--- --- Início do programa! --- ---\n")
    print("Vamos descobrir a sua média de notas!\n")
    funcao_principal()
    print("\n--- --- Fim do programa! --- ---\n")