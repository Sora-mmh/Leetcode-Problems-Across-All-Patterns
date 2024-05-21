from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines, line = [], []
        counter = 0
        for idx, word in enumerate(words):
            if len(word) < maxWidth and counter + len(word) + 1 <= maxWidth:
                counter += len(word) + 1
                line.append(word)
            else:
                lines.append(line)
                line = [word]
                counter = len(word)
        lines.append(line)
        text = []
        for line in lines:
            new_line = line[0]
            num_words = len(line)
            allocated_spaces = []
            remained_spaces = maxWidth - len("".join(line))
            if remained_spaces % (num_words - 1) != 0:

                spaces_per_word = remained_spaces // (num_words - 1)
            print(remained_spaces)
        return lines
