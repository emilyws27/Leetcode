# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = deque()
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            curLevel = []
            for  i in range(size):
                curNode = queue.popleft()
                curLevel.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            result.appendleft(curLevel)
        return result