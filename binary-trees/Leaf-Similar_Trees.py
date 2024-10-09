from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaves, root2_leaves = [], []

        def get_leaves1(root):
            if not root.left and not root.right:
                root1_leaves.append(root.val)
            if root.left:
                get_leaves1(root.left)
            if root.right:
                get_leaves1(root.right)

        def get_leaves2(root):
            if not root.left and not root.right:
                root2_leaves.append(root.val)
            if root.left:
                get_leaves2(root.left)
            if root.right:
                get_leaves2(root.right)

        get_leaves1(root1)
        get_leaves2(root2)
        print("leaves 1 : ", root1_leaves)
        print("leaves 2 : ", root2_leaves)
        return root1_leaves == root2_leaves
