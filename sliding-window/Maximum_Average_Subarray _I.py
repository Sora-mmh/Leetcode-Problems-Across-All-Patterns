from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / k
        else:
            s = max_s = sum(nums[:k])
            for idx in range(k, len(nums)):
                s += nums[idx] - nums[idx - k]
                max_s = max(s, max_s)
            return max_s / k
