class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        len_time = len(timeSeries)
        if len_time == 0:
            return 0
        if len_time == 1:
            return duration
        temp_sum = 0
        for i in range(len_time - 1):
            temp_sum += min(duration, timeSeries[i+1] - timeSeries[i])
        return temp_sum + duration