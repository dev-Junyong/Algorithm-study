class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.help_met(nums1, nums2)
        else:
            return self.help_met(nums2, nums1)
        
    def help_met(self, nums1, nums2):
        res = []
        while len(nums1) != 0:
            x = nums1.pop()
            if x in nums2:
                res.append(x)
                nums2.remove(x)
            
        return res