class Solution:
    def reverse(self, x: int) -> int:
        nums_list = list(str(x))
        if x >= 0:
            reversed_nums_list = nums_list[::-1]
        elif x < 0:
            nums_list = nums_list[1:]
            reversed_nums_list = ["-"] + nums_list[::-1]
        reversed_nums = int("".join(reversed_nums_list))
        if -(2**31) <= reversed_nums <= 2**31 - 1:
            return reversed_nums
        else:
            return 0
