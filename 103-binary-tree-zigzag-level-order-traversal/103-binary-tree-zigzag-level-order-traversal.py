# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        ltor = True
        while queue:
            size = len(queue)
            level = deque()
            for i in range(size):
                curNode = queue.popleft()
                if ltor:
                    level.append(curNode.val)
                else:
                    level.appendleft(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            result.append(list(level))
            ltor = not ltor
        return result