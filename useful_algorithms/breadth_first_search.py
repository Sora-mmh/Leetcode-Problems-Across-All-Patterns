class Node:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return str(self.val)

    # follow the binary tree logic when adding values greater
    # than or less than the current node
    def insert_node(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert_node(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert_node(val)

    @staticmethod
    def insert_nodes(vals: list, root):
        for i in vals:
            root.insert_node(i)

    # The BFS algorithm starts at the root node and travels through every
    # child node at the current level before moving to the next level.
    # You may use collections.deque as your data structure

    def bfs(self, root=None):
        if root is None:
            return
        queue = [root]

        while len(queue) > 0:
            cur_node = queue.pop(0)

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)
