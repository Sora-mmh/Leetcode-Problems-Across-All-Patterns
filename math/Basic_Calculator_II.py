class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        last_op = '+'
        for i in range(len(s) + 1):
            c = s[i] if i < len(s) else '\0'
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s):
                if last_op == '+':
                    stack.append(num)
                if last_op == '-':
                    stack.append(-num)
                if last_op == '*':
                    stack.append(stack.pop() * num)
                if last_op == '/':
                    stack.append(int(stack.pop() / num))
                last_op = c
                num = 0
        return sum(stack)


        # def do_one_operation(c1, op, c2):
        #     if op == "+":
        #         return str(int(c1) + int(c2))
        #     elif op == "-":
        #         return str(int(c1) - int(c2))
        #     elif op == "/":
        #         return str(int(c1) // int(c2))
        #     elif op == "*":
        #         return str(int(c1) * int(c2))

        # def calculate_one_item(ss):
        #     items = list(ss)
        #     while len(items) != 1:
        #         if "/" in items:
        #             div_idx = items.index("/")
        #             res = do_one_operation(items[div_idx - 1], "/", items[div_idx + 1])
        #             items[div_idx - 1: div_idx + 2] = [res]
        #         elif "*" in items:
        #             mul_idx = items.index("*")
        #             res = do_one_operation(items[mul_idx - 1], "*", items[mul_idx + 1])
        #             items[mul_idx - 1: mul_idx + 2] = [res]
        #         elif "+" in items:
        #             sum_idx = items.index("+")
        #             res = do_one_operation(items[sum_idx - 1], "+", items[sum_idx + 1])
        #             items[sum_idx - 1: sum_idx + 2] = [res]
        #         elif "-" in items:
        #             sub_idx = items.index("-")
        #             res = do_one_operation(items[sub_idx - 1], "-", items[sub_idx + 1])
        #             items[sub_idx - 1: sub_idx + 2] = [res]
        #     return "".join(items)

        # s = s.replace(" ", "")
        # if s.isdigit():
        #     return int(s)
        # else:
        #     ss = list(s) 
        #     print("ss", ss)
        #     x = int(calculate_one_item(ss))
        #     print("res", x)
        #     return min(max(x, -2 ** 31), 2 ** 31 - 1)
        
