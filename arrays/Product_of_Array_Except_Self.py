class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = [1] * len(nums)
        right_mul = [1] * len(nums)
        for idx in range(1, len(nums)):
            left_mul[idx] *= left_mul[idx - 1] * nums[idx - 1]
        for idx in range(len(nums) - 2, -1, -1):
            right_mul[idx] *= right_mul[idx + 1] * nums[idx + 1]
        return [left * right for left, right in zip(left_mul, right_mul)]
        

