from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return 
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                root.val = self.get_max_left_val(root.left)
                root.left = self.deleteNode(root.left, root.val)
        return root

    def get_max_left_val(self, root):
        while root.right:
            root = root.right
        return root.val
        

        
