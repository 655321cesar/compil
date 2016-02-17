class Multimaq:

    def __init__(self, filename):

        self.filename = filename

    def parse(self):
        with open(self.filename, 'r') as read:
            no = 0
            name = 'auto_' + str(no) + '.txt'
            linha = read.readline()
            while linha and linha not in ['\n', '\r\n']:
                with open(name, 'w') as write:
                    while linha and linha not in ['\n', '\r\n']:
                        write.write(linha)
                        linha = read.readline()
                no += 1
                name = 'auto_' + str(no) + '.txt'
                linha = read.readline()
        return no
