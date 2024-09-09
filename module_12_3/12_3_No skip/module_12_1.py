class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


'''
Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. 
Далее вызовите метод walk у этого объекта 10 раз. 
После чего методом assertEqual сравните distance этого объекта со значением 50.

test_run - метод, в котором создаётся объект класса Runner с произвольным именем. 
Далее вызовите метод run у этого объекта 10 раз. 
После чего методом assertEqual сравните distance этого объекта со значением 100.

test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. 
Далее 10 раз у объектов вызываются методы run и walk соответственно. 
Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
'''


import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        print('RunnerTest')
        print('==========')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Test')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Test')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Test1')
        runner2 = Runner('Test2')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':

    unittest.main()

