# 12! A Batalha Final
# a! Descrição: Um herói precisa decidir qual arma usar na batalha final! Ele tem três armas: uma espada, um arco e uma lança! Cada arma tem um poder de ataque e uma durabilidade! A escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que 70! Crie um programa que receba os valores de ataque e durabilidade das três armas e determine qual é a mais adequada! Se nenhuma atender, o programa deve sugerir que o herói busque uma nova arma!
# b! Conceito: Operadores lógicos, relacionais, desvio condicional aninhado!

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    # Encuquei pesado com essa questão, professor... Fiz questão de colocar quando apenas uma arma fosse adequada (e assim vencedora) e quando nenhuma o fosse, mas também quando mais de uma fosse e um critério de desempate entre elas para ainda assim uma ser recomendada como melhor em todas as combinações possíveis. Imagino que devam existir formas bem mais concisas de desenvolver mesmo com os detalhes que adicionei, mas a cabeça já estava saindo fumaça!

    print('Você precisa escolher a melhor arma para a Batalha Final de acordo com o ataque e durabilidade! Vamos lá?')

    atk_swd = int(input('Digite o poder de ataque da espada (entre 0 e 100): '))
    dur_swd = int(input('Digite o nível de durabilidade da espada (entre 0 e 100): '))
    atk_bow = int(input('Digite o poder de ataque do arco (entre 0 e 100): '))
    dur_bow = int(input('Digite o nível de durabilidade do arco (entre 0 e 100): '))
    atk_spe = int(input('Digite o poder de ataque da lança (entre 0 e 100): '))
    dur_spe = int(input('Digite o nível de durabilidade da lança (entre 0 e 100): '))

    ref_atk = 50
    ref_dur = 70

    good_swd = atk_swd > ref_atk and dur_swd > ref_dur
    good_bow = atk_bow > ref_atk and dur_bow > ref_dur
    good_spe = atk_spe > ref_atk and dur_spe > ref_dur

    soma_swd = atk_swd + dur_swd
    soma_bow = atk_bow + dur_bow
    soma_spe = atk_spe + dur_spe

    if good_swd and good_bow and good_spe:
        if soma_swd == soma_bow == soma_spe:
            print('As três armas são igualmente adequadas para a Batalha Final!')
        elif soma_swd == soma_bow and soma_swd > soma_spe:
            print('As três armas são adequadas para a Batalha Final, mas a espada e o arco são igualmente melhores!')
        elif soma_swd == soma_spe and soma_swd > soma_bow:
            print('As três armas são adequadas para a Batalha Final, mas a espada e a lança são igualmente melhores!')
        elif soma_bow == soma_spe and soma_bow > soma_swd:
            print('As três armas são adequadas para a Batalha Final, mas o arco e a lança são igualmente melhores!')
        elif soma_swd >= soma_bow and soma_swd >= soma_spe:
            print('As três armas são adequadas para a Batalha Final, mas a melhor é a espada!')
        elif soma_bow >= soma_swd and soma_bow >= soma_spe:
            print('As três armas são adequadas para a Batalha Final, mas a melhor é o arco!')
        else:
            print('As três armas são adequadas para a Batalha Final, mas a melhor é a lança!')
    elif good_swd and good_bow:
        if soma_swd == soma_bow:
            print('Sua espada e arco são igualmente adequados para a Batalha Final!')
        elif soma_swd > soma_bow:
            print('Sua espada e arco são adequados para a Batalha Final, mas a melhor é a espada!')
        else:
            print('Sua espada e arco são adequados para a Batalha Final, mas o melhor é o arco!')
    elif good_swd and good_spe:
        if soma_swd == soma_spe:
            print('Sua espada e lança são igualmente adequadas para a Batalha Final!')
        elif soma_swd > soma_spe:
            print('Sua espada e lança são adequadas para a Batalha Final, mas a melhor é a espada!')
        else:
            print('Sua espada e lança são adequadas para a Batalha Final, mas a melhor é a lança!')
    elif good_bow and good_spe:
        if soma_bow == soma_spe:
            print('Seu arco e lança são igualmente adequados para a Batalha Final!')
        elif soma_bow > soma_spe:
            print('Seu arco e lança são adequados para a Batalha Final, mas o melhor é o arco!')
        else:
            print('Seu arco e lança são adequados para a Batalha Final, mas a melhor é a lança!')
    elif good_swd:
        print('A espada é a sua arma adequada para a Batalha Final!')
    elif good_bow:
        print('O arco é a sua arma adequada para a Batalha Final!')
    elif good_spe:
        print('A lança é a sua arma adequada para a Batalha Final!')
    else:
        print('Vê se arruma uma arma melhor para a Batalha Final, seu herói de meia tijela!')
    
if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")