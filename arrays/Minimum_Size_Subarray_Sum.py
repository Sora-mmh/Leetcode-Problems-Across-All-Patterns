from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Solution 1
        if sum(nums) < target:
            return 0
        else:
            min_path = len(nums) + 1
            start = sub_idx = 0
            sub_sum = 0
            while sub_idx < len(nums):
                sub_sum += nums[sub_idx]
                while sub_sum >= target:
                    min_path = min(min_path, sub_idx - start + 1)
                    sub_sum -= nums[start]
                    start += 1
                sub_idx += 1
            return 0 if min_path == len(nums) + 1 else min_path

        # Solution 2
        # if sum(nums) < target:
        #     return 0
        # else:
        #     min_paths = []
        #     for idx in range(len(nums)):
        #         sub_idx, sub_sum = idx, 0
        #         while sub_sum < target and sub_idx < len(nums):
        #             sub_sum += nums[sub_idx]
        #             sub_idx += 1
        #         if sub_sum >= target:
        #                 min_paths.append(sub_idx - idx)                    
        #     return min(min_paths) 
        
