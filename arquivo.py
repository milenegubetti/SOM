"""
Esse modulo define uma classe Arquivo
"""

class Arquivo():
    """
    Esta classe representa um arquivo
    """

    def __init__(self, caminho, nome, formato):
        """
        Esse metodo cria um objeto da classe Arquivo

        :param caminho: o caminho do arquivo
        :param nome: o nome do arquivo
        :param formato: o formato do arquivo
        """
        self.caminho = caminho
        self.nome = nome
        self.formato = formato

    def escrever(self, cabecalho):
        """
        Esse metodo escreve um conjunto de bytes no arquivo

        :param cabecalho: o conteudo que sera escrito no arquivo
        """
        try:
            self.arquivo = open(self.caminho+"/"+self.nome+"."+self.formato, "wb")
        except FileNotFoundError:
            exit()
        self.arquivo.write(cabecalho)
        self.arquivo.close()

    def ler(self):
        """
        Esse metodo le o arquivo

        :return: o conteudo do arquivo, em bytes
        """
        self.arquivo = open(self.caminho+"/"+self.nome+"."+self.formato, "rb")
        conteudo = self.arquivo.read()
        self.arquivo.close()

        return conteudo
