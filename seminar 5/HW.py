import unittest
#посчитать количество уникальных бинарных деревьев поиска (то есть построенных по правилу) они могут быть вырожденными (в вершинах стоят числа от 1 до n)

#Обозначим через f(n) количество бинарных деревьев с n вершинами. Тогда f(n) = f(0) * f(n – 1) + f(1) * f(n – 2) + … + f(n – 1) * f(0)
# f(0) = f(1) = 1
# f(2) = f(0) * f(1) + f(1) * f(0)
# f(3) = f(0) * f(2) + f(1) * f(1) + f(2) * f(0)
# f(4) = f(0) * f(3) + f(1) * f(2) + f(2) * f(1) + f(3) * f(0)
# ...  (числа Каталана)

def treesNumber(N):
    if N == 0 or N == 1:
        return 1
    f_mem = [0] * (N+1) #инициализируем list из нулей
    f_mem[0] = f_mem[1] = 1

    for i in range(2, N+1):
        for j in range(i):
            f_mem[i] += f_mem[j] * f_mem[i - j - 1]  #заполняем массив

    return f_mem[N]

class Test(unittest.TestCase):
    def test_treesNumber_0(self):
        self.assertEqual(treesNumber(0), 1)

    def test_treesNumber_1(self):
        self.assertEqual(treesNumber(1), 1)

    def test_treesNumber_4(self):
        self.assertEqual(treesNumber(4), 14)

    def test_treesNumber_20(self):
        self.assertEqual(treesNumber(20), 6564120420)


if __name__ == '__main__':
    unittest.main()

