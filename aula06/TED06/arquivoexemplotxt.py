# Um arquivo TXT é um dos formatos mais simples para armazenar dados de texto. Ele não possui qualquer formatação ou estilo. No Python é possível manipular arquivos txt de diversas formas, como para analisar dados ou processar texto. 

# Formas mais básicas de manipulação de arquivos txt no Python envolvem comandos para abrir o arquivo (open), ler (read), escrever e adicionar informações ao final (write) e fechar o arquivo (close), entre várias outras possibilidades.

# Para manipular um arquivo txt no Python, você precisa primeiro abri-lo, usando a função open(). É possível utilizar parâmetros como r (modo de leitura), w (modo de escrita), a (modo de adicionar novas informações ao final), x (criação de arquivo), b (modo binário), entre outros.

# Exemplo:

arquivo = open("aula06/ted06/vingadores.txt", "r")
arquivo.close()
# Aqui foi  criada a variável arquivo, onde o arquivo vingadores.txt foi aberto. Em seguida o arquivo foi fechado com o comando close.

# Após abri-lo no programa, caso você queira ler o arquivo, você pode usar opções como read() (para ler todo o arquivo de uma vez, não recomendada para quando o arquivo for muito extenso e seu programa precise de memória livre), readline() (para ler uma linha por vez), entre outros.

# Exemplo:

arquivo = open("aula06/ted06/vingadores.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
# Aqui, após a abertura do arquivo, foi criada a variável conteudo, onde o conteúdo do arquivo vingadores.txt foi lido e armazenado. Em seguida, o programa imprime a variável conteúdo, que contém as informações do arquivo e fecha o arquivo.

# Exemplo 2:

arquivo = open("aula06/ted06/vingadores.txt", "r")
linha = arquivo.readline()
while linha:
    print(linha.strip())
    linha = arquivo.readline()
arquivo.close()
# Aqui, após a abertura do arquivo, foi criada a variável linha, onde as linhas do arquivo vingadores.txt são lidas e impressas no programa através de um loop while. Ao final o arquivo é fechado. Com o strip(), eu removo quebras de linha e espaços extras no início e final de cada linha do arquivo.

# Para escrever em um arquivo txt é preciso que ele seja aberto em modo de escrita "w" ou append "a" utilizando write().

# Exemplo:

arquivo = open("aula06/ted06/vingadores.txt", "a")
arquivo.write("\nSpiderman")
arquivo.close()
# Aqui, após a abertura do arquivo, foi criada uma linha abaixo de todas as linhas já existentes no arquivo, com o vingador subestimado, Spiderman (o do Tom Rolland faz juz à subestimação mesmo... Se fosse o do Tobey ou do Andrew, se tornaria o líder da equipe em pouco tempo!).

# Existem outras formas de manipular arquivos txt no Python, como usando os comandos for, para realizar loops de leitura, ou with, para abrir e fechar os arquivos sem se preocupar com o comando close, por exemplo. Além disso, existem comandos mais avançados como o split(), que divide linhas levando em consideração um caractere especificado; replace(), que substitui valores específicos; strip(), que remove espaços em branco das linhas, entre outras opções. Também é possível utilizar bibliotecas específicas de manipulação de arquivos, como a Pandas. 