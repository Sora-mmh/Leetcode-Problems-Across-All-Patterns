class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        idx = 0
        for char in s:
            if char != "]":
                result.append(char)
            else:
                chars = ""
                while result[-1] != "[" and result[-1].isalpha():
                    chars = result.pop() + chars
                result.pop()
                num_str = ""
                while result and result[-1].isdigit():
                    num_str = result.pop() + num_str
                num = int(num_str)
                result.append(chars * num)
        return "".join(result)
            






        


                
            
        
