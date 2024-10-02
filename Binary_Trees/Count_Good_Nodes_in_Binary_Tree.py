# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def pre_order(root, max_val):    
            if not root:
                return 0
            if root.val >= max_val:
                counter = 1
            else:
                counter = 0
            max_val = max(max_val, root.val)
            counter += pre_order(root.left, max_val)
            counter += pre_order(root.right, max_val)
            return counter
        counter = pre_order(root, root.val)
        return counter



        
