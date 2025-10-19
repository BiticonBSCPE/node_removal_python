class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        
    def remove_beginning (self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next 
        if self.head is None:
            self.tail = None
        return data
    
    def remove_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
    
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        self.tail = current
        return data
    
    def remove_at(self, data):
        if self.head is None:
            return None

        if self.head.data == data:
            return self.remove_beginning()

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            return None

        if current.next.next is None:
            self.tail = current

        current.next = current.next.next
        return data