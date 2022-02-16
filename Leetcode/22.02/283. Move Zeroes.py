class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        flag = 0
        while flag < len_nums:
            if nums[flag] == 0:
                nums.append(nums.pop(flag))
                len_nums -= 1
            else:
                flag += 1