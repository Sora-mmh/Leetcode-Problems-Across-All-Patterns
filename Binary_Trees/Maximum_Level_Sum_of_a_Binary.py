from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            from collections import deque
            nodes = deque([root])
            lvls = []
            while nodes:
                lvl = []
                for _ in range(len(nodes)):
                    current_node = nodes.popleft()
                    lvl.append(current_node.val)
                    if current_node.left:
                        nodes.append(current_node.left)
                    if current_node.right:
                        nodes.append(current_node.right)
                lvls.append(sum(lvl))
            return lvls.index(max(lvls)) + 1 
                     

