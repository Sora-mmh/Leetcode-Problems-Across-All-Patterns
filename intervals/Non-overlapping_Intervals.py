from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        def overlap(a, b):
            return a[0] <= b[0] < a[1] or b[0] <= a[0] < b[1]

        intervals.sort(key=lambda e: e[1])
        non_overlapped_intervals = []
        for interval in intervals:
            if interval not in non_overlapped_intervals:
                non_overlapped_intervals.append(interval)
            if len(non_overlapped_intervals[:-1]) != 0:
                check_overlapping = [
                    overlap(interval, non_overlapped_interval)
                    for non_overlapped_interval in non_overlapped_intervals[:-1]
                ]
                if any(check_overlapping):
                    non_overlapped_intervals.pop()

        return len(intervals) - len(non_overlapped_intervals)
