class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        idx, n = 0, len(s)
        if k == len(s):
            return 1
        else:
            count = 0
            while idx < n - k + 1:
                q = int(s[idx: idx + k])
                if q != 0 and num % q == 0:
                    count += 1
                idx += 1
            return count 
