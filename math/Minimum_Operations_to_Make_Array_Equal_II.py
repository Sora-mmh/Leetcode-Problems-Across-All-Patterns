from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        else:
            steps = []
            for num1, num2 in zip(nums1, nums2):
                if abs(num1 - num2) % k == 0:
                    steps.append((num2 - num1) // k)   
                else:
                    return -1
                    
            if sum(steps) == 0:
                return sum([abs(s) for s in steps]) // 2
            else:
                return -1
        


