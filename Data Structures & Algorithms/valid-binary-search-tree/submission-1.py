# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root, lower, upper):
            if not root: return True
            if root.val<=lower or root.val>=upper:
                return False

            return (is_valid(root.left, lower, root.val) 
            and is_valid(root.right, root.val, upper) )

        lower, upper = -float('inf'), float('inf')

        return is_valid(root, lower, upper)



        
