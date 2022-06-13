class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        len_nums = len(nums)
        sum_nums = sum(nums)
        left_sum = 0
        i = 0

        while i < len_nums:
            if left_sum == (sum_nums - left_sum - nums[i]):
                return i
            left_sum += nums[i]
            i += 1
        return -1