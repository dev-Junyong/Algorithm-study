class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        if len(set_nums) < 3:
            return max(set_nums)
        return sorted(set_nums)[-3]