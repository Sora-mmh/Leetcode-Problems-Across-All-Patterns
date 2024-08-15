class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        else:
            from collections import Counter

            chars_occ_dict1 = Counter(word1)
            chars_occ_dict2 = Counter(word2)
            chars1 = list(chars_occ_dict1.keys())
            chars2 = list(chars_occ_dict2.keys())
            occ1 = list(chars_occ_dict1.values())
            occ2 = list(chars_occ_dict2.values())
            if sorted(chars1) == sorted(chars2):
                return sorted(occ1) == sorted(occ2)
