import unittest
from treeNode import *
from task_1 import buildTree

#сравнить два дерева 
def isSame(a, b):
    if a == None and b == None: #если узлы пустые в обоих деревьях, то True
        return True
    if a == None or b == None: #если у одног оесть узел, а у другого нет, то False
        return False

    if a.val != b.val:  #если значения разные, то False
        return False

    if a.val == b.val:  #если значения равны, то идм дальше
        return isSame(a.left, b.left) and isSame(a.right, b.right)

class Test(unittest.TestCase):
    def test_isSame_0_0(self):
        arr = []
        a = buildTree(arr, 0)
        b = buildTree(arr, 0)
        self.assertTrue(isSame(a, b))

    def test_isSame_1_1(self):
        arr = [0]
        a = buildTree(arr, 0)
        b = buildTree(arr, 0)
        self.assertTrue(isSame(a, b))

    def test_isSame_1_0(self):
        arr_a = [0]
        arr_b = []
        a = buildTree(arr_a, 0)
        b = buildTree(arr_b, 0)
        self.assertFalse(isSame(a, b))

    def test_isSame_many_True(self):
        arr_a = arr_b = [16, 12, 18, None, 15, 17, None]
        a = buildTree(arr_a, 0)
        b = buildTree(arr_b, 0)
        self.assertTrue(isSame(a, b))

    def test_isSame_many_False1(self):
        arr_a = [16, 12, 18, None, 15, 17, None]
        arr_b = [16, 12, 18, None, 15, None, None]
        a = buildTree(arr_a, 0)
        b = buildTree(arr_b, 0)
        self.assertFalse(isSame(a, b))

    def test_isSame_many_False2(self):
        arr_a = [16, 12, 18, None, 15, 17, None]
        arr_b = [16, 12, 18, None, 15, 18, None]
        a = buildTree(arr_a, 0)
        b = buildTree(arr_b, 0)
        self.assertFalse(isSame(a, b))


if __name__ == '__main__':
    unittest.main()

