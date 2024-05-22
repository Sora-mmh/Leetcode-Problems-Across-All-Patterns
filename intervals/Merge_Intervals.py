from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        non_overlapping_intervals = [intervals[0]]
        for idx in range(1, len(intervals)):
            interval = intervals[idx]
            if intervals[idx][0] > non_overlapping_intervals[-1][-1]:
                non_overlapping_intervals.append(intervals[idx])
            else:
                if intervals[idx][-1] < non_overlapping_intervals[-1][0]:
                    non_overlapping_intervals.append(intervals[idx])
                else:
                    new_min_interval, new_max_interval = min(
                        intervals[idx][0], non_overlapping_intervals[-1][0]
                    ), max(intervals[idx][-1], non_overlapping_intervals[-1][-1])
                    non_overlapping_intervals.pop()
                    non_overlapping_intervals.append(
                        [new_min_interval, new_max_interval]
                    )
        return non_overlapping_intervals
