class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
            if node is not None: #if it is not None
                next = node.next_node #lets set the next node to the next pointer
                node.next_node = prev #and here actually flip the pointer
                self.reverse_list(next, node)
            else:
                self.head = prev #set head equal to last node
            # prev = None
            # current = self.head
            # while current:
            #     nxt = current.next_node  
            #     current.next_node = prev
            #     prev = current
            #     current = nxt
            # self.head = prev


# ll = LinkedList()
# ll.add_to_head(1)
# ll.add_to_head(2)
# ll.reverse_list()