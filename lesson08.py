# classメソッド lesson08.py
class T(object):
    words = []
    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

print(c.words)

# cc = T()
# cc.add_word('add 11')
# cc.add_word('add 22')
#
# print(cc.words)

