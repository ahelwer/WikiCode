import unittest

suite = []

from string_algo_tests.simple_matching_functional_tests import GeneralSimpleMatching
suite.append(unittest.TestLoader().loadTestsFromTestCase(GeneralSimpleMatching))

from string_algo_tests.string_utils_unit_tests import MatchLengthTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(MatchLengthTests))

from string_algo_tests.string_utils_unit_tests import AlphabetIndexTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(AlphabetIndexTests))

from string_algo_tests.boyer_moore_unit_tests import BadCharacterTableTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(BadCharacterTableTests))

from string_algo_tests.boyer_moore_unit_tests import GoodSuffixTableTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(GoodSuffixTableTests))

from string_algo_tests.boyer_moore_unit_tests import FullShiftTableTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(FullShiftTableTests))

from string_algo_tests.knuth_morris_pratt_tests import SpTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(SpTests))

from string_algo_tests.z_algorithm_unit_tests import FundamentalPreprocessTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(FundamentalPreprocessTests))

