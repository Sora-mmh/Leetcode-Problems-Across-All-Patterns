from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        root, root_idx = TreeNode(preorder[0]), inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: root_idx + 1], inorder[: root_idx])
        root.right = self.buildTree(preorder[root_idx + 1 :], inorder[root_idx + 1 :])
        return root
         
