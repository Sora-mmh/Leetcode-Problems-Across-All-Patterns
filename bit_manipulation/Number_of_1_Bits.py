class Solution:
    def hammingWeight(self, n: int) -> int:
        bits_to_str = "{0:b}".format(n)
        return len([bit for bit in list(bits_to_str) if bit == "1"])

        # Solution 2
        # counter = 0
        # while n:
        #     if n & 1:
        #         counter += 1
        #     n = n >> 1
        # return counter
