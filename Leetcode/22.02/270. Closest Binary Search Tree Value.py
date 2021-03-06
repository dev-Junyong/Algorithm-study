# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        while root:
            res = min(res, root.val, key=lambda x: abs(target - x))
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return res
                