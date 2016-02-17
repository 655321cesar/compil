__author__ = 'Cesar Santos'


class Token:
    def __init__(self, token):
        self.token = token
        self.val = ord(token)
        self.classe = 'trash'

    def tokenize(self):
        if 97 <= self.val <= 122:
            self.classe = 'id'

        elif 65 <= self.val <= 90:
            self.classe = 'submaq'

        elif 48 <= self.val <= 57:
            self.classe = 'digit'

        elif self.val in [40, 41, 91, 93, 123, 125]:
            self.classe = 'delimit'

        return self
