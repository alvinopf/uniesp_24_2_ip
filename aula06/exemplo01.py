from time import sleep

def enviar_lembrete():

    spam = 0
    # variável de controle (spam)
    while spam < 5:
        print(f'Altere sua senha. Lembrete nº {spam}')
        spam += 1
        # spam += 1 é a mesma coisa que spam = spam + 1 que é o incremento para que o programa tenha um fim
        sleep(2)

if __name__ == '__main__':

    enviar_lembrete()