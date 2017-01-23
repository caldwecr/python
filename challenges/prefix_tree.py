class PrefixTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def find_child(self, value):
        if value in self.children:
            return self.children[value]
        else:
            return None

    def find_or_create_child(self, value):
        found_child = self.find_child(value)
        if not found_child:
            child = PrefixTreeNode(value)
            self.set_child(child)
            return child
        else:
            return found_child

    def set_child(self, child):
        if child.value in self.children.keys():
            raise ValueError('Cannot overwrite existing child')
        else:
            self.children[child.value] = child

    def total_children(self):
        sum([child.total_children() for child in self.children.values()])

class PrefixTree:
    """Expressly written with the given assumption that add operations do not insert duplicate values"""
    def __init__(self):
        self.nodes = {}

    def add(self, name):
        pass

    def find(self, prefix):
        pass