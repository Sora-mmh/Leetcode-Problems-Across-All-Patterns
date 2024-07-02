# DFS patterns with recursion


# visit all left branches, when encountring a null node,
# retreat one step, print the node value than visit right nodes
# ==> for lesser values to greater values
def in_order(root=None):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


# print current node value, advance to left nodes,
# than go to the previous frame and visit right nodes
# ==> root values, than left values than right values
def pre_order(root=None):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)


# visit all left branches, when encountring a null node,
# retreat one step, visit right nodes and print the current node
# ==> left values than right values on the same branch
def post_order(root=None):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)
