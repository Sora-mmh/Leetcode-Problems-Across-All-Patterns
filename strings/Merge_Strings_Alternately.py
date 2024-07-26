class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        for idx in range(min(len(word1),len(word2))):
            merged_word += word1[idx] + word2[idx]
        if len(word1) > len(word2):
            merged_word += word1[len(word2):]
        if len(word1) < len(word2):
            merged_word += word2[len(word1):]
        return merged_word
