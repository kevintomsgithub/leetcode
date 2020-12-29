class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        def helper(arr, combination, total, required_sum, start):
            if total > required_sum:
                return
            elif total == required_sum:
                self.res.append(combination)
                # print(self.res)
                return
            else:
                for i in range(start, len(arr)):
                    helper(arr, combination + [arr[i]], total + arr[i], required_sum, i)
        
        helper(sorted(candidates), [], 0, target, 0)
        return self.res

x = Solution()
print(x.combinationSum([2, 5], 10))