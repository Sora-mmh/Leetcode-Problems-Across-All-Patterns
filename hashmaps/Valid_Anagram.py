class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_occ = {c: 0 for c in s}
            s_occ_baseline = s_occ.copy()
            for c_s, c_t in zip(s, t):
                s_occ[c_s] += 1
                if c_t not in s:
                    return False
                else:
                    s_occ[c_t] -= 1
            return s_occ == s_occ_baseline
