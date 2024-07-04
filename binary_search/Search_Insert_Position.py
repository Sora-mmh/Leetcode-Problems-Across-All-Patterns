from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] == target:
                return idx
            idx += 1

        idx = len(nums) - 1
        while idx >= 0 and nums[idx] >= target:
            idx -= 1

        return idx + 1
