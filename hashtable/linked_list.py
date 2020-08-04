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
    
    def add_to_head (self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the head
        else:
            # set the current head's next reference to our new node
            self.head.set_next = self.head
            self.head = new_node

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