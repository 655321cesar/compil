__author__ = 'Cesar'

from maquinadeestados import Automato
from maquinadeestados import MaquinaDeEstados


if __name__ == "__main__":

    automato = Automato("teste.txt")
    arquivo = open('cadeia.txt', 'r')
    entrada = arquivo.readline().rstrip('\n')
    tokens = list(entrada)
    maq = MaquinaDeEstados(automato, tokens)
    maq.executar()




"""
    print automato.alfabeto

    for transicao in automato.transicoes:
        print (transicao.nome, transicao.estado_atual, transicao.token, transicao.prox_estado)

"""