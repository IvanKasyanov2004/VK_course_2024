import queue

#является ли a подстрокой b
def isSubsequence(a, b):
    a = list(a) # разбили строку на символы
    b = list(b)
    p1 = 0 #ставим указатели на начало
    p2 = 0

    for p2 in range(len(b)): 
        if(a[p1] == b[p2]): #если совпали значения, то двигаем p1
            p1 += 1
            if(p1 == len(a)): #если дошли до конца a, то True
                return True
    
    return False
    

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