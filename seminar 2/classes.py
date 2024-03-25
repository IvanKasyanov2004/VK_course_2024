class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self, array):
        if len(array) != 0:
            self.head = Node(array[0])
        else:
            self.head = None
        current = self.head
        for i in range(1, len(array)):
            new_node = Node(array[i])
            current.next = new_node
            current = new_node

    def printList(list):
        cur = list.head
        while cur != None:
            print(cur.data, end=' ')
            cur = cur.next