# Longest Common Prefix
class Trie():
    def __init__(self):
        self.root = {'*': '*'}

    def insert(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = '*'
    
    def lcp(self):
        children = list(self.root.keys())
        print(children)
        pos_x = children.index('*')
        del children[pos_x]
        num_children = len(children)
        if num_children>1:
            return ''
        if num_children == 0:
            return ''
        first_child = children[0]
        curr_node = self.root[first_child]
        lcp_str = str(first_child)
        print(lcp_str)
        while curr_node:
            print('cc node - ',len(curr_node))
            num_children = len(curr_node.keys())
            if num_children>1:
                return lcp_str
            next_node = list(curr_node.keys())[0]
            lcp_str += next_node
            curr_node = curr_node[next_node]
        return ''
        
# T = Trie()
# word_list = ["","b"]
# word_list = ["flower","flow","flight"]
# word_list = ["dog","racecar","car"]
# for word in word_list:
#     T.insert(word)

def longestCommonPrefix(strs):
    if len(strs) == 0: return ''
    if len(strs) == 1: return strs[0]
    smallest_str = min(strs, key=len)
    greatest_c_p = ''
    for index, i in enumerate(smallest_str):
        match = 0
        for j in strs:
            if i == j[index]:
                match += 1
        if match == len(strs):
            greatest_c_p += i
        else:
            return greatest_c_p
    return greatest_c_p

a = ["dog", "dog", 'dog']
print(longestCommonPrefix(a))