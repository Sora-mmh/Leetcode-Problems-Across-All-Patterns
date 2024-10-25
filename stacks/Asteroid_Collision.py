from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = [asteroids[0]]
        idx, n = 1, len(asteroids)
        for idx in range(1, n):
            result.append(asteroids[idx])
            while len(result) >= 2 and result[-1] * result[-2] < 0 and result[-1] < result[-2]:
                if abs(result[-1]) > abs(result[-2]):
                    result.pop(-2)
                elif abs(result[-1]) < abs(result[-2]):
                    result.pop()
                else:
                    result.pop()
                    result.pop()         
        return result

        
