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


l3 = link_list(node(20))
l3.push(node(99))
l3.push(node(202))
l3.push(node(204))
l3.push(node(204))
l3.push(node(204))
l3.push(node(205))
l3.push(node(205))


def remove_dupe(link_list):
    dummy = node(None)
    current = link_list.head
    dummy.next = current
    while(current.next):
        exist_value = current.value
        next_value = current.next.value
        print(next_value)
        print(exist_value)
        if exist_value == next_value:
            current.next = current.next.next
        if current.next is None:
            break
        if current.value != current.next.value:
            print('possible error')
            current = current.next
    return dummy.next

    
check = remove_dupe(l3)