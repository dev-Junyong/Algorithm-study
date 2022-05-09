class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        miss = 0
        flag = 0

        for i in range(1, len(nums)+1):
            if i not in cnt:
                miss = i
            if cnt[i] == 2:
                flag = i
        return [flag, miss]