class Solution:
    def isValid(self, s: str) -> bool:
        chars = [s[0]]
        for c in s[1:]:
            chars.append(c)
            if len(chars) >= 2:
                if (
                    chars[-1] == ")"
                    and chars[-2] == "("
                    or chars[-1] == "}"
                    and chars[-2] == "{"
                    or chars[-1] == "]"
                    and chars[-2] == "["
                ):
                    chars = chars[:-2]
        return len(chars) == 0
