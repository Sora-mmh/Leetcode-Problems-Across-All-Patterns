from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plots_counter = 0
        if len(flowerbed) == 1:
            plots_counter = 1 if flowerbed[0] == 0 else 0
        else:
            if flowerbed[0] == flowerbed[1] == 0:
                flowerbed[0] = 1
                plots_counter += 1
            if flowerbed[-2] == flowerbed[-1]:
                flowerbed[-1] = 1
                plots_counter += 1
            for plot in range(1, len(flowerbed) - 1):
                if flowerbed[plot] == flowerbed[plot - 1] == flowerbed[plot + 1] == 0:
                    flowerbed[plot] = 1
                    plots_counter += 1
        return n <= plots_counter
