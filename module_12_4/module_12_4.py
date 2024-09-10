from runners import Runner
import logging
import unittest


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='error.log', filemode='w', level=logging.INFO,
                            encoding='utf-8',
                            format="{asctime} - {levelname:>7} - {message}", style="{")
        logging.info('All tests started')

    def test_walk(self):
        logging.info('test_walk')
        try:
            runner = Runner('Usain', -1)
            logging.warning('test_walk')
            runner = Runner('Test')
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('test_walk OK')
        except ValueError as e:
            logging.warning(e)
            raise e
        except TypeError as e:
            logging.warning(e)
            raise e

    def test_run(self):
        logging.info('test_run')
        try:
            runner = Runner(123)
            logging.warning('test_run')
            runner = Runner(123)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('test_walk OK')
        except ValueError as e:
            logging.warning(e)
            raise e
        except TypeError as e:
            logging.warning(e)
            raise e

    @classmethod
    def tearDownClass(cls):
        logging.info('All tests completed')


if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        logging.error(f'Error: {e}')
