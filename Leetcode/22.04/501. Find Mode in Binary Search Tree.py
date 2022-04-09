# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        qu = []
        nodefre = {}
        qu.append(root)
        
        while len(qu) > 0:
            node = qu.pop(0)
            if node.val in nodefre:
                nodefre[node.val] +=1
            else:
                nodefre[node.val] = 1

            if node.left is not None:
                qu.append(node.left)

            if node.right is not None:
                qu.append(node.right)

        max_val = max(nodefre.values())
        res = [k for k, v in nodefre.items() if v == max_val]

        return res