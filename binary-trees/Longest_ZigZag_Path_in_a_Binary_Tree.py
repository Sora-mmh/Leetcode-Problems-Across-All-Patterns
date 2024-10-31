from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_dist = 0
        def dfs(root, direction, dist):
            if not root:
                return 0
            else:
                self.max_dist = max(self.max_dist, dist)
                if direction == "right":
                    dfs(root.left, "left", dist + 1)
                    dfs(root.right, "right", 1)
                if direction == "left":
                    dfs(root.right, "right", dist + 1)
                    dfs(root.left, "left", 1)
        
        dfs(root.right, "right", 1)
        dfs(root.left, "left", 1)
        return self.max_dist
