class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        all_num = set(range(1, len_nums + 1))

        for num in nums:
            if num in all_num:
                all_num.remove(num)

        return list(all_num)