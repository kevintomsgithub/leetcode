import heapq
from typing import List


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        max_heap = []
        tmp = [False] * len(nums)

        # left -> right
        for i, n in enumerate(nums):
            if len(max_heap) == k and -max_heap[0] < n:
                tmp[i] = True
            heapq.heappush(max_heap, -n)
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        count = 0
        max_heap = []
        # right -> left
        for i in range(len(nums) - 1, -1, -1):
            if len(max_heap) == k and -max_heap[0] < nums[i] and tmp[i]:
                count += 1
            heapq.heappush(max_heap, -nums[i])
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return count


nums = [2, 3, 6, 5, 2, 3]
k = 2

solution = Solution()
result = solution.kBigIndices(nums, k)
print(result)
