class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a
        a, b = a[::-1], b[::-1]

        def add_with_carry(a, b, r="0"):
            if len(a) == 0:
                if r == "1":
                    return r
                else:
                    return ""

            elif len(a) == 1:
                if a[0] == "0" == b[0]:
                    if r == "0":
                        return "0"
                    else:
                        return r
                elif a[0] == "0" and b[0] == "1" or a[0] == "1" and b[0] == "0":
                    if r == "0":
                        return "1"
                    else:
                        return "10"
                elif a[0] == "1" == b[0]:
                    if r == "0":
                        return "10"
                    else:
                        return "11"

            elif len(a) > 1:
                if a[0] == "0" == b[0]:
                    if r == "0":
                        return add_with_carry(a[1:], b[1:]) + "0"
                    elif r == "1":
                        return add_with_carry(a[1:], b[1:]) + "1"
                elif a[0] == "0" and b[0] == "1" or a[0] == "1" and b[0] == "0":
                    if r == "0":
                        return add_with_carry(a[1:], b[1:]) + "1"
                    elif r == "1":
                        return add_with_carry(a[1:], b[1:], r="1") + "0"
                elif a[0] == "1" == b[0]:
                    if r == "0":
                        return add_with_carry(a[1:], b[1:], r="1") + "0"
                    elif r == "1":
                        return add_with_carry(a[1:], b[1:], r="1") + "1"

        return add_with_carry(a, b)
