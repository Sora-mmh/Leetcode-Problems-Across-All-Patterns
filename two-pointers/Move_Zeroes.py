from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros_counter = len([e for e in nums if e == 0])
        idx, counter = 0, 0
        while idx < len(nums) and counter != zeros_counter:
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                counter += 1
            else:
                idx += 1
