class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        set_nums = set(nums)
        long = 0
        for num in set_nums:
            if num + 1 in counter:
                long = max(long, counter[num] + counter[num + 1])
        return long