# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return
        stack = [(root, False)]
        res = 0
        while len(stack) != 0:
            root, is_left = stack.pop()
            if root.left == None and root.right == None and is_left:
                res = res + root.val
            if root.left != None:
                stack.append((root.left, True))
            if root.right != None:
                stack.append((root.right, False))
        return res