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

        intervals.sort(key=lambda x:x.start) #O(nlogn) - O(n)
        last_end = float('-inf')
        
        for interval in intervals: #O(n)
            
            if interval.start < last_end:
                return False
            last_end = interval.end
        return True





# 0------------30
#        15------------40
