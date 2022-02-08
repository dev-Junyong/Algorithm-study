class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda interval:interval[0])
        
        prev = None
        
        for i in intervals:
            if prev and i[0] < prev[1]:
                return False
            prev = i
        return True