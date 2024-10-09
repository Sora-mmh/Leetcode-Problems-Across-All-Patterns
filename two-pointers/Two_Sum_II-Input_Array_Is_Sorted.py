from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ### Solution 1
        left = 0
        found = False
        while left < len(numbers) - 1 and not found:
            if (target - numbers[left]) in numbers[left + 1 :]:
                found = True
                lost_idx = left + 1
                while numbers[lost_idx] != target - numbers[left]:
                    lost_idx += 1
                return [left + 1, lost_idx + 1]
            else:
                left += 1

        ### Solution 2

        # left, right = 0, len(numbers) - 1
        # while left < right :
        #     computed = numbers[right] + numbers[left]
        #     if computed == target:
        #         return [left + 1, right + 1]
        #     elif computed > target:
        #         right -= 1
        #     else:
        #         left += 1
