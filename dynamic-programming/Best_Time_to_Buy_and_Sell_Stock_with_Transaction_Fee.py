from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = - prices[0], 0
        for idx in range(1, len(prices)):
            buy = max(buy, sell - prices[idx])
            sell = max(sell, buy + prices[idx] - fee)
        return sell
