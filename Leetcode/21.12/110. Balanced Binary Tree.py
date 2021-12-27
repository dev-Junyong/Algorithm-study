# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if root is None:
                return 0
            left_hei, right_hei = getHeight(root.left), getHeight(root.right)
            
            if left_hei < 0 or right_hei < 0 or abs(left_hei - right_hei) > 1:
                return -1
            return max(left_hei, right_hei) + 1
        return (getHeight(root) >= 0)