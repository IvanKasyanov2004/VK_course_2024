#построить дерево по массиву
#можно решить итерационным способом
import unittest
from treeNode import *


def buildTree(arr, i):
    if (i >= len(arr)):
        return None
    
    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2*i + 1)
    root.right = buildTree(arr, 2*i + 2)

    return root


class TestBuildTree(unittest.TestCase):
    def test_buildTree(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        root = buildTree(arr, 0)
        
        self.assertEqual(root.val, 8)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 11)
        self.assertEqual(root.left.left.val, 7)
        self.assertEqual(root.left.right.val, 16)
        self.assertEqual(root.right.left.val, 3)
        self.assertEqual(root.right.right.val, 1)

    def test_empty_array(self):
        arr = []
        root = buildTree(arr, 0)
        
        self.assertIsNone(root)

if __name__ == '__main__':
    unittest.main()