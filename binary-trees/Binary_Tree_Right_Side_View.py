from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        else:
            import collections

            nodes = collections.deque()
            nodes.append(root)
            right_side_nodes = []
            while nodes:
                L = []
                for _ in range(len(nodes)):
                    node = nodes.popleft()
                    L.append(node.val)
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                right_side_nodes.append(L)
            result = []
            for lvl in right_side_nodes:
                result.append(lvl[-1])
            return result
