class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_occ = {c: 0 for c in ransomNote}
        magazine_occ = {c: 0 for c in magazine}
        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                ransomNote_occ[c] += 1
        for c in magazine:
            magazine_occ[c] += 1
        idx = 0
        while (
            idx < len(ransomNote)
            and ransomNote_occ[ransomNote[idx]] <= magazine_occ[ransomNote[idx]]
        ):
            idx += 1
        if idx == len(ransomNote):
            return True
        else:
            return False
