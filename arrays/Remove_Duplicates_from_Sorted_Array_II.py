from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        repl = 1
        counter = 1
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                counter += 1
            else:
                counter = 1
            if counter <= 2:
                nums[repl] = nums[idx]
                repl += 1
        return repl



        
