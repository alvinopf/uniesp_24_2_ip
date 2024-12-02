import requests
from time import sleep
from loguru import logger
from deep_translator import GoogleTranslator

URL = 'https://api.adviceslip.com/advice'

# Função para exibir o menu e capturar a escolha do usuário
def menu():
    print("\nMenu de Opções:")
    print("1. Quantos conselhos você deseja receber?")
    print("2. Quer visualizar os conselhos recebidos?")
    print("3. Deseja salvar os conselhos visualizados em um arquivo?")
    print("4. Quer visualizar os conselhos que foram salvos no arquivo?")
    print("5. Gostaria de ver os conselhos em inglês?")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")
    return escolha

# Função para buscar um conselho em inglês da API
def fetch_advice(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Levanta uma exceção se o status não for 200
        slip = resposta.json().get('slip', {})
        advice_id = slip.get('id')  # Obtém o ID do conselho
        advice_text = slip.get('advice')  # Obtém o texto do conselho
        if advice_id and advice_text:
            return advice_id, advice_text
        else:
            logger.error("ID ou texto do conselho ausente na resposta.")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao acessar a API: {e}")
        return None

# Função para traduzir um conselho para português
def translate_advice(advice):
    try:
        return GoogleTranslator(source='english', target='portuguese').translate(advice)
    except Exception as e:
        logger.error(f"Erro ao traduzir o conselho: {e}")
        return None

# Função para salvar conselhos em um arquivo
def save_advice_to_file(conselhos, filename="conselhos.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            for conselho in conselhos:
                file.write(f"ID {conselho[0]}: {conselho[1]}\n")
        print(f"Conselhos salvos em {filename}.")
    except OSError as e:
        logger.error(f"Erro ao salvar o arquivo: {e}")

# Função para ler conselhos salvos em um arquivo
def read_saved_advices(filename="conselhos.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Nenhum arquivo encontrado.")
        return []
    except OSError as e:
        logger.error(f"Erro ao ler o arquivo: {e}")
        return []

# Função principal
def main():
    conselhos_recebidos = []  # Lista para armazenar os conselhos obtidos
    conselhos_traduzidos = []  # Lista para armazenar os conselhos traduzidos

    while True:
        escolha = menu()
        
        if escolha == "1":  # Quantos conselhos o usuário deseja receber?
            try:
                E = int(input('Digite a quantidade de conselhos: '))
                for i in range(n_conselhos):
                    logger.info(f'Ciclo {i + 1} de chamada de API iniciado')
                    conselho = fetch_advice(URL)
                    if conselho:
                        conselhos_recebidos.append(conselho)
                    else:
                        print(f"Conselho {i + 1}: Não foi possível obter o conselho.")
                    sleep(1)
            except ValueError:
                print("Por favor, insira um número válido.")
            print('===* Conselhos obtidos com sucesso *===')

        elif escolha == "2":  # Visualizar os conselhos recebidos
            if conselhos_recebidos:
                conselhos_traduzidos = [
                    (c[0], translate_advice(c[1])) for c in conselhos_recebidos if c
                ]
                for i, (advice_id, conselho) in enumerate(conselhos_traduzidos, start=1):
                    print(f"Conselho {i} (ID {advice_id}): {conselho}")
            else:
                print("Nenhum conselho recebido ainda.")

        elif escolha == "3":  # Salvar os conselhos visualizados
            if conselhos_traduzidos:
                save_advice_to_file(conselhos_traduzidos)
            else:
                print("Nenhum conselho traduzido para salvar.")

        elif escolha == "4":  # Visualizar conselhos salvos no arquivo
            conselhos_salvos = read_saved_advices()
            if conselhos_salvos:
                print("Conselhos salvos:")
                for conselho in conselhos_salvos:
                    print(conselho.strip())
            else:
                print("Nenhum conselho salvo no arquivo.")

        elif escolha == "5":  # Ver conselhos em inglês
            if conselhos_recebidos:
                print("Conselhos em inglês:")
                for i, (advice_id, conselho) in enumerate(conselhos_recebidos, start=1):
                    print(f"Advice {i} (ID {advice_id}): {conselho}")
            else:
                print("Nenhum conselho recebido ainda.")

        elif escolha == "6":  # Sair do programa
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
