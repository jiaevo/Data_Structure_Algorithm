class node:
    def __init__(self,data):
        self.data = data

class tree:
    def __init__(self,root):
        self.key = root
        self.leftnode = None
        self.rigtnode = None
    
    def insert(self,node):
        if self.key:
            if self.key.data < node.data:
                if self.leftnode:
                    self.leftnode.insert(node)
                else:
                    self.leftnode = tree(node)
            if self.key.data > node.data:
                if self.rightnode:
                    self.rightnode.insert(node)
                else:
                    self.rightnode = tree(node)
        else:
            self.key = tree(node)

def symmetric(tree):
    if tree is None:
        return True
    def dfs_left(tree,res):
        if tree is None:
            res.append(None)
            return
        res.append(tree.key.data)
        dfs_left(tree.leftnode,res)
        dfs_left(tree.rightnode,res)
        return res

    def dfs_right(tree,res):
        if tree is None:
            res.append(None)
            return
        res.append(tree.key.data)
        dfs_right(tree.rightnode,res)
        dfs_right(tree.lefnode,res)
        return res   
    return dfs_left(tree.leftnode,[]) == dfs_right(tree.rightnode,[])    