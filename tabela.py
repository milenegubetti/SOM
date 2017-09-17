"""
Esse modulo define uma classe Tabela
"""
from matematica import *


class Tabela():
    """
    Esta classe representa uma tabela
    """
    def __init__(self, lista):
        """
        Esse metodo cria um objeto da classe Tabela

        :param lista: a lista que contem os identificadores e o respectivo RGB
        """
        self.lista = lista
        self.tamanho = len(self.lista)

    def classificar(self, referencia):
        """
        Esse metodo encontra o melhor neuronio na tabela

        :param referencia: um pixel da imagem original
        :return: o identificador do melhor neuronio
        """
        distancia_minima = distancia_euclidiana(referencia, [self.lista[0][1],self.lista[0][2],self.lista[0][3]], 3)
        identificador = self.lista[0][0]

        for i in range(self.tamanho):
            distancia = distancia_euclidiana(referencia, [self.lista[i][1],self.lista[i][2],self.lista[i][3]], 3)
            if distancia < distancia_minima:
                distancia_minima = distancia
                identificador = self.lista[i][0]

        return identificador
