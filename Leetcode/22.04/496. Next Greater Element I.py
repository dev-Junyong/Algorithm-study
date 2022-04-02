class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def find(e, idx):
            flag = -1
            for i in range(idx, len(e)):
                if e[i]>e[idx]:
                    flag = e[i]
                    break
            return flag
        res = []
        for num in nums1:
            idx = nums2.index(num)
            res.append(find(nums2, idx))
        return res