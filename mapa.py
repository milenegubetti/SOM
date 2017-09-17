"""
Esse modulo define uma classe Mapa
"""
from random import randint
from matematica import *
from tabela import Tabela


class Mapa():
    """
    Esta classe representa um mapa
    """

    def __init__(self, tamanho):
        """
        Esse metodo cria um objeto da classe Mapa

        :param tamanho: as dimensoes do mapa (x,y)
        """
        self.largura = tamanho[0]
        self.altura = tamanho[1]
        self.lista = [[[randint(0,255), randint(0,255), randint(0,255)] for x in range(self.largura)] for y in range(self.altura)]

    def atualizar(self, posicao, referencia, epoca):
        """
        Esse metodo atualiza o mapa

        :param posicao: a posicao do melhor neuronio
        :param referencia: um pixel da imagem original
        :param epoca: a epoca do treinamento
        """
        for y in range(self.altura):
            for x in range(self.largura):

                distancia = distancia_euclidiana([x,y], posicao, 2)

                for i in range(3):
                    self.lista[x][y][i] += gaussiana(distancia, 0.5) * aprendizado(epoca) * (referencia[i] - self.lista[x][y][i])

    def classificar(self, referencia):
        """
        Esse metodo encontra o melhor neuronio no mapa

        :param referencia: um pixel da imagem original
        :return: a posicao do melhor neuronio
        """
        distancia_minima = distancia_euclidiana(referencia, self.lista[0][0], 3)
        posicao = [0,0]

        for y in range(self.altura):
            for x in range(self.largura):
                distancia = distancia_euclidiana(referencia, self.lista[x][y], 3)
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    posicao = [x,y]

        return posicao

    def arredondar(self):
        """
        Esse metodo arredonda todos os elementos da lista
        """
        for y in range(self.altura):
            for x in range(self.largura):
                for i in range(3):
                    self.lista[x][y][i] = int(self.lista[x][y][i])

    def gerar_tabela(self):
        """
        Esse metodo gera uma tabela, da seguinte forma: [id, R, G, B]

        :return: um objeto da classe Tabela
        """
        lista = []
        count = 0
        for y in range(self.altura):
            for x in range(self.largura):
                lista.append([count, self.lista[x][y][0], self.lista[x][y][1], self.lista[x][y][2]])
                count += 1

        return Tabela(lista)
