from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections

        if not root:
            return root
        values = []
        nodes = collections.deque()
        nodes.append(root)
        while nodes:
            L = []
            for _ in range(len(nodes)):
                node = nodes.popleft()
                L.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            values.append(L)
        return values
