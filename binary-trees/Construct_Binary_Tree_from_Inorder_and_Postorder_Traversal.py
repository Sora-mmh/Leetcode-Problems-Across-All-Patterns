from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(postorder[-1])
        left_inorder = inorder[: root_idx]
        right_inorder = inorder[root_idx + 1: ]
        left_postorder = postorder[: len(left_inorder)]
        right_postorder = postorder[len(left_inorder): -1]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
