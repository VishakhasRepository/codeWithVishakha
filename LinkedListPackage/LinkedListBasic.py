# linkedlist nodes contains address of next node

# difference between linked list and array
# deletion- a node can be deleted with its cell but in array only cell value is deleted but cell remains as it is
# size = while creating linked list , no need to specify the size of linked list, but for list specify the size is required

class Node:
    def __init__(self, value=None):  #initialize node with reference and value
        self.value = value   #O(1)
        self.next = None    #this next is the second part of a node, node has two parts


class SingleLinkedList:   #initialize head and tail value - 1st step
    def __init__(self):
        self.head = None   #O(1)
        self.tail = None   #O(1)


singlyLinkedList = SingleLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2   #O(1)
singlyLinkedList.tail = node2


#time complexity for creating a single linked list is o1 and space complexiyt is o1 here
