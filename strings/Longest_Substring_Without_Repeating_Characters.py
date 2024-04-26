class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        else:
            end = 0
            max_len = 0
            characters = []
            while end < len(s):
                if s[end] in characters:
                    if max_len < len(characters):
                        max_len = len(characters)
                    if s[end] == s[end - 1]:
                        characters = []
                    else:
                        idx = characters.index(s[end])
                        characters = characters[idx + 1 :]
                characters.append(s[end])
                end += 1
            return max(max_len, len(characters))
