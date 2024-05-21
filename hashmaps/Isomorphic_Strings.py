class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def get_chars_idx_and_order(s: str):
            s_chars_positions = {c: [] for c in s}
            for idx, c in enumerate(s):
                s_chars_positions[c].append(idx)
            return s_chars_positions

        s_chars_positions = get_chars_idx_and_order(s)
        t_chars_positions = get_chars_idx_and_order(t)
        return list(s_chars_positions.values()) == list(t_chars_positions.values())
