from .interface import AbstractLinkedList
from .node import Node


# VIRTUAL ENV IS NAMED "linkedlist-env"... - (linkedlist-env)jkoppc9:~/workspace (master) $ 
class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """
    
    def __init__(self, elements=None):
        self.start = None
        self.end = None
        self.elems = []
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return '{}'.format([x for x in self])

    def __len__(self):
        length = 0
        for elem in self:
            length+=1
        return length

    def __iter__(self):
        start = self.start
        while start:
            yield start.elem
            start = start.next
        raise StopIteration

    def __getitem__(self, index):
        if index > len(self) or self.start is None:
            raise IndexError
        for i, elem in enumerate(self):
            if i==index:
                return elem

    def __add__(self, other):
        new = LinkedList([elem for elem in self])
        for i in other:
            new.append(i)
        return new

    def __iadd__(self, other):
        for i in other:
            self.append(i)
        return self

    def __eq__(self, other):
        if self is None or other is None or self is None and other is None:
            return False
        if other.start is None and self.start is None:
            return True
        elif other.start is None or self.start is None:
            return False
        n1 = self.start
        n2 = other.start
        if len(self) == len(other):
            while True:
                if n1.elem != n2.elem:
                    return False    
                if n1.next is None:
                    return True
                n1 = n1.next
                n2 = n2.next
        return False

    def __ne__(self, other):
        return not self == other
    
    def append(self, elem):
        # creating first element
        if self.start is None:
            self.start = Node(elem)
            self.end = self.start
            return self.start
        # appending
        # create and update end node
        new_node = Node(elem)
        self.end.next = new_node
        self.end = new_node

    def count(self):
        amount = len(self)
        return amount

    def pop(self, index=None):
        def remove_first(self):
            elem = self.start.elem
            self.start = self.start.next
            return elem
            
        if len(self) == 0 or index >= len(self):
            raise IndexError
        if index is None:
            index = (len(self)-1)
        if index == 0:
            return remove_first(self)
# elif none of the above, just go through regular, or use index = len(self)-1
        node = self.start
        hold = None
        match = 0
        while True:
            if match == index:
                hold.next = node.next
                return node.elem
            hold = node
            node = node.next
            match +=1