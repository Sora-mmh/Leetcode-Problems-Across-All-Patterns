from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = 0
        for r in range(n):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1

        # Solution 2 : use also sliding window but with a list as a storage (TODO: last element case)
        # sequence = []
        # max_length, counter = 0, k
        # idx, n = 0, len(nums)

        # def get_first_zero_index(L):
        #     i = 0
        #     while i < n and L[i] != 0:
        #         i += 1
        #     return i

        # while idx < n - 1:
        #     # print("sequence", sequence, "counter", counter)
        #     if  nums[idx] == 1:
        #         sequence.append(nums[idx])
        #     if nums[idx] == 0:
        #         sequence.append(nums[idx])
        #         counter -= 1
        #     print("sequence after fulling", sequence)
        #     if counter <= 0:
        #         if nums[idx + 1] == 0:
        #             print("sequence when counter is full", sequence, "counter", counter)
        #             max_length = max(max_length, len(sequence))
        #             lz_idx = get_first_zero_index(sequence)
        #             sequence = sequence[lz_idx + 1:]
        #             counter = k - len([e for e in sequence if e == 0])
        #     idx += 1
        # return max_length
        
