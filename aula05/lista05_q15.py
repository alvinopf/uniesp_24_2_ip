# 15. Portal de Viagem no Tempo
# a. Descrição: Um cientista está criando um portal de viagem no tempo que só pode ser ativado se todos os parâmetros estiverem corretos: energia acima de 80%, coordenadas de destino precisas, e o tempo ajustado corretamente. Crie um programa que receba esses valores e use operadores lógicos para verificar se o portal pode ser ativado. Se qualquer parâmetro estiver incorreto, o programa deve indicar qual é o problema.
# b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.

# Criação da função funcao_processamento() que será usada neste programa
def funcao_processamento():

    print('A ativação do portal para a viagem no tempo é criteriosa! Vamos verificar as condições para a permissão de viagem?')

    nivel_energia = input('Digite se o nível de energia atual da máquina está acima ou abaixo de 80% (acima/abaixo): ')
    coordenadas_destino = input('Digite se as coordenadas do destino desejado são precisas (precisas/imprecisas): ')
    ajuste_de_tempo = input('Digite se o tempo foi ajustado corretamente nas configurações da máquina (ajustado/incorreto): ')

    if nivel_energia == 'acima' and coordenadas_destino == 'precisas' and ajuste_de_tempo == 'ajustado':
        print('A viagem é possível e o portal pode ser ativado!')
    elif nivel_energia == 'acima' and coordenadas_destino == 'precisas' and ajuste_de_tempo == 'incorreto':
        print('O tempo não foi ajustado corretamente. O portal não deve ser ativado!')
    elif nivel_energia == 'acima' and coordenadas_destino == 'imprecisas' and ajuste_de_tempo == 'ajustado':
        print('As coordenadas são imprecisas. O portal não deve ser ativado!')
    elif  nivel_energia == 'acima' and coordenadas_destino == 'imprecisas' and ajuste_de_tempo == 'incorreto':
        print('As coordenadas são imprecisas e o tempo não foi ajustado corretamente. O portal não deve ser ativado!')
    elif nivel_energia == 'abaixo' and coordenadas_destino == 'precisas' and ajuste_de_tempo == 'ajustado':
        print('O nível de energia está abaixo do recomendado. O portal não deve ser ativado!')
    elif nivel_energia == 'abaixo' and coordenadas_destino == 'precisas' and ajuste_de_tempo == 'incorreto':
        print('O nível de energia está abaixo do recomendado e o tempo não foi ajustado corretamente. O portal não deve ser ativado!')    
    elif nivel_energia == 'abaixo' and coordenadas_destino == 'imprecisas' and ajuste_de_tempo == 'ajustado':
        print('O nível de energia está abaixo do recomendado e as coordenadas são imprecisas. O portal não deve ser ativado!')
    elif nivel_energia == 'abaixo' and coordenadas_destino == 'imprecisas' and ajuste_de_tempo == 'incorreto':
        print('O nível de energia está abaixo do recomendado, as coordenadas são imprecisas e o tempo não foi ajustado corretamente. O portal não deve ser ativado!')
 
if __name__ == '__main__':

    # Mensagem de início do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")