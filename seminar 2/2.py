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


def reverseLinkedList(list):
    prev = None
    cur = list.head

    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    list.head = prev #на последнем шаге cur = None, prev - голова


list1 = List([1, 2, 3, 4, 5])
printList(list1)
reverseLinkedList(list1)
print("->", end = ' ')
printList(list1)
print()

#пустой массив
list2 = List([1])
printList(list2)
reverseLinkedList(list2)
print("->", end = ' ')
printList(list2)
print()

#пустой массив
list3 = List([])
printList(list3)
reverseLinkedList(list3)
print("->", end = ' ')
printList(list3)