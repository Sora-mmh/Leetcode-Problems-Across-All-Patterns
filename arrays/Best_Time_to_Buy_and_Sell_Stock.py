from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price, max_profit = float("inf"), 0
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            elif price - lowest_price > max_profit:
                max_profit = price - lowest_price
        return max_profit

        # best_day = [0, 0]
        # for d in range(len(prices)):
        #     for f in range(d + 1, len(prices)):
        #         if prices[f] > prices[d]:
        #             v = prices[f] - prices[d]
        #             if v > best_day[1]:
        #                 best_day[1] = v
        #                 best_day[0] = f
        # return best_day[1]
