'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

class Solution:
    def wordBreak(self, s, wordDict):
        def helper(i=0, mem={}):
            if i == len(s):
                return ['']
            if i in mem:
                return mem[i]
            result = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    for tail in helper(j, mem):
                        result.append( s[i:j] + (' ' + tail if tail!= '' else ''))
            mem[i] = result
            return result
        return helper()

    def wordBreak_(self, s, wordDict):
        output = []
        def helper(i=0, prev_words=[], mem={}):
            if i == len(s):
                output.append(prev_words)
                return output[-1]
            if i in mem:
                output.append(mem[i])
                return output[-1]
            word = ''
            result = []
            for j in range(i, len(s)):
                word += s[j]
                if word in wordDict:
                    mem[i] = (helper(j+1, prev_words+[word]))
        helper()
        print(output)
        return list(map(lambda x:' '.join(x), output))

    def wordBreak__(self, s, wordDict):
        output = []
        def helper(i=0, prev_words=[], mem={}):
            if i == len(s):
                output.append(prev_words)
                return output[-1]
            if i in mem:
                output.append(mem[i])
                return output[-1]
            word = ''
            result = []
            for j in range(i, len(s)):
                word += s[j]
                if word in wordDict:
                    mem[i] = (helper(j+1, prev_words+[word]))
        helper()
        print(output)
        return list(map(lambda x:' '.join(x), output))

# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

x = Solution().wordBreak(s, wordDict)
print(x)