from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        dp = [True] + [False] * m
        for idx in range(1, m + 1):
            for word in wordDict:
                start = idx - len(word)
                if start >= 0 and dp[start] and s[start:idx] == word:
                    dp[idx] = True
                    break
        return dp[-1]
