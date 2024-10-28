class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        r_queue, d_queue = deque([]), deque([])
        for idx in range(len(senate)):
            if senate[idx] == "R":
                r_queue.append(idx)
            else:
                d_queue.append(idx)
        idx = len(senate)
        while r_queue and d_queue:
            first_r, first_d = r_queue.popleft(), d_queue.popleft()
            if first_r < first_d:
                r_queue.append(idx)
            else:
                d_queue.append(idx)
            idx += 1
        return "Radiant" if r_queue else "Dire"



        
