"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

            
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            m1 = intervals[i - 1]
            m2 = intervals[i]

            if m2.start < m1.end:
                return False
        
        return True
