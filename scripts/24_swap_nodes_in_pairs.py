class node:
    def __init__(self,data):
        self.value = data
        self.next = None

class link_list:
    def __init__(self,node):
        self.head = node
    def push(self,node):
        current = self.head
        while(current.next):
            current = current.next
        current.next = node
    def printlist(self):
        current = self.head
        while(current.next):
            print(current.value)
            current=current.next
        print(current.value)

#edged case odd number of nodes: current.next is None, finish

def swapnodes(linklist):
    current = linklist.head
    prev = None
    while(current.next and current):
        temp = current.next
        current.next = temp.next
        temp.next = current
        if prev is None:
            linklist.head = temp
            print(linklist)
        else:
            prev.next = temp
        prev = current
        current = current.next

    return linklist.head

l4 = link_list(node(20))
l4.push(node(99))
l4.push(node(202))
l4.push(node(204))
l4.push(node(205))