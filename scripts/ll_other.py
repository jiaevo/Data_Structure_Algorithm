class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class link_list:
    def __init__(self):
        self.head = None
    def __repr__(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        return 'end'       
    def push(self,data):
        if self.head is None:
            self.head = node(data)
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = node(data)
    def insert(self,data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode


# convert list to linklist
def convert_list_ll(list1):
    l1 = link_list()
    for i, value in enumerate(list1):
        if l1.head is None:
            l1.head = node(value)
            current = l1.head
        else:
            current.next = node(value)
            current = current.next
    return l1

l3 = link_list()
l3.push(99)
l3.push(202)




