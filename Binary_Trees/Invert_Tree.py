from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.right and root.left:
                temp = root.right
                root.right = root.left
                root.left = temp
            elif root.left and not root.right:
                root.right = root.left
                root.left = None
            elif root.right and not root.left:
                root.left = root.right
                root.right = None
            self.invertTree(root.right)
            self.invertTree(root.left)
            return root
