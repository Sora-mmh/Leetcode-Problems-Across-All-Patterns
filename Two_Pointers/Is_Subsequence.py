class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0 and len(s) != 0:
            return False
        if len(s) == 0:
            return True
        idx, counter = 0, 0
        while idx < len(t):
            if counter >= len(s):
                break
            if t[idx] == s[counter]:
                counter += 1
            idx += 1
        if counter != len(s):
            return False
        else:
            return True
