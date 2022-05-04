#####################################################################################################################################
'''
----------- Question ---------
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

 

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.

Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.

Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
'''
#####################################################################################################################################
import sys
from collections import defaultdict

class Solution:
    def get_encode_string(self, s):
        i = 1
        prev_char = s[0]
        character_counter = 1
        encoded_str = ''
        while i < len(s):
            if s[i] == prev_char:
                character_counter += 1
            else:
                if character_counter == 1:
                    encoded_str += prev_char
                else:
                    encoded_str += f'{prev_char}{character_counter}'
                prev_char = s[i]
                character_counter = 1
            i += 1
        if s[i-1] == prev_char:
            if character_counter == 1:
                encoded_str += prev_char
            else:
                encoded_str += f'{prev_char}{character_counter}'
        return encoded_str

    def get_combinations(self, k, available, used=[]):
        if len(used) == k: 
            return [used]
        elif len(available) == 0: 
            return []
        else:
            return self.get_combinations(k, available[1:], used + [available[0]]) + self.get_combinations(k, available[1:], used)

    def replace_chars(self, s, c_list):
        for c in c_list:
            s = s.replace(c, '')
        return s

    def delete_char_combinations(self, k, s, mem={}):
        if k == 0:
            return [s]
        if s in mem:
            return mem[s]
        else:
            to_return = []
            for i in range(len(s)):
                new_s = s[:i] + s[i+1:]
                to_return += self.delete_char_combinations(k-1, new_s)
            mem[s] = list(set(to_return))
            return to_return

    def get_max_len(s, k):
        most_freq = 0
        for i in range(len(s)):
            c = s[i]
            d[c] += 1
            most_freq = max(most_freq, d[c])
            compressed_length = 1 + (len(str(most_freq)) if most_freq > 1 else 0)
            print(s[:i+1], compressed_length)
    
    def getLengthOfOptimalCompression_kevin(self, s: str, k: int) -> int:
        if k == 0: return len(self.get_encode_string(s))
        if len(s) == 1 and k == 0: return 1
        if len(s) == 1 and k == 1: return 0
        # unique_char = list(set(s))
        # print('unique chars: ', unique_char)
        # combinations = self.get_combinations(k, unique_char)
        # print('combinations: ', combinations)
        # reduced_strings = list(map(lambda x: self.replace_chars(s, x), combinations))
        # print('reduced_str : ', reduced_strings)
        # reduced_str_lens = list(map(self.get_encode_string, reduced_strings))
        # print('reduced_str : ', reduced_str_lens)
        delete_combinations = list(set(self.delete_char_combinations(k, s)))
        print('del_combination_str : ', delete_combinations)
        reduced_str = list(map(self.get_encode_string, delete_combinations))
        print('reduced_strings     : ', reduced_str)
        return len(min(reduced_str, key=len))

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def dp(start, k):
            if (start, k) in memo: return memo[(start, k)]
            if start == n or n-start <= k: return 0
            ans = sys.maxsize
            count = defaultdict(int)
            most_freq = 0
            for j in range(start, n):
                c = s[j]
                count[c] += 1
                most_freq = max(most_freq, count[c])

                compressed_length = 1 + (len(str(most_freq)) if most_freq > 1 else 0)

                if k >= j-start+1-most_freq:
                    ans = min(ans, compressed_length + dp(j+1, k - (j-start+1-most_freq)))

            memo[(start, k)] = ans
            return ans

        n = len(s)
        memo = {}
        return dp(0, k)
        
# s = 'aaabcccd'
s = 'abcdefghijklmnopqrstuvwxyz'
k = 16

solution = Solution()
x = solution.getLengthOfOptimalCompression(s, k)

print(x)