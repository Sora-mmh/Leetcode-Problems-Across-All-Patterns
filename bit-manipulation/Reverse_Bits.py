class Solution:
    def reverseBits(self, n: int) -> int:
        bits_to_str = "{0:b}".format(n)
        bits_len = 32
        if len(bits_to_str) < bits_len:
            diff = bits_len - len(bits_to_str)
            bits_to_str = "0" * diff + bits_to_str
        reversed_bits = "0b" + bits_to_str[::-1]
        return int(reversed_bits, 2)

        # Solution 2
        # reversed_bits = 0
        # for _ in range(bits_len):
        #     left_bit = n & 1
        #     n = n >> 1
        #     reversed_bits = reversed_bits << 1
        #     reversed_bits = reversed_bits | left_bit
        # return reversed_bits
