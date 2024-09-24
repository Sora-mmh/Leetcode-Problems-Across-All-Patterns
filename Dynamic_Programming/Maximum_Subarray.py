from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = s = nums[0]
        for e in nums[1:]:
            s = max(e, s + e)
            max_sum = max(s, max_sum)
        return max_sum
