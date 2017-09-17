"""
Esse modulo define uma classe Imagem
"""
from PIL import Image


class Imagem():
    """
    Esta classe representa uma imagem
    """
    def __init__(self, caminho, nome, formato):
        """
        Esse metodo cria um objeto da classe Imagem

        :param caminho: caminho da imagem
        :param nome: nome da imagem
        :param formato: formato da imagem
        """
        self.caminho = caminho
        self.nome = nome
        self.formato = formato

    def inicializar(self):
        """
        Esse metodo abre e carrega uma imagem, alem de salvar a largura e altura
        """
        self.abrir()
        self.largura = self.imagem.size[0]
        self.altura = self.imagem.size[1]
        self.carregar()        

    def abrir(self):
        """
        Esse metodo abre uma imagem
        """
        try:
            self.imagem = Image.open(self.caminho+"/"+self.nome+"."+self.formato)
        except FileNotFoundError:
            exit()

    def carregar(self):
        """
        Esse metodo carrega os pixels da imagem
        """
        self.pixels = self.imagem.load()

    def salvar(self, largura, altura, imagem_rotulada, tabela):
        """
        Esse metodo salva uma imagem

        :param largura: largura da imagem inicial
        :param altura: altura da imagem inicial
        :param imagem_rotulada: lista que contem ids
        :param tabela: objeto da classe Tabela
        """
        self.imagem = Image.new("RGB", (largura, altura), "black")
        self.carregar()

        count = 0

        for y in range(altura):
            for x in range(largura):
                self.pixels[x,y] = (tabela.lista[imagem_rotulada[count]][1], tabela.lista[imagem_rotulada[count]][2], tabela.lista[imagem_rotulada[count]][3])
                count += 1

        self.imagem.save(self.caminho+"/"+self.nome+"."+self.formato)
