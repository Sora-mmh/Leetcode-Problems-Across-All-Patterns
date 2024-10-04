from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits != "":
            digits_chars = {
                "2": "abc", 
                "3": "def", 
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
                }
            results = []
            def get_combinations(result, digits):
                if len(digits) == 0:
                    results.append(result)
                else:
                    for c in digits_chars[digits[0]]:
                        get_combinations(result + c, digits[1:])
            
            get_combinations("", digits)
            return results
        else:
            return []

