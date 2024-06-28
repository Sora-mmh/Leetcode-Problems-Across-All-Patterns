from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            sorted_array = sorted(nums)
            idx = 1
            interruptions = []
            consec = 1
            while idx < len(sorted_array):
                if sorted_array[idx] - sorted_array[idx - 1] in [0, 1]:
                    if sorted_array[idx] - sorted_array[idx - 1] == 1:
                        consec += 1
                else:
                    interruptions.append(consec)
                    consec = 1
                idx += 1
            interruptions.append(consec)
            return max(interruptions)
