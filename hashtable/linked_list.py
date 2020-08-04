class Node:
    def __init__(self, value, next):
        # the value at this linked list node
        self.value = value
        self.next = None
        # reference to the next node in the list
      

    def get_value(self):
        return self.value
        

    def get_next(self):
        return self.next_node
     

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next
       

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None
    
    def add_to_head (self, node):
        node.next = self.head
        self.head = node

    def delete(self, value):
        cur = self.head
            
        # Special case of deleting the head of the list
        if cur.value == value:
            self.head = self.head.next
            return cur
                
        # General case
        prev = cur
        cur = cur.next
            
        while cur is not None:
            if cur.value == value:  # Delete this one
                prev.next = cur.next   # Cuts out the old node
                return cur
            else:
                prev = prev.next
                cur = cur.next
        return None