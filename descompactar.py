"""
Esse modulo e responsavel pelo processo de descompactacao
"""
import gzip as g
from imagem import Imagem
from tabela import Tabela
from bitwise import Bitwise
from arquivo import Arquivo


def descompactar(caminho, nome, formato):
    """
    Essa funcao descompacta o arquivo e salva uma imagem no formato .TIFF
    
    :param caminho: o caminho do arquivo compactado
    :param nome: o nome do arquivo compactado
    :param formato: o formato do arquivo compactado
    """

    # Abre e le o arquivo
    arquivo = Arquivo(caminho, nome, formato)
    cabecalho_compactado = arquivo.ler()

    #----------------------------------------

    # Descompactacao do cabecalho por meio do gzip
    cabecalho = g.decompress(cabecalho_compactado)

    #----------------------------------------

    # Cabecalho
    numero_magico = int.from_bytes(cabecalho[0:1], byteorder="big") 
    if numero_magico != 42:
        exit()

    largura = int.from_bytes(cabecalho[1:3], byteorder="big")
    altura = int.from_bytes(cabecalho[3:5], byteorder="big")
    quantidade_cores = int.from_bytes(cabecalho[5:6], byteorder="big")
    lista = list(cabecalho[6:262])
    conteudo = list(cabecalho[262:len(cabecalho)])

    #----------------------------------------
    
    # Amplia para 8 bits
    bit = Bitwise(6)
    imagem_rotulada = bit.ampliar(conteudo, largura*altura)

    #----------------------------------------

    # Cria a tabela
    matriz = [[lista[y], lista[y+1], lista[y+2], lista[y+3]] for y in range(0, len(lista), 4)]
    tabela = Tabela(matriz)

    #----------------------------------------

    # Cria um objeto da classe Imagem
    final = Imagem(caminho, nome+"_som", "TIFF")
    # Salva a imagem
    final.salvar(largura, altura, imagem_rotulada, tabela)
