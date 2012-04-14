import unittest

from string_algo.boyer_moore import bad_character_table, good_suffix_table, full_shift_table
from string_algo.string_utils import alphabet_index

class BadCharacterTableTests(unittest.TestCase):

    def test_basic(self):
        S = 'abcdefghijklmnopqrstuvwxyz'
        expected = [[-1] for x in range(26)]
        for i in range(26):
            for x in expected:
                x.append(x[-1])
            expected[i][-1] = i
        self.assertEqual(expected, bad_character_table(S))

    def test_empty_string(self):
        self.assertEqual([[] for x in range(26)], bad_character_table(''))

    def test_single_char_string(self):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for c in alpha:
            expected = [[-1,-1] for x in range(26)]
            expected[alphabet_index(c)][1] = 0
            self.assertEqual(expected, bad_character_table(c))

    def test_repeated_char_string(self):
        S = 'aaaa'
        expected = [[-1,-1,-1,-1,-1] for x in range(26)]
        expected[0] = [-1,0,1,2,3]
        self.assertEqual(expected, bad_character_table(S))

    def test_alternating_string(self):
        S = 'aabbaa'
        expected = [[-1,-1,-1,-1,-1,-1,-1] for x in range(26)]
        expected[0] = [-1,0,1,1,1,4,5]
        expected[1] = [-1,-1,-1,2,3,3,3]
        self.assertEqual(expected, bad_character_table(S))

class GoodSuffixTableTests(unittest.TestCase):

    def test_single_suffix_occurrence(self):
        S = 'aabaacaab'
        expected = [-1,-1,-1,-1,-1,-1,2,-1,-1]
        self.assertEqual(expected, good_suffix_table(S))

    def test_multiple_suffix_occurrence(self):
        S = 'aacaacaacaac'
        expected = [-1,-1,-1,8,-1,-1,5,-1,-1,2,-1,-1]
        self.assertEqual(expected, good_suffix_table(S))

    def test_suffix_matches_substring(self):
        S = 'xaabaab'
        expected = [-1,-1,-1,-1,3,-1,-1]
        self.assertEqual(expected, good_suffix_table(S))

    def test_last_char_matches_first(self):
        S = 'abcdefga'
        expected = [-1,-1,-1,-1,-1,-1,-1,0]
        self.assertEqual(expected, good_suffix_table(S))

    def test_no_suffix_occurrences(self):
        S = 'abcdefghijklmnopqrstuvwxyz'
        expected = [-1 for x in range(26)]
        self.assertEqual(expected, good_suffix_table(S))

    def test_repeated_char_string(self):
        S = 'aaaaaa'
        expected = [-1,4,3,2,1,0]
        self.assertEqual(expected, good_suffix_table(S))

    def test_empty_string(self):
        self.assertEqual([], good_suffix_table(''))

    def test_single_character_string(self):
        self.assertEqual([-1], good_suffix_table('a'))

class FullShiftTableTests(unittest.TestCase):

    def test_no_suffix_prefix_matches(self):
        S = 'abcdefgh'
        expected = [8,0,0,0,0,0,0,0]
        self.assertEqual(expected, full_shift_table(S))

    def test_single_suffix_prefix_match(self):
        S = 'aabaab'
        expected = [6,3,3,3,0,0]
        self.assertEqual(expected, full_shift_table(S))

    def test_multiple_suffix_prefix_matches(self):
        S = 'aabaabaabaab'
        expected = [12,9,9,9,6,6,6,3,3,3,0,0]
        self.assertEqual(expected, full_shift_table(S))

    def test_empty_string(self):
        self.assertEqual([], full_shift_table(''))

    def test_single_character_string(self):
        self.assertEqual([1], full_shift_table('a'))

