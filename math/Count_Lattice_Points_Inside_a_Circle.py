class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        global res
        res = set()
        def count_points_in_one_circle(circle):
            c_x, c_y, r = circle
            for x in range(c_x - r, c_x + r + 1):
                y_lim = int(sqrt(r**2  - (c_x - x)**2))
                for y in range(c_y - y_lim, c_y + y_lim + 1):
                    res.add((x, y))
        
        for circle in circles:
            count_points_in_one_circle(circle)
        return len(res)

            # pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            # c_x, c_y, r = circle
            # rs = [(c_x, c_y + r), (c_x, c_y - 1), (c_x + r, c_y), (c_x - r, c_y)]
            # q = deque([(c_x, c_y)])
            # res.add((c_x, c_y))
            # while q:
            #     print("queue", q)
            #     # print("set", res)
            #     pt = q.popleft()
            #     for idx, p in enumerate(pos):
            #         curr_x, curr_y = pt[0] + p[0], pt[1] + p[1]
            #         if ((curr_x - c_x)**2 + (curr_y - c_y)**2) ** .5 <= r and (curr_x, curr_y) not in res:
            #             q.append((curr_x, curr_y))
            #             res.add((curr_x, curr_y))
        
