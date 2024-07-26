from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        slow_idx, fast_idx = 0, 0
        occurences = []
        while fast_idx < len(chars):
            while fast_idx < len(chars) and chars[fast_idx] == chars[slow_idx]:
                fast_idx += 1
            occurences.append(fast_idx - slow_idx)
            slow_idx = fast_idx 

        counter = 0
        idx = 0
        while idx < len(chars) and counter < len(occurences):
            chars.append(chars[idx])
            if occurences[counter] > 1:
                chars.extend(list(str(occurences[counter])))
            idx += occurences[counter]
            counter += 1
        del chars[: n]
        return len(chars) 
            
