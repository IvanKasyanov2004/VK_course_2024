from classes import *

def findMiddle(list):
    slow = fast = list.head
    while fast != None and fast.next != None: #возвращает правый после середины
        slow = slow.next
        fast = fast.next.next
    return slow

list1 = List([1, 2, 3, 4, 5])
list1.printList()
print("->", end = ' ')
print(findMiddle(list1).data)

list2 = List([1, 2, 3, 4, 5, 6])
list2.printList()
print("->", end = ' ')
print(findMiddle(list2).data)

list3 = List([1, 2])
list3.printList()
print("->", end = ' ')
print(findMiddle(list3).data)

list4 = List([1])
list4.printList()
print("->", end = ' ')
print(findMiddle(list4).data)