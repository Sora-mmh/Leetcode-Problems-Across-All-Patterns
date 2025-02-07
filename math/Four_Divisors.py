class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            divisors = set()
            for i in range(1, int(num ** (.5)) + 1):
                if num % i == 0:
                    divisors.add(num // i)
                    divisors.add(i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                out += sum(divisors)
        return out

