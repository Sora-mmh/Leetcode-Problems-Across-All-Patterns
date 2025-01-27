from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x, y = 1, z	
        # for x in range(1, z+1):
        #     for y in range(1, z+1):
        #         if customfunction.f(x, y) == z:
        #             res.append([x, y])
        while x <= z and y > 0:
            z1 = customfunction.f(x,y)
            if z1 == z:
                res.append([x,y])
                x += 1
                y -= 1
            elif z1 > z:
                y -= 1
            else:
                x += 1
        return res
