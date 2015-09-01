__author__ = 'Cesar'

from extraiautomato import Automato


class MaquinaDeEstados:
    def __init__(self, automato, entrada):
        self.estadoInicial = automato.estados.pop(0)
        self.estadoAtual = self.estadoInicial
        self.estadosFinais = []
        self.entrada = []
        self.entrada = entrada
        self.automato = Automato
        self.automato = automato

        for estado in automato.estados:
            if estado[0] == '*':
                self.estadosFinais.append(estado[1:])

    def executar(self):
        deve_verificar_estado = False

        print self.entrada
        while True:
            try:
                token = self.entrada.pop(0)
                try:
                    if token not in self.automato.alfabeto:
                        print "Cadeia de entrada possui tokens nao presentes no alfabeto"
                        return 1
                finally:

                    trans_validas = []
                    for transicao in self.automato.transicoes:
                        if transicao.estado_atual == self.estadoAtual:
                            trans_validas.append(transicao)
                    for transicao in trans_validas:

                            if transicao.token == token:
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
                #if self.estadoAtual in self.estadosFinais:
            except:
                if self.estadoAtual in self.estadosFinais:
                    print "atingiu estado final"
                else:
                    self.estadoAtual = None
                    print "Cadeia de entrada acabou e a maq nao estava em um estado Final"
                break

