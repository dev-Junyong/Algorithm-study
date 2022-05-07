# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        
        if not root: 
            return res
        
        qu = deque([root])
        
        while qu:
            len_qu = len(qu)
            sum_level = 0         
            for _ in range(len_qu):
                node = qu.popleft()
                sum_level += node.val
                
                if node.left: 
                    qu.append(node.left)
                if node.right: 
                    qu.append(node.right)
            
            res.append(sum_level / len_qu)
        
        return res  
            