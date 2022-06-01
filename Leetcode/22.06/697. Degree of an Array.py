class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        idx = {}
        for i, num in enumerate(nums):
            if num in idx:
                idx[num].append(i)
                if degree < len(idx[num]):
                    degree = len(idx[num]) 
            else:
                idx[num] = [i]
                if degree < len(idx[num]):
                    degree = len(idx[num]) 
        max_len = 21e8
        for i, item in enumerate(idx):
            if len(idx[item]) != degree:
                continue
            else:
                if idx[item][-1] - idx[item][0] + 1 < max_len:
                    max_len = idx[item][-1] - idx[item][0] + 1
        return max_len