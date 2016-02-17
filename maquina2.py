from automatodepilhaestruturado import *
from multimaq import *

__author__ = 'Cesar'

if __name__ == "__main__":

    no_automatos = Multimaq("teste.txt").parse()
    arquivo = open('cadeia.txt', 'r')
    entradapura = arquivo.readline().rstrip('\n')
    entrada = [Token(item).tokenize() for item in entradapura]
    automatos = []

    for no in range(no_automatos):
        nome = 'auto_' + str(no) + '.txt'
        automatos.append(Automato(nome))

    pilha = []

    maq = MaquinaDeEstados(automatos[0].name, automatos, entrada, pilha)
    maq.executar()




"""
    print automato.alfabeto

    for transicao in automato.transicoes:
        print (transicao.nome, transicao.estado_atual, transicao.token, transicao.prox_estado)

"""