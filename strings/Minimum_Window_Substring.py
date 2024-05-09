class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        elif t in s or t == s:
            return t
        else:
            min_length = m * n
            sub_window = ""
            occurence_map = {c: 0 for c in list(set(t))}
            for c in t:
                occurence_map[c] += 1
            backup_occurence_map = occurence_map.copy()
            chars = []
            start_idx = 0
            while start_idx < m:
                t_count = n
                occurence_map = backup_occurence_map.copy()
                chars = []
                idx = start_idx
                while idx < m:
                    if s[idx] in t:
                        if len(chars) == 0:
                            sub_start_idx = idx
                        occurence_map[s[idx]] -= 1
                        t_count -= 1
                        chars.append(s[idx])
                        if occurence_map[s[idx]] < 0:
                            occurence_map[s[idx]] += 1
                            t_count += 1
                    if t_count == 0:
                        if (idx + 1 - sub_start_idx) < min_length:
                            sub_window = s[sub_start_idx : idx + 1]
                            min_length = idx + 1 - sub_start_idx
                        t_count = n
                        occurence_map = backup_occurence_map.copy()
                        chars = []
                    idx += 1
                start_idx += 1
            return sub_window
