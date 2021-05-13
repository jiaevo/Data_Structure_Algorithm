import copy

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class link_list:
    def __init__(self):
        self.head = None
    def push(self,node):
        current = self.head
        if current is None:
            self.head = node
        else:
            while(current.next):
                current = current.next
            current.next = node
    def insert(self,node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


def merge_sorted_ll(l1,l2):
# deepcopy to not overwrite existing link listed
# by change l1_point, and l2_point, the original link listed will be changed if not using deepcopy
    l1_point = copy.deepcopy(l1.head)
    l2_point = copy.deepcopy(l2.head)
    
    if l1_point == None:
        return l2_point
    if l2_point == None:
        return l1_point
    
    dummynode = node(0)
    tail = dummynode
    while l1_point and l2_point:
        print(tail.data)
        if l1_point.data < l2_point.data:
            tail.next = l1_point
            l1_point = l1_point.next
        else:
            tail.next = l2_point
            l2_point = l2_point.next
        tail = tail.next
    
    if l1_point != None:
        tail.next = l1_point 
    elif l2_point != None:
        tail.next = l2_point
    
    return dummynode.next



link1 = link_list()
link1.push(node(3))
link1.push(node(4))
link1.push(node(10))
link2 = link_list()
link2.push(node(2))
link2.push(node(11))

link3 = link_list()
link3.head = merge_sorted_ll(link1,link2)


link3 = link_list()
link3.push(node(20))
link3.push(node(30))
link3.push(node(40))
temp = link3.head
next = temp.next
temp.next = node(50)
link3.printlist()