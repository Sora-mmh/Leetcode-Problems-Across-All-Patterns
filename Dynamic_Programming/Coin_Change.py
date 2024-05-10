class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        iterator = [amount + 1] * (amount + 1)
        iterator[0] = 0
        for e in range(1, amount + 1):
            for c in coins:
                if e - c >= 0:
                    iterator[e] = min(iterator[e], 1 + iterator[e - c])
        return iterator[amount] if iterator[amount] != amount + 1 else -1
