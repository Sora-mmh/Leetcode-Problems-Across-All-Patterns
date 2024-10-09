# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root.val in [p.val, q.val]:
            return root
        left_branch = self.lowestCommonAncestor(root.left, p, q)
        right_branch = self.lowestCommonAncestor(root.right, p, q)
        if left_branch and right_branch:
            return root
        return left_branch or right_branch
