class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        if len(nums) < 2:
            return [str(nums[0])]
        s, e = 0, 1
        while e < len(nums):
            if nums[e] - nums[s] > 1:
                res.append(str(nums[s]))
                s += 1
                e += 1
            else:
                start = s
                while e+1 < len(nums) and nums[e+1] - nums[e] == 1:
                    e += 1
                res.append('{}->{}'.format(nums[start], nums[e]))
                s = e+1
                e = e+2
        if s == len(nums)-1:
            res.append(str(nums[s]))
        return res