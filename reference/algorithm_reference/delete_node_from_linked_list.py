class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    # def push(self, value):
    #     new_node = Node(value)
    #     new_node.next = self.head # insert node at the beginning
    #     self.head = new_node