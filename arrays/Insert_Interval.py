from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        import numpy as np

        def overlap(interval1, interval2):
            start1, end1 = interval1
            start2, end2 = interval2
            if end1 < end2:
                return end1 >= start2
            elif end1 > end2:
                return end2 >= start1
            elif end1 == end2 or start1 == start2:
                return True

        ####### Solution 1 #######
        newElstart, newElend = newInterval
        idx = 0
        insert = False
        new_intervals = []
        while idx < len(intervals):
            if not overlap(intervals[idx], newInterval):
                new_intervals.append(intervals[idx])
                print("st", new_intervals)
                idx += 1
            else:
                new_start = min(newInterval[0], intervals[idx][0])
                new_end = max(newInterval[1], intervals[idx][1])
                if len(new_intervals) != 0 and new_start in new_intervals[-1]:
                    new_intervals.pop()
                new_intervals.append([new_start, new_end])
                newInterval = [new_start, new_end]
                insert = True
                idx += 1
        if not insert or len(intervals) == 0:
            new_intervals.append(newInterval)
        return sorted(new_intervals)

        ####### Solution 2 #######
        if len(intervals) == 0:
            return [newInterval]
        else:
            newElstart, _ = newInterval
            new_intervals = []
            overlappings = [overlap(e, newInterval) for e in intervals]
            overlapping_indices = [
                idx for idx, overlapping in enumerate(overlappings) if overlapping
            ]
            non_overlapping_indices = [
                idx for idx, overlapping in enumerate(overlappings) if not overlapping
            ]
            if len(non_overlapping_indices) == len(intervals):
                for idx in non_overlapping_indices:
                    if newElstart < intervals[idx][1]:
                        intervals.insert(idx, newInterval)
                        return intervals
                intervals.append(newInterval)
                return intervals
            else:
                overlapping_intervals = [intervals[idx] for idx in overlapping_indices]
                overlapping_intervals.append(newInterval)
                overlapping_intervals = np.array(overlapping_intervals)
                new_start_per_interval = np.min(overlapping_intervals.flatten())
                new_end_per_interval = np.max(overlapping_intervals.flatten())
                for idx, e in enumerate(intervals):
                    if idx in non_overlapping_indices:
                        new_intervals.append(e)
                new_intervals.insert(
                    overlapping_indices[0],
                    [new_start_per_interval, new_end_per_interval],
                )
                return new_intervals
