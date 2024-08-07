from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid + 1] < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
