__author__ = 'Cesar'


class Transicao:
    def __init__(self, nome, estado_atual, token, prox_estado):
        self.nome = nome
        self.estado_atual = estado_atual
        self.token = token
        self.prox_estado = prox_estado


class Automato:

    def __init__(self, filename):
        self.filename = filename
        self.estados = []
        self.n_estados = 0
        self.alfabeto = []
        self.tam_alfabeto = 0
        self.transicoes = []


        arquivo = open(self.filename, 'r')

        linha = arquivo.readline().rstrip('\n')
        self.estados = linha.split('"')[1::2]
        self.n_estados = self.estados.__len__()

        linha = arquivo.readline().rstrip('\n')
        self.alfabeto = linha.split('"')[1::2]
        self.tam_alfabeto = self.alfabeto.__len__()

        trans = 0
        while True:

            linha = arquivo.readline().rstrip('\n')
            if not linha:
                break
            nome = 'transicao_'+str(trans)
            splitline = linha.split('"')[1::2]
            estado_atual = splitline.pop(0)
            token = splitline.pop(0)
            prox_estado = splitline.pop(0)

            transicao = Transicao(nome, estado_atual, token, prox_estado)
            self.transicoes.append(transicao)
            trans += 1




""""
if __name__ == "__main__":

    automato = IdentificaAutomato("teste.txt")
    print automato.estados
    print automato.n_estados
    print automato.alfabeto
    print automato.tam_alfabeto
    print automato.transicoes
    print automato.transicao.prox_estado


"""""
