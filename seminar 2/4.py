from classes import *

#удаление всех элемеентовс сданным значением
def removeElements(list, val):
    dummy = Node(0) # вводится сторожевой элемент dummy (если удалили голову, то новая голова будет все равно dummy.next)
    dummy.next = list.head
    prev = dummy
    cur = list.head

    while cur != None:
        if cur.data == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    list.head = dummy.next


list1 = List([1, 2, 3, 4, 5])
list1.printList()
print("->", end = ' ')
removeElements(list1, 2)
list1.printList()
print()

list2 = List([1, 2, 3, 2, 5])
list2.printList()
print("->", end = ' ')
removeElements(list2, 2)
list2.printList()
print()

list3 = List([2, 2, 3, 2, 5])
list3.printList()
print("->", end = ' ')
removeElements(list3, 2)
list3.printList()
print()

list4 = List([2, 2])
list4.printList()
print("->", end = ' ')
removeElements(list4, 2)
list4.printList()
print()