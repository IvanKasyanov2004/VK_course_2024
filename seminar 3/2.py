import queue

def isSubsequence(a, b):
    a = list(a) # разбили строку на символы
    b = list(b)
    q = queue.Queue() # заполняем очередь FIFO элементами a
    for el in a:
        q.put(el)

    for el in b: # удаляем из очереди если в b есть такой
        if q.queue[0] == el:
            q.get()

    return q.qsize() == 0

a = "uio"
b = "quefio"
print(a, end = ', ')
print(b, end = ' -> ')
print(isSubsequence(a, b))

a = "oiu"
b = "quefio"
print(a, end = ', ')
print(b, end = ' -> ')
print(isSubsequence(a, b))

