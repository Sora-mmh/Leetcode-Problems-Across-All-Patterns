from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        idx, n = 0, len(nums)
        k, max_length = 0, 0
        for r in range(n):
            if nums[r] != 1:
                k += 1
            while k > 1:
                if nums[idx] == 0:
                    k -= 1
                idx += 1
            max_length = max(max_length, r - idx + 1 - k)
        return max_length - 1 if max_length == n else max_length
