class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        max_x1 = max(ax1, bx1)
        max_y1 = max(ay1, by1)
        min_x2 = min(ax2, bx2)
        min_y2 = min(ay2, by2)
        overlap = (min_x2 - max_x1) * (min_y2 - max_y1) if min_x2 - max_x1 > 0 and min_y2 - max_y1 > 0 else 0
        return area - overlap
            


