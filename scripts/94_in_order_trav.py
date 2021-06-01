class node:
    def __init__(self,data):
        self.data = data

class binary_tree:
    def __init__(self,node):
        self.root = node
        self.leftnode = None
        self.rightnode = None
    def push(self,node):
        if node.data <= self.root.data:
            if self.leftnode == None:
                self.leftnode = binary_tree(node)
            else:
                self.leftnode(node)
        else:
            if self.rightnode == None:
                self.rightnode = binary_tree(node)
            else:
                self.rightnode(node)

def inorder(tree):
    if tree:
        inorder(tree.leftnode)
        print(tree.root.data)
        inorder(tree.rightnode)
        