"""
Esse modulo e responsavel pelo processo de compactacao
"""
import gzip as g
from imagem import Imagem
from mapa import Mapa
from bitwise import Bitwise
from arquivo import Arquivo


def compactar(caminho, nome, formato):
    """
    Essa funcao compcta uma imagem e salva num arquivo .SOM
    
    :param caminho: o caminho da imagem
    :param nome: o nome da imagem
    :param formato: o formato da imagem
    """

    # Cria um objeto da classe Imagem
    original = Imagem(caminho, nome, formato)
    # Abre, cria o cabecalho e carrega os pixels da imagem original 
    original.inicializar()
    # Cria o mapa
    mapa = Mapa([8,8])

    # Elimina as repeticoes da imagem
    pixels = set()

    for y in range(original.altura):
        for x in range(original.largura):
            if original.pixels[x,y] not in pixels:
                pixels.add(original.pixels[x,y])

    pixels = list(pixels)

    print("eliminei os pixels repetidos")
    print(len(pixels))

    epocas = 1

    for epoca in range(epocas):
        # Percorre a imagem original
        for referencia in pixels:
            # Procura o neuronio mais proximo no mapa 
            posicao = mapa.classificar(referencia)
            # Atualiza o mapa
            mapa.atualizar(posicao, referencia, epoca)

    print("percorri a imagem")

    # Arredonda o RGB dos neuronios
    mapa.arredondar()
    # Gera a tabela com o id e o RGB
    tabela = mapa.gerar_tabela()

    print("gerei a tabela")
    
    #----------------------------------------

    imagem_rotulada = []
    # Percorre a imagem original
    for y in range(original.altura):
        for x in range(original.largura):
            # Pega um pixel da imagem original como referencia
            referencia = original.pixels[x,y]
            # Procura o neuronio mais proximo no mapa
            identificador = tabela.classificar(referencia)
            # Adiciona o identificador a imagem rotulada
            imagem_rotulada.append(identificador)

    print("gerei a imagem rotulada")

    #----------------------------------------
    
    bit = Bitwise(6)
    # Reduz de 8bits para 6bits
    imagem_rotulada_6bits = bit.reduzir(imagem_rotulada)

    print("reduzi o número de bits")
    
    #----------------------------------------
    
    # Cabecalho
    numero_magico = (42).to_bytes(1, byteorder="big")
    largura = (original.largura).to_bytes(2, byteorder="big")
    altura = (original.altura).to_bytes(2, byteorder="big")
    quantidade_cores = (tabela.tamanho).to_bytes(1, byteorder="big")
    tabela = bytes([coluna for linha in tabela.lista for coluna in linha])
    conteudo = bytes(imagem_rotulada_6bits)

    cabecalho = numero_magico + largura + altura + quantidade_cores + tabela + conteudo
    
    print("criei o cabeçalho")

    #----------------------------------------
    
    # Compactacao do cabecalho por meio do gzip
    cabecalho_compactado = g.compress(cabecalho)
    
    print("compactei o cabeçalho")

    #----------------------------------------
    
    # Salva o cabecalho num arquivo
    arquivo = Arquivo(caminho, nome, "som")
    arquivo.escrever(cabecalho_compactado)

    print("salvei num arquivo")
