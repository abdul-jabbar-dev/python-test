
class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def push(self, value):
        temp = self.head
        new_node = node(value)
        if temp == None:
            self.head = new_node
            print(self)
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


linklist = linked_list()
linklist.push(5)
linklist.push(3)
linklist.push(6)
linklist.traversal()
