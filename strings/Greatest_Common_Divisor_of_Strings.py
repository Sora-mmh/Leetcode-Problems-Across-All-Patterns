class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

        # Solution 2
        # history = [str1, str2] if len(str1) > len(str2) else [str2, str1]
        # substracted = history[-2].replace(history[-1], "")
        # history.append(substracted)
        # while history[-1] != "" and history[-3] != history[-1]:
        #     substracted = history[-2].replace(history[-1], "")
        #     history.append(substracted)
        # return history[-2] if history[-1] == "" else return ""
            


        
