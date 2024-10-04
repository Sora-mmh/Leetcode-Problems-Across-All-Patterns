from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def get_combinations(start, combination, s):
            if s == n and len(combination) == k:
                results.append(combination)
            for num in range(start, 10):
                if s + num <= n:
                    get_combinations(num+1, combination + [num], s + num)   
        get_combinations(1, [], 0)
        return results


        
