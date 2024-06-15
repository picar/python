class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def append(self, node):
        self.len += 1
        if self.head is None:
            self.head = node
            self.tail = self.head
            return self
        self.tail.next = node
        return self
    
    def delete_head(self):
        if len(self) == 1:
            self.head = None
            self.tail = None
            return self
        self.len -= 1
        self.head = self.head.next
        return self
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
    
    def __len__(self):
        return self.len

    def __repr__(self) -> str:
        return str(list(self))
    