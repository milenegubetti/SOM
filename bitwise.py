"""
Esse modulo define uma classe Bitwise
"""
from math import ceil


class Bitwise:
    """
    Esta classe representa o bitwise
    """

    def __init__(self, quant):
        """
        Esse metodo cria um objeto da classe Bitwise

        :param quant: a quantidade de bits
        """
        self.quant = quant

    def reduzir(self, bytes_entrada):
        """
        Esse metodo reduz uma lista de 8 bits para uma lista de quant bits

        :param bytes_entrada: uma lista de bytes
        :return: uma lista de bytes reduzida
        """
        posicao_byte_entrada = 0
        posicao_bit_entrada = 0
        posicao_byte_saida = 0
        posicao_bit_saida = 0

        tamanho = len(bytes_entrada)

        bytes_saida = [0 for i in range(ceil((tamanho*self.quant)/8))]

        for i in range(tamanho*self.quant):
        
            bytes_saida[posicao_byte_saida] = bytes_saida[posicao_byte_saida] | (((bytes_entrada[posicao_byte_entrada] & (1<<posicao_bit_entrada))>>posicao_bit_entrada)<<posicao_bit_saida)

            posicao_bit_entrada += 1 
            if posicao_bit_entrada == self.quant:
                posicao_byte_entrada += 1
                posicao_bit_entrada = 0

            posicao_bit_saida += 1
            if posicao_bit_saida == 8:
                posicao_byte_saida += 1
                posicao_bit_saida = 0

        return bytes_saida

    def ampliar(self, bytes_entrada, tamanho):
        """
        Esse metodo amplia uma lista de quant bits para uma lista de 8 bits

        :param bytes_entrada: uma lista de bytes reduida
        :param tamanho: o tamanho da lista original
        :return: uma lista de bytes ampliada
        """
        posicao_byte_entrada = 0
        posicao_bit_entrada = 0
        posicao_byte_saida = 0
        posicao_bit_saida = 0

        bytes_saida = [0 for i in range(tamanho)]

        for i in range(tamanho*self.quant):

            bytes_saida[posicao_byte_saida] = bytes_saida[posicao_byte_saida] | (((bytes_entrada[posicao_byte_entrada] & (1<<posicao_bit_entrada))>>posicao_bit_entrada)<<posicao_bit_saida)

            posicao_bit_entrada += 1
            if posicao_bit_entrada == 8:
                posicao_byte_entrada += 1
                posicao_bit_entrada = 0

            posicao_bit_saida += 1
            if posicao_bit_saida == self.quant:
                posicao_byte_saida += 1
                posicao_bit_saida = 0

        return bytes_saida
