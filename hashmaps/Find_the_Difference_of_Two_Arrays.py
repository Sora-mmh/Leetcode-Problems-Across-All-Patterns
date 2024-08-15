from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set(nums1) - set(
            nums2
        )  # ans1 = set([e for e in nums1 if e not in nums2])
        ans2 = set(nums2) - set(
            nums1
        )  # ans2 = set([e for e in nums2 if e not in nums1])
        return [list(ans1), list(ans2)]
