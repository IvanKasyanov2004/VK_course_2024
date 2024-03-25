from classes import *

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
list1.printList()
reverseLinkedList(list1)
print("->", end = ' ')
list1.printList()
print()

#пустой массив
list2 = List([1])
list2.printList()
reverseLinkedList(list2)
print("->", end = ' ')
list2.printList()
print()

#пустой массив
list3 = List([])
list3.printList()
reverseLinkedList(list3)
print("->", end = ' ')
list3.printList()