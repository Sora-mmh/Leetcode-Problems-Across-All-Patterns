from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums) and sum(nums[:idx]) != sum(nums[idx + 1 :]):
            idx += 1
        if sum(nums[:idx]) == sum(nums[idx + 1 :]) and idx != len(nums):
            return idx
        else:
            return -1
