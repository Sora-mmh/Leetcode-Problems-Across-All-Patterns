from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        result = 0
        for idx in range(n):
            tank += gas[idx] - cost[idx]
            if tank < 0:
                tank = 0
                result = idx + 1
        return result

        # for idx1 in range(n):
        #     if gas[idx1] != 0:
        #         tank = gas[idx1]
        #         result = idx1
        #         idx2 = idx1 + 1  if idx1 + 1 < n else n - 1 - idx1
        #         while tank >=  cost[idx2 - 1] and idx2 != idx1:
        #             tank +=  gas[idx2] - cost[idx2 - 1]
        #             idx2 += 1
        #             if idx2 >= n:
        #                 idx2 -= n
        #         if idx2 == idx1 and tank >= cost[idx2 - 1]:
        #             return idx1
        # return -1
