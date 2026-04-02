# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        level_order = []
        if not root: return level_order

        q.append(root)
        

        while q:
            level_order.append([])
            for _ in range(len(q)):
                node = q.popleft()
                level_order[-1].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return level_order
        