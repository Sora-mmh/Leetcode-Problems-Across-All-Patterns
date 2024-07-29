class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = s.split()[::-1]
        return " ".join(reversed_words)
