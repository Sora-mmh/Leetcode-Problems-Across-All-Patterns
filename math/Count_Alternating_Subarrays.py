class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1] * n
        for idx in range(1, n):
            if nums[idx] != nums[idx - 1]:
                count[idx] = count[idx - 1] + 1
        return sum(count)
