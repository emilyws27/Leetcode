# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

    
        def longestPath(t):
            nonlocal diameter
            if t == None:
                return 0
            right = longestPath(t.right)
            left = longestPath(t.left)
            diameter = max(diameter, left+right)
            return max(left,right) + 1
        
        longestPath(root)
        return diameter
            
        