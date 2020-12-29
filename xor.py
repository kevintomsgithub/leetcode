class TrieNode():
    def __init__(self):
        self.characters = {}
        self.end = False
        
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num):
        bn = '{:032b}'.format(num)
        cur = self.root
        for i in range(len(bn)):
            if bn[i] not in cur.characters:
                cur.characters[bn[i]] = TrieNode()
            cur = cur.characters[bn[i]]
        cur.end = True
      
    def getMax(self, num):
        bnum = '{:032b}'.format(num)
        cur = self.root
        op = ''
        for i in range(len(bnum)):
            cm = ''
            if bnum[i] == '0': cm = '1'
            else: cm = '0'
            
            if cm in cur.characters:
                op += cm
                cur = cur.characters[cm]
            else:
                op += bnum[i]
                cur = cur.characters[bnum[i]]
        op = int(op, 2)
        return op

    def BFS(self):
        q = [self.root]
        v = []
        while q:
            n = q.pop(0)
            # print(n.characters)
            for i, j in n.characters.items():
                print(i, j)
                if i not in v and j.end == False:
                    v.append(i)
                    q.append(j)
        
class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        T = Trie()
        for nm in nums:
            T.insert(nm)

        def list_words(trie):
            my_list = []
            for k,v in trie.characters.items():
                if k != '_':
                    for el in list_words(v):                
                        my_list.append(k+el)
                else:
                    my_list.append('')
            return my_list

        print(list_words(T.characters))
        
        res = 0
        for nm in nums:
            r = 0
            an_op = T.getMax(nm)
            r = nm ^ an_op
            if r > res: res = r
        
        return res

x = Solution().findMaximumXOR([3, 10, 5, 25])
print(x)