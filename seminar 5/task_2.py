import unittest
from treeNode import *
from task_1 import buildTree
#понять симметрично ли дерево


def isSimmetricQueue(arr_nodes):
    if len(arr_nodes) == 0:
        return True
    left = 0
    right = len(arr_nodes) - 1

    while left < right:
        if arr_nodes[left].val != arr_nodes[right].val:
            return False
        left += 1
        right -= 1

    return True

def isSimmetricArray(arr):
    if len(arr) == 0:
        return True
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True

#обход в ширину (BFS)
def isSimmetricBFS(bt):
    if bt == None:
        return True
    nodes = [bt]
    while len(nodes) != 0:
        queue = []
        for current in nodes:
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        if not isSimmetricQueue(queue):
            return False
        nodes = queue
    return True


#другой вариант - вывести дерево обходом в глубину и понять симметричен ли массив, который получился
#рекурсия медленне
def deptSearch(root, arr):
    if root == None:
        return True
    
    deptSearch(root.left, arr)
    arr.append(root.val)
    deptSearch(root.right, arr)

def isSimmetricDFS(bt):
    arr = []
    deptSearch(bt, arr)
    return isSimmetricArray(arr)


class Test(unittest.TestCase):
    def test_IsSymmetricBFS_False(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        root = buildTree(arr, 0)
        self.assertFalse(isSimmetricBFS(root))

    def test_IsSymmetricBFS_True(self):
        arr = [3, 8, 8, 9, 6, 6, 9]
        root = buildTree(arr, 0)
        self.assertTrue(isSimmetricBFS(root))

    def test_IsSymmetricBFS_True_None(self):
        arr = [3, 8, 8, 9, None, None, 9]
        root = buildTree(arr, 0)
        self.assertTrue(isSimmetricBFS(root))

    def test_emptyTree_BFS(self):
        arr = []
        root = buildTree(arr, 0)        
        self.assertTrue(isSimmetricBFS(root))


    def test_IsSymmetricDFS_False(self):
        arr = [8, 9, 11, 7, 16, 3, 1]
        root = buildTree(arr, 0)
        self.assertFalse(isSimmetricDFS(root))

    def test_IsSymmetricDFS_True(self):
        arr = [3, 8, 8, 9, 6, 6, 9]
        root = buildTree(arr, 0)
        self.assertTrue(isSimmetricDFS(root))

    def test_IsSymmetricDFS_True_None(self):
        arr = [3, 8, 8, 9, None, None, 9]
        root = buildTree(arr, 0)
        self.assertTrue(isSimmetricDFS(root))

    def test_emptyTree_DFS(self):
        arr = []
        root = buildTree(arr, 0)        
        self.assertTrue(isSimmetricDFS(root))

if __name__ == '__main__':
    unittest.main()