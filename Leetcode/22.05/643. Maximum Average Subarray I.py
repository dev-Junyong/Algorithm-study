class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        temp = -21e8
        for i, num in enumerate(nums):
            res += num
            if i >= k:
                res -= nums[i - k]
            if i >= k - 1:
                temp = max(temp, res)
        
        return temp / k