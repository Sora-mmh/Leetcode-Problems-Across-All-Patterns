class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        elif t in s or t == s:
            return t
        else:
            chars = []
            possible_windows = []
            unique = list(set(list(t)))
            for c in s:
                if c in t:
                    chars.append(c)
                print(chars, len(chars))
                if len(chars) == len(t) and unique in chars:
                    start_idx, end_idx = s.index(chars[0]), s.index(chars[-1])
                    new_window = s[start_idx : end_idx + 1]
                    print(start_idx, end_idx)
                    print("new window", new_window)
                    possible_windows.append(new_window)
                    chars = []
                    s = s[end_idx + 1 :]
            print("possible windows", possible_windows)
            if len(possible_windows) == 0:
                return ""
            sorted_windows = sorted(possible_windows, key=lambda x: len(x))
            print(sorted_windows)
            return sorted_windows[0]
