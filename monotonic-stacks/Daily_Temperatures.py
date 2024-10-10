from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        days = [0] * n
        for idx in range(n):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                current_t = stack.pop()
                days[current_t] = idx - current_t
            stack.append(idx)
        return days

