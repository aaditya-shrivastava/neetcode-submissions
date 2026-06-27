class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        end = intervals[0][1]
        for s, e in intervals[1:]:
            if s < end:
                ans += 1
                end = min(end, e)
            else:
                end = e
        return ans