from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) >= 2:
            idx = 1
            while idx < len(nums):
                if (
                    nums[idx] == nums[idx - 1]
                    and isinstance(nums[idx], int)
                    and (isinstance(nums[idx - 1], int))
                ):
                    nums.pop(idx)
                    nums.append("_")
                else:
                    idx += 1
            return len([num for num in nums if num != "_"])
        else:
            return len(nums)
