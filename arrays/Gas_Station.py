from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # differences = [gas[i] - cost[i] for i in range(n)]
        # differences = [i for i,difference in enumerate(differences) if difference >= 0]
        # gas = [gas[i] for i in differences]
        # cost = [cost[i] for i in differences]
        # n = len(gas)
        for idx1 in range(n):
            if gas[idx1] != 0:
                tank = gas[idx1]
                result = idx1
                idx2 = idx1 + 1 if idx1 + 1 < n else n - 1 - idx1
                # print(f"for idx1={idx1}, idx2 starts at {idx2}")
                # print("current tank", tank)
                while tank >= cost[idx2 - 1] and idx2 != idx1:
                    # print("update the tank", tank, cost[idx2 - 1], gas[idx2])
                    tank += gas[idx2] - cost[idx2 - 1]
                    idx2 += 1
                    if idx2 >= n:
                        idx2 -= n
                    # print("tank", tank)
                    # print("next idx2", idx2)
                # print("out of while loop", idx1, idx2)
                # print("tank", tank, cost[idx2 - 1])
                if idx2 == idx1 and tank >= cost[idx2 - 1]:
                    return idx1
        return -1
