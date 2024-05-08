import unittest
from treeNode import *
from task_1 import buildTree
#понять минимальную глубину дерева

def minDepth(root):
    if root == None:
        return 0

    if root.left != None and root.right != None:
        return 1 + min(minDepth(root.left), minDepth(root.right))
    
    if root.left != None and root.right == None:
        return 1 + minDepth(root.left)

    if root.right != None and root.left == None:
        return 1 + minDepth(root.right)

    return 1  # Если у узла нет ни левого, ни правого ребенка, возвращаем 1



class Test(unittest.TestCase):
    def test_minDepth_0(self):
        arr = []
        root = buildTree(arr, 0)
        self.assertEqual(minDepth(root), 0)

    def test_minDepth_1(self):
        arr = [0]
        root = buildTree(arr, 0)
        self.assertEqual(minDepth(root), 1)

    def test_minDepth_3(self):
        arr = [11, 8, 16, 2, 9, 6, None, 7, None, None, 9]
        root = buildTree(arr, 0)
        self.assertEqual(minDepth(root), 3)


if __name__ == '__main__':
    unittest.main()