//no order binary tree
class Node:
    def __init__(self,data):
        self.data = data

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftnode = None
        self.rightnode = None

    
    def insert(self,Node):
        if self.key:
            if Node.data < self.key.data:
                if self.leftnode is None:
                    self.leftnode = BinaryTree(Node)
                else:
                    self.leftnode.insert(Node)
            elif Node.data > self.key.data:
                if self.rightnode is None:
                    self.rightnode = BinaryTree(Node)
                else:
                    self.rightnode.insert(Node)
        else:
            self.key = BinaryTree(Node)                

//print tree by value
    def PrintTree(self):
        if self.leftnode:
            self.leftnode.PrintTree()
        print( self.key.data),
        if self.rightnode:
            self.rightnode.PrintTree()

def prettytree(tree,level = 0):
    if tree:
        prettytree(tree.leftnode,level+1)
        print(' ' * 4 * level + '->', tree.key.data)
        prettytree(tree.rightnode,level+1)

//get dpeth of tree
def max_depth(tree):
    if tree:
        left_level = max_depth(tree.leftnode)
        right_level = max_depth(tree.rightnode)
        if left_level > right_level:
            return left_level + 1
        else:
            return right_level + 1
    else:
        return 0

//get width of each level
def width(tree,level):
    if tree is None:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return width(tree.leftnode,level - 1) + width(tree.rightnode,level -1)



//example - auto sort by using insert method 
root_node = Node(10)
tree1 = BinaryTree(root_node)
left_node = Node(5)
right_node = Node(12)
tree1.insert(left_node)
tree1.insert(right_node)
left_node1 = Node(7)
tree1.insert(left_node1)
left_node2 = Node(6)
tree1.insert(left_node2)
right_node2 = Node(22)
tree1.insert(right_node2)
left_node3 = Node(4)
tree1.insert(left_node3)

//example - manual insert by using leftnode and rigtnode method
root_node2 = Node(21)
tree2 = BinaryTree(root_node2)
tree2.leftnode = BinaryTree(Node(10))
tree2.leftnode.rightnode = BinaryTree(Node(31))
tree2.rightnode = BinaryTree(Node(99))