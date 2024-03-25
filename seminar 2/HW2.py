from classes import *

def mergeSortedLists(list1, list2):
    if list1 is None: #если лист пустой, то возвращаем другой
        return list2
    if list2 is None:
        return list1

    if list1.head.data > list2.head.data: #выбираем лист, который будем возвращать (у него голова меньше)
        p1 = list2.head
        p2 = list1.head
        return_list2 = True
    else:
        p2 = list2.head
        p1 = list1.head
        return_list2 = False 

    while p1.next != None and p2 != None:  #p1 движется по листу, после него вставляем p2 
        if p1.next.data > p2.data:
            tmp = p1.next
            p1.next = p2
            p2 = tmp
        p1 = p1.next

    if p1.next == None: #если вышли из цикла потому что p1 прошел весь лист, то другой лист просто приклеиваем
        p1.next = p2

    if return_list2 == True:
        return list2
    else:
        return list1

list1 = List([4, 5, 6, 7, 10, 11])
list2 = List([5, 7, 8, 20, 22])
list1.printList()
print(",", end=' ')
list2.printList()
print("-> ", end = '')
mergeSortedLists(list1, list2).printList()
print()

list1 = List([9])
list2 = List([5, 7, 8, 20, 22])
list1.printList()
print(",", end=' ')
list2.printList()
print("-> ", end = '')
mergeSortedLists(list1, list2).printList()
print()

list1 = List([5, 7, 8, 20, 22])
list2 = List([25])
list1.printList()
print(",", end=' ')
list2.printList()
print("-> ", end = '')
mergeSortedLists(list1, list2).printList()
print()


list1 = List([1, 1, 2, 2, 2])
list2 = List([2, 2, 2, 2])
list1.printList()
print(",", end=' ')
list2.printList()
print("-> ", end = '')
mergeSortedLists(list1, list2).printList()