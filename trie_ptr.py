class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                curr.children[letter] = Node()
                curr = curr.children[letter]
        curr.is_word = True
        print(f'inserted {word}')

    def _traverse(self, word):
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        return curr

    def search(self, word):
        node = self._traverse(word)
        if node:
            return node.is_word
        return False

    def begins_with(self, word):
        node = self._traverse(word)
        return True if node else False

    def wild_search(self, word):
        def dfs(root, word):
            for i, c in enumerate(word):
                if c == '.':
                    for _c in root.children:
                        if dfs(root.children[_c], word[i+1:]):
                            return True
                if c not in root.children:
                    return False
                root = root.children[c]
            return root.is_word

        root = self.root
        return dfs(root, word)

trie = Trie()
trie.insert("cats")
trie.insert("caps")
trie.insert("captain")