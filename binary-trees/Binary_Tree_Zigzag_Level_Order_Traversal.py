from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        else:
            import collections

            nodes = collections.deque()
            nodes.append(root)
            levels = []
            counter = 0
            while nodes:
                L = []
                for _ in range(len(nodes)):
                    node = nodes.popleft()
                    L.append(node.val)
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                levels.append(L)
            result = []
            for idx, lvl in enumerate(levels):
                if idx % 2 == 0:
                    result.append(lvl)
                else:
                    result.append(lvl[::-1])
            return result
