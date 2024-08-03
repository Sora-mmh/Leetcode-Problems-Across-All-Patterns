class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub_s = s[:k]
        vowels = "aeiou"
        length = max_length = len([c for c in sub_s if c in vowels])
        for idx in range(k, len(s)):
            if s[idx] in vowels and not sub_s[0] in vowels:
                length += 1
            elif s[idx] not in vowels and sub_s[0] in vowels:
                length -= 1
            sub_s = sub_s[1:] + s[idx]
            max_length = max(max_length, length)
        return max_length
