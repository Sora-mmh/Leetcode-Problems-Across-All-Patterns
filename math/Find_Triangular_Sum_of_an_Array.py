class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            new_nums = []
            for idx in range(1, len(nums)):
                new_nums.append((nums[idx - 1] + nums[idx]) % 10)
            return helper(new_nums)
        return helper(nums)
