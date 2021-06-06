# classメソッド lesson08.py
class T(object):
    words = "kreis"

    def printword(self):
        print(self.words)

    @classmethod
    def classprintWrod(cls):
        print(cls.words)

    @staticmethod
    def staticprintword(word):
        print(word)
c = T()
c.printword()


T.classprintWrod()
T.staticprintword("RUFT")

