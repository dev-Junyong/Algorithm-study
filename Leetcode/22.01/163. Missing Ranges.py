class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        
        prev = lower - 1
        for i in range(len(nums) + 1):
            if i == len(nums):
                now = upper + 1
            else:
                now = nums[i]
            if now - prev > 2:
                res.append(f'{prev+1}->{now-1}')
            elif now - prev == 2:
                res.append(f'{prev+1}')
            prev = now
        return res