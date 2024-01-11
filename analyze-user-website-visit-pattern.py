"""
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i] .
A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.
(The websites in a 3-sequence are not necessarily distinct.)
Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

Input: username =
I"joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"1,
timestamp = [1,2,3,4,5,6,7,8,9,10], website =
["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
Output: ["home", "about", "career"]
Explanation:
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"] ["joe", 3, "career"] ("james", 4, "home"] ["james", 5, "cart"] ("james", 6, "maps"] ["james", 7, "homel"] ("mary", 8, "home"] ["mary", 9, "about"] ["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2
users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    def get_seq_of_three(self, seq) -> List[List[str]]:
        if len(seq) < 3:
            return None
        for i in range(len(seq) - 2):
            yield seq[i : i + 3]

    def mostVisistedPattern(
        self, username: str, timestamp: List[int], website: List[str]
    ) -> List[str]:
        seq_map = defaultdict(list)

        for u, w in zip(username, website):
            seq_map[u].append(w)

        results = []
        for s in seq_map.values():
            result = list(self.get_seq_of_three(s))
            if result:
                results += result
        # ["a", "b", "c"] -> "abc"
        seq_str_map = defaultdict(int)
        for s in results:
            seq_str = "".join(s)
            if seq_str not in seq_str_map:
                seq_str_map[seq_str] = s

        seq_list = map(lambda x: "".join(x), results)

        c = Counter(seq_list)
        m = max(c.values())
        results = sorted([k for k, v in c.items() if v == m])
        return list(map(lambda x: seq_str_map[x], results))[0]


# test
username = [
    "joe",
    "joe",
    "joe",
    "james",
    "james",
    "james",
    "james",
    "mary",
    "mary",
    "mary",
]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = [
    "home",
    "about",
    "career",
    "home",
    "cart",
    "maps",
    "home",
    "home",
    "about",
    "career",
]

output = ["home", "about", "career"]

solution = Solution()
result = solution.mostVisistedPattern(username, timestamp, website)

print(result)
print(result == output)

# tmp = solution.get_seq_of_three([1, 2, 3, 4])
# print(list(tmp))
