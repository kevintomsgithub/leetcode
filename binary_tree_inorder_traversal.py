def inorderTraversal(root):
    stack = []; traversal = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            traversal.append(root.val)
            root = root.right
    return traversal