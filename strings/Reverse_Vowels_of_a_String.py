class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_str = "aeiouAEIOU"
        vowels = [e for e in s if e in vowels_str]
        v = 0
        s_list = list(s)
        for idx in range(len(s_list) - 1, -1, -1):
            if s_list[idx] in vowels_str:
                s_list[idx] = vowels[v]
                v += 1
        return "".join(s_list)
