# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        # The idea is that we traverse both tree depth side all at once then we hit the return + 1

        # This means we have reach the tail
        if not root:
            return 0
        # We do not need a aux head in this situation as we are using recursion
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
         
