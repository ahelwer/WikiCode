import unittest
from string_algo_tests.simple_matching_functional_tests import GeneralSimpleMatching

suite = []
suite.append(unittest.TestLoader().loadTestsFromTestCase(GeneralSimpleMatching))

