# Using Trie
class Trie:
    
    def __init__(self):
        self.root = {'*': '*'}
        
    def add_word(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = '*'
        
    def dfs(self, curr, word, result):
        if len(result) == 3: return result
        if curr == "*":
            result.append(word[:-1])
            return
        for l in sorted(curr.keys()):
            self.dfs(curr[l], word+l, result)
        return result
        
            
    def get_three_suggestions(self, word):
        curr = self.root
        for letter in word:
            if letter in curr: 
                curr = curr[letter]
            else: return []
        return self.dfs(curr, word, [])
                

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        for word in products: t.add_word(word)
            
        results = []
        for i in range(len(searchWord)):
            results.append(t.get_three_suggestions(searchWord[:i+1]))
        
        return results

"""
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
"""

# Using Binary Search
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        l, r = 0, len(products)-1
        results = []
        
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != c): l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c): r -= 1
            results.append(products[l:r+1][:3])
        
        return results
        
            