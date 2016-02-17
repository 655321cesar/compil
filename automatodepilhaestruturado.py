__author__ = 'Cesar'


from lexic import Token


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
        self.name = linha.split('"')[1::2]

        linha = arquivo.readline().rstrip('\n')
        self.estados = linha.split('"')[1::2]
        self.n_estados = self.estados.__len__()

        linha = arquivo.readline().rstrip('\n')
        alfa = linha.split('"')[1::2]
        self.alfabeto = [Token(item).tokenize() for item in alfa]
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
            token = Token(token).tokenize()
            prox_estado = splitline.pop(0)

            transicao = Transicao(nome, estado_atual, token, prox_estado)
            self.transicoes.append(transicao)
            trans += 1


class MaquinaDeEstados:
    def __init__(self, name, automatos, entrada, pilha):

        self.name = name
        self.automatos = automatos
        for aut in self.automatos:
            if aut.name == self.name:
                self.automato = aut
        self.estadoInicial = self.automato.estados.pop(0)
        self.estadoAtual = self.estadoInicial
        self.estadosFinais = []
        self.entrada = entrada
        self.pilha = pilha

        for estado in self.automato.estados:
            if estado[0] == '*':
                self.estadosFinais.append(estado[1:])

    def executar(self):
        deve_verificar_estado = False

        print [i.token for i in self.entrada]
        for token in self.entrada:
            if token.token not in [item.token for item in self.automato.alfabeto]:
                print "Cadeia de entrada possui tokens nao presentes no alfabeto"
                return 1

        while True:
            try:
                token = self.entrada.pop(0)
                trans_validas = []
                for transicao in self.automato.transicoes:
                    if transicao.estado_atual == self.estadoAtual:
                        trans_validas.append(transicao)

                for transicao in trans_validas:
                    if transicao.token.token == token.token:
                        if token.classe == 'submaq':
                            self.pilha.append(transicao.prox_estado)
                            sub = MaquinaDeEstados(token.token, self.automatos, self.entrada, self.pilha)
                            sub.executar()
                            self.estadoAtual = self.pilha.pop()
                            deve_verificar_estado = False
                        else:
                            self.estadoAtual = transicao.prox_estado
                            print self.estadoAtual
                            deve_verificar_estado = False
                            break

                    else:
                        deve_verificar_estado = True

                if deve_verificar_estado:
                    if self.estadoAtual in self.estadosFinais:
                        print "atingiu estado final"

                    else:
                        self.estadoAtual = None
                        print "nao ha transicao desse estado e a maq nao estava em um estado Final"
                        return 1

            except:
                if self.estadoAtual in self.estadosFinais:
                    print "atingiu estado final"
                else:
                    self.estadoAtual = None
                    print "Cadeia de entrada acabou e a maq nao estava em um estado Final"
                break
