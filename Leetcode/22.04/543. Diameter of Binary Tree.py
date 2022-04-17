# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        if root is None: 
            return 0
        
        def func(root):
            if root is None: 
                return 0
            left = func(root.left)
            right = func(root.right)
            if left + right > self.max:
                self.max = left+right
            return max(left, right) + 1
        func(root)
        return self.max