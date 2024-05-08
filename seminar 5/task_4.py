import unittest
from treeNode import *
from task_1 import buildTree
#найти произведение наименьшего и наибольшего чисел в деерве

def minMaxMultiplication(data):
    if len(data) < 2:
        return -1
    if len(data) == 2:
        return data[0] * data[1]
    min_index = 1 #минимальный индекс - левый потомок
    max_index = 2 #максимальный индекс - правый потомок

    i = min_index
    while i < len(data) and data[i] != None: #ищем индекс пока не выйдем за пределы массива или не наткнемся на лист (следующий элемент None)
        i = 2*i + 1  
    min_index = int((i - 1) / 2)  #нашли индекс минимального (вернули предпоследнее i в цикле)

    i = max_index
    while i < len(data) and data[i] != None:
        i = 2*i + 2  
    max_index = int((i - 2) / 2) #нашли индекс максимального (вернули предпоследнее i в цикле)

    return data[min_index] * data[max_index]


class Test(unittest.TestCase):
    def test_minMaxMul_1(self):
        arr = [0]
        self.assertEqual(minMaxMultiplication(arr), -1)

    def test_minMaxMul_2(self):
        arr = [1,2]
        self.assertEqual(minMaxMultiplication(arr), 2)

    def test_minMaxMul_many(self):
        arr = [16, 12, 18, 11, 15, 17, 21, None, None, None, None, None, None, 19, 24]
        self.assertEqual(minMaxMultiplication(arr), 264)


if __name__ == '__main__':
    unittest.main()

    