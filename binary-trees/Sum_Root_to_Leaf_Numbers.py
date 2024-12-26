from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def add_path_total(root, curr_s=0):
            if not root:
                return 0
            if not root.left and not root.right:
                return curr_s * 10 + root.val
            return add_path_total(root.left, curr_s * 10 + root.val) + add_path_total(root.right, curr_s * 10 + root.val)
        return add_path_total(root)

        
