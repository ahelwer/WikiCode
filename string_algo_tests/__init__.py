import unittest

suite = []

# Functional tests for algorithms matching a single P against a text T
from string_algo_tests.simple_matching_functional_tests import GeneralSimpleMatching
suite.append(unittest.TestLoader().loadTestsFromTestCase(GeneralSimpleMatching))

# Functional tests for algorithms matching a set of P against a text T
from string_algo_tests.set_matching_functional_tests import GeneralSetMatching
suite.append(unittest.TestLoader().loadTestsFromTestCase(GeneralSetMatching))

# Unit tests for string_algo.string_utils.match_length
from string_algo_tests.string_utils_unit_tests import MatchLengthTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(MatchLengthTests))

# Unit tests for string_algo.string_utils.alphabet_index
from string_algo_tests.string_utils_unit_tests import AlphabetIndexTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(AlphabetIndexTests))

# Unit tests for string_algo.boyer_moore.bad_character_table
from string_algo_tests.boyer_moore_unit_tests import BadCharacterTableTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(BadCharacterTableTests))

# Unit tests for string_algo.boyer_moore.good_suffix_table
from string_algo_tests.boyer_moore_unit_tests import GoodSuffixTableTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(GoodSuffixTableTests))

# Unit tests for string_algo.boyer_moore.full_shift_table
from string_algo_tests.boyer_moore_unit_tests import FullShiftTableTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(FullShiftTableTests))

# Unit tests for string_algo.knuth_morris_pratt.build_sp
from string_algo_tests.knuth_morris_pratt_tests import SpTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(SpTests))

# Unit tests for string_algo.z_algorithm.fundamental_preprocess
from string_algo_tests.z_algorithm_unit_tests import FundamentalPreprocessTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(FundamentalPreprocessTests))

# Unit tests for string_algo.aho_corasick.construct_pattern_trie
from string_algo_tests.aho_corasick_unit_tests import ConstructPatternTrieTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(ConstructPatternTrieTests))

# Unit tests for string_algo.aho_corasick.link_pattern_trie
from string_algo_tests.aho_corasick_unit_tests import LinkPatternTrieTests
suite.append(unittest.TestLoader().loadTestsFromTestCase(LinkPatternTrieTests))

