from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_pic, second_pic = float("inf"), float("inf")
        for num in nums:
            if num > second_pic and second_pic > first_pic:
                return True
            if num > first_pic:
                second_pic = num
            else:
                first_pic = num 
        return False



        # idx = 1
        # stack = [nums[0]]
        # while idx < n:
        #     print("current start idx", idx, "stack", stack)
        #     if nums[idx] > stack[-1]:
        #         stack.append(nums[idx])
        #     if len(stack) == 2:
        #         if nums[idx] < stack[-1] and nums[idx] > stack[-2]:
        #             stack.pop()
        #             stack.append(nums[idx])
        #         if nums[idx] < stack[-1] and nums[idx] < stack[-2]:
        #             stack = [nums[idx]]
        #     if len(stack) == 3:
        #         return True
        #     idx += 1
        # return len(stack) == 3



        # current_num_idx = 0
        # while current_num_idx < n:
        #     pic_counter = 0
        #     last_pic = nums[current_num_idx]
        #     for idx in range(current_num_idx+1, n):
        #         # print("current start idx", current_num_idx, "pic_counter", pic_counter)
        #         if nums[idx] > last_pic:
        #             pic_counter += 1
        #             last_pic = nums[idx]
        #         if nums[idx] < last_pic and nums[idx] > nums[current_num_idx]:
        #             last_pic = nums[idx]
        #         if pic_counter == 2:
        #             return True
        #     current_num_idx += 1
        # return True if pic_counter == 2 else False
            
