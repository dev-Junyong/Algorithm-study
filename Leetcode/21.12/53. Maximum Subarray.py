class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarr = max_subarr = nums[0]
        for num in nums[1:]:
            subarr = max(num, subarr + num)
            max_subarr = max(max_subarr, subarr)
        
        return max_subarr