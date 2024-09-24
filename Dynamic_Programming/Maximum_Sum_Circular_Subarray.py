from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = curr_min = curr_max = 0
        max_sum = min_sum = nums[0]
        for e in nums:
            curr_max = max(e, curr_max + e)
            max_sum = max(max_sum, curr_max)
            curr_min = min(e, curr_min + e)
            min_sum = min(min_sum, curr_min)
            s += e
        return max(max_sum, s - min_sum) if max_sum > 0 else max_sum
