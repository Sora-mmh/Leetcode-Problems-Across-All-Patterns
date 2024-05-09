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


# class Solution:
# def minWindow(self, s: str, t: str) -> str:
#     m, n = len(s), len(t)
#     if n > m:
#         return ""
#     elif t in s or t == s:
#         return t
#     else:
#         chars = []
#         possible_windows = []
#         unique = list(set(list(t)))
#         for c in s:
#             if c in t:
#                 chars.append(c)
#             print(chars, len(chars))
#             if len(chars) == len(t) and unique in chars:
#                 start_idx, end_idx = s.index(chars[0]), s.index(chars[-1])
#                 new_window = s[start_idx : end_idx + 1]
#                 print(start_idx, end_idx)
#                 print("new window", new_window)
#                 possible_windows.append(new_window)
#                 chars = []
#                 s = s[end_idx + 1 :]
#         print("possible windows", possible_windows)
#         if len(possible_windows) == 0:
#             return ""
#         sorted_windows = sorted(possible_windows, key=lambda x: len(x))
#         print(sorted_windows)
#         return sorted_windows[0]


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         m, n = len(s), len(t)
#         if n > m:
#             return ""
#         elif t in s or t == s:
#             return t
#         else:
#             chars = []
#             possible_windows = []
#             t_count = n
#             occurence_map = {c: 0 for c in list(set(t))}
#             for c in t:
#                 occurence_map[c] += 1
#             backup_occurence_map = occurence_map.copy()
#             chars = []
#             print(occurence_map)
#             start_idx, idx = 0, 0
#             chars, possible_windows = [], []
#             while start_idx < m:
#                 print(start_idx, idx)
#                 while idx < m and t_count != 0:
#                     if s[idx] in t:
#                         occurence_map[s[idx]] -= 1
#                         t_count -= 1
#                         chars.append(s[idx])
#                     if s[idx] in t and occurence_map[s[idx]] < 0:
#                         occurence_map[s[idx]] += 1
#                         t_count += 1
#                     idx += 1
#                 if t_count == 0 and sum(occurence_map.values()) == 0:
#                     print("here", occurence_map)
#                     print(s[start_idx : idx + 1])
#                     possible_windows.append(s[start_idx : idx + 1])
#                     chars = []
#                     t_count = n
#                     start_idx += 1
#                     idx = start_idx
#                     occurence_map = backup_occurence_map

#             print(possible_windows)
#             if len(possible_windows) != 0:
#                 possible_windows = sorted(possible_windows, key=lambda x: len(x))
#                 return possible_windows[0]
#             else:
#                 return ""

# for idx,c in enumerate(s):
#     if c in t :
#         if len(chars) == 0:
#             start_idx = idx
#         chars.append(c)
#         occurence_map[c] -= 1
#         t_count -= 1
#     if c in t and occurence_map[c] < 0:
#         print("occurence 0,",c, occurence_map)
#         start_idx += 1
#         t_count += 1
#         occurence_map[c] += 1
#     print(occurence_map)
#     if t_count == 0:
#         end_idx = idx
#         possible_windows.append(s[start_idx : end_idx + 1])
#         occurence_map = backup_occurence_map
#         chars = []
#         t_count = n
# print(possible_windows)
# if len(possible_windows) != 0:
#     possible_windows = sorted(possible_windows, key = lambda x : len(x))
#     return possible_windows[0]
# else:
#     return ""
