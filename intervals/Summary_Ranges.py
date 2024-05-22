from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) != 0:
            range_idx = [nums[0]]
            for idx in range(len(nums) - 1):
                if nums[idx + 1] - nums[idx] == 1:
                    range_idx.append(nums[idx + 1])
                else:
                    ranges.append(range_idx)
                    range_idx = [nums[idx + 1]]
            ranges.append(range_idx)
            for idx in range(len(ranges)):
                if len(ranges[idx]) == 1:
                    range_idx = str(ranges[idx][0])
                    ranges[idx] = range_idx
                else:
                    ranges[idx] = str(ranges[idx][0]) + "->" + str(ranges[idx][-1])
        return ranges
