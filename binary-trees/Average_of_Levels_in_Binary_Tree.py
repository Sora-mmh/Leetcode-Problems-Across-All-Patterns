from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return root
        else:
            averages = []
            import collections

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
                averages.append(sum(L) / len(L))
            return averages
