# Stack LIFO, keep adding new element to the right, since pop always consume the most right element(Last)
class stack:
    def __init__(self):
        self.elements = []
    def push(self,new_ele):
        self.elements.append(new_ele)
    def pop(self):
        self.elements.pop()
#Queue FIFO, keep adding new element to the left, since pop always consume the most right element(First)
class queue:
    def __init__(self):
        self.elements = []
    def push(self,new_ele):
        self.elements.insert(0,new_ele)
    def pop(self):
        self.elements.pop()