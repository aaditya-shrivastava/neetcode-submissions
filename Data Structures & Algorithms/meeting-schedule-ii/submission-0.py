"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        rooms = e = 0
        for s in start:
            if s < end[e]:
                rooms += 1
            else:
                e += 1
        return rooms