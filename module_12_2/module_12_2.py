from unittest import TestCase, main, skip
from testees import Runner, Tournament

'''
Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. 
Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. 
У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. 
В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) 
и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.
'''


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        print('All results:')
        cls.all_results = {}

    def setUp(self, runner1=Runner('Usain', 10),
              runner2=Runner('Andrew', 9),
              runner3=Runner('Nick', 3), distance=90):
        self.usain = runner1
        self.andrew = runner2
        self.nick = runner3
        self.distance = distance
        self.all_results.clear()
        print('-' * 30)
        print()

    def tearDown(self):
        print('-' * 30)
        self.usain.distance = 0
        self.andrew.distance = 0
        self.nick.distance = 0


    #@skip
    def test_runner_order(self):
        tournament = Tournament(self.distance, self.usain, self.nick)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(self.nick == list(self.all_results.values())[-1], 'Nick is the last runner')
        print('test_runner_order OK')

    #@skip
    def test_runner_order2(self):
        tournament = Tournament(self.distance, self.nick, self.andrew)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(self.nick == list(self.all_results.values())[-1], 'Nick is the last runner')
        print('test_runner_order2 OK')

    #@skip
    def test_runner_order3(self):
        tournament = Tournament(self.distance, self.usain, self.andrew, self.nick)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(self.nick == list(self.all_results.values())[-1], 'Nick is the last runner')
        print('test_runner_order3 OK')

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i, cls.all_results[i])


if __name__ == '__main__':
    main()

