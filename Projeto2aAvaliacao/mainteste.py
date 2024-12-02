import tkinter as tk
from tkinter import messagebox
import requests
from time import sleep
from loguru import logger
from deep_translator import GoogleTranslator
import os

# Criação da constante com o endereço da API de conselhos:
URL = 'https://api.adviceslip.com/advice'

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
        messagebox.showinfo('Sucesso', f'Conselhos salvos em {nome_txt}')
    except Exception as bug:
        logger.error(f'Erro ao salvar o arquivo: {bug}')
        messagebox.showerror('Erro', f'Erro ao salvar o arquivo: {bug}')

# Função para ler conselhos salvos no txt
def ler_txt_conselho(nome_txt='conselhos.txt'):
    try:
        with open(nome_txt, 'r', encoding='utf-8') as txt:
            return txt.readlines()
    except Exception as bug:
        logger.error(f'Erro ao ler o arquivo: {bug}')
        return None

# Função principal (modificada para GUI)
def main_gui():
    conselhos_recebidos = []
    conselhos_traduzidos = []

    # Função de buscar conselhos
    def buscar_conselhos():
        try:
            n_conselhos = int(entry_conselhos.get())
            conselhos_recebidos.clear()
            for i in range(n_conselhos):
                conselho = busca_conselho(URL)
                if conselho:
                    conselhos_recebidos.append(conselho)
                else:
                    listbox_conselhos.insert(tk.END, f"Conselho {i + 1}: Não foi possível obter o conselho.")
                sleep(1)
            messagebox.showinfo('Sucesso', 'Conselhos obtidos com sucesso!')
        except ValueError:
            messagebox.showerror('Erro', 'Por favor, insira um número válido!')

    # Função de exibir conselhos traduzidos
    def mostrar_conselhos():
        listbox_conselhos.delete(0, tk.END)  # Limpar a lista
        if conselhos_recebidos:
            for id_conselho, texto_conselho in conselhos_recebidos:
                translated_advice = traduzir_conselho(texto_conselho)
                listbox_conselhos.insert(tk.END, f'ID {id_conselho}: {translated_advice}')
        else:
            messagebox.showwarning('Aviso', 'Nenhum conselho recebido ainda.')

    # Função de salvar conselhos
    def salvar_conselhos():
        if conselhos_recebidos:
            conselhos_traduzidos = [
                (id_conselho, traduzir_conselho(texto_conselho)) 
                for id_conselho, texto_conselho in conselhos_recebidos
            ]
            salvar_txt_conselho(conselhos_traduzidos)
        else:
            messagebox.showwarning('Aviso', 'Nenhum conselho recebido para salvar!')

    # Função para ver conselhos salvos
    def ver_conselhos_salvos():
        conselhos_salvos = ler_txt_conselho()
        listbox_conselhos.delete(0, tk.END)  # Limpar a lista
        if conselhos_salvos:
            for conselho in conselhos_salvos:
                listbox_conselhos.insert(tk.END, conselho.strip())
        else:
            messagebox.showwarning('Aviso', 'Nenhum conselho salvo no arquivo.')

    # Função de exibir conselhos em inglês
    def mostrar_conselhos_ingles():
        listbox_conselhos.delete(0, tk.END)
        if conselhos_recebidos:
            for id_conselho, texto_conselho in conselhos_recebidos:
                listbox_conselhos.insert(tk.END, f'ID {id_conselho}: {texto_conselho}')
        else:
            messagebox.showwarning('Aviso', 'Nenhum conselho recebido ainda.')

    # Função de apagar o arquivo e encerrar o programa
    def encerrar_programa():
        try:
            os.remove('conselhos.txt')
            messagebox.showinfo('Arquivo Apagado', 'O arquivo de conselhos foi apagado!')
        except FileNotFoundError:
            messagebox.showwarning('Aviso', 'Arquivo de conselhos não encontrado, nada para apagar.')
        root.quit()

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Programa de Conselhos")
    root.geometry("600x400")

    # Widgets
    label = tk.Label(root, text="Seja bem-vindo, Seu Zé! Quantos conselhos você quer receber?")
    label.pack(pady=10)

    entry_conselhos = tk.Entry(root)
    entry_conselhos.pack(pady=5)

    button_buscar = tk.Button(root, text="Buscar Conselhos", command=buscar_conselhos)
    button_buscar.pack(pady=5)

    button_mostrar = tk.Button(root, text="Mostrar Conselhos Traduzidos", command=mostrar_conselhos)
    button_mostrar.pack(pady=5)

    button_salvar = tk.Button(root, text="Salvar Conselhos", command=salvar_conselhos)
    button_salvar.pack(pady=5)

    button_ver_salvos = tk.Button(root, text="Ver Conselhos Salvos", command=ver_conselhos_salvos)
    button_ver_salvos.pack(pady=5)

    button_ingles = tk.Button(root, text="Ver Conselhos em Inglês", command=mostrar_conselhos_ingles)
    button_ingles.pack(pady=5)

    button_encerrar = tk.Button(root, text="Encerrar e Apagar Arquivo", command=encerrar_programa)
    button_encerrar.pack(pady=20)

    listbox_conselhos = tk.Listbox(root, width=50, height=10)
    listbox_conselhos.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main_gui()