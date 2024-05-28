from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        idx = 0
        while len(tokens) != 1:
            if tokens[idx] in operators:
                if (
                    tokens[idx - 1] not in operators
                    and tokens[idx - 2] not in operators
                ):
                    if tokens[idx] == "+":
                        tokens[idx] = str(int(tokens[idx - 2]) + int(tokens[idx - 1]))
                    elif tokens[idx] == "-":
                        tokens[idx] = str(int(tokens[idx - 2]) - int(tokens[idx - 1]))
                    elif tokens[idx] == "*":
                        tokens[idx] = str(int(tokens[idx - 2]) * int(tokens[idx - 1]))
                    elif tokens[idx] == "/":
                        tokens[idx] = str(
                            int(int(tokens[idx - 2]) / int(tokens[idx - 1]))
                        )
                    tokens = tokens[: idx - 2] + tokens[idx:]
                    idx -= 2
            idx += 1
        return int(tokens[0])
