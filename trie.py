class Trie:
    def __init__(self):
        self.root = {'*': '*'}
    
    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = '*'
    
    def does_word_exist(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return '*' in curr_node


tire = Trie()
words = ['cat', 'catwalk', 'cost', 'costly']
for word in words:
    tire.add_word(word)

print(tire.does_word_exist('cat'))   # True
print(tire.does_word_exist('cater')) # False
print(tire.does_word_exist('cast'))  # False
print(tire.does_word_exist('costl')) # False

while 1:
    x = input()
    print(tire.does_word_exist(x))