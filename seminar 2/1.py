class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

def hasCycle(head):
    if head == None or head.next == None: # если в списке один элемент или ноль (даже нельзы поставить указатели)
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast == None or fast.next == None:  #быстрый указатель дошел до конца
            return False
        slow = slow.next
        fast = fast.next.next

    return True #если в какой-то момент slow == fast, то есть цикл


a1, a2, a3, a4, a5, a6, a7, a8 = Node(), Node(), Node(), Node(), Node(), Node(), Node(), Node()
head_a = a1

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
a7.next = a8
a8.next = a3

b1, b2, b3, b4, b5 = Node(), Node(), Node(), Node(), Node()
head_b = b1

b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5


print(hasCycle(head_a))
print(hasCycle(head_b))