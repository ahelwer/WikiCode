import unittest

from string_algo.aho_corasick import string_set_search as ac

class GeneralSetMatching(unittest.TestCase):

    def check_all(self, pattern_list, T, expected):
        self.longMessage = True
        info = 'Pattern list - \"%s\", T - \"%s\", Algorithm - ' %(pattern_list, T)
        self.assertEqual(expected, ac(pattern_list, T), msg=info+'Aho-Corasick')

    def test_empty_set(self):
        self.check_all([], 'text', [])

    def test_empy_text(self):
        self.check_all(['foo', 'bar'], '', [[],[]])

    def test_empty_strings(self):
        self.check_all(['',''], 'text', [[],[]])

    def test_single_chars(self):
        self.check_all(['a','b','c'], 'abc', [[0],[1],[2]])

    def test_eclipsing_patterns(self):
        self.check_all(['aaa', 'aa', 'a'], 'aaaa', [[0,1],[0,1,2],[0,1,2,3]])

    def test_split_patterns(self):
        self.check_all(['abb', 'bb'], 'abbb', [[0],[1,2]])

    def test_near_matches(self):
        self.check_all(['aaba', 'bbc'], 'aabbaabc', [[],[]])

    def test_prefix_suffix_match(self):
        self.check_all(['abba', 'ab', 'ba'], 'abbabba', [[0,3],[0,3],[2,5]])

