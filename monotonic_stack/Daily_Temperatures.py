from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = []
        n = len(temperatures)
        for idx in range(n - 1):
            sub_idx = idx + 1
            while sub_idx < n and temperatures[sub_idx] <= temperatures[idx]:
                sub_idx += 1
            if sub_idx == n and temperatures[sub_idx - 1] <= temperatures[idx]:
                answers.append(0)
            else:
                answers.append(sub_idx - idx)
        answers.append(0)
        return answers
