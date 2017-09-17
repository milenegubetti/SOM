"""
Esse modulo contem funcoes matematicas
"""
from math import exp


def distancia_euclidiana(x, y, n):
    """
    Essa funcao calcula a distancia euclidiana entre n pontos

    :param x: um numero ou uma lista de numeros 
    :param y: um numero ou uma lista de numeros
    :param n: quantidade de pontos
    :return: a distancia euclidiana
    """
    distancia = 0
    for i in range(n):
        distancia += (x[i]-y[i])**2
    distancia = distancia**(1/2)
    
    return distancia

def gaussiana(distancia, abertura):
    """
    Essa funcao calcula uma funcao de gauss
    
    :param 0.1: altura do pico da curva
    :param distancia: posicao do centro do pico
    :param abertura: largura do sino
    :return: o resultado da funcao exponencial

    """
    return 0.1 * exp((-(distancia**2)/(2*abertura**2)))

def aprendizado(epoca):
    """
    Essa funcao calcula o aprendizado
    
    :param epoca: numerador
    :param decaimento: denominador
    :return: o resultado da funcao exponencial
    """
    decaimento = 10
    
    return 0.1 * exp(-epoca/decaimento)
