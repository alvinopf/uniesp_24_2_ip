# Importação de Bibliotecas
import requests
from time import sleep
from loguru import logger
from deep_translator import GoogleTranslator

# Criação da constante com o endereço da API de conselhos:
URL = 'https://api.adviceslip.com/advice'

# Criação das Funções do Programa
# Função para apresentar o menu e requisitar a escolha do usuário:
def menu():
    print('\nSeja bem-vindo, Seu Zé! Quer alguns conselhos?')
    print('\nVeja as opções abaixo:')
    print('\n1. Busca de novos conselhos!')
    print('2. Quero ver os conselhos recebidos!')
    print('3. Quero salvar os conselhos em um arquivo!')
    print('4. Quero ver os conselhos que foram salvos no arquivo!')
    print('5. Quero ver os conselhos em inglês!')
    print('6. Pronto, não quero mais nada!\n')

    opcao = input('Escolha uma das opções digitando o seu número: ')
    return opcao

# Função para buscar um conselho da API
def busca_conselho(URL):
    try:
        resposta_conselho = requests.get(URL)
        id_conselho = resposta_conselho.json()['slip']['id']
        texto_conselho = resposta_conselho.json()['slip']['advice']
        if id_conselho and texto_conselho:
            return id_conselho, texto_conselho
        else:
            logger.error('ID ou texto do conselho não foram encontrados.')
            return None
    except requests.exceptions.RequestException as bug:
        logger.error(f'Erro ao acessar a API: {bug}')
        return None

# Função de tradução dos conselhos para português
def traduzir_conselho(advice):
    try:
        return GoogleTranslator(source='english', target='portuguese').translate(advice)
    except Exception as bug:
        logger.error(f'Erro ao traduzir o conselho: {bug}')
        return None

# Função para salvar conselhos em um arquivo txt
def salvar_txt_conselho(conselhos, nome_txt='conselhos.txt'):
    try:
        with open(nome_txt, 'a', encoding='utf-8') as txt:
            for conselho in conselhos:
                txt.write(f'ID {conselho[0]}: {conselho[1]}\n')
        print(f'Conselhos salvos em {nome_txt}')
    except Exception as bug:
        logger.error(f'Erro ao salvar o arquivo: {bug}')
        return None

# Função para ler apenas as últimas linhas do arquivo
def ler_ultimas_linhas(nome_txt='conselhos.txt', n_linhas=10):
    try:
        with open(nome_txt, 'r', encoding='utf-8') as txt:
            todas_as_linhas = txt.readlines()  # Lê todas as linhas
            return todas_as_linhas[-n_linhas:]  # Retorna apenas as últimas n_linhas
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except Exception as bug:
        logger.error(f'Erro ao ler o arquivo: {bug}')
        return None

# Função principal
def main():
    conselhos_recebidos = []
    n_conselhos = 0  # Variável para armazenar a quantidade de conselhos solicitados

    while True:
        opcao = menu()

        if opcao == '1':
            conselhos_recebidos = []  # Resetar a lista para evitar duplicação
            
            while True:  # Loop para validar a entrada de n_conselhos
                try:
                    n_conselhos = int(input('\nQuantos conselhos você quer receber? '))
                    if n_conselhos < 0:  # Validar se o número não é negativo
                        print('\nPor favor, insira um número válido!')
                    elif n_conselhos == 0:  # Voltar ao menu inicial se o usuário digitar 0
                        print('\nVocê escolheu voltar ao menu inicial.')
                        break  # Sai do loop interno e retorna ao menu principal
                    else:
                        break  # Sai do loop se o número for válido
                except ValueError:
                    print('\nPor favor, insira um número válido!')

            if n_conselhos > 0:  # Apenas busca conselhos se o número for maior que zero
                for i in range(n_conselhos):
                    logger.info(f'Ciclo {i + 1} de chamada de API iniciado')
                    conselho = busca_conselho(URL)
                    if conselho:
                        conselhos_recebidos.append(conselho)
                    else:
                        print(f'\nConselho {i + 1}: Não foi possível obter o conselho.')
                    sleep(1)
                print('Conselhos obtidos com sucesso!')

        elif opcao == '2':
            if conselhos_recebidos:
                for id_conselho, texto_conselho in conselhos_recebidos:
                    print(f'ID {id_conselho}: {traduzir_conselho(texto_conselho)}')
            else:
                print('\nNenhum conselho recebido ainda.')

        elif opcao == '3':
            if conselhos_recebidos:
                conselhos_traduzidos = [
                    (id_conselho, traduzir_conselho(texto_conselho)) 
                    for id_conselho, texto_conselho in conselhos_recebidos
                ]
                salvar_txt_conselho(conselhos_traduzidos)
            else:
                print('Nenhum conselho recebido para salvar!')
        
        elif opcao == '4':
            if n_conselhos > 0:
                conselhos_salvos = ler_ultimas_linhas(nome_txt='conselhos.txt', n_linhas=n_conselhos)
                if conselhos_salvos:
                    print('Conselhos salvos nesta execução:')
                    for conselho in conselhos_salvos:
                        print(conselho.strip())
                else:
                    print('Nenhum conselho salvo no arquivo.')
            else:
                print('Nenhum conselho foi solicitado nesta execução.')

        elif opcao == '5':
            if conselhos_recebidos:
                print('Conselhos em inglês:')
                for id_conselho, texto_conselho in conselhos_recebidos:
                    print(f'ID {id_conselho}: {texto_conselho}')
            else:
                print('Nenhum conselho recebido ainda.')
        
        elif opcao == '6':
            print('Encerrando o programa! Até mais!')
            break
        
        else:
            print('Opção inválida. Tente de novo!')

if __name__ == '__main__':
    main()