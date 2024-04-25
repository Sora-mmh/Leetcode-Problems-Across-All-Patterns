class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        else:
            left, right = 0, len(s) - 1
            max_len = 0
            sub_string = ""
            while left < len(s):
                if s[left] not in sub_string:
                    sub_string += s[left]
                    print(sub_string)
                    max_len = len(sub_string)
                else:
                    if max_len < len(sub_string):
                        max_len = len(sub_string)
                    sub_string = s[left]
                left += 1
            return max_len
