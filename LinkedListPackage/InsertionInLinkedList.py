

class CreateNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        #insert in linked list
        def insertSLL(self, value, location):
            newNode = CreateNode(value)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                if location == 0:



singleLinkedList = SingleLinkedList()
print([node.value for node in singleLinkedList])

