class node:
    def __init__(self,val):
        self.data = val
        self.next = None

class linked_list:
    def __init__(self,node):
        self.head = node
    def push(self,node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def printll(self):
        current = self.head
        while current.next:
            print(current.data)
            current = current.next
        print(current.data)

def remove_last_n(linked_list,n):
    first_pointer = linked_list.head
    second_pointer = linked_list.head
    pos = 0
    while pos < n:
        # if(second_pointer.next == None):
            # if(pos == n - 1):
            #     linked_list.head = linked_list.head.next
            #     return linked_list.head
            second_pointer = second_pointer.next
            pos = pos+1
    if pos == 0:
        linked_list.head = first_pointer.next
    while second_pointer.next != None:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    first_pointer.next = first_pointer.next.next

link3 = linked_list(node(1))
link3.push(node(3))
link3.push(node(4))
link3.push(node(7))