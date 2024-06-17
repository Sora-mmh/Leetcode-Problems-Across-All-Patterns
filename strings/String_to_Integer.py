class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print("after deleting white spaces", s)
        if s[0] == "-":
            negative = True
            s = s[1:]
        else:
            negative = False
        print("if negative ", negative)
        idx = 0
        while s[0] == "0":
            s = s[idx + 1 :]
            idx += 1
        print("after deleting zeros", s)
        idx = 0
        while idx < len(s):
            if 48 <= ord(s[idx]) <= 57:
                idx += 1
            else:
                break
        s = s[:idx]
        print("after deleting non digits", s)
        if negative:
            s = "-" + s
        print(s)
        if int(s) > 2**31 - 1:
            return 2**31 - 1
        elif int(s) < -(2**31):
            return -(2**31)
        else:
            return int(s)
