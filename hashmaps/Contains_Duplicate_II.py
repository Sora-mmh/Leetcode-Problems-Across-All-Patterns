from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplication_distances = {}
        for idx in range(len(nums)):
            if (
                nums[idx] in duplication_distances
                and idx - duplication_distances[nums[idx]] <= k
            ):
                return True
            else:
                duplication_distances[nums[idx]] = idx
        return False
