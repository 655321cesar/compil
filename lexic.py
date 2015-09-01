__author__ = 'Cesar Santos'


class Analisador:
    def __init__(self, token):
        self.token = token
        self.val = ord(token)

    def analiza(self):
        if 65 <= self.val <= 90 or 97 <= self.val <= 122:
            return 'a'

        elif 48 <= self.val <= 57:
            return 'n'

        else:
            return chr(self.val)
