import unittest
from string_algo_tests.simple_matching_functional_tests import GeneralSimpleMatching
from string_algo_tests.string_utils_unit_tests import MatchLengthTests, AlphabetIndexTests

suite = []
suite.append(unittest.TestLoader().loadTestsFromTestCase(GeneralSimpleMatching))
suite.append(unittest.TestLoader().loadTestsFromTestCase(MatchLengthTests))
suite.append(unittest.TestLoader().loadTestsFromTestCase(AlphabetIndexTests))

