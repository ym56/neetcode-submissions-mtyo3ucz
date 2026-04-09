"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedByStartTime = sorted(intervals, key=lambda i: i.start)
        print(sortedByStartTime)
        prevEndTime = -1
        for time in sortedByStartTime:
            if (prevEndTime > time.start):
                return False
            prevEndTime = time.end
        return True