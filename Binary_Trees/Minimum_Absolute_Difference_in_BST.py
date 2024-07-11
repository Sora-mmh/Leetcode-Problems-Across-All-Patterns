from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def inorder(root):
            if root:
                inorder(root.left)
                values.append(root.val)
                inorder(root.right)

        inorder(root)
        return min([values[idx] - values[idx - 1] for idx in range(1, len(values))])
