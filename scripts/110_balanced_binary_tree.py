class node:
    def __init__(self,data):
        self.data = data
class binary_tree:
    def __init__(self,node):
        self.root = node
        self.left = None
        self.right = None
    def push(self,node):
        if node.data <= self.root.data:
            if self.left is None:
                self.left = binary_tree(node)
            else:
                self.left.push(node)
        else:
            if self.right is None:
                self.right = binary_tree(node)
            else:
                self.right.push(node)

def getdepth(tree):
    if tree is None:
        return 0
    else:
        leftdepth = getdepth(tree.left)
        rightdepth = getdepth(tree.right)
        if leftdepth > rightdepth:
            return leftdepth + 1
        else:
            return rightdepth + 1

def balanced_tree(tree):
    if tree is None:
        return True
    else:
        lefttree = getdepth(tree.left)
        righttree = getdepth(tree.right)
        if abs(lefttree-righttree) > 1:
            return False
        else:
            return True
