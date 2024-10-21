from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_pths(root, target):
            if not root:
                return 0
            else:
                count = 0
                if root.val == target:
                    count += 1
                count += count_pths(root.left, target - root.val)
                count += count_pths(root.right, target - root.val)
                return count
        
        def dfs(root):
            if not root:
                return 0
            else:
                count = count_pths(root, targetSum)
                count += dfs(root.left)
                count += dfs(root.right)
                return count
        
        return dfs(root)


        
