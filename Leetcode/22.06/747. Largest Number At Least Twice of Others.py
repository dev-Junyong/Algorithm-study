class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        temp_lst = []
        for num in nums:
            if max_num / 2 < num:
                temp_lst.append(num)
        
        if len(temp_lst) == 1:
            return nums.index(temp_lst[0])
        else:
            return -1