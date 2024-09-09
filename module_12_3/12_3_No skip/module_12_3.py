from module_12_1 import RunnerTest
from module_12_2 import TournamentTest
import unittest


suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)