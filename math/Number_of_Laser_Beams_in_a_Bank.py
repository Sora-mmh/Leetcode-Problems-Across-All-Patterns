class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        beams = 0
        if m == 1:
            return beams
        else:
            cameras_per_row = [sum(map(int, list(bank[idx]))) for idx in range(m)]
            filtered = [cameras for cameras in cameras_per_row if cameras != 0]
            for idx in range(len(filtered) - 1):
                beams += filtered[idx] * filtered [idx + 1]
        return beams
            
