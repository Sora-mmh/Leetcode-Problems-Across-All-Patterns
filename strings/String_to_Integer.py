class Solution:
    def myAtoi(self, s: str) -> int:

        digits, operators = "0123456789", "-+"
        ops = {"-": -1, "+": 1}
        encountred = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == " " and len(encountred) == 0:
                s_list[i] = ""
            elif s_list[i] == " " and len(encountred) != 0:
                s_list = s_list[:i]
                break
            elif s_list[i] != " ":
                encountred.append(s_list[i])
        s = "".join(s_list)

        if len(s) == 0:
            return 0
        else:
            if s[0] not in digits and s[0] not in operators:
                return 0

            digits_before_ops = []
            for i in range(len(s)):
                if s[i] in digits:
                    digits_before_ops.append(s[i])
                if (s[i] not in digits and s[i] not in operators) or (
                    s[i] in operators and len(digits_before_ops) != 0
                ):
                    s = s[:i]
                    break

            if len(digits_before_ops) == 0:
                return 0
            else:
                extracted_ops = [c for c in s if c in operators]
                result = int("".join([c for c in s if c in digits]))
                if len(extracted_ops) != 0:
                    if len(extracted_ops) != 1:
                        return 0
                    else:
                        result *= ops[extracted_ops[0]]
                result = max(-(2**31), result)
                result = min(result, 2**31 - 1)
                return result
