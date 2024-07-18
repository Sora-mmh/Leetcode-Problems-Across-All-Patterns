from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        # Solution2
        def check_anagram(str1: str, str2: str):
            return Counter(str1) == Counter(str2)

        results = []
        idx = 0
        while idx < len(strs) or len(strs) != 0:
            str1 = strs[idx]
            anagrams = [str1]
            strs = strs[idx + 1 :]
            for idx2, str2 in enumerate(strs):
                if check_anagram(str1, str2):
                    anagrams.append(str2)
            for str2 in anagrams[1:]:
                strs.remove(str2)
            results.append(anagrams)
        return results
