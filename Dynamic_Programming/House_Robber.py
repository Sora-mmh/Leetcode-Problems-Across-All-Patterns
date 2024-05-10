class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        iterator = [0] * n
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        else:
            iterator[0] = nums[0]
            iterator[1] = max(nums[0], nums[1])
            for idx in range(2, n):
                iterator[idx] = max(nums[idx] + iterator[idx - 2], iterator[idx - 1])
            return iterator[-1]

