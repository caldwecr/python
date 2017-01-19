""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    if root.left is None:
        if root.right is None:
            return True
        elif check_binary_search_tree_(root.right):
            return root.data < min_data(root.right)
        else:
            return False
    elif root.right is None:
        if check_binary_search_tree_(root.left):
            return root.data > max_data(root.left)
        else:
            return False
    else:
        if check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right):
            return root.data > max_data(root.left) and root.data < min_data(root.right)
        else:
            return False

def min_data(bst_root):
    if hasattr(bst_root, 'minimum'):
        return bst_root.minimum
    elif bst_root.left is None:
        bst_root.minimum = bst_root.data
    else:
        bst_root.minimum = min_data(bst_root.left)
    return bst_root.minimum

def max_data(bst_root):
    if hasattr(bst_root, 'maximum'):
        return bst_root.maximum
    elif bst_root.right is None:
        bst_root.maximum = bst_root.data
    else:
        bst_root.maximum = max_data(bst_root.right)
    return bst_root.maximum